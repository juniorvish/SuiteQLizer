import requests
import json

def suiteqlRequest(query, config):
    headers = {
        'Authorization': f"Bearer {config['access_token']}",
        'Content-Type': 'application/json'
    }
    url = f"{config['account_url']}/services/rest/record/v1/suiteql"
    payload = {
        'q': query
    }
    response = requests.post(url, headers=headers, json=payload)
    return response.json()

def parseJsonResponse(jsonResponse):
    parsedResponse = []
    for item in jsonResponse['items']:
        parsedItem = {}
        for key, value in item.items():
            parsedKey = key.lower().replace(' ', '_')
            parsedItem[parsedKey] = value
        parsedResponse.append(parsedItem)
    return parsedResponse

def runSuiteQLizer(query, config):
    jsonResponse = suiteqlRequest(query, config)
    parsedResponse = parseJsonResponse(jsonResponse)
    return parsedResponse