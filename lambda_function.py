import boto3
import json
import os

def lambda_handler(event, context):
    # Détection automatique de l'endpoint LocalStack
    endpoint = f"http://{os.environ['LOCALSTACK_HOSTNAME']}:4566" if 'LOCALSTACK_HOSTNAME' in os.environ else "http://localhost:4566"
    
    ec2 = boto3.client('ec2', endpoint_url=endpoint, region_name="us-east-1")
    
    query_params = event.get('queryStringParameters') or {}
    action = query_params.get('action')
    instance_id = "i-51f8a34f64ad0e1e8"

    try:
        if action == 'start':
            ec2.start_instances(InstanceIds=[instance_id])
            res = "Demarrage envoye"
        elif action == 'stop':
            ec2.stop_instances(InstanceIds=[instance_id])
            res = "Arret envoye"
        elif action == 'status':
            status = ec2.describe_instances(InstanceIds=[instance_id])
            state = status['Reservations'][0]['Instances'][0]['State']['Name']
            res = f"Statut: {state}"
        else:
            res = "Action requise: start, stop, ou status"

        return {
            'statusCode': 200,
            'body': json.dumps({'message': res, 'instance': instance_id})
        }
    except Exception as e:
        return {'statusCode': 500, 'body': json.dumps({'error': str(e)})}