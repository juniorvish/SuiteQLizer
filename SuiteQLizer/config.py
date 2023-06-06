import os

# SuiteTalk API credentials
ACCOUNT_ID = os.environ.get("ACCOUNT_ID")
CONSUMER_KEY = os.environ.get("CONSUMER_KEY")
CONSUMER_SECRET = os.environ.get("CONSUMER_SECRET")
TOKEN_ID = os.environ.get("TOKEN_ID")
TOKEN_SECRET = os.environ.get("TOKEN_SECRET")

# SuiteQL endpoint
SUITEQL_ENDPOINT = f"https://{{ACCOUNT_ID}}.suitetalk.api.netsuite.com/services/rest/query/v1/suiteql"