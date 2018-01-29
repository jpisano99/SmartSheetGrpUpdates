__author__ = 'jpisano'
import requests
import json
import smartsheet
from settings import smartsheet as smart_token


my_token  = smart_token['SMARTSHEET_TOKEN']
#group_id = 2220602078586756 # ww-tetration-managers
group_id = 3460026560997252 # ww-tetration-tsa
sheet_id = 232517618952068 #TA Feature Request

# Initialize client
ss_client = smartsheet.Smartsheet(my_token)

# Make sure we don't miss any errors
ss_client.errors_as_exceptions(True)

#print(ss_client.Sheets.list_sheets())

sheet = ss_client.Sheets.get_sheet(sheet_id)

cols = sheet.columns
for col in cols:
    print(col.id,col.title)
    if col.title == 'Status':
        status_col_id = col.id

    if col.title == 'Feature Title':
        title_col_id = col.id

    if col.title == 'Created By':
        owner_col_id = col.id

rows= sheet.rows
for row in rows:
    print (row.id,row.row_number,
        row.get_column(title_col_id).value,
        row.get_column(status_col_id).value,
        row.get_column(owner_col_id).value)

#Create the email model
email_spec = ss_client.models.MultiRowEmail()
email_spec.send_to = [
    ss_client.models.Recipient({'email': 'jpisano@cisco.com'})]
#   ,ss_client.models.Recipient({'email': 'alandon@cisco.com'})]
email_spec.subject = 'Please update based on meeting'
email_spec.message = 'some message'
email_spec.cc_me = False
email_spec.row_ids = [7316065746216836]
email_spec.column_ids = [5909580073985924]

# Send the actual update request
new_update_request = ss_client.Sheets.send_update_request(
    sheet_id,           # sheet_id
    email_spec
)