from llama_index.core import SimpleDirectoryReader
import sys
from exception import customexception
from logger import logging

def load_data(data):
    """load pdf documents from a specific directory 
    """
    try:
        logging.info("data loading started...")
        loader = SimpleDirectoryReader("Data") #reading the data
        documents = loader.load_data()     #loading the data 
        logging.info("data loading completed...")
        return documents
    except Exception as e: #exception is run time errors are captured here
        logging.info("exception in loading data...")
        raise customexception(e,sys)