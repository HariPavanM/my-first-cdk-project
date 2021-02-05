from aws_cdk import (
    aws_ec2 as _ec2,
    core
)

class CustomEc2Stack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        my_vpc = _ec2.Vpc.from_lookup(self, 'CustomVpcId', vpc_name=f'custom_vpc/CustomVpcId')

#print(CustomVpcStack.custom-vpc-id)
        vpc = _ec2.Vpc.from_lookup(self,
        "ImportedVPC",
        vpc_id=my_vpc.vpc_id)

        web_server = _ec2.Instance(self,
        "webServerId",
            instance_type=_ec2.InstanceType(instance_type_identifier="t2.micro"),
            instance_name="myEc2instance",
            machine_image =_ec2.MachineImage.generic_linux(
                {"us-east-1":"ami-047a51fa27710816e"}
            ),
            vpc=vpc,
            vpc_subnets=_ec2.SubnetSelection(
                subnet_type=_ec2.SubnetType.PUBLIC
                )
            )
