# LangChain Chatbot using Flask

LangChain Chatbot is a simple conversational agent built with Flask and LangChain. The chatbot provides a RESTful API for predicting answers based on user input and predefined context using LangChain's powerful language models.

## Routes

### 1. `GET /`

- **Description:** Render the home page.

### 2. `POST /predict`

- **Description:** Predict the answer based on the user's input message using LangChain.
- **Request Payload:**
  ```json
  {
    "message": "User's input message"
  }
  ```
- **Response:**
  ```json
  {
    "answer": "Predicted answer from LangChain"
  }
  ```

## Usage

1. **Install Dependencies:**
   ```bash
   pip install flask langchain
   ```

2. **Run the Flask App:**
   ```bash
   python app.py
   ```

3. **Interact with the Chatbot:**
   - Access the home page at `http://127.0.0.1:5000/`.
   - Send POST requests to `http://127.0.0.1:5000/predict` with the user's input message to get predicted answers.

## LangChain Integration

This chatbot leverages LangChain for its language modeling and retrieval capabilities. Here's a brief overview of the key components:

- **LangChain Models:**
  - Uses GooglePalm language model from LangChain for natural language understanding.

- **Retrieval Models:**
  - Utilizes a FAISS vector store for document retrieval.
  - Employs Hugging Face embeddings for encoding document and input text.

- **Prompt Template:**
  - Defines a prompt template for generating answers based on context and user questions.

## Configuration

- Create a `.env` file with your Google API key:

  ```env
  GOOGLE_API_KEY=your_google_api_key
  ```

- Ensure you have a `faqs.csv` file for loading FAQ data.

## Running Locally

1. **Create Vector Database:**
   ```bash
   python chat.py
   ```

2. **Run the Flask App:**
   ```bash
   python app.py
   ```

3. **Access the Chatbot:**
   - Visit `http://127.0.0.1:5000/` in your browser.
   - Use POST requests to `http://127.0.0.1:5000/predict` for API interaction.

## Contributing

Contributions to improve and extend the functionality of this chatbot are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
