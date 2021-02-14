from aws_cdk import (
    aws_ec2 as _ec2,
    core
)

class CustomEc2Stack(core.Stack):

     def __init__(self, scope: core.Construct, construct_id: str, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        #Reading bootstrap script file
        with open("bootstrap_scripts/install_http.sh", mode='r') as file:
            user_data = file.read()


        #Webserver Instance 001
                #Define Ec2 instance attributes
        web_server = _ec2.Instance(self,
                "webServerId",
                instance_type=_ec2.InstanceType(instance_type_identifier="t1.micro"),
                instance_name="myWebserver3",
                machine_image =_ec2.MachineImage.generic_linux(
                    {"us-east-1":"ami-047a51fa27710816e"}
                ),
                #Assign VPC
                vpc=vpc,
                vpc_subnets=_ec2.SubnetSelection(
                    subnet_type=_ec2.SubnetType.PUBLIC
                    ),
                #Assign user data
                user_data = _ec2.UserData.custom(user_data),
                
                
            )
        #Allow web traffic by opening up ports on SG
        web_server.connections.allow_from_any_ipv4(
            _ec2.Port.tcp(80), description = "Allow web traffic"
        )

        output_1= core.CfnOutput(self,
            "WebserverURL",
            description="URL to Webserver",
            value=f"http://{web_server.instance_public_ip}"
            )


