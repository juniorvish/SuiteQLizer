import requests
from suiteql import suiteqlRequest, parseJsonResponse
from config import API_URL, API_HEADERS

def displayResults(jsonResponse):
    for result in jsonResponse:
        print(result)

def runSuiteQLizer():
    query = input("Enter your SuiteQL query: ")
    response = suiteqlRequest(query, API_URL, API_HEADERS)
    jsonResponse = response.json()
    parsedJsonResponse = parseJsonResponse(jsonResponse)
    displayResults(parsedJsonResponse)

if __name__ == "__main__":
    runSuiteQLizer()