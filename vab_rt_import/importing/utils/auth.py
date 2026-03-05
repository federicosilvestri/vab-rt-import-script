from vab_rt_import.importing.vab_rt_api_client import AuthenticatedClient
import json
from pathlib import Path

AUTH_FILE = Path(__file__).parent.parent.parent / "auth.json"

def get_client() -> AuthenticatedClient:
    data = json.loads(AUTH_FILE.read_text())
    return AuthenticatedClient(
        base_url="http://localhost:8000",
        token=data["access"],
        raise_on_unexpected_status=True,
    )