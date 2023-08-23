from flask import Flask, render_template,jsonify,request, redirect
from flask_cors import CORS
import requests,openai,os
from dotenv.main import load_dotenv
import pdb
from intuitlib.client import AuthClient
from intuitlib.enums import Scopes
import pdb
from quickbooks import QuickBooks
from quickbooks.cdc import change_data_capture
from quickbooks.objects import Invoice

app = Flask(__name__)
CORS(app)

load_dotenv()
API = os.getenv("API")
data = {}
data['auth'] = False 
authclient = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data', methods=['POST'])
def get_data():
    
    data = request.get_json()
    text=data.get('data')
    openai.api_key = API
    
    user_input = text
    print(user_input)
    try:
        response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_input,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
        )
       
        model_reply = response['choices'][0]['text']
        #print(response,model_reply)
        return jsonify({"response":True,"message":model_reply})
    except Exception as e:
        print(e)
        error_message = f'Error: {str(e)}'
        return jsonify({"message":error_message,"response":False})


@app.route("/callback")
def callback():
    auth_code = request.args.get('code')
    realm_id = request.args.get('realmId')
    global authclient
    global data
    data['compID'] = realm_id
    authclient.get_bearer_token(auth_code, realm_id=realm_id)
   # pdb.set_trace()
    data["access_token"] = authclient.access_token
    data["refresh_token"] = authclient.refresh_token
    return render_template("index.html")
    
@app.route('/auth')
def auth(): 
    global data
    if data['auth']: 
        return render_template("index.html")
    client_id = os.getenv("client_ID")
    client_secret = os.getenv("client_secret")
    redirect_uri = "http://localhost:5000/callback"
    environment = "sandbox"
    #Instainate Client
    auth_client = AuthClient(client_id,client_secret,redirect_uri, environment)
    global authclient 
    authclient = auth_client
    
    #prepare scopes
    scopes = [
        Scopes.ACCOUNTING
    ]

    #Get authorization URL
    auth_url = authclient.get_authorization_url(scopes)
    data["auth"] = True
    return redirect(auth_url)

if __name__ == '__main__':
    app.run()
