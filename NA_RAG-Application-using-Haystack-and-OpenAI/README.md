# NA_RAG-Application-using-Haystack-and-OpenAI

In this project, I explored the working of a Rag application using Haystack framework and OpenAI llm model.

On my research, I found Langchain to be more efficient than Haystack but wanted to explore more of Haystack on its front. 

1. In this repo, I took the dataset from hugging face.
2. Stored the meta and content of this data in a Document format that can be understood by the Haystack.
3. Initialised the embedding model from huggingface
4. Created the embeddings of the document created.
5. stored the embeddings in the documentstore.
6. Initialised a different embedding model for the user query to create its embedding.
7. Created an inmemory based retriver that will store all the embeddings.
8. Now for any rag application, we need to create a chat template. Created that.
9. Using open api key for genertaing the generation model ie. the llm that would help in synthesising the response.
10. Built the rag pipeline and combined all the components related to prompt, llm, retriever.
11. Get the response at the end. 
