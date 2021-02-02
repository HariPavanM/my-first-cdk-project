from aws_cdk import (
    aws_s3 as _s3,
    core
)

class MyFirstCdkProjectStack(core.Stack):

    def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # The code that defines your stack goes here
        mybucket = _s3.Bucket(
            self,
            "myBucketId",
            versioned= True,
            encryption= _s3.BucketEncryption.KMS_MANAGED
           
        )
       # print(self.node.try_get_context('dev')['region'])

        output_1 = core.CfnOutput(
            self,
            "mybucketoutput",
            value=mybucket.bucket_name,
            description="This is my first CDK bucket",
            export_name="mybucketoutput"

        )