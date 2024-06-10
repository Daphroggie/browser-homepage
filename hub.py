import streamlit as st
import io
import contextlib


class Redirect:
    def __init__(self, logo, name, link):
        st.image(image=logo, use_column_width=True)
        st.page_link(page=link, label=f"Redirect to {name}")
        


st.markdown(
    "<h1>WELCOME TO THE HUB <sup style='font-size:.6em;'>(not that kind)</sup></h1>",
    unsafe_allow_html=True
)

utils, socials, productivity, docs = st.columns(4)
with socials:
    youtube = Redirect(logo="Redirect Icons/youtube.png", name="YouTube", link="https://www.youtube.com")
    discord = Redirect(logo="Redirect Icons/discord.png", name="Discord", link="https://www.discord.com/app")
with productivity:
    trello = Redirect(logo="Redirect Icons/trello.png", name="Trello", link="https://www.trello.com")

