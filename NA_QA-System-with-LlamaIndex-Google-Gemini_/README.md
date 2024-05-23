# QA-System-with-LlamaIndex-Google-Gemini

The following projects builds the simple Question-Answering system using llamaindex framework and Google Gemini model. 

1. The Data used here is a text file which would be ingested in our in memory vector store.
2. Further using Mlops we have made directory files like QAwithPDF, setup.py, logger.py and exception.py.
3. QAwithPDF is like an internal local package with the __init__.py file in it- having the modules in it defined:
data_ingestion : Includes the function defined in it as to how to ingest the data.
embedding : Includes the fucntion defined to use the embed model through gemini. This essentially converts the text data to numerical repressentation of the text we pass.
model_api : Includes the llm model ie. google-pro to be used for our project.
4. Logger.py file includes the logs that we do while execution of code.
5. Exception.py file includes any errors that we face during the execution of the code.
6. Streamlit.py makes a simple question- answering framwork that gives us the ability to load the file and uses the llm and embed model to retrieve the answer from that specific pdf and uses llm to synthesis the response.
7. setup.py is the file used for downloading any inner package/local package in our current virtual environment.
