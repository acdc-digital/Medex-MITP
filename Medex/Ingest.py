import os
import json
from tqdm import tqdm

# Import necessary modules from langchain
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredAPIFileLoader
from langchain.vectorstores import MyScale, MyScaleSettings

# Set API keys as environment variables for security
os.environ['OPENAI_API_KEY'] = "sk-hXivM******************************1oebUTTQ"
os.environ['MYSCALE_API_KEY'] = "6B7*******************************27p"

# Configure MyScale settings
# MyScale is a vector store used for storing and retrieving embeddings
config = MyScaleSettings(host="**********12345.us-east-1.aws.myscale.com", port=443, username="******acdc.digital", password="passwd_NA*****************GNt")
index = MyScale(OpenAIEmbeddings(), config)

def process_files(directory):
    # Initialize an empty list to hold file loaders
    file_loaders = []

    # Loop through all files in the directory
    for filename in os.listdir(directory):
        # Check if the file is a PDF
        if filename.endswith(".pdf"):
            # Construct the full file path
            file_path = os.path.join(directory, filename)

            # Create a file loader for the PDF file
            # The file loader uses the MyScale API key and a 'fast' strategy
            file_loader = UnstructuredAPIFileLoader(
                file_path,
                api_key=os.environ['MYSCALE_API_KEY'],
                strategy="fast",  # use the 'fast' strategy
                request_kwargs={"timeout": 600}  # set a timeout of 600 seconds
            )

            # Add the file loader to the list
            file_loaders.append(file_loader)

    # Create an embeddings object and a text splitter
    embeddings = OpenAIEmbeddings()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=5500, chunk_overlap=1000)

    # Wrap your file_loaders with tqdm for progress bar
    # Loop through each file loader and process the file
    for loader in tqdm(file_loaders, desc="Processing files"):
        # Load the document
        doc = loader.load()

        # Split the document into chunks
        docs = text_splitter.split_documents(doc)

        # Initialize an empty dictionary to hold the embeddings
        doc_embeddings = {}

        # Loop through each chunk
        for i, d in enumerate(docs):
            # Set the source metadata to the file path
            d.metadata = {"source": loader.file_path}

            # Generate embeddings for the chunk and store them in the dictionary
            doc_embeddings[i] = embeddings.embed_documents([d.page_content])

            # Add the chunk to the MyScale index
            index.add_documents([d])

        # Write the embeddings to a JSON file
        with open(f"{loader.file_path}.json", "w") as f:
            f.write(json.dumps(doc_embeddings, default=str))

# Directory containing PDF files to process
directory = "/***********/acdc-digital/Medex_Drafts/medex_7.1.23/medexical/source_docs"
# Call the process_files function to process all PDF files in the directory
process_files(directory)