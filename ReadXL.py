__author__ = 'jpisano'
import requests
import json
import smartsheet
import xlrd
from settings import app
from settings import smartsheet as smart_token

my_token  = smart_token['SMARTSHEET_TOKEN']
#group_id = 2220602078586756 # ww-tetration-managers
#group_id = 3460026560997252 # ww-tetration-tsa
#group_id = 5060915491039108 ## ww-tetration-pss
group_id = 7510627397724036 # tetration-jpisano

working_file = app['WORKING_DIR'] + app['WORKING_FILE']

print("\t\tOpening Workbook: ", working_file)
wb = xlrd.open_workbook(working_file)

#loop through the mailer .xlsx workbook and build a payload to send to Smartsheets
ws = wb.sheets()
x=0
payload = []
for sheet in ws:
    emails = sheet.col(0)
    x = -1
    for email in emails:
        x = x+1
        if x != 0 :
            if str.startswith(email.value,'group.') :
                continue
            else:
                print(email.value + '@cisco.com')
                payload.append ({'email': email.value +'@cisco.com'})
        else:
            continue

#payload has the list of members to be added
my_data = json.dumps(payload)

#URL to add a member(s)
url = 'https://api.smartsheet.com/2.0/groups/'+str(group_id)+'/members'
myheader ={'Authorization' : 'Bearer ' + my_token,'Content-Type':'application/json'}
response = requests.post (url, headers=myheader, data=my_data)
print(response.text)




