import asyncio
import json

#from okta_jwt_verifier import AccessTokenVerifier, IDTokenVerifier
from okta_jwt_verifier import BaseJWTVerifier

loop = asyncio.get_event_loop()

# def is_access_token_valid(token, issuer):
#     jwt_verifier = BaseJWTVerifier(issuer=issuer, audience='api://default')
#     try:
#         loop.run_until_complete(jwt_verifier.verify_access_token(token))
#         return True
#     except Exception:
#         return False


async def is_access_token_valid(token, issuer):
    jwt_verifier = BaseJWTVerifier(issuer=issuer, audience='api://default')
    #jwt_verifier.verify_access_token(token)
    try:
        loop.run_until_complete(jwt_verifier.verify_access_token(token))
        return True
    except Exception:
        return False


# def is_id_token_valid(token, issuer, client_id, nonce):
#     jwt_verifier = IDTokenVerifier(issuer=issuer, client_id=client_id, audience='api://default')
#     try:
#         loop.run_until_complete(jwt_verifier.verify(token, nonce=nonce))
#         return True
#     except Exception:
#         return False

async def is_id_token_valid(token, issuer, client_id, nonce):
    jwt_verifier = BaseJWTVerifier(issuer=issuer, client_id=client_id, audience='api://default')
    #jwt_verifier.verify_id_token(token, nonce=nonce)
    try: 
        loop.run_until_complete(jwt_verifier.verify_id_token(token, nonce=nonce))
        return True
    except Exception:
        return False


def load_config(fname='./client_secrets.json'):
    config = None
    with open(fname) as f:
        config = json.load(f)
    return config


config = load_config()
