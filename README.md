# med-LLM
> Medical large language model

## Introduction
------------
The provided code implements a Streamlit-based application named "medical_LLM," specifically tailored to facilitate conversational interactions with multiple PDF documents containing medical data and reports. By harnessing the power of natural language processing (NLP) techniques, this application empowers users to ask questions in plain language about the contents of uploaded medical PDFs, subsequently generating pertinent responses based on the document content. 

## How It Works
------------

![PDF-LangChain](https://github.com/Abhisekguha/MED_LLM/assets/119780796/4cb65e38-8013-4a31-91a1-ded3a6eb98a3)

![image](https://github.com/Abhisekguha/MED_LLM/assets/119780796/8dfd5f1d-7b78-4323-88c1-671013656811)


The application follows these steps to provide responses to your questions:

1. PDF Loading: The app reads multiple PDF documents and extracts their text content.

2. Text Chunking: The extracted text is divided into smaller chunks that can be processed effectively.

3. Language Model: The application utilizes a language model to generate vector representations (embeddings) of the text chunks.

4. Similarity Matching: When you ask a question, the app compares it with the text chunks and identifies the most semantically similar ones.

5. Response Generation: The selected chunks are passed to the language model, which generates a response based on the relevant content of the PDFs.

## Dependencies and Installation
----------------------------
To install the MultiPDF Chat App, please follow these steps:

1. Clone the repository to your local machine.

2. Install the required dependencies by running the following command:
   ```
   pip install -r requirements.txt
   ```

3. Obtain an API key from OpenAI and add it to the `.env` file in the project directory.
```commandline
OPENAI_API_KEY=your_secrit_api_key
```

## Usage
-----
To use the MultiPDF Chat App, follow these steps:

1. Ensure that you have installed the required dependencies and added the OpenAI API key to the `.env` file.

2. Run the `main.py` file using the Streamlit CLI. Execute the following command:
   ```
   streamlit run app.py
   ```
3. The application will launch in your default web browser, displaying the user interface.

4. Load multiple PDF documents into the app by following the provided instructions.

5. Ask questions in natural language about the loaded PDFs using the chat interface.

## License
-------
The med-LLM App is released under the [MIT License](https://opensource.org/licenses/MIT).
