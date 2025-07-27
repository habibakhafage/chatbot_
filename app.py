import streamlit as st
import requests

st.title("Chatbot")
# st.header("header")
# st.subheader("Sub")
# st.text("This is text")
# st.markdown("*Streamlit* is **really** ***cool***.")

# query = st.text_input("Enter Ur Query")

# if st.button("Submit"):
#     st.write(f"The answer to {query}")

# st.feedback("stars")

# st.sidebar.title("Chat2")

# col1,col2,col3 = st.sidebar.columns(3)

# with col1:
#     st.button("col1")
# with col2:
#     st.button("col2")
# with col3:
#     st.button("col3")

url = "http://127.0.0.1:8000/llm/"

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

query = st.text_input("Enter Ur Query")

if query:
    # bot_response = "Hello"
    payload = {
  "query": query
}


    with requests.post(url, json=payload, stream=False) as r:
        r.raise_for_status()
        response_data = r.json()
        bot_response = response_data.get("answer", "No response found.")
        # full_response += bot_response
        # message_placeholder.markdown(full_response)

        st.session_state.chat_history.append(("User",query))
        st.session_state.chat_history.append(("Bot",bot_response))

for role, message in st.session_state.chat_history:
    if role == "User":
        st.text(f"User :{message}")
    if role == "Bot":
        st.text(f"Bot :{message}")