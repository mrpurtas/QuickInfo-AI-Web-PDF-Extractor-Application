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





#https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/562de7f497af4f6c99783267a53f1979.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/3f0e806003c14f85a858f9a7352f2d58.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/15374a36cadb45eca3e6783df890e78f.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/68d46800cc6b40c4bb746573ff400784.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/111afafb33474699983de41ad2476bd0.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/1b2477249e88440d94e9a9fc49c8c07c.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/8e53421a98954c95a490ec28511baf3f.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/daac6ddd95df47c08847a6a26b718e91.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/b34787ae28524454ac50c5e5acd61a26.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/b5d0ec7de3694442ba6d9136736cbdb9.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/35ac1f1d330b4644a2e34fb8294f6833.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/1f14b2b77c2945f08f338cd985c01e23.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/b21864d31d6a4e3981259a97c929acf9.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/28a5bf3486404952bf3b1a106321e839.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/1d115ca4bd304653b1b675136f6f967e.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/af93d38092f6411f9a8e6a1847c72faf.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/6854725959e8497cb3545c6881fac1a9.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/43ec4c0b8750441fafb2f7b85084577a.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/0c46cae049c04d029d0f91658e3ac861.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/7b109625938745e796d7ede7a9e46dd1.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/5acc9b39bc0a4cdc82073f9bd24c546e.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/01174d1091aa49daaacc769533757cf8.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/1c98968387a847bd9f2679d770a96db7.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/562de7f497af4f6c99783267a53f1979.html?locale=en-US,https://help.sap.com/docs/SAP_NETWEAVER_740/9c91640bf34c49d8bad6bc560bedd707/5bd83096736747faa9f3240f010469e9.html?locale=en-US,