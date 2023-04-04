import os
import jwt
import datetime
from dotenv import load_dotenv 

load_dotenv()

def generate_secret_key():

        with open(os.environ.get('filename'), "r") as f:
            private_key = f.read()

        team_id = os.environ.get('team_id')
        client_id = os.environ.get('client_id')
        key_id = os.environ.get('key_id')

        timestamp_now = datetime.datetime.now().timestamp()
        timestamp_exp = timestamp_now + (86400 * 180) # 6 months

        headers={"kid": key_id}
        data = {
                "iss": team_id,
                "iat": timestamp_now,
                "exp": timestamp_exp,
                "aud": "https://appleid.apple.com",
                "sub": client_id
            }

        secret_key = jwt.encode(payload=data, key=private_key, algorithm="ES256", headers=headers)
        return secret_key

client_secret_key = generate_secret_key()
print('client_secret_key', client_secret_key)
