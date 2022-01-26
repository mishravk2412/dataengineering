import boto3
import json

client = boto3.client('emr', region_name='us-east-1')

response = client.run_job_flow(
    Name="Process student data EMR",
    ReleaseLabel='emr-6.3.0',
    Applications=[
        {
            'Name': 'Hadoop'
        },
        {
            'Name': 'Zookeeper'
        },
        {
            'Name': 'Spark'
            
        }
#        {
 #           'Name': 'Hive'
  #      },
    ],
    
    Instances={
        'InstanceGroups': [
            {
                'Name': "Master",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm1.xlarge',
                'InstanceCount': 1,
            },
            {
                'Name': "Slave",
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm1.xlarge',
                'InstanceCount': 3,
            }
        ],
        'Ec2KeyName': 'ec2-key-pair',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False,

    },
    Steps=[
    {
        'Name': 'Run Spark',
        'ActionOnFailure': 'CANCEL_AND_WAIT',
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': ['spark-submit', 's3://varunetlproject/studentAnalysis.py']
        }
    }
    ],
    LogUri="s3://varunetlproject/",
    VisibleToAllUsers=True,
    ServiceRole='EMR_DefaultRole',
    JobFlowRole='EMR_EC2_DefaultRole',
    AutoScalingRole="EMR_AutoScaling_DefaultRole"
)

print(json.dumps(response, indent=4, sort_keys=True, default=str))
