import os
import json
from langchain.vectorstores import MyScale, MyScaleSettings
from langchain.embeddings.openai import OpenAIEmbeddings

# Set API keys as environment variables for security
os.environ['OPENAI_API_KEY'] = "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"
os.environ['MYSCALE_API_KEY'] = "6B71NumcMB7QXcguTapGBjCEWqM27p"

# Configure MyScale settings
config = MyScaleSettings(host='msc-3f5d0ca4.us-east-1.aws.myscale.com', port=443, username='smatty662', password='passwd_CAdIn9GSXH7GNt')
index = MyScale(OpenAIEmbeddings(), config)

def retrieve_from_index(query):
    # Retrieve documents from the index based on the query
    results = index.retrieve_documents(query)

    # Return the results
    return results

def query_retriever(query):
    # Call the retrieve_from_index function to get the results
    results = retrieve_from_index(query)

    # Print the results
    print("Search Results:")
    for result in results:
        print(f"- Document: {result.metadata['source']}")
        print(f"  Score: {result.score}")
        print(f"  Content: {result.content}")
        print()

# Example usage
query = "example query"
query_retriever(query)
