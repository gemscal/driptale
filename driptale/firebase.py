import json
import os

import firebase_admin
from firebase_admin import credentials, firestore

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
