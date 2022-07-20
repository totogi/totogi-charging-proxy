import os
from typing import Mapping

INIT_URL = os.environ['INIT_URL']

def headers(idToken: str) -> Mapping[str, str]:
    headers = {
        'Authorization': f'Bearer {idToken}'
    }
    return headers
