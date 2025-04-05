import streamlit as st
import pandas as pd
import difflib

# Set up the Streamlit page
st.set_page_config(page_title="Chatbot", page_icon="🤖")
st.title("🤖 NLP Processed Chatbot")

# Load processed keywords and answers from CSV
@st.cache_data
def load_data():
    df = pd.read_csv("keyword_answer_output.csv")
    df.dropna(inplace=True)
    return dict(zip(df['keyword'], df['answer']))

qa_dict = load_data()

# Initialize session state for chat
if "chat" not in st.session_state:
    st.session_state.chat = []

# User chat input
user_input = st.chat_input("Ask a question...")

if user_input:
    # Preprocess the input (you already did NLP offline, so here we'll match using fuzzy logic)
    processed_input = user_input.lower()  # Keep it simple
    matches = difflib.get_close_matches(processed_input, qa_dict.keys(), n=1, cutoff=0.5)

    if matches:
        response = qa_dict[matches[0]]
    else:
        response = "🤖 I'm not sure how to answer that yet."

    # Store conversation
    st.session_state.chat.append(("user", user_input))
    st.session_state.chat.append(("bot", response))

# Display chat history
for role, text in st.session_state.chat:
    with st.chat_message("user" if role == "user" else "assistant"):
        st.markdown(text)
