from py_clob_client.client import ClobClient
from dotenv import dotenv_values

config = dotenv_values(".env")

endpoint: str = "https://clob.polymarket.com/"
key: str = config["POLYMARKET_PRIVATE_KEY"]
chain_id: int = 137

client: ClobClient = ClobClient(endpoint, key=key, chain_id=chain_id)

creds = client.derive_api_key()

print(creds)
