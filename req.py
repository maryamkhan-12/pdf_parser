import streamlit as st
import requests

# Streamlit app
def main():
    st.title("Blog Content Generator")
    st.write("This app sends your blog generation requests to a FastAPI server.")

    # Sidebar inputs
    st.sidebar.header("Configure Blog Settings")
    
    # Define the API endpoint (adjust if needed)
    api_url = st.sidebar.text_input("FastAPI Server URL", "http://127.0.0.1:8000/blogs/pipeline/")

    # Input fields for the blog generation parameters
    blog_type = st.sidebar.selectbox("Type of Blog", ["How to", "Listicle", "Guide", "Review"])
    target_audience = st.sidebar.text_input("Target Audience", "Parents")
    tone = st.sidebar.selectbox("Tone", ["Informative", "Casual", "Formal", "Humorous"])
    point_of_view = st.sidebar.selectbox("Point of View", ["First-person", "Second-person", "Third-person"])
    target_country = st.sidebar.text_input("Target Country", "US")
    keywords = st.sidebar.text_area("Keywords (comma-separated)", "child development, parenting tips, educational activities")

    # Convert comma-separated keywords to a list
    keywords_list = [kw.strip() for kw in keywords.split(",") if kw.strip()]

    # Button to send request
    if st.sidebar.button("Generate Blog"):
        # Create the payload based on user inputs
        payload = {
            "TypeOf": blog_type,
            "target_audience": target_audience,
            "tone": tone,
            "point_of_view": point_of_view,
            "target_country": target_country,
            "keywords": keywords_list
        }

        st.write("Sending request to the FastAPI server...")

        # Show a spinner while the request is being processed
        with st.spinner("Generating blog content... Please wait..."):
            try:
                # Send a POST request to the FastAPI server
                response = requests.post(api_url, json=payload)
                response.raise_for_status()  # Check for HTTP errors

                # Display the response JSON
                response_data = response.json()
                st.success("Blog generated successfully!")
                st.json(response_data)

            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred: {e}")

# Run the app
if __name__ == "__main__":
    main()
