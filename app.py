import streamlit as st
from home_page import run_home_page
from post_page import run_task_page
from manage_page import run_manage_page

def main():
    st.title("App com CRUD 💻")
    
    menu = ["Home","Tasks","Manage","About"] 
    choice = st.sidebar.selectbox("Menu", menu)
    
    if choice == "Home":
        #st.subheader("Home")
        run_home_page()
        
    elif choice == "Tasks":
        st.subheader("Post Tasks")
        run_task_page()
        
    elif choice == "Manage":
        st.subheader("Manage Tasks")
        run_manage_page()
        
    else:
        st.subheader("About")
        
if __name__ == '__main__':
    main()