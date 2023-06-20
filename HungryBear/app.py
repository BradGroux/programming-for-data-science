import streamlit as st
import openai

# authenticate
openai.api_key = st.secrets["api_key"]

# Title
st.title("Hungry Bear")

# Header
st.header("OpenAI feeds you, literally 😋")

# Request user input
instructions = st.text_area("What meal are you planning for? Breakfast, Lunch or Dinner? ")

# Button
if len(instructions) < 1000:
    if st.button("Show Options"):
        response = openai.Completion.create(
            model = "text-davinci-003",
            prompt = "Act like my personal chef and give me food suggesstions based upon the following prompt: " + instructions,
            temperature = 0,
            max_tokens = 1000
        )
        output = response.choices[0].text
        st.info(output)
else:
    st.warning("Please enter less than 1000 characters")