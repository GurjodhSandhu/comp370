import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader


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

#code for login
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




#---------------------------------------page code start---------------------------------------------------------------------------------
if st.session_state["authentication_status"]:
    pointbalance = str(config['credentials']['usernames'][username]['points'])
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
        div.stButton > button:first-child {
            background-color: #FFE2E0;
            color: black;
            font-size: 20px;
            height: 2em;
            width: 12em;
            border-radius: 10px 10px 10px 10px;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://png2.cleanpng.com/sh/b01c461b1083058d46fffedf4c4f8b8a/L0KzQYm3VcA1N5RrfZH0aYP2gLBuTfJzaZpzRdZ7YYfsfri0gBxqeF5miuY2NXHocrXqhvEybZRneqY3NUm7RIa4VsYyPWM6TKIBOUezQYO9Ur5xdpg=/kisspng-brain-drawing-clip-art-5aebdcfa1ecbb4.5984516615254069701262.png" width="100"></div></div>',
        unsafe_allow_html=True
    )
    st.write(f'Welcome *{st.session_state["name"]}* Shop section')      #front end (main page)
    st.header('you currently have: '+ pointbalance + ' points')         #front end displaying point balance (main page)

    # sidebar code
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])

    st.sidebar.write(badge + username)                                       #front-end side bar to display badge
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points') #front-end display the current points

    colm1, colm2 = st.columns(2)
    with colm1:
        st.write("👩‍💻 costs 20 points")                                         #front end to display the badge information and cost
        if st.button(label="Buy 👩‍💻", key="item1"): #front end - buy button with label buy and badge
            cost = 20
            id = 1
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")                                  #front end - display a message if user cant afford badge
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")                          #front end - display a message if user already owns this badge
            elif(id != -1):
                removepoint(cost)

            st.write("bought") #front end write out a confirmation message

            config['credentials']['usernames'][username]['ownedbadges'].append(id)

#repeat for each if statement
    with colm2:
        st.write("👨‍💻 costs 20 points")
        if st.button(label="Buy 👨‍💻", key="item2"):
            cost = 20
            id = 2
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.write("👨‍🎤 costs 20 points")
        if st.button(label="Buy 👨‍🎤", key="item3"):
            cost = 20
            id = 3
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.write("👩‍🎤 costs 20 points")
        if st.button(label="Buy 👩‍🎤", key="item4"):
            cost = 20
            id = 4
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm2:
        st.write("👨‍🎓 costs 20 points")
        if st.button(label="Buy 👨‍🎓", key="item5"):
            cost = 20
            id = 5
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm1:
        st.write("👩‍🎓 costs 20 points")
        if st.button(label="Buy 👩‍🎓", key="item6"):
            cost = 20
            id = 6
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)
    with colm2:
        st.write("🧙 costs 20 points")
        if st.button(label="Buy 🧙", key="item7"):
            cost = 20
            id = 7
            if (config['credentials']['usernames'][username]['points'] - cost < 0):
                st.write("insufficient funds")
                id = -1
            if id in config['credentials']['usernames'][username]['ownedbadges']:
                st.write("you already own this badge")
            elif (id != -1):
                removepoint(cost)
                st.write("bought")
                config['credentials']['usernames'][username]['ownedbadges'].append(id)


#---------------------------------------page code end---------------------------------------------------------------------------------






#code for login
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
