#!/usr/bin/env python

import os
import boto3
import logging
import string
import shutil

def upload_handler(event, context):
   for record in event['Records']:
       if record['eventName'] in ('ObjectCreated:Put', 'ObjectCreated:Post', 'ObjectCreated:CompleteMultipartUpload'):
           s3 = boto3.resource('s3')
           oldbucketname = 'nd-auto-styles-temp-production'
           newbucketname = 'nd-auto-styles-production'
           filename = record['s3']['object']['key']
           copy_source = {
               'Bucket': oldbucketname,
               'Key': filename
           }
           s3.meta.client.copy(copy_source, newbucketname, filename)
   return "done"

