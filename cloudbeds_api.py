import json
import requests

def load_secret(api, property_id):
# function to load secrets
    f = open('int.secrets','r')

    secrets = json.loads(f.read())
    print(secrets)
    return secrets[api][str(property_id)]

#def save_secret():
#save secrets 


def call_cb_endpoint(endpoint, method, property_id, params):
# function to 

    url = 'https://hotels.cloudbeds.com/api/v1.1/'+endpoint
    cb_secret = load_secret('cloudbeds', property_id)
    headers={"x-api-key": cb_secret}
    if method == 'get':
        response = requests.get(url, headers=headers)
        print(response.text)

def reservations(property_id, params):
    call_cb_endpoint('getReservations', 'get', property_id, params)

#def rooms():

#def write_access_code():

#def write_app_setting():

reservations(185495, {})
