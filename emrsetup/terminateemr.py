import boto3

client = boto3.client('emr', region_name='us-east-1')

response = client.list_clusters()

cluster_id = response['Clusters'][0]['Id']

response = client.terminate_job_flows(
    JobFlowIds=[cluster_id]
)

print("Terminated " + cluster_id)