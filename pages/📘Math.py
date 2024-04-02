import streamlit_authenticator as stauth
import streamlit as st
import yaml
from yaml.loader import SafeLoader
import json
#Title of the website and makes site in widemode and sets the page font to Lilita One
st.set_page_config(page_title="WebsiteName", layout="wide")

import streamlit as st



st.markdown("""<style>
    figure {
  border: thin #c0c0c0 solid;
  display: flex;
  flex-flow: column;
  max-width: 150px;
}
img {
  max-width: 150px;
  max-height: 150px;
}
figcaption {
  background-color: #222;
  color: #fff;
  font: italic smaller sans-serif;
  padding: 3px;
  text-align: center;
} </style>
    """,unsafe_allow_html=True)





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

def multichoicegame(unit,questionfile):
    gamequestion = open(questionfile)
    questions = json.load(gamequestion)

    score = 0
    feedback = []
    st.title("Math Questionnaire")
    for i, question in enumerate(questions, 1):
        st.markdown(f"<span style='font-weight:bold'> Question {i}:  {question['question']}</span>", unsafe_allow_html=True)
        if len(question['correct_answers']) > 1:
            user_answers = []
            for option in question['options']:
                if st.checkbox(option, key=f'{unit}{i}{option}'):
                    user_answers.append(option)
        else:
            user_answer = st.radio("", question['options'], key=f'{unit}Unit1{i}')
        if len(question['correct_answers']) > 1:
            if set(user_answers) == set(question['correct_answers']):
                score += 1
                feedback.append("That is Correct✅")
            else:
                feedback.append("That is Wrong ❌")
        else:
            if user_answer == question['correct_answers'][0]:
                score += 1
                feedback.append("That is Correct✅")
            else:
                feedback.append("That is Wrong ❌")
    if st.button("SUBMIT",key=unit):
        st.write("Game Results :")
        for i, fb in enumerate(feedback, 1):
            st.write(f"Question {i}: {fb}")

        percentage = (score/len(question))
        st.write(f"Score final : {score}/{len(questions)}")
        pointsgained = round(percentage/10)
        st.write(f"You gained :red[ {pointsgained}] points")
        addpoint(pointsgained)


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
        authenticator.logout()  # logout button
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
    # Creating container for header
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
    # Display header with colored container and image
    st.markdown(
    '<div class="title-container">BrainyBytes Lab<div class="image-container"><img src="https://png2.cleanpng.com/sh/b01c461b1083058d46fffedf4c4f8b8a/L0KzQYm3VcA1N5RrfZH0aYP2gLBuTfJzaZpzRdZ7YYfsfri0gBxqeF5miuY2NXHocrXqhvEybZRneqY3NUm7RIa4VsYyPWM6TKIBOUezQYO9Ur5xdpg=/kisspng-brain-drawing-clip-art-5aebdcfa1ecbb4.5984516615254069701262.png" width="100"></div> &nbsp &nbsp &nbsp Math section</div>',
    unsafe_allow_html=True
    )

    colm1 , colm2 = st.columns(2)
    with colm1:
        st.image("images/Ratiogame.jpg", caption="Ratio Game") #game1
        with st.popover("play"):
            multichoicegame('unit1','math_unit1_questions.json')

        st.image("images/AlgebraGame.jpg", caption="Algebra Game") #game3
        with st.popover("play"):
            multichoicegame('unit3','math_unit3_questions.json')
        st.image("images/placehold.png", caption="Placeholder Game") #game5
        with st.popover("play"):
            st.write("Game code here")

    with colm2:
        st.image("images/NegativeNumbers.jpg", caption="Negative Numbers Game") #game1
        with st.popover("play"): #game2 negative numbers

            multichoicegame('unit2','math_unit2_questions.json')

        st.image("images/placehold.png", caption="Placeholder Game")
        with st.popover("play"): #game4
            st.write("Game code here")

        st.markdown("""<figure>
                  <img src="https://www.w3schools.com/images/w3schools_green.jpg" alt="Elephant at sunset" />
                    <figcaption>Ratio Game</figcaption>
                    </figure>
                """, unsafe_allow_html=True)
        with st.popover("play"): #game6
            st.write("Game code here")




    #sidebar code
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

