import requests
import os
import json
from dotenv import load_dotenv

# Loading Environmnt Variables
load_dotenv()

parts_url = 'https://api.devrev.ai/parts.list'
user_url='https://api.devrev.ai/dev-users.self'
work_create_url='https://api.devrev.ai/works.create'

# Header for Parts List 
headers = {
    'Authorization':os.getenv('PAT'),  
}

# Header for work.create
work_create_headers = {
    'Authorization':os.getenv('PAT'),
    'Content-Type':'application/json'
}

# Data for creating the issue
data = {
  "type":"issue",
  "applies_to_part":"",
  "owned_by":[
    ""
  ],
  "title":"New issue using API"
}

# accessing the applies_to_part id value 
parts_response = requests.post(parts_url,headers=headers)

parts_response_data = json.loads(parts_response.text)
for part in parts_response_data["parts"]:
    if part["id"]:
        data["applies_to_part"] = str(part["id"])

# accessing the owned_by id value 
user_response = requests.post(user_url,headers=headers)
user_response_data = json.loads(user_response.text)
getdevId=user_response_data["dev_user"]
data["owned_by"]=[getdevId["id"]]

# Request to create the issue
work_response = requests.post(work_create_url,headers=work_create_headers,json=data)
work_response_data = json.loads(user_response.text)

if work_response.status_code ==201:
  print("Issue Created! check dashboard")