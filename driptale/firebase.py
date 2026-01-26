import json
import os

import firebase_admin
from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from firebase_admin import auth, credentials, firestore

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
        creds_dict = json.loads(creds_json)
        return credentials.Certificate(creds_dict)
    else:
        raise ValueError(f"Invalid environment: {settings.ENVIRONMENT}")


cred = get_firebase_credentials()
firebase_admin.initialize_app(cred)
db = firestore.client()

security = HTTPBearer(auto_error=False)


def verify_firebase_token(
    credentials: HTTPAuthorizationCredentials | None = Depends(security),
):
    """
    Verify Firebase ID token and return user information.
    """
    if not credentials or not credentials.credentials:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Missing authentication token",
        )

    token = credentials.credentials

    try:
        decoded_token = auth.verify_id_token(token)
        return decoded_token

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
