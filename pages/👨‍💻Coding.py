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

if st.session_state["authentication_status"]: #if the user is authenticated currently
    #do stuff here
    st.write(f'Welcome *{st.session_state["name"]}* Coding section')
    st.title("Coding header")

    # sidebar code
    pointbalance = config['credentials']['usernames'][username]['points']  # amount of points a user currently has
    badge = badgeidtoimage(
        config['credentials']['usernames'][username]['selectbadgeid'])  # badge user currently has selected

    st.sidebar.write(badge + username)
    st.sidebar.write('you currently have: ' + str(pointbalance) + ' points')


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

