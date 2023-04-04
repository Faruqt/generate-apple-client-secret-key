import os
import jwt
import datetime
from dotenv import load_dotenv 

load_dotenv()

def generate_token():

        with open(os.environ.get('filename'), "r") as f:
            private_key = f.read()
        team_id = os.environ.get('team_id')
        client_id = os.environ.get('client_id')
        key_id = os.environ.get('key_id')
        validity_minutes = 180
        timestamp_now = datetime.datetime.now().timestamp()
        timestamp_exp = timestamp_now + (24 * 60 * 60 * validity_minutes) # 6 months
        data = {
                "iss": team_id,
                "iat": timestamp_now,
                "exp": timestamp_exp,
                "aud": "https://appleid.apple.com",
                "sub": client_id
            }
        token = jwt.encode(payload=data, key=private_key, algorithm="ES256", headers={"kid": key_id})
        print('token', token)

token = generate_token()
