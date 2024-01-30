import requests
import streamlit as st
from streamlit_lottie import st_lottie
#tasks

#make a navigation bar
#Make a place I want to visit section
#crop images with PIl library

st.set_page_config(page_title = "Michael's Webpage", page_icon = ":star: :wave:", layout = "wide")

#assets

contrller_ani = "https://lottie.host/7c8fc54f-5943-4be9-bc22-a71cfd4a5628/LWSFleRzhq.json"
capybara_image = "capybara.jpg"

genshin_image = "genshin.jpg"
genshin_image2 = "Jean.jpg"
genshin_image3 = "Raiden.jpg"

honkai_image = "honkai.jpg"
honkai_image2 = "himeko.jpg"
honkai_image3 = "March.jpg"

def loadlottie(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

#Header
with st.container():
    st.header(":wave: Hi, I'm Michael!")
    st.write("I like capybaras")
    st.image(capybara_image)
    st.write("I know python, C, Java, html, and CSS")

#body
with st.container():
    st.write("---")
    st.header("The games I play!")
    st_lottie(contrller_ani, height=600, key="controller")
    st.write("##")

    st.markdown('<h2 style="text-align: center;">Genshin Impact<h2>', unsafe_allow_html=True)
    image1_column, image2_column, image3_column = st.columns((3))
    with image2_column:
        st.image(genshin_image, width = 500)
    with image1_column:
        st.image(genshin_image2, width = 500)
    with image3_column:
        st.image(genshin_image3, width = 500)
    aligncolumn1, aligncolumn2, aligncolumn3 = st.columns((1, 10, 1))
    with aligncolumn2:
        st.info("Genshin Impact is a popular open-world action RPG game that allows you to explore a vast fantasy world called Teyvat, where you can meet different characters, use elemental powers, and fight enemies. You can also play with your friends online and enjoy various events and activities. I created an image of a scene from Genshin Impact with colorful characters and magical effects.")
    st.write("##")

    text_column4, text_column5, text_column6 = st.columns((1, 10, 1))
    with text_column5:
        st.markdown('<h2 style="text-align: center;">Honkai Starrail<h2>', unsafe_allow_html=True)
    image4_column, image5_column, image6_column = st.columns((3))
    with image4_column:
        st.image(honkai_image, width = 500)
    with image5_column:
        st.image(honkai_image2, width = 500)
    with image6_column:
        st.image(honkai_image3, width = 500)
    aligntxt4, aligntxt5, aligntxt6 = st.columns((1, 10, 1))
    with aligntxt5:
        st.info("Honkai Starrail is set in a science-fantasy universe where humanity and non-human sentient beings follow the Paths of deity-like beings known as Aeons. The game features the main character, referred to as the “Trailblazer”, traveling across worlds resolving disasters caused by the “Stellaron”. The game follows the gameplay style of classic Japanese role-playing games: players build up a lineup of characters, and control a team of four in turn-based combat. In addition to various stats that affect characters’ strength, each character has an elemental affinity that affects their ability to deal damage to certain targets, a character class referred to as a “path” that defines their role in combat, and set of unique abilities used in combat. Elements of open-world and dungeon exploration are present, with multiple mechanics, including the gacha system, carried over from HoYoverse’s previous action RPG Genshin Impact.")
    st.write("##")
