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

if st.session_state["authentication_status"]: #if the user is authenticated currently
    st.title("Profile Page")
   #function to take a badges image and turn it into the badges id #
    def badgeimagetoid(image):
        if image == "👨":
            id = 0
        if image == "👩‍💻":
            id = 1
        if image == "👨‍💻":
            id = 2
        if image == "👨‍🎤":
            id = 3
        if image == "👩‍🎤":
            id = 4
        if image == "👨‍🎓":
            id = 5
        if image == "👩‍🎓":
            id = 6
        if image == "🧙":
            id = 7
        return id #
   #function to take a badges id # and turn it into the badges image
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

    allbadges = ['👩‍💻','👨‍💻','👨‍🎤','👩‍🎤','👨‍🎓','👩‍🎓','🧙']
    availablebadges = []
    ownedbadgesid = config['credentials']['usernames'][username]['ownedbadges']
    for i in ownedbadgesid:
        availablebadges.append(badgeidtoimage(i))

    option = st.selectbox(
        'Display a Badge',
        (availablebadges))
    st.write('You selected:', option)

   # sidebar code
    pointbalance = config['credentials']['usernames'][username]['points']  # amount of points a user currently has
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected

    st.sidebar.write(badge + username)
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points')

    config['credentials']['usernames'][username]['selectbadgeid'] = badgeimagetoid(option)


if st.session_state["authentication_status"]: #updating user info
    try:
        if authenticator.update_user_details(st.session_state["username"]):
            st.success('Entries updated successfully')
    except Exception as e:
        st.error(e)

if st.session_state["authentication_status"]: #reseting password
    try:
        if authenticator.reset_password(st.session_state["username"]):
            st.success('Password modified successfully')
    except Exception as e:
        st.error(e)

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
