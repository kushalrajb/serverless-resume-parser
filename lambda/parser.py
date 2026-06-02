import json
import boto3
import os
import re
from datetime import datetime
import PyPDF2

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')

TABLE_NAME = os.environ.get('DYNAMODB_TABLE', 'ParsedResumes')

def extract_email(text):
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    match = re.search(email_pattern, text)
    return match.group(0) if match else "Email not found"

def lambda_handler(event, context):
    table = dynamodb.Table(TABLE_NAME)
    
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        key = record['s3']['object']['key']
        
        try:
            # Download the PDF from S3 to the Lambda local ephemeral /tmp space
            local_path = f"/tmp/{os.path.basename(key)}"
            s3.download_file(bucket, key, local_path)
            
            # Extract text using the PyPDF2 package bundled by the pipeline
            raw_text = ""
            with open(local_path, 'rb') as f:
                reader = PyPDF2.PdfReader(f)
                for page in reader.pages:
                    page_text = page.extract_text()
                    if page_text:
                        raw_text += page_text + " "
            
            candidate_email = extract_email(raw_text)
            
            # Persist data to DynamoDB
            table.put_item(
                Item={
                    'ResumeID': key,
                    'UploadDate': str(datetime.now()),
                    'CandidateEmail': candidate_email,
                    'RawTextLength': len(raw_text)
                }
            )
            print(f"Successfully processed and stored entry for: {key}")
            
        except Exception as e:
            print(f"❌ Error processing {key}: {str(e)}")
            raise e

    return {'statusCode': 200, 'body': 'Success'}
