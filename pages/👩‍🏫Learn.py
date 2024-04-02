import pandas as pd
import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import streamlit.components.v1 as components

# Sets page in widemode,specifically allowing header to span across page.
st.set_page_config(page_title="WebsiteName", layout="wide")

def addpoint(points): #function to add points to user
    config['credentials']['usernames'][username]['points'] += points
def removepoint(points): #function to remove points from user
    config['credentials']['usernames'][username]['points'] -= points
    if config['credentials']['usernames'][username]['points'] < 0:
        config['credentials']['usernames'][username]['points'] = 0
def badgeidtoimage(id):
        if id == 0:
            image = "👨"
        if id == 1:
            image = "👩‍💻"

        if id == 2:
            image = "👨‍💻"

        if id == 3:
            image = "👨‍🎤"

        if id == 4:
            image = "👩‍🎤"

        if id == 5:
            image = "👨‍🎓"

        if id == 6:
            image = "👩‍🎓"

        if id == 7:
            image = "🧙"

        return image

with open('config.yaml') as file: #opening data file with user information
    config = yaml.load(file, Loader=SafeLoader)

authenticator = stauth.Authenticate( #setting up cookies
    config['credentials'],
    config['cookie']['name'],
    config['cookie']['key'],
    config['cookie']['expiry_days'],
    config['preauthorized']
)
authenticator.login()

if st.session_state["authentication_status"]: #if the user is authenticated currently
    with st.sidebar:
        authenticator.logout() #logout button
elif st.session_state["authentication_status"] is False: # if incorrect password/username inputed when clicking login
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None: #if fields login fields are empty
    st.warning('Please enter your username and password')

username = st.session_state["username"] #intilizes value of username to the current user's name

if st.session_state["authentication_status"]:
    # creating a 'points' category if currently empty
    if 'points' not in config['credentials']['usernames'][username]:
        config['credentials']['usernames'][username]['points'] = 1 #set users point balance to 1


#----------------------page code start---------------------------------
if st.session_state["authentication_status"]: #if the user is authenticated currently
    pointbalance = config['credentials']['usernames'][username]['points']  # amount of points a user currently has
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected
    # Create container for header
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Lilita+One&display=swap');
        .title-container {
            display: flex;
            align-items: center;
            padding: 10px;
            background-color: #FFE2E0;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            font-size: 50px; 
            margin-top: -105px; 
            font-family: 'Lilita One', cursive; 
            color: #FF8C84

        }
        .image-container {
            margin-left: 20px; /* Adjust the margin to create space between title and image */
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    # Display title with colored background and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://png2.cleanpng.com/sh/b01c461b1083058d46fffedf4c4f8b8a/L0KzQYm3VcA1N5RrfZH0aYP2gLBuTfJzaZpzRdZ7YYfsfri0gBxqeF5miuY2NXHocrXqhvEybZRneqY3NUm7RIa4VsYyPWM6TKIBOUezQYO9Ur5xdpg=/kisspng-brain-drawing-clip-art-5aebdcfa1ecbb4.5984516615254069701262.png" width="100"></div></div>',
        unsafe_allow_html=True
    )
    # Display title with colored background and image
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://png2.cleanpng.com/sh/b01c461b1083058d46fffedf4c4f8b8a/L0KzQYm3VcA1N5RrfZH0aYP2gLBuTfJzaZpzRdZ7YYfsfri0gBxqeF5miuY2NXHocrXqhvEybZRneqY3NUm7RIa4VsYyPWM6TKIBOUezQYO9Ur5xdpg=/kisspng-brain-drawing-clip-art-5aebdcfa1ecbb4.5984516615254069701262.png" width="100"></div></div>',
        unsafe_allow_html=True)
    m1cardquestion = ["What is 1 + (-1)", "What is 1 - (-1)", "What is 1 * -1", "What is -1 * -1"]
    m1cardanswer = [
        "Answer: :red[0] adding a negative value (-1) to another value is the same as substracting the its positive inverse",
        "Answer: :red[2] Subtracting a negative value is the same as adding its positive inverse.",
        "Answer: :red[-1] multiplying a positive value by a negative results in negative number.",
        "Answer: :red[1] Multiplying a negative number with a negative number results in a positive number"]

    st.header("Negative - addition/subtraction/multiplication/division")
    i = 0
    colm1, colm2 = st.columns(2)
    with colm1:
        while i < len(m1cardquestion):
            st.write(m1cardquestion[i])  # card question
            with st.popover("Answer"):
                st.write(m1cardanswer[i])  # card answer
            i += 1

    with colm2:
        st.markdown("""<iframe width="560" height="315" src="https://www.youtube.com/embed/NQSN00zL5gg?si=NLr9wwoi6aZ9Wv4v" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>""", unsafe_allow_html=True)
        #components.iframe("https://www.youtube.com/embed/NQSN00zL5gg?si=NLr9wwoi6aZ9Wv4v", width=700, height=400)

    st.header("Ratios ")
    colmn1 ,colmn2 = st.columns(2)
    with colmn1:
        st.write("testing")

    with colmn2:
        st.write("testing")



    #----------------------page code end---------------------------------

else: #registration for the website
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
            config['credentials']['usernames'][username_of_registered_user]['points'] = 20
            config['credentials']['usernames'][username_of_registered_user]['ownedbadges'] = [0]
            config['credentials']['usernames'][username_of_registered_user]['selectbadgeid'] = 0

    except Exception as e:
        st.error(e)


with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)



