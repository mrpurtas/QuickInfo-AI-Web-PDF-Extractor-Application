import streamlit as st
import raghelper

st.set_page_config(page_title="LangChain ile Bellek Genişletme", layout="wide")
st.title("LangChain ile Bellek Genişletme: URL")
st.divider()


col_input, col_rag, col_normal = st.columns([1,2,2])

# with col_input:
#     target_url = st.text_input(label="İşlenecek Web Adresini Giriniz:")
with col_input:
    target_url = st.text_input(label="İşlenecek Web Adreslerini Giriniz (URL'leri virgülle ayırın):")
    url_list = target_url.split(',')

    st.divider()
    prompt = st.text_input(label="Sorunuzu Giriniz", key="url_prompt")   #aşagıda da benzer wıdgetlar kullanacagımız ıcın key atadık unutmayalım 
    st.divider()
    submit_btn = st.button(label="Sor", key="url_button")

    if submit_btn:
        
        with col_rag:
            with st.spinner("Yanıt Hazırlanıyor..."):
                st.success("YANIT - RAG Devrede")
                #st.markdown(raghelper.rag_with_multiple_url(target_url=target_url, prompt=prompt)) 
                st.markdown(raghelper.rag_with_multiple_url(url_list=url_list, prompt=prompt))

                
                #lısteler ve tabloları kacırmamk ıcın mmarkdown kullandık

        with col_normal:
            with st.spinner("Yanıt Hazırlanıyor..."):
                st.info("YANIT - RAG Devre Dışı")
                st.markdown(raghelper.ask_gemini(prompt=prompt))
                st.divider()


st.title("LangChain ile Belge Geliştirme: PDF")
st.divider()

col_input, col_rag, col_normal = st.columns((1,2,2))

with col_input:
    selected_file = st.file_uploader(label="İşlenecek Dosyayı Seçiniz", type=["pdf"])
    st.divider()
    prompt = st.text_input(label="Sorunuzu Giriniz:", key="pdf_prompt")
    st.divider()
    submit_btn = st.button(label="Sor", key="pdf_button")
    st.divider()

if submit_btn:

    with col_rag:
        with st.spinner("Yanıt Hazırlanıyor..."):
            st.success("YANIT - RAG Devrede")
            AI_Response, relevant_documents = raghelper.rag_with_pdf(f"./data/{selected_file.name}", prompt=prompt)
            st.markdown(AI_Response)
            st.divider()
            for doc in relevant_documents:
                st.caption(doc.page_content)
                st.markdown(f"**Kaynak: {doc.metadata}**")
                st.divider()
    with col_normal:
        with st.spinner("Yanıt Hazırlanıyor..."):
            st.info("YANIT - RAG Devre Dışı")
            st.markdown(raghelper.ask_gemini(prompt=prompt))
            st.divider()





