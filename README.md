

# Welcome to Medex: turning medical language to everyday speak  

![logo1](https://github.com/acdc-digital/Medex-Public-MITP/blob/main/Medex/Assets/Group%203.png)<h2>MITP: Medical Information Training & Personalization</h2>

[![Langchain](https://img.shields.io/badge/powered%20by-Langchain-GreenYellow)](https://github.com/langchain-ai/langchain) [![Unstructured.IO](https://img.shields.io/badge/Unstructured.io-blue)](https://github.com/Unstructured-IO/unstructured) [![Deeplake](https://img.shields.io/badge/Deep%20Lake%20-ff5a1f.svg)](https://github.com/activeloopai/deeplake) [![Cloaked](https://img.shields.io/badge/CloakedAI-maroon)](https://ironcorelabs.com/products/cloaked-ai/)

* Medex-MITP: Empowering patients with artificial intellegence. 
* MITP: Stands for Medical Information Training & Personalization.
* Vector-db Encrypted: Uses CloakedAI for additional privacy protection.
* Objective: 

Despite decades of development in medicine and the growing interest in precision healthcare, 
the vast majority of diagnoses happen once patients begin to show noticeable signs of illness. Early 
indication and detection of diseases, however, can provide patients and carers with the chance of early 
intervention, better disease management, and efficient allocation of healthcare resources.


<h4>Daily updates have moved to our Wiki, which otherwise is being used as a conceptual journal of types: https://github.com/acdc-digital/Medex-Public-MITP/wiki/Daily%E2%80%90Updates</h4>

<h2>What is Medex?</h2>
  
Medex is an open-source project that leverages artificial intelligence to transform how we access and understand medical information. It acts as a bridge between complex medical literature and the people who need this information.

<h2>How Does It Work?</h2>

Medex uses a sophisticated AI model to take medical queries, search through PubMed articles, and provide clear, insightful responses. It's like having a personal medical researcher. Additionally, Medex generates hypothetical answers based on the query, searches PubMed for relevant findings, and combines this information for contextual understanding. This approach offers low latency and can be integrated into any existing search endpoint without requiring a vector database.

But that's not all. Medex goes a step further by generating hypothetical answers based on your query, searching PubMed for relevant findings, and combining all this information into a simple output for contextual understanding. It's a hybrid approach that offers relatively low latency and can be integrated into any existing search endpoint, without requiring the upkeep of a vector database.

<h2>Why Medex?</h2>

Medex aims to make healthcare information more accessible, understandable, and user-friendly. It's about breaking barriers between people and the medical information they need, empowering individuals to make informed health decisions.

<h2>Join the Mission. 🤝</h2>

But Medex isn't just about technology. It's about people like you. Whether you're a coder, a scientist, or someone who believes in making healthcare information more accessible, you're welcome here. We believe in the power of community and collaboration, and we know that the best ideas come from diverse perspectives coming together to solve a common problem.

So, roll up your sleeves and dive into this project. Contribute your code, share your ideas, and help us make Medex even better. Together, we can make a difference in the world of healthcare.

<h1>Daily-Updtae Highlights:</h1>
<h2> Tournament Champions! Milvus & Cohere 🧑🏼‍🚀 🚀 </h2>

After a fun day of organizing and running an experimental evaluation tournament, we've come to find Milvus VectorStore and Cohere LLM to be the tools of choice for Medex. More details on these tournaments can be found in our daily-updates Wiki, and within the individual Tournament Results, https://github.com/acdc-digital/Medex-Public-MITP/wiki/LLM-Tournament and https://github.com/acdc-digital/Medex-Public-MITP/wiki/VectorStore-Tournament. 

<h4>ai-Utility and Langchain updates</h4>
I found this cool website; [ai-utils] https://ai-utils.dev/concept/ which seems to have some integration information, and described as, "A TypeScript-first library for building AI apps, chatbots, and agents." on their Github page here: https://github.com/lgrammel/ai-utils.js. 

Also, Langchain recently had a couple cool improvements to their infrastructure including improved document in some areas, added/ adding new integrations, and publishing a very helpful integrations specific page. I really like how Langchain is evolving in deliverying information to their Users. You can find the integrations page here: https://integrations.langchain.com/.
<h6>End Article.</h6>

<h4>The OpenAI Cookbook</h4>
The OpenAI-Cookbook [https://github.com/openai/openai-cookbook] has been an incredible resource. Recently, I've discovered, "Question/ answering using an API and HyDe." Which I believe will be a sucessful priliminary implementation  of how we're going to transform our User query's. 


![image](Medex/Assets/search_rerank_answer.png)

The concept is simple enough: Step 1: Search; User asks a question and GPT generates a list of potential queries. Search queries are executed in parallel. Step 2: Re-rank; Embeddings for each result are used to calculate semantic similarity to a generated hypothetical ideal answer to the user question. Results are ranked and filtered based on this similarity metric.
Step 3: Answer; Given the top search results, the model generates an answer to the user’s question, including references and links.
This hybrid approach offers relatively low latency and can be integrated into any existing search endpoint, without requiring the upkeep of a vector database.
<h6>End Article.</h6>

<h4>Visualizing Medex in Figjam</h4>
The below is a placeholder for now until the finished diagram is done. We're slowly working through the visualization of the program in order to understand its User-Centric attributes. We want to esnure that Medex is not only the engine, but the whole vehicle that helps our Users get the information they need, when they need it. 

![Image](https://github.com/acdc-digital/Medex-Public-MITP/blob/main/Medex/Assets/Medex-Comms_Flow5.png)
<h6>End of Article.</h6>

<h2>Getting Started w/ Medex 🚀🚀🚀</h2> 

To get started with Medex, simply clone this repository and follow the instructions provided in the repository's README. The project is in active development, so don't hesitate to ask questions, report issues, or suggest improvements. We're all here to learn and grow together.

```
git clone https://github.com/acdc-digital/Medex-Public-MITP  
```
```cd /Users/filepath/Medex-Public-MITP/Medex```  and simply copy and paste into your notebook as needed. The Jupyter Playground will eventually become a Colab notebook, but for now, set up a new environment and follow along with the code-blocks. We'll keep the blocks in the playground as the latest stable version, as other documents may continue to get tinkered with throughout development and may or may-not be runnable at certain times. 

<h1>Final Words 🎉</h1>

Welcome to the Medex community! We're thrilled to have you here and we can't wait to see how you contribute to this project. Remember, change doesn't happen from the top down, but from the bottom up. So let's make a difference, together.
