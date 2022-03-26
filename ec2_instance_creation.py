import boto3

def create_ec2_instance():
    try:
        print("Creating the EC2 Instance...")
        resource_ec2 = boto3.client('ec2')
        resource_ec2.run_instances(
            ImageId=" ami-04505e74c0741db8d",
            MinCount=1,
            MaxCount=1,
            InstanceType="t2.micro",
            keyName="my-project-key"
        )
    except Exception as o:
        print("Instance Creation Unsuccessful..!")


create_ec2_instance()