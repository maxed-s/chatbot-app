import os
import requests
from dotenv import load_dotenv

load_dotenv()

QUICKBOOKS_ONLINE_BASE_URL = os.getenv("QUICKBOOKS_ONLINE_BASE_URL")
QUICKBOOKS_PAYMENT_PRODUCTION_BASE_URL = os.getenv("QUICKBOOKS_PAYMENT_PRODUCTION_BASE_URL")

## will get from answer from chatbot model
def creat_account(realmID):  
    api_url = f"{QUICKBOOKS_ONLINE_BASE_URL}/v3/company/{realmID}/account"  
    json_object = {"Name": "", "AccountType": ""}
    response = requests.post(api_url, json=json_object)
    return response.json()

def query_account(realmID, selectStatement):
    api_url = f"{QUICKBOOKS_ONLINE_BASE_URL}/v3/company/{realmID}/query?query={selectStatement}"
    response = requests.get(api_url)
    return response.json()

def read_account(realmID, accountId):
    api_url = f"{QUICKBOOKS_ONLINE_BASE_URL}/v3/company/{realmID}/account/{accountId}"
    response = requests.get(api_url)
    return response.json()

def update_account(realmID):
    api_url = f"{QUICKBOOKS_ONLINE_BASE_URL}/v3/company/{realmID}/account"
    # json need to be initialized
    json_obj = {}
    response = requests.post(api_url, json=json_obj)
    return response.json()

# QuickBooks payment apis
def creat_bank_account(id):
    api_url = f"/quickbooks/v4/customers/{id}/bank-accounts"
    json_obj = {"phone": "", "routingNumber": "", "name": "", "accountType": "", "accountNumber": ""}
    response = requests.post(api_url, json=json_obj)
    return response.json()

def creat_bank_account_from_token(id):
    api_url = f"/quickbooks/v4/customers/{id}/bank-accounts/createFromToken"
    json_obj = {"value": ""}
    response = requests.post(api_url, json=json_obj)
    return response.json()

def delete_bank_account(id, bankaccount_id):
    api_url = f"/quickbooks/v4/customers/{id}/bank-accounts/{bankaccount_id}"
    response = requests.delete(api_url)
    return response.json()

def bank_account_details(id, bankaccount_id):
    api_url = f"/quickbooks/v4/customers/{id}/bank-accounts/{bankaccount_id}"
    response = requests.get(api_url)
    return response.json()

def list_of_bank_accounts(id):
    api_url = f"/quickbooks/v4/customers/{id}/bank-accounts"
    response = requests.get(api_url)
    return response.json()
