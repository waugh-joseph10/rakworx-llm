print('Import Libraries')

from langchain.text_splitter import RecursiveCharacterTextSplitter, MarkdownHeaderTextSplitter, MarkdownTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.document_loaders import UnstructuredMarkdownLoader
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain import hub
from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import GPT4AllEmbeddings
from gpt4all import GPT4All
from langchain_community.vectorstores import Chroma
from langchain_core.runnables import RunnablePassthrough, RunnablePick

# Load RAG prompt default
rag_prompt = hub.pull("rlm/rag-prompt-llama")

print('Load Data')

loader = UnstructuredMarkdownLoader('rakworx.md')
data = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)
vectorstore = Chroma.from_documents(documents=all_splits, embedding=GPT4AllEmbeddings())

print('Vectorstore Built')

print('Import LLM')

llm = LlamaCpp(
    model_path="llama-2-13b-chat.Q4_K_M.gguf",
    n_gpu_layers=1,
    n_batch=512,
    n_ctx=2048,
    f16_kv=True,  # MUST set to True, otherwise you will run into problem after a couple of calls
    verbose=False
)

# Chain
def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

chain = (
    RunnablePassthrough.assign(context=RunnablePick("context") | format_docs)
    | rag_prompt
    | llm
    | StrOutputParser()
)
while True:
    question = input("\nNEW QUESTION:\nEnter your question or type 'exit' to quit: ")
    if question.lower() == 'exit':
        print("Exiting the program.")
        break

    try:
        docs = vectorstore.similarity_search(question)
        print('The chatbot is generating the response...')
        response = chain.invoke({"context": docs, "question": question})
        print(response)
        print('\n\n\n')
    except Exception as e:
        print(f"An error occurred: {e}")