from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import OpenAIEmbeddings
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.document_loaders import PyPDFLoader
from langchain_community.vectorstores import FAISS  #metınlerı embedding modellerıne gore vektorlere cevırıp saklar ve facebookun kutuphanesıdır
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import CohereEmbeddings
from langchain_community.embeddings import HuggingFaceInferenceAPIEmbeddings
import os
from dotenv import load_dotenv

load_dotenv()

my_key_openai = os.getenv("OPENAI_API_KEY")
my_key_google = os.getenv("GOOGLE_API_KEY")
my_key_cohere = os.getenv("COHERE_API_KEY")
my_key_hf = os.getenv("HUGGING_FACE_ACCESS_TOKEN")


llm_gemini = ChatGoogleGenerativeAI(google_api_key=my_key_google, model="gemini-pro")


embeddings = OpenAIEmbeddings(api_key=my_key_openai)


#embeddings = CohereEmbeddings(cohere_api_key=my_key_cohere, model="embed-multilingual-v3.0") 
# openaıdan farklı olarak hangı dılde embeddıng yapacaksak onun modelını kullanmalıyız
# embed-english-v3.0 ----ing için

# embeddings = HuggingFaceInferenceAPIEmbeddings(
#     api_key=my_key_hf,
#     model_name="sentence-transformers/all-MiniLM-16-v2"
# )

#access key alırken uzaktakı bır projeye degıstırmeyecegız ıcın read ıcın alacagız



def ask_gemini(prompt):

    AI_Response = llm_gemini.invoke(prompt)

    return AI_Response.content

# def rag_with_url(target_url, prompt):

#     loader = WebBaseLoader(target_url)

#     raw_documents = loader.load()

#     text_spilitter = RecursiveCharacterTextSplitter(
#         chunk_size=1000,
#         chunk_overlap=0,
#         length_function=len
#     )

#     spilitted_documents = text_spilitter.split_documents(raw_documents)

#     vectorstore = FAISS.from_documents(spilitted_documents, embeddings)
#     retriever = vectorstore.as_retriever()

#     relevant_documents = retriever.get_relevant_documents(prompt)

# #relevant_documents lıste tıpınde ancak bıze bır prompt için strıng gerektıgı ıcın bu for loopunda bır strınge donsuturuyoruz lıstemızı : context_Data

#     context_data = ""

#     for document in relevant_documents:
#         context_data = context_data + " " + document.page_content

#     final_prompt = f"""Şöyle bir sorun var: {prompt}
#     Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data}.
#     Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
#     """

#     AI_Response = llm_gemini.invoke(final_prompt)

#     return AI_Response.content

def rag_with_multiple_url(url_list, prompt):
    context_data = ""
    
    for target_url in url_list:
        loader = WebBaseLoader(target_url)
        raw_documents = loader.load()

        text_spilitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=0,
            length_function=len
        )

        spilitted_documents = text_spilitter.split_documents(raw_documents)
        vectorstore = FAISS.from_documents(spilitted_documents, embeddings)
        retriever = vectorstore.as_retriever()

        relevant_documents = retriever.get_relevant_documents(prompt)

        for document in relevant_documents:
            context_data += " " + document.page_content

    final_prompt = f"""Şöyle bir sorun var: {prompt}
    Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data}.
    Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
    """

    AI_Response = llm_gemini.invoke(final_prompt)

    return AI_Response.content





def rag_with_pdf(filepath, prompt):
    
    loader = PyPDFLoader(filepath)

    raw_documents = loader.load()

    text_spilitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=0,
        length_function=len
    )

    spilitted_documents = text_spilitter.split_documents(raw_documents)

    vectorstore = FAISS.from_documents(spilitted_documents, embeddings)
    retriever = vectorstore.as_retriever()

    relevant_documents = retriever.get_relevant_documents(prompt)

    context_data = ""

    for document in relevant_documents:
        context_data = context_data + " " + document.page_content

    final_prompt = f"""Şöyle bir sorun var: {prompt}
    Bu soruyu yanıtlamak için elimizde şu bilgiler var: {context_data}.
    Bu sorunun yanıtını vermek için yalnızca sana burada verdiğim eldeki bilgileri kullan. Bunların dışına asla çıkma.
    """

    AI_Response = llm_gemini.invoke(final_prompt)

    return AI_Response.content, relevant_documents