# Quivr Playground

This directory contains the Quivr Playground code, which is a powerful tool for exploring and experimenting with Quivr functionality. 

## Overview

The Quivr Playground is designed to provide a user-friendly interface for interacting with the Quivr system. It allows users to perform various operations, such as querying the vectorstore index, retrieving documents, and analyzing search results. The code is written in Python and utilizes several libraries and APIs to achieve its functionality.

## Key Features

The Quivr Playground offers the following key features:

1. Vectorstore Index Search: Users can perform similarity searches on the vectorstore index to find relevant documents based on a query.

2. Document Retrieval: The code provides a function to retrieve documents from the index based on a query.

3. Condensed Search Results: The `query_retriever` function prints the search results in a condensed format, displaying the document metadata, type, and text.

4. Integration with OpenAI: The code integrates with OpenAI's language models and embeddings to enhance the search and retrieval capabilities.

5. Progress Bar: The `process_files` function utilizes the `tqdm` library to display a progress bar while processing PDF files.

## Usage

To use the Quivr Playground, follow these steps:

1. Set the necessary API keys as environment variables for security.

2. Configure the MyScale settings and initialize the LlamaIndex components.

3. Call the `process_files` function to process PDF files in a specified directory. This function splits the documents into chunks, generates embeddings, and adds them to the vectorstore index.

4. Use the `query_retriever` function to perform searches and retrieve documents based on a query.

## Dependencies

The Quivr Playground relies on the following dependencies:

- Python: The code is written in Python and requires a Python interpreter to run.

- OpenAI: The code integrates with OpenAI's language models and embeddings.

- langchain: A library for language processing and document handling.

- tqdm: A library for displaying progress bars.

- requests: A library for making HTTP requests.

Please make sure to install these dependencies before running the code.

## Feedback and Contributions

We welcome your feedback and contributions to the Quivr Playground. If you encounter any issues or have suggestions for improvement, please let us know. You can also join our community slack for further discussions.

Thank you for using the Quivr Playground!

