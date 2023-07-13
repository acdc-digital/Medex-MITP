# Medex-Public-MITP

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

![Unstructured.IO](https://img.shields.io/badge/Library-Unstructured.io-blue) ![LibraryName](https://img.shields.io/badge/Library-OpenAI-black) ![LibraryName](https://img.shields.io/badge/Library-Langchain-green) ![LibraryName](https://img.shields.io/badge/Library-MyScale-purple) ![LibraryName](https://img.shields.io/badge/Library-LlamaIndex-red)

'https://github.com/acdc-digital/Medex-Public-MITP/wiki/DailyE28090Updates




12/7/2023: I'm excited to have implemented the translation component for ingestion into a playground within Google Colab and I'm able to share that directly by publishing it to the Main page. You can tinker with your own medical questions, and our transformer will analyze pubmed for relevant articles, explode the embeddings based on the User-query, create a hypothetical answer, search pubmeds findings for relevant answers, then combine all the User information into a simple output for contextual understanding. 
<h6>End Update.</h6>

11/7/2023: today we're iomplementing the OpenAI-Cookbook [https://github.com/openai/openai-cookbook]. Recently, I've discovered, "Question/ answering using an API and HyDe." Which I believe will be a sucessful priliminary implementation  of how we're going to transform our User query's. 

![image](Medex/Assets/search_rerank_answer.png)

The concept is simple enough: Step 1: Search; User asks a question and GPT generates a list of potential queries. Search queries are executed in parallel. Step 2: Re-rank; Embeddings for each result are used to calculate semantic similarity to a generated hypothetical ideal answer to the user question. Results are ranked and filtered based on this similarity metric.
Step 3: Answer; Given the top search results, the model generates an answer to the user’s question, including references and links.
This hybrid approach offers relatively low latency and can be integrated into any existing search endpoint, without requiring the upkeep of a vector database.
<h6>End Update.</h6>

10/7/2023: we've added a Quivr playground. You can learn more about Quivr here: [https://github.com/StanGirard/quivr]. I find that Quivr embodies a lot of the same concepts we're trying to achieve, as such, I thought it would be a good idea to keep a simple jipyter notebook on-hand to test functionality and compare against our own. So far, we're already seeing some areas for improvement based on the specifications made available by StanGirard at the repo linked above. 
<h6>End Update.</h6>

9/7/2023: Conceptual visualization chart has been updated to reflect current direction and thought pattern. We'll also begin adding meta-data that will support the user query response. 

We are just getting started uploading and creating the information to make this a coherent space. My best estimate is that we'll be much easier to comprehend by the end of the month (July, 2023). In the meantime, feel free to explore and check-out what we have to offer. Alongside a great initiative for our Medex application, within the 'medex' folder you'll find our curated collection of resources that guide our research and understanding for this project. This includes medex-specific research papers, course-offerings, reading resources, helpful links, and more that will be beneficial to anyone working on q/a applications. Alongside the development of the project, we strive to generate an open platform for not only builders, but researchers, inventors, creatives, and more who can add to the repository in a posititive way. You are a contributor simply by uploading a document that's relevant to the project. 
<h6>End Update.</h6>

Welcome to the Medex public repo, the Public-Version for Open-Source Medex updates, changes, and contributions. Application specific readme notes can be found within the main directory. Application overview (not complete- the below is a placeholder for now until the finished diagram is done): 

![Image](Medex-Comms_Flow5.png)

<h3>Get started</h3> 

```
git clone https://github.com/acdc-digital/Medex-Public-MITP  
```
by going to: ```cd /Users/filepath/Medex-Public-MITP/Medex```  and simply copy and paste into your notebook as needed. The Jupyter Playground will eventually become a Colab notebook, but for now, set up a new environment and following along with the code-blocks. We'll keep the blocks in the playground as the latest stable version, as other documents may continue to get tinkered with throughout development.

<h1>Hello! Welcome to Medex Playground. A new starting point on our application journey.</h1>

<h1> Latest Update: 9/7/2023 </h1>

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

<h1>Final Words 🎉</h1>

Welcome to the Medex community! We're thrilled to have you here and we can't wait to see how you contribute to this project. Remember, change doesn't happen from the top down, but from the bottom up. So let's make a difference, together.
