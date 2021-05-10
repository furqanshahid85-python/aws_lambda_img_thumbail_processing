import os
import json
import uuid
import boto3

from PIL import Image

img_width = 200
img_height = 200
dest_bucket = 'lambda-img-thumbnail-dest-bucket'
s3_client = boto3.client('s3')

def lambda_handler(event, context):
    print(event)
    
    # getting bucket and object key from event object
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']
    
    # creating download path and downloading the img object from S3
    object_key = str(uuid.uuid4()) + '-' + key
    img_download_path = '/tmp/{}'.format(object_key)
    
    with open(img_download_path,'wb') as img_file:
        s3_client.download_fileobj(source_bucket, key, img_file)
    
    # thumbnail img path
    img_thumbnail_path = '/tmp/thumbnail-{}'.format(object_key)

    # Creating and saving img thumbnail from downloaded img
    source_img = Image.open(img_download_path)
    source_img.thumbnail((img_width,img_height))
    source_img.save(img_thumbnail_path)
    
    # uploading img thumbnail to destination bucket
    upload_key = 'thumbnail-{}'.format(object_key)
    s3_client.upload_file(img_thumbnail_path, dest_bucket,upload_key)
