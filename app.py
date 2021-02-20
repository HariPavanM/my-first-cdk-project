#!/usr/bin/env python3

from aws_cdk import core


#from my_first_cdk_project.my_first_cdk_project_stack import MyFirstCdkProjectStack

#app = core.App()
#env_US = core.Environment(region=app.node.try_get_context('dev')['region'])
#MyFirstCdkProjectStack(app, "my-first-cdk-project", env=env_US)
#print(env_US.region) This prints the property of env_US

#This code will be useful for triggering pipeline in a different account or region preset in cdk.json
#env_EU = core.Environment(region=app.node.try_get_context('prod')['region']
#MyFirstCdkProjectStack(app, "my-first-cdk-project", env=env_EU)

from resource_stacks.custom_vpc import CustomVpcStack
##from resource_stacks.custom_ec2 import CustomEc2Stack
from resource_stacks.custom_ec2_v1 import CustomEc2Stackv1
from resource_stacks.custom_AMI import CustomAMIStack
#from resource_stacks.custom_ec2 import CustomEc2Stack

#import os module's environ dictionary to access environment variables
import os

app = core.App()

#Picking up environment variables from default AWS profile;not to be in prod
env_prod = core.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"])

#Custom Vpc Stack
#CustomVpcStack(app,"my-custom-vpc-stack", env = env_prod)
vpc_stack = CustomVpcStack(app,"my-custom-vpc-stack", env = env_prod)

#Custom Ec2 Stack
##ec2_stack = CustomEc2Stack(app,"my-custom-ec2-stack", vpc = vpc_stack.vpc, env = env_prod)
#CustomEc2Stack(app,"my-custom-ec2-stack")
custom_AMI = CustomAMIStack(app,"my-custom-AMI-stack", env = env_prod)
ec2_stack = CustomEc2Stackv1(app,"my-custom-ec2-v1-stack",ami = custom_AMI.linux_ami,vpc = vpc_stack.vpc, env = env_prod)

#Adds tags to all resources created under app

app.synth()
