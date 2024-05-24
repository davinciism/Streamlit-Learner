import streamlit as st

st.write("Hello World")
mov = st.text_input("Favorite movie?")

st.write(f"Your favorite movie is: {mov}")

st.link_button("Profile", url="/profile")
st.link_button("Dashboard", url="/dashboard")


# Implementing same tab naivgation

st.markdown('<a href="/profile" target="_self">Go to profile</a>',unsafe_allow_html=True)