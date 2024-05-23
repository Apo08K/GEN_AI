import streamlit as st
from  QAWithPDF.data_ingestion import load_data
from   QAWithPDF.embedding import download_gemini_embedding
from QAWithPDF.model_api import load_model


def main():
    st.set_page_config("QA")

    doc = st.file_uploader("upload your document")

    st.header("QA with documents(information retriveal)")

    user_question = st.text_input("Ask your question?")

    if st.button("submit and process"):  #This line checks if the "submit and process" button is clicked.
        with st.spinner("processing.."):   #with in this way ensures that the spinner animation starts before the code block is executed and stops after the code block finishes execution
            document = load_data(doc)
            model= load_model()
            query_engine = download_gemini_embedding(model,document)

            response = query_engine.query(user_question)

            st.write(response.response)

if __name__=="__main__":
    main()