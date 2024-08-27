# ChatLlamaAPI Chatbot with FastAPI

This project implements a web-based chatbot using the ChatLlamaAPI from Langchain and FastAPI. The chatbot maintains a conversation history and provides a RESTful API for interaction.

## Features

- Web-based RESTful API using FastAPI
- Conversation history for context-aware responses
- Easy integration with ChatLlamaAPI

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.7 or higher installed on your system
- A Llama API key (sign up at [Llama API website](https://www.llamaapi.com/))

## Installation

1. Clone this repository or download the `main.py` file.

2. Install the required Python packages:

   ```
   pip install langchain fastapi uvicorn
   ```

3. Set up your Llama API key:
   - Open `main.py` in a text editor
   - Replace `"your-api-key-here"` with your actual Llama API key:
     ```python
     os.environ["LLAMA_API_KEY"] = "your-actual-api-key"
     ```

## Usage

To run the chatbot server:

1. Open a terminal or command prompt.

2. Navigate to the directory containing `main.py`.

3. Run the following command:

   ```
   uvicorn main:app --reload
   ```

4. The server will start, typically on `http://127.0.0.1:8000`.

5. You can interact with the chatbot using HTTP requests or visit the auto-generated API documentation at `http://127.0.0.1:8000/docs`.

## API Endpoints

- `GET /`: Returns a welcome message
- `POST /chat`: Sends a message to the chatbot and receives a response

### Example using curl:

```bash
curl -X 'POST' \
  'http://127.0.0.1:8000/chat' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{"message": "Hello, who are you?"}'
```

## Example Response

```json
{
  "response": "Hello! I'm an AI chatbot powered by the Llama API. I'm here to assist you with any questions or conversations you'd like to have. How can I help you today?"
}
```

## Contributing

Contributions to this project are welcome. Please feel free to fork the repository and submit pull requests.

## License

This project is open source and available under the [MIT License](https://opensource.org/licenses/MIT).