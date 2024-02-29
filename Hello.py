import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader

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
    authenticator.logout() #logout button
elif st.session_state["authentication_status"] is False: # if incorrect password/username inputed when clicking login
    st.error('Username/password is incorrect')
elif st.session_state["authentication_status"] is None: #if fields login fields are empty
    st.warning('Please enter your username and password')

if st.session_state["authentication_status"]: #if the user is authenticated currently
    #do stuff here
    st.write(f'Welcome *{st.session_state["name"]}* to comp 370 project')
    st.title("Temperory header")
    st.write('your username is: ' + st.session_state["username"])
    st.write('your email is: '+config['credentials']['usernames'][st.session_state["username"]]['email'])
    st.write('you currently have: '+str(config['credentials']['usernames'][st.session_state["username"]]['points']) + ' points')


else: #registration for the website
    try:
        email_of_registered_user, username_of_registered_user, name_of_registered_user = authenticator.register_user(preauthorization=False)
        if email_of_registered_user:
            st.success('User registered successfully')
    except Exception as e:
        st.error(e)

with open('config.yaml', 'w') as file:
    yaml.dump(config, file, default_flow_style=False)
