import streamlit as st


def main():
    st.set_page_config(page_title="Chat with your Docs", page_icon=":books") 


    st.header("Chat with your Docs :books:")
    st.text_input("Ask a question about your docs")
    
    with st.sidebar:
      st.subheader("Your Docs")
      st.file_uploader("Upload your files here click process")
      st.button("process")

if __name__ == '__main__':
    main()