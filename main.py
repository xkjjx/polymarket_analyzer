from py_clob_client.client import ClobClient, ApiCreds
from dotenv import dotenv_values

config = dotenv_values(".env")

endpoint: str = "https://clob.polymarket.com/"
creds = ApiCreds(config["API_KEY"], config["API_SECRET"], config["API_PASSPHRASE"])
key: str = config["POLYMARKET_PRIVATE_KEY"]
chain_id: int = 137

client: ClobClient = ClobClient(endpoint, chain_id=chain_id, key=key, creds=creds)

marketsData = client.get_markets(next_cursor="")

markets = marketsData["data"]

questions = []

for market in markets:
    questions.append(market["question"])

print(questions)
