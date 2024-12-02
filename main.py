from py_clob_client.client import ClobClient, ApiCreds
from dotenv import dotenv_values

config = dotenv_values(".env")

endpoint: str = "https://clob.polymarket.com/"
creds = ApiCreds(config["POLYMARKET_API_KEY"], config["POLYMARKET_API_SECRET"], config["POLYMARKET_API_PASSPHRASE"])
key: str = config["POLYMARKET_PRIVATE_KEY"]
chain_id: int = 137

client: ClobClient = ClobClient(endpoint, chain_id=chain_id, key=key, creds=creds)

marketsData = client.get_markets(next_cursor="")

markets = marketsData["data"]

questions = []
outcomes = []
rewards = []

for market in markets:
    questions.append(market["question"])
    outcomes.append(market["tokens"])
    rewards.append(market["rewards"])

for question, outcome in zip(questions, outcomes):
    print(question, len(outcome), len(rewards))