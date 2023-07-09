<h1>HuggingFace Models: https://huggingface.co/models </h1>

<h4>Long-Llama_250k</h4>
1. https://huggingface.co/syzymon/long_llama_3b; LongLLaMA is an OpenLLaMA model finetuned with the FoT method, with three layers used for context extension. Crucially, LongLLama is able to extrapolate much beyond the context length seen in training: 8k. E.g., in the key retrieval task, it can handle inputs of length 256k.
<h4>Wizard_13B</h4>
2. https://huggingface.co/ehartford/Wizard-Vicuna-13B-Uncensored/tree/main; This is wizard-vicuna-13b trained with a subset of the dataset - responses that contained alignment / moralizing were removed. The intent is to train a WizardLM that doesn't have alignment built-in, so that alignment (of any sort) can be added separately with for example with a RLHF LoRA.
<h4>BioMedLM 2.7B</h4>
3. https://huggingface.co/stanford-crfm/BioMedLM/tree/main; BioMedLM 2.7B is new language model trained exclusively on biomedical abstracts and papers from The Pile. This GPT-style model can achieve strong results on a variety of biomedical NLP tasks, including a new state of the art performance of 50.3% accuracy on the MedQA biomedical question answering task.
<h4>Instructor-XL</h4>
4. https://huggingface.co/hkunlp/instructor-xl; We introduce Instructor👨‍🏫, an instruction-finetuned text embedding model that can generate text embeddings tailored to any task (e.g., classification, retrieval, clustering, text evaluation, etc.) and domains (e.g., science, finance, etc.) by simply providing the task instruction, without any finetuning. Instructor👨‍ achieves sota on 70 diverse embedding tasks! The model is easy to use with our customized sentence-transformer library. For more details, check out our paper and project page!
<h4>Longformer</h4>
5. https://huggingface.co/allenai/longformer-base-4096; Longformer is a transformer model for long documents. It is made up of a modified version of the standard attention layer (which scales linearly with sequence length) and a local sliding window attention layer (which scales linearly with window size). The model is trained on a new corpus of 1.2 million documents with a total of 2.1 billion words. It achieves state-of-the-art results on summarization and question answering.	
<h4>Flacon-40B_Instruct</h4>
6. https://github.com/pinecone-io/examples/blob/master/generation/llm-field-guide/falcon-40b/falcon-40b-chatbot.ipynb; Falcon-40B is a large-scale language model trained on 40 billion tokens from the Common Crawl corpus. It is trained with the Instruct method, which allows it to be fine-tuned to perform well on a variety of tasks. This notebook demonstrates how to fine-tune Falcon-40B to perform well on a chatbot task.
