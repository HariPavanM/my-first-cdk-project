from aws_cdk import (
    aws_ec2 as _ec2,
    core
)

class CustomEc2Stackv1(core.Stack):

     def __init__(self, scope: core.Construct, construct_id: str, ami, vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        #This code deploys an ec2 instance per subnet  across all subnets in a VPC - excludes ISOLATED
             

        AZs_list = vpc.availability_zones
        count_of_AZs = range(len(AZs_list))
        #print(count_of_AZs)
        #print(AZs_list)
        
        for x in count_of_AZs:
            
        # Instance 00x in PUBLIC SUBNET
            publicinstancename = _ec2.Instance(self,
                f"Public_Instance_{x}",
                instance_type=_ec2.InstanceType(instance_type_identifier="t1.micro"),
                instance_name=f"PublicInstance_{x}_{AZs_list[x]}",
                #assign machine image prebaked with bootstrap data
                machine_image = ami,
                #Assign VPC passed from other stack
                vpc=vpc,
                #Assign Subnet
                vpc_subnets=_ec2.SubnetSelection(
                    subnet_type=_ec2.SubnetType.PUBLIC,
                ),
                #Assign AZ
               availability_zone = AZs_list[x]                                        
            )

        # Instance 00x in PRIVATE SUBNET
            privateinstancename = _ec2.Instance(self,
                f"Private_Instance_{x}",
                instance_type=_ec2.InstanceType(instance_type_identifier="t1.micro"),
                instance_name=f"PrivateInstance_{x}_{AZs_list[x]}",
                #assign machine image prebaked with bootstrap data
                machine_image = ami,
                #Assign VPC passed from other stack
                vpc=vpc,
                #Assign Subnet
                vpc_subnets=_ec2.SubnetSelection(
                    subnet_type=_ec2.SubnetType.PRIVATE,
                ),
                #Assign AZ
               availability_zone = AZs_list[x]                                        
            )

        
        #Allow web traffic by opening up ports on SG
            publicinstancename.connections.allow_from_any_ipv4(
            _ec2.Port.tcp(80), 
            description = "Allow web traffic for Webserver1"
            ),
        #Modfying the SG of private instances to allow traffic from SG of public instances
            privateinstancename.connections.allow_from(
            publicinstancename,
            _ec2.Port.tcp(3000),
            description = "Allow any traffic from sg of public instances"
            )
        

            output_public_instances= core.CfnOutput(self,
                f"PublicInstance_name_{x}",
                description="URL to Webserver" f"Instance_name_{x}",
                value=f"http://{publicinstancename.instance_public_ip}"
            )
            # output_private_instances= core.CfnOutput(self,
            #     f"PrivateInstance_name_{x}",
            #     description="PublicIP of Private Instance -" f"Instance_name_{x}",
            #     value=f"http://{privateinstancename.instance_public_ip}"
            # )
        