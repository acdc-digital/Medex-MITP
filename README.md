# Medex-Public-MITP
<h2>Hello! Welcome to the Medex Public Playground. A new starting point on our application journey.</h2>

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white) 

![Unstructured.IO](https://img.shields.io/badge/Library-Unstructured.io-blue) ![LibraryName](https://img.shields.io/badge/Library-OpenAI-black) ![LibraryName](https://img.shields.io/badge/Library-Langchain-green) ![LibraryName](https://img.shields.io/badge/Library-MyScale-purple) ![LibraryName](https://img.shields.io/badge/Library-LlamaIndex-red)

<h4>Daily updates have moved to our Wiki: https://github.com/acdc-digital/Medex-Public-MITP/wiki/Daily%E2%80%90Updates</h4>


The OpenAI-Cookbook [https://github.com/openai/openai-cookbook] has been an incredible resource. Recently, I've discovered, "Question/ answering using an API and HyDe." Which I believe will be a sucessful priliminary implementation  of how we're going to transform our User query's. 


![image](Medex/Assets/search_rerank_answer.png)

The concept is simple enough: Step 1: Search; User asks a question and GPT generates a list of potential queries. Search queries are executed in parallel. Step 2: Re-rank; Embeddings for each result are used to calculate semantic similarity to a generated hypothetical ideal answer to the user question. Results are ranked and filtered based on this similarity metric.
Step 3: Answer; Given the top search results, the model generates an answer to the user’s question, including references and links.
This hybrid approach offers relatively low latency and can be integrated into any existing search endpoint, without requiring the upkeep of a vector database.
<h6>End Article.</h6>



Welcome to the Medex public repo, the Public-Version for Open-Source Medex updates, changes, and contributions. Application specific readme notes can be found within the main directory. Application overview (not complete- the below is a placeholder for now until the finished diagram is done): 

![Image](Medex-Comms_Flow5.png)

<h3>Get started</h3> 

```
git clone https://github.com/acdc-digital/Medex-Public-MITP  
```
by going to: ```cd /Users/filepath/Medex-Public-MITP/Medex```  and simply copy and paste into your notebook as needed. The Jupyter Playground will eventually become a Colab notebook, but for now, set up a new environment and following along with the code-blocks. We'll keep the blocks in the playground as the latest stable version, as other documents may continue to get tinkered with throughout development.

<h1>Hello! Welcome to Medex Playground. A new starting point on our application journey.</h1>


<h1>Final Words 🎉</h1>

Welcome to the Medex community! We're thrilled to have you here and we can't wait to see how you contribute to this project. Remember, change doesn't happen from the top down, but from the bottom up. So let's make a difference, together.
