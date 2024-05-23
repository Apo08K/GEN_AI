# NA_RAG-Application-using-Langchain-Mistral-AI-and-Weviate-db


This file creates a rag application using langchain framework, Vector database as Weavite database and LLM as Mistral-AI accessed through Hugging Face. 

1. Firstly we create the weavite client accessing the weavite vector store cloud through its cluster and api key. This vector store would help us in maintaining the embeddings of the chunks of the text of the single of the document that we extracted.

2. We use embeding model as sentence-transformers/all-mpnet-base-v2 from Hugging Face as the embedding model for our document chunks /doc.

3. After loading the text content from PyPDFLoader, we created the chunks of the specific document using RecursiveCharacterTextSplitter.

4. This essentially creates the chunk of sentences with each chunk size of 1000 tokens and chunk overlap of 20 tokense.

5. For generating the LLM response, we create the template of the chatprompt.
   
6. And used the llm model of mistral -7B for generating the respoonse.

   
7. After this we create the rag chain that combines the prompt, model and output parser to give the response to the asked query. 
