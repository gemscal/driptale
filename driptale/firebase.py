import json
import os

from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials, firestore, initialize_app

from driptale.config import settings
from driptale.constant import ENVIRONMENT


def get_firebase_credentials():
    """
    Get firebase credentials based on the environment.
    """
    if settings.ENVIRONMENT == ENVIRONMENT.DEVELOPMENT:
        return credentials.Certificate(settings.FIREBASE_CRED)
    elif settings.ENVIRONMENT == ENVIRONMENT.PRODUCTION:
        creds_json = os.getenv("FIREBASE_CRED")
        if not creds_json:
            raise ValueError("FIREBASE CREDENTIAL environment variable is not set")
        creds_dict = json.loads(creds_json)
        return credentials.Certificate(creds_dict)
    else:
        raise ValueError(f"Invalid environment: {settings.ENVIRONMENT}")


cred = get_firebase_credentials()
initialize_app(cred)
db = firestore.client()

security = HTTPBearer(auto_error=False)


def verify_firebase_token(
    token_credentials: HTTPAuthorizationCredentials | None = Depends(security),
) -> str:
    """
    Verify Firebase ID token and return the authenticated user's uid.
    """
    if not token_credentials or not token_credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token",
        )

    token = token_credentials.credentials

    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token["uid"]

    except auth.ExpiredIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Expired authentication token",
        )
    except auth.RevokedIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Revoked authentication token",
        )
    except auth.InvalidIdTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication token",
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Authentication Failed: {str(e)}",
        )
