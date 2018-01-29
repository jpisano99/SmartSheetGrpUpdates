__author__ = 'jpisano'
import requests
import json
import smartsheet
from settings import smartsheet as smart_token

# import csv
# import pprint
my_token  = smartsheet['SMARTSHEET_TOKEN']

ss_client = smartsheet.Smartsheet(my_token)
ss_client.errors_as_exceptions(True)

#url = 'https://api.smartsheet.com/2.0/sheets'
#myheader = {'Authorization' : 'Bearer 519zl07z3k1uef6rfjxqqm5630', 'Content-Type':'application/json'}
#jim = jim.Smartsheet('1234')
#jim = smartsheet.list_groups()

# Get ALL Groups
url = 'https://api.smartsheet.com/2.0/groups'
myheader ={'Authorization' : 'Bearer ' + my_token,'Content-Type':'application/json'}
payload = {'includeAll':'True'}
response = requests.get (url, headers=myheader, params=payload)

print()
print('request   ',response.request.headers)
print()
print('headers   ',response.headers)
print()
print('text     ',response.text)
print()
print('content    ',response.content)
print()
print('status    ',response.status_code)

print (response.text)
data = json.loads(response.text)
print(data)
groups = data["data"]
print()

#Look for Tetration group ids
x= 0
group_name = 'ww-tetration-tsa'
group_name = 'ww-tetration-pss'
group_name = 'tetration-jpisano'
for group in groups:
    if group["name"].startswith(group_name):
        x=x+1
        #print (x,")  Group Name : ",group['id'],group['name'])
        group_id = group['id']
        break

print('Found it:  '+'Group Name : ', group['id'], group['name'])

#Get the Group Members
url = 'https://api.smartsheet.com/2.0/groups/'+str(group_id)
myheader = {'Authorization': 'Bearer ' + my_token, 'Content-Type': 'application/json'}
payload = {'includeAll': 'True'}
response = requests.get(url, headers=myheader, params=payload)
print()
print('RESPONSE text:     ',response.text)
print()

data = json.loads(response.text)
print("DATA:  ",data)
members = data["members"]
print()

x= 0
for member in members:
        x=x+1
        print (x,") Member : ",member[('id')],member['email'],member['firstName'],member['lastName'])

