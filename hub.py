import streamlit as st


class Redirect:
    def __init__(self, logo, name, link):
        st.image(logo)
        st.link_button(label=f"Redirect to {name}, url=link")


