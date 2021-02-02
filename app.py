#!/usr/bin/env python3

from aws_cdk import core

from my_first_cdk_project.my_first_cdk_project_stack import MyFirstCdkProjectStack

app = core.App()
env_US = core.Environment(region=app.node.try_get_context('dev')['region'])
MyFirstCdkProjectStack(app, "my-first-cdk-project", env=env_US)
#print(env_US.region) This prints the property of env_US

#This code will be useful for triggering pipeline in a different account or region preset in cdk.json
#env_EU = core.Environment(region=app.node.try_get_context('prod')['region']
#MyFirstCdkProjectStack(app, "my-first-cdk-project", env=env_EU)

app.synth()
