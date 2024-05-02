import streamlit as st
import requests

# Define the API endpoint URL
API_URL = "https://jsonplaceholder.typicode.com/posts/1"

# Function to make API call
def fetch_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        st.error("Failed to fetch data from the API")

# Main function
def main():
    st.title("Streamlit App with API Integration")

    # Button to trigger API call
    if st.button("Fetch Data from API"):
        # Make API call and display the results
        data = fetch_data()
        if data:
            st.write("Data fetched successfully:")
            st.write(data)

# Run the main function
if __name__ == "__main__":
    main()
