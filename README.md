# Generate Apple Client Secret Key

This script will generate a new client secret key and print the new key to the console, so you can copy and paste it into your Project using the "Sign in with Apple" feature.

Apple doesn't accept client secret JWTs with an expiration date more than six months after the creation date. That means you'll need to rotate your client secret, at minimum, every six months. 

(**Note:** To be on a safer side, always rotate your client secret every five months instead).

## Prerequisites

- Python 3.6+
- Apple Developer Account
- A private key file obtained from Apple Developer Portal
- A client ID obtained from Apple Developer Portal
- A team ID obtained from Apple Developer Portal
- A key ID obtained from Apple Developer Portal


## Usage

1. Clone this repository
2. Create a new environment file named `.env` and add the following variables:

```
client_id=your_client_id
team_id=your_team_id
filename=your_key_filename.p8
key_id=your_key_id
```

3. Run ```pip install -r requirements.txt``` to install the dependencies
4. Move your private key file to the root of the project
4. Run ```python generate_client_secret.py``` to generate a new client secret key

## References

- [Apple Developer Documentation](https://developer.apple.com/documentation/sign_in_with_apple/generate_and_validate_tokens)
- [What is sign in with apple](https://developer.okta.com/blog/2019/06/04/what-the-heck-is-sign-in-with-apple)
