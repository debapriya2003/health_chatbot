# Health & Medical Chatbot

This is a health and medical chatbot built using OpenAI's GPT model, Streamlit for the frontend, and MongoDB Atlas for data storage.

## Features
- Chat with the bot about health-related topics.
- View chat history.
- Save user queries and bot responses.

## Requirements
- Python 3.9 or higher
- MongoDB Atlas account
- OpenAI API key

## Setup Instructions

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/health-chatbot.git
    ```

2. Navigate into the project directory:
    ```bash
    cd health-chatbot
    ```

3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Set up MongoDB Atlas and get your connection string.

5. Set up your OpenAI API key in the `backend.py` file.

6. Run the app using Streamlit:
    ```bash
    streamlit run app.py
    ```

## Deployment

For production deployment, you can use platforms like [Streamlit Cloud](https://streamlit.io/cloud), [Heroku](https://heroku.com), or [AWS](https://aws.amazon.com).

## License
MIT License.
