import os
import streamlit as st
import time
from langchain_openai import OpenAI
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env (especially openai api key)

st.title("News Research Tool 📈")
st.sidebar.title("News Article URLs")

# Initialize session state to store the vectorstore
if 'vectorstore' not in st.session_state:
    st.session_state.vectorstore = None

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i + 1}")
    if url:  # Only append non-empty URLs
        urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")

main_placeholder = st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked and urls:  # Only process if there are URLs
    try:
        # load data using WebBaseLoader instead of UnstructuredURLLoader
        main_placeholder.text("Data Loading...Started...✅✅✅")
        loader = WebBaseLoader(urls)
        data = loader.load()

        if not data:
            main_placeholder.error("No data was loaded from the provided URLs. Please check if the URLs are valid.")
        else:
            # split data
            text_splitter = RecursiveCharacterTextSplitter(
                separators=['\n\n', '\n', '.', ','],
                chunk_size=1000
            )
            main_placeholder.text("Text Splitter...Started...✅✅✅")
            docs = text_splitter.split_documents(data)

            # create embeddings and save it to FAISS index
            main_placeholder.text("Embedding Vector Started Building...✅✅✅")
            embeddings = OpenAIEmbeddings()

            if docs:
                # Store directly in session state instead of pickling
                st.session_state.vectorstore = FAISS.from_documents(docs, embeddings)
                time.sleep(2)
                main_placeholder.success("Processing complete! You can now ask questions about the articles.")
            else:
                main_placeholder.error(
                    "No documents were created after splitting. The articles might be too short or in an unsupported format.")
    except Exception as e:
        main_placeholder.error(f"An error occurred: {str(e)}")

query = st.text_input("Question: ")  # Moved outside the main_placeholder to keep it visible

if query:
    if st.session_state.vectorstore is not None:
        try:
            chain = RetrievalQAWithSourcesChain.from_llm(llm=llm, retriever=st.session_state.vectorstore.as_retriever())
            result = chain({"question": query}, return_only_outputs=True)

            # result will be a dictionary of this format --> {"answer": "", "sources": [] }
            st.header("Answer")
            st.write(result["answer"])

            # Display sources, if available
            sources = result.get("sources", "")
            if sources:
                st.subheader("Sources:")
                sources_list = sources.split("\n")  # Split the sources by newline
                for source in sources_list:
                    if source.strip():  # Only display non-empty sources
                        st.write(source)
        except Exception as e:
            st.error(f"Error when processing your question: {str(e)}")
    else:
        st.warning("Please process some URLs before asking questions.")