
Overview

This AI-powered application allows users to analyze multiple news articles simultaneously by providing URLs, then ask natural language questions to extract insights and information across sources.

Project Highlights

✅ Web Content Extraction & Processing

Extracted and processed content from multiple news URLs using LangChain's WebBaseLoader with RecursiveCharacterTextSplitter for optimal context retention in a streamlined pipeline.

✅ Vector Database Implementation with FAISS

Implemented Facebook AI Similarity Search (FAISS) with OpenAI embeddings for efficient semantic retrieval, using session-based storage to maintain context throughout user interactions.

✅ LLM-powered Question Answering System

Created an information extraction system with OpenAI's language models via LangChain's RetrievalQAWithSourcesChain, providing source attribution and balancing accuracy with token optimization.

✅ Interactive Streamlit Web Application

Built an intuitive UI with Streamlit featuring URL inputs, processing indicators, and query functionality with real-time feedback mechanisms in a responsive layout.
Tech Stack & Libraries Used

🔹 LangChain (WebBaseLoader, RecursiveCharacterTextSplitter, RetrievalQAWithSourcesChain)

🔹 FAISS (Vector Database)

🔹 OpenAI (Embeddings & Language Model)

🔹 Streamlit (Web UI)

Installation and Setup
Prerequisites

Python 3.7 or higher

pip (Python package installer)

Step 1: Clone the Repository
bashCopygit clone [your-repository-url]
cd [repository-name]

Step 2: Install Dependencies
Install all required packages from the requirements.txt file:
bashCopy  pip install -r requirements.txt

Step 3: Set Up Environment Variables
Create a .env file in the project root directory and add your OpenAI API key:
CopyOPENAI_API_KEY=your_api_key_here
You can get an API key from the OpenAI website.

Step 4: Run the Application
Start the Streamlit application:
bashCopy streamlit run main.py
The application will open in your default web browser. If it doesn't open automatically, you can access it at http://localhost:8501.
Usage

Enter news article URLs in the input field (one URL per line) 

Click "Process URLs" to extract and analyze the content

Ask natural language questions about the articles in the query box

View the AI's responses with source attribution

Features

Multi-source news analysis ,
Natural language query capability ,
Source attribution for answers ,
Session-based context retention ,
Responsive and intuitive user interface

Troubleshooting

API Key Issues: Ensure your OpenAI API key is correctly set in the .env file.

Package Installation Problems: Make sure you're using a compatible Python version and that all dependencies are installed correctly.

Streamlit Connection Issues: Check if port 8501 is available on your machine.

URL Processing Errors: Verify that the provided URLs are accessible and contain valid content.
