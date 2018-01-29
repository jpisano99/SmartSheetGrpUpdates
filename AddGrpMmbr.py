__author__ = 'jpisano'
import requests
import json
from settings import smartsheet as smart_token


my_token  = smart_token['SMARTSHEET_TOKEN']
user_email = 'alandon@cisco.com'
#group_id = 2220602078586756 # ww-tetration-managers
#group_id = 3460026560997252 # ww-tetration-team
group_id = 7510627397724036 # tetration-jpisano

# # ADD a new member to group via email
payload = ({"email": user_email},{"email":'hsze@cisco.com'})
print (payload)
# This takes the dict payload and makes it a json string
my_data= json.dumps(payload)
print (my_data)

#URL to add a member
url = 'https://api.smartsheet.com/2.0/groups/'+str(group_id)+'/members'
myheader ={'Authorization' : 'Bearer ' + my_token,'Content-Type':'application/json'}
response = requests.post (url, headers=myheader, data=my_data)
print(response.text)