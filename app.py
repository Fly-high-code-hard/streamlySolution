import streamlit as st

def main():
    st.set_page_config(page_title="My Streamlit App", layout="wide")
    
    st.title("Welcome to my Streamlit App!")
    st.write("This is a basic template to start working with Streamlit.")
    
    # Sidebar
    st.sidebar.header("Settings")
    option = st.sidebar.selectbox("Select an option", ["Home", "Analytics", "Contacts"])
    
    if option == "Home":
        st.subheader("Home Page")
        st.write("Welcome to the home page!")
    
    elif option == "Analytics":
        st.subheader("Analytics Section")
        number = st.number_input("Enter a number", min_value=0, max_value=100, value=50)
        st.write(f"You selected the number: {number}")
    
    elif option == "Contacts":
        st.subheader("Contacts")
        st.write("Contact us via email: example@example.com")
    
if __name__ == "__main__":
    main()