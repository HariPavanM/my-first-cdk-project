from aws_cdk import (
    aws_ec2 as _ec2,
    core
)

class CustomAMIStack(core.Stack):

     def __init__(self, scope: core.Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
           
        #Reading bootstrap script file
        # with open("bootstrap_scripts/install_http.sh", mode='r') as file:
        #     user_data = file.read()

        #Code to pick up the latest Linux AMI
        self.linux_ami = _ec2.AmazonLinuxImage(
            generation=_ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
            edition=_ec2.AmazonLinuxEdition.STANDARD,
            storage=_ec2.AmazonLinuxStorage.GENERAL_PURPOSE,
            #user_data = user_data
            user_data=_ec2.UserData.add_execute_file_command(self,file_path='../bootstrap_scripts/install_http.sh')
        )
        print(self.linux_ami)
       # returned_image = linux_ami.get_image(self)
        #self.Image_Config = _ec2.MachineImageConfig(image_id=self.linux_ami,os_type=_ec2.OperatingSystemType.UNKNOWN, user_data=_ec2.UserData.custom(user_data))
        # core.CfnOutput(
        #     self,
        #     "LatestLinuxAMIChosen",
        #     #value=self.Image_Config.image_id,
        #     value=self.linux_ami,
        #     description="AMI with latest linux baked-in",
        #     export_name="LatestLinuxAMIChosen"
        # )