__author__ = 'jpisano'
import requests
import json
# import csv
# import pprint
from settings import smartsheet as smart_token

my_token  = smart_token['SMARTSHEET_TOKEN']

def main():

    url = 'https://api.smartsheet.com/2.0/sheets'
    myheader = {'Authorization' : 'Bearer '  + my_token, 'Content-Type':'application/json'}

    response = requests.get (url, headers=myheader)
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
    sheets = data["data"]
    #print(type(sheets))
    print()


    for sheet in sheets:
        if sheet["name"].startswith('TA Feature Request'):
            print ("TA Feature Request Sheet ID: ",sheet['id'],sheet['name'])
            #sheet_id = sheets[('name')]
            sheet_id = sheet['id']


    print('***********************')
    print('Tetration Feature Requests')
    print('**********************')
    print()

    url = 'https://api.smartsheet.com/2.0/sheets/'+str(sheet_id)
    myheader = {'Authorization' : 'Bearer ' + my_token , 'Content-Type':'application/json'}

    response = requests.get (url, headers=myheader)
    print (response.text)

if __name__ == "__main__":
    main()