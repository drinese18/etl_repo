import json
import os
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

import boto3
client = boto3.client('glue')

glueJobName = "test-data-generator-scripted"

def lambda_handler(event, context):
    logger.info('## INITIATED BY EVENT: ')
    #logger.info(event['detail'])
    response = client.start_job_run(JobName = glueJobName)
    logger.info('## STARTED GLUE JOB: ' + glueJobName)
    logger.info('## GLUE JOB RUN ID: ' + response['JobRunId'])
    return response
    
    
    #return {
    #    'statusCode': 200,
    #    'body': json.dumps('Hello from Lambda!')
    #}
