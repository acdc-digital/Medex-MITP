* Last (first) update: 6/7/23; These documents are being continuously updated. Today (6/7/23) was the first day of the project release. While I've been working dilligently in the background, it's always been a goal of mine to cerate a meaningful public repository. I'm excited to share this with you. I hope you enjoy it. 

[]: # Path: readme.md

<h1>Hello! Welcome to Medex Playground. A new starting point on our application journey.</h1>

<h2>Ingest.py</h2>

<h4>The process_files function in the ingest.py script is responsible for processing all the PDF files in a given directory. It does this by creating a UnstructuredAPIFileLoader for each PDF file, which is used to load the document and split it into chunks. These chunks are then embedded using the OpenAIEmbeddings and added to the MyScale index. The embeddings are also saved to a JSON file for each document.

The improvements made to this function are primarily focused on the use of partitioning bricks from the Unstructured library. Partitioning bricks are used to extract structured content from raw unstructured documents, breaking them down into elements such as Title, NarrativeText, and ListItem. This allows the application to decide what content to keep for its specific use case.

Here's how the ingestion work:

Document Loading: The UnstructuredAPIFileLoader is used to load the document. This loader uses the Unstructured library to extract structured content from the raw unstructured document. This is done using partitioning bricks, which break the document down into elements such as Title, NarrativeText, and ListItem.
Document Splitting: The CharacterTextSplitter is used to split the document into chunks. This is necessary because language models like GPT-3 have a maximum token limit, and large documents need to be split into smaller chunks to be processed.
Embedding Generation: The OpenAIEmbeddings is used to generate embeddings for each chunk. These embeddings are vector representations of the text that capture semantic meaning and can be used for tasks like similarity search.
Indexing: The MyScale index is used to store and retrieve the embeddings. This allows the application to quickly find similar documents or chunks based on their embeddings.
Metadata Tracking: The Unstructured library tracks a variety of metadata about the elements extracted from documents. This metadata can be used to filter document elements based on criteria of interest, such as page number or source file.</h4>