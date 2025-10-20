import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters


from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_chroma import Chroma
from langchain_community.document_loaders import PyPDFLoader


load_dotenv()
BOT_TOKEN = "YOUR_BOT_TOKEN"
file_path = "YOUR_PDF_PATH"
loader = PyPDFLoader(file_path)
docs = loader.load()


splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=20)
text_list = [doc.page_content for doc in docs]
chunks = splitter.create_documents(text_list)

embeddings = OpenAIEmbeddings(model="text-embedding-3-small")
vector_store = Chroma.from_documents(chunks, embeddings)
retriever = vector_store.as_retriever(search_type="similarity", search_kwargs={"k": 4})

llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.2)

prompt = PromptTemplate(
    template="""
You are a helpful assistant.
Answer ONLY from the provided transcript context.
If the context is insufficient, just say you don't know.

{context}
Question: {question}
""",
    input_variables=['context', 'question']
)

def ask_rag(question: str) -> str:
 
    retrieved_docs = retriever.invoke(question)
    context_text = "\n\n".join(doc.page_content for doc in retrieved_docs)
    final_prompt = prompt.invoke({"context": context_text, "question": question})
    answer = llm.invoke(final_prompt)
    return answer.content




async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hey! 👋 Main ek RAG-powered Telegram bot hoon. Apna sawal bhejo!")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text("⏳ Soch raha hoon...")


    try:
        response = ask_rag(user_message)
        await update.message.reply_text(f"🤖 {response}")
    except Exception as e:
        print("Error:", e)
        await update.message.reply_text("❌ Sorry, kuch galat ho gaya.")


def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("🚀 Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
