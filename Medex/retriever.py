import os
import json
import requests

# Set API key as environment variable for security
os.environ['UNSTRUCTURED_API_KEY'] = "<YOUR_API_KEY>"

def search_vectorstore(query):
    # API endpoint for vectorstore similarity search
    url = "https://api.unstructured.io/general/v0/general"

    # Set the headers and parameters for the API request
    headers = {
        "accept": "application/json",
        "Content-Type": "multipart/form-data",
        "unstructured-api-key": os.environ['UNSTRUCTURED_API_KEY']
    }
    params = {
        "strategy": "fast",
        "files": "",
        "output_format": "json"
    }

    # Make the API request with the query as the file content
    response = requests.post(url, headers=headers, params=params, data=query)

    # Parse the response JSON
    results = json.loads(response.text)

    # Return the search results
    return results

def retrieve_from_index(query):
    # Retrieve documents from the index based on the query
    results = search_vectorstore(query)

    # Return the results
    return results

def query_retriever(query):
    # Call the retrieve_from_index function to get the results
    results = retrieve_from_index(query)

    # Print the results in a condensed format
    print("Search Results:")
    for result in results:
        print(f"- Document: {result['metadata']['filename']}")
        print(f"  Type: {result['type']}")
        print(f"  Text: {result['text']}")
        print()

# Example usage
query = "example query"
query_retriever(query)
