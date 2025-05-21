import streamlit as st

st.title("Job Posting Classifier")
st.write("This app helps categorize job postings based on required skills.")

# User input for job search
keyword = st.text_input("Enter job keyword (e.g., 'Data Science')")

if st.button("Scrape Jobs"):
    st.write(f"Scraping jobs for keyword: {keyword}...")
    # Call your scraping function here
