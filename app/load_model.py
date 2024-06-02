from dotenv import load_dotenv
import os
import boto3
import torch
from io import BytesIO
load_dotenv()
AWS_ACCESS_KEY = os.getenv("AWS_S3_ACCESS_KEY")
AWS_SECRET_KEY = os.getenv("AWS_S3_SECRET_KEY")
s3 = boto3.client("s3", aws_access_key_id=AWS_ACCESS_KEY, aws_secret_access_key=AWS_SECRET_KEY)
local_dir = './model/model_state_dict.pt'
bucket = 'spotifymodel'
s3_dir = 'model/model_state_dict.pt'

def load_model_s3():
    response = s3.get_object(Bucket=bucket, Key=s3_dir)
    model_bytes = response['Body'].read()

    #model = torch.load(BytesIO(model_bytes), map_location=torch.device('cpu'))
    return BytesIO(model_bytes)