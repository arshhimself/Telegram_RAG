# RAG-Powered Telegram Bot

- This is a Telegram bot that uses **RAG (Retrieval-Augmented Generation)** to answer questions from a PDF document using OpenAI embeddings and LLMs.
- All you have to do is give a PDF file (can be anything book, resume, script) and the bot will answer respective to that information present in the PDF. 
---

## Features

- Answer questions directly from PDF content.
- Uses OpenAI's `text-embedding-3-small` for vector embeddings.
- Uses `gpt-4o-mini` for generating answers.
- Simple Telegram bot interface.

---

## Prerequisites

- Python 3.10+  
- Pip or pipenv/venv for dependency management.
- Telegram bot token (from BotFather).
- PDF file for the bot to read.

---

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/arshhimself/Telegram_RAG
```
### 2.Create a virtual environment and activate it
```
python -m venv venv
```
```
# macOS/Linux
source venv/bin/activate
# Windows
venv\Scripts\activate 
```
### 3. Install dependencies
```
pip install -r requirements.txt

```

### 4.Prepare environment variables
- Create a .env file in the project root with the following content:
```
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

- Set PDF_PATH and BOT_TOKEN
```
PDF_PATH=path/to/your/pdf.pdf
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

---

# How to Run
```
python bot.py
```
- The bot will start polling Telegram for messages.

- Send /start to your bot in Telegram to begin.

- Ask any question related to the uploaded PDF, and the bot will answer based on its content.


---

## How to Get Your Telegram Bot Token

1. **Open Telegram**  
   Make sure you have the Telegram app installed on your phone or desktop.

2. **Start a chat with BotFather**  
   Search for `@BotFather` in Telegram and start a conversation.

3. **Create a new bot**  
   Type `/newbot` and send. BotFather will ask you for:
   - **Bot name:** This is the display name of your bot (can be anything).  
   - **Bot username:** Must be unique and end with `bot` (e.g., `MyRAGBot`).

4. **Receive the token**  
   After creating the bot, BotFather will give you a message containing the **API token**. It looks like:  123456789:ABCDefGhIJKlmNoPQRsTUVwxyZ


5. **Save the token in `.env`**  
Open your `.env` file and add:

```
BOT_TOKEN=123456789:ABCDefGhIJKlmNoPQRsTUVwxyZ
```



---

Currently it only reads the text from the PDF but can be changed by just some changes .
