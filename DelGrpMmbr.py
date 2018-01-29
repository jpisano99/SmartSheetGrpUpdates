__author__ = 'jpisano'
import requests
import json
import smartsheet
from settings import smartsheet as smart_token

my_token  = smart_token['SMARTSHEET_TOKEN']
group_id = 2220602078586756
user_email = 'alandon@cisco.com'


# GET a users id
url = 'https://api.smartsheet.com/2.0/users'
myheader ={'Authorization' : 'Bearer '  + my_token,'Content-Type':'application/json'}
payload = {'email':user_email}
response = requests.get (url, headers=myheader, params=payload)

data = json.loads(response.text)
user_info = data["data"]

for user in user_info:
    user_id = user['id']

#URL to delete a member
url = 'https://api.smartsheet.com/2.0/groups/'+str(group_id)+'/members/'+str(user_id)
myheader ={'Authorization' : 'Bearer ' + my_token,'Content-Type':'application/json'}
response = requests.delete (url, headers=myheader)
print(response.text)