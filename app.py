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
from resource_stacks.custom_ec2 import CustomEc2Stack

#import os module's environ dictionary to access environment variables
import os

app = core.App()

#Picking up environment variables from default AWS profile;not to be in prod
env_prod = core.Environment(account=os.environ["CDK_DEFAULT_ACCOUNT"], region=os.environ["CDK_DEFAULT_REGION"])

#Custom Vpc Stack
CustomVpcStack(app,"my-custom-vpc-stack", env = env_prod)
#CustomVpcStack(app,"my-custom-vpc-stack")

#Custom Ec2 Stack
CustomEc2Stack(app,"my-custom-ec2-stack", env = env_prod)
#CustomEc2Stack(app,"my-custom-ec2-stack")

#Adds tags to all resources created under app
core.Tag.add(app,key="Project Name", value=app.node.try_get_context('envs')['prod']['project name'])
app.synth()
