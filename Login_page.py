import pandas as pd
import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader

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
    #do stuff here
    challenges = pd.read_csv('challenges.csv')
    #main page code
    st.write(f'Welcome *{st.session_state["name"]}*')
    st.write(f'Challenge #1: :red[*{challenges["Challenge"][0]}*] worth :green[ *{challenges["pointsworth"][0]}*] points status: :red[*{challenges["tracker"][0]}*]/:red[*{challenges["tracker2"][0]}*]')
    st.write(f'Challenge #2: :red[*{challenges["Challenge"][1]}*] worth :green[ *{challenges["pointsworth"][1]}*] points status: :red[*{challenges["tracker"][1]}*]/:red[*{challenges["tracker2"][1]}*]')
    st.write(f'Challenge #3: :red[*{challenges["Challenge"][2]}*] worth :green[ *{challenges["pointsworth"][2]}*] points status: :red[*{challenges["tracker"][2]}*]/:red[*{challenges["tracker2"][2]}*]')

    #sidebar code
    st.sidebar.write(badge + username)
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points')

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
