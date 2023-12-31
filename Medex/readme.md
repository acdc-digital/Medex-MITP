<h1>Hello! Welcome to Medex Playground. A new starting point on our application journey.</h1>

<h1> Latest Update: 9/7/2023 </h1>

July 9, 2023 (evening); signing-off, the integration of the chat-assistant was pretty cool. I'm excited to continue trying its functionality. 

July 9, 2023: We had to take a step back today in order to continue some testing methods. This reduction in our code-base included a llama-index wrapper that would allow us to use a retriever from the same library. We will conitnue to explore this method. However, I wanted to ensure our participants had a working ingest.py file in the meantime. Now, we can ingest the source_docs folder, and the documents will be converted to .json files per use of the unstructured.io document-api library.

Today, we're going to expand the ingestion pipeline by including multiple formats other than the .pdf format we've been using for testing to date.

Update: Noon; July 9, 2023

Today we're thinking about the strategic action for what we're trying to retrieve. Our key elements for retrieval include, but are not limited to;

a. quality of retrieval response; the chat-assistant needs to be able to retrieve the query, translate to user-knowledge-level, assess hypothetical/similar embeddings, evaluate multiple retrieval responses, and respond to the User with a coherent reply and appropriate meta-data sources. a.a. the appropriate benchmarks and evaluation methods will need to be in place for this. this means collecting responses from other LLM's for comparison, and determining evaluation criteria for quantifying responses (such as to make a leaderboard in which our model should always strive to be at the top spot).

b. along with retrieval, the user query translation is important. I believe we only need to make some simple additions to ensure this working even slightly well, and we'll work on the robust-ness of the application following successful and passing benchmarks and tests.

c. I think we're using a retrieve function in Langchain. But I've also found some interesting methods in Llama-Index. I think we need to begin creating a chart for evaluating the methods available, and determining exactly how we want to achieve the main purpose of forward/backward layman-medical/medical-layman. We can begin by creating a list of possible retrievers that have either partial functionality we can add to, or whole components that will need to be embedded within our source code.

d. I am concerned about hallucinations given the medical environment. So, just as important as the techniques being used to transform the user query, we also need to be cognitive of where the retrieval information is coming from and what the context of that document/ file is. We know agents/ (openai) functions can reduce the likelihood of hallucinations- so that is the direction of our continued research in this space.
<h6>End Update.</h6>

Update: July 7, 2023 

To get started, simply clone this repo-and enter your key values in the playground. You should immediately (upon completion of our initial setup here) you should be able to enter your configurations into the playground-codeblocks as needed, and then being q/a over your data. Given this is day #2 of our project, the code is still being updated. Keep in mind, this means we'll begin seeing health/medical specific components beginning to be integrated in the coming weeks. As time progresses, the less effective generic data/documents will be, and the more effective health/medical specific data/documents will be.

Last night, and after evaluation and further consideration I've decided to implement the Llama-Index. The considerations for approval are the following:
a. the Llama-Index uses new technologies to integrate query revisions, such as the Transform Query function, which takes a User-Query and transforms it into a query that is more likely to return the desired results. 
b. Hypothetical Document Embeddings (HyDE) query transform; HyDe is a new method for transforming queries that uses a neural network to generate a query that is more likely to return the desired results. It takes the User query, provides an answer, and then uses those answers to generate similar embeddings. 
c. easily integrates with our existing Langchain and Medex-Index.
d. improved ingestion function such as Transformer-Embedding Accleration, which is a new method for accelerating the embedding generation process. It uses a transformer model to generate embeddings for each chunk of text, which are then used to index the document. This allows the application to quickly find similar documents or chunks based on their embeddings. Query Splitting which enables the model to query specific chunks, in specific documents, and return the results. Or, even Query Transformations where the query is expanded into 5+ relevant queries, all answers are searched within the embeddings, and then the best anwer is formed. 

Generally, I believe the implementation of the Llama-Index will help to substantially accelerate our progress, while being able to provide moderate improvements to our existing models in complex areas of forward/backward document processing. 
<h6>End Update.</h6>

Last (first) update: 6/7/23; These documents are being continuously updated. Today (6/7/23) was the first day of the project release. While I've been working dilligently in the background, it's always been a goal of mine to cerate a meaningful public repository. I'm excited to share this with you. I hope you enjoy it. 

I'm having some difficulty with the privacy concerns related to the sample_patient_files that I've been recieving. As of today (7,7,2023) - I'm planning to blackout the privacy details of these documents so that the samples can be used by everyone. However, given the length, 2,000+ pages per document, it may take some time to ensure this is completed efficiently and according to our standards for the privacy of our Users, even in prototyping stages. In the meantime, I will not be pushing the sample-patient-files until they're ready/ likely next week. 
<h6>End Update.</h6>

[]: # Path: readme.md
[]: # See knowledge-base snippets from Medex/Course-Work/Helpful_Links and Cool_Repos, followed by relevant coursework (free and paid), model catalogue and downloadable products. Sample patient files will be uploaded soon. 
[]: # The .env requirements and setup instructions for the virtual environment and .env keys, you can check the .env file in the <Medex> directory, and/or the my-venv instructions within the jupyter-playground. I'll piece together a more formiddable instruction set, with new files that are easier to navigate in the near future. 
[]: # 

<h1>Project Document/Script Descriptions</h1>

- Ingest.py

The process_files function in the ingest.py script is responsible for processing all the PDF files in a given directory. It does this by creating a UnstructuredAPIFileLoader for each PDF file, which is used to load the document and split it into chunks. These chunks are then embedded using the OpenAIEmbeddings and added to the MyScale index. The embeddings are also saved to a JSON file for each document.

The improvements made to this function are primarily focused on the use of partitioning bricks from the Unstructured library. Partitioning bricks are used to extract structured content from raw unstructured documents, breaking them down into elements such as Title, NarrativeText, and ListItem. This allows the application to decide what content to keep for its specific use case.

Here's how the ingestion work:

Document Loading: The UnstructuredAPIFileLoader is used to load the document. This loader uses the Unstructured library to extract structured content from the raw unstructured document. This is done using partitioning bricks, which break the document down into elements such as Title, NarrativeText, and ListItem.
Document Splitting: The CharacterTextSplitter is used to split the document into chunks. This is necessary because language models like GPT-3 have a maximum token limit, and large documents need to be split into smaller chunks to be processed.
Embedding Generation: The OpenAIEmbeddings is used to generate embeddings for each chunk. These embeddings are vector representations of the text that capture semantic meaning and can be used for tasks like similarity search.
Indexing: The MyScale index is used to store and retrieve the embeddings. This allows the application to quickly find similar documents or chunks based on their embeddings.
Metadata Tracking: The Unstructured library tracks a variety of metadata about the elements extracted from documents. This metadata can be used to filter document elements based on criteria of interest, such as page number or source file.
