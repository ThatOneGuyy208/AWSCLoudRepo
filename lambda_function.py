import boto3
import json
import os
import datetime
import dateutil.tz

s3 = boto3.resource('s3')
ses = boto3.client('ses', region_name='us-east-1')

def lambda_handler(event, context):
	key = event.get("Records")
	bname = event.get("Records")
	if key is not None:
		key = key[0]['s3']['object']['key']
		bname = bname[0]['s3']['bucket']['name']
	
	# get current time
	central = dateutil.tz.gettz('US/Central')
	now = datetime.datetime.now(tz=central)
	current_time = now.strftime("%H:%M:%S")
    
	name = "Jaired Lyons" #enter your name here
	body = "This email is an alert from " + name + ". A file has been deleted from one of your s3 buckets." + "\n"
	subject = "S3 Object deleted from: " + str(bname) + '\n'
	body += "Deleted from bucket: " + str(bname) + '\n'
	body += "File deleted: " + str(key) + '\n'
	body += "At time(cst): " + current_time
	
	ses.send_email(
    	Source = 'jairedlyons@gmail.com',  ### needs to be changed to a verified email address
    	Destination = {
    		'ToAddresses': [
    			'jaired.lyons@drake.edu' ### needs to be changed to a verified email address
		    ]
	    },
	    Message = {
	    	'Subject': {
	    		'Data': subject,
	    		'Charset': 'UTF-8'
		    },
		    'Body': {
		    	'Text':{
				    'Data': body,
				    'Charset': 'UTF-8'
			    }
		    }
	    }
    )
    