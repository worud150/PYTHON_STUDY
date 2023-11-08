1. 


import boto3
import openpyxl
import os

service_name = 's3'
endpoint_url = 'https://kr.object.ncloudstorage.com'
region_name = 'kr-standard'
access_key = '38B5E44703F342F4AD23' 
secret_key = 'DC701EE03C337C64E46E613EF99CB1A60532D5CE'
bucket = 'aidata-2021-01-056'  # 버킷 이름

wb = openpyxl.Workbook()
ws = wb.active
ws.append(['경로','파일명'])
s3 = boto3.client(service_name, endpoint_url=endpoint_url, aws_access_key_id=access_key,aws_secret_access_key=secret_key)
prefix=['095.교통사고 영상 데이터/07.보완조치/1.Dataset/원천데이터/이미지/']
for idx, i in enumerate(prefix, start=2):
  response = s3.list_objects(Bucket=bucket, MaxKeys=20000,Prefix=i)
  while True:
      for content in response['Contents']:
        content_key = content['Key']
        print(content_key)
        if content_key[-1] != '/':
          content_split = content_key.split('/')
          ws.append([os.path.dirname(content_key),os.path.basename(content_key)])
      if response.get('IsTruncated'):
        response = s3.list_objects(Bucket=bucket, MaxKeys=20000, Marker=response.get('NextMarker'),Prefix=i)
      else:
        break

wb.save(r'C:\Users\user\Desktop\업무\004. 파이썬 코드\000. Practice\교통사고원천영상.xlsx')
