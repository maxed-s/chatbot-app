from qbClient import AuthClient
import constant as cfg
import requests
from future.moves.urllib.parse import urlencode
import os
from dotenv import load_dotenv

load_dotenv()

QUICKBOOKS_ONLINE_SANDBOX_BASE_URL = os.getenv("QUICKBOOKS_ONLINE_SANDBOX_BASE_URL")
QUICKBOOKS_PAYMENT_SANDBOX_BASE_URL = os.getenv("QUICKBOOKS_PAYMENT_SANDBOX_BASE_URL")

auth_client = AuthClient(**cfg.client_secrets)

def getCustomerData(accessToken):
    #making Request
    base_url = QUICKBOOKS_ONLINE_SANDBOX_BASE_URL
    url = '{0}/v3/company/{1}/companyinfo/{1}'.format(base_url, cfg.qBData["realm_id"])
    auth_header = 'Bearer {0}'.format(accessToken)
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json'
    }
    response = requests.get(url, headers=headers)

    print("Response = ",response)
    print("Response Data = ",response.text)

    print("Success")

def refresh_token():
    response = auth_client.refresh(refresh_token=cfg.refreshToken)
    return response

def getPaymentData(accessToken):
    #making Request
    base_url = f'{QUICKBOOKS_PAYMENT_SANDBOX_BASE_URL}/quickbooks/v4/payments/charges/'
    auth_header = 'Bearer {0}'.format(accessToken)
    data = {
        'Authorization': auth_header
    }
    headers = {
        'Authorization': auth_header,
        'Accept': 'application/json;charset=UTF-8',
        'Content-type': '*/*'
    }

    response = requests.get(base_url, headers=headers)

    print("Response 2 = ",response)
    print("Response Data 2 = ",response.text)

    print("Success")


if __name__ == "__main__":
    # fetchData()
    response = refresh_token()
    getCustomerData(accessToken = response["access_token"])
    response2 = auth_client.get_user_info(access_token=response["access_token"])
    print(response2.text)
    print("\n\n\n")
    getPaymentData(accessToken = response["access_token"])