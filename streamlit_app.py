from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st
from functions import *
from PIL import Image
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
import datetime
import requests
import os
import time
import numpy as np 
from csv import DictWriter

pageheader = st.container()
main_page = st.container()

#login in check (cache)

df = pd.read_csv("user base.csv", sep=";")

if 1 in list(df["logged_in"]):
    logged_in = True
    logged_in_user = df.index[df["logged_in"]==1].tolist()[0]

if 1 not in list(df["logged_in"]):
    logged_in = False
    logged_in_user = -1

#header bodie (site selection)

with pageheader:
    coli, cold, colf = st.columns(3)
    logo_image = Image.open('logo.png')
    cold.image(logo_image)
    page = st.selectbox("Choose your page", ["Login", "Betting", "Ranking", "Analytics"])

#main bodie (4 different sites)

with main_page:

    #login page

    if page == "Login":

        st.subheader("Welcome to BetCoin™!")

        st.write("Create a user or login with your existing account.")
        st.write("Every new user starts with a blance of 100.")
        st.write("You can bet on 5 different crypto coins to go up or down within the next 15 seconds.")
        st.write("Bets entries range between 1 and 10. The return is double or nothing.")
        st.write("Look on the ranking page how you compare to other players.")
        st.write("Have fun!")

        st.subheader("Login or Create a User")

        if logged_in == False:

            #user login

            st.write("Please login in with your username and password. If you have no account please create a new user")
            
            col1, col2 = st.columns(2)
                
            username = col1.text_input("Username")

            password = col2.text_input("Password")

            if col1.button("Login"):

                if logged_in == True:

                    st.write("You are already logged in. To switch users please log out before!")

                if logged_in == False:
                
                    #create dataframe

                    df = pd.read_csv("user base.csv", sep=";")

                    #check if user is in database

                    if username in list(df["username"]):

                        user_id = df.index[df['username']==username].tolist()[0] #assign index

                        if password == df["password"][user_id]: #compare the password the user has typed in whith the password in the data base
                            
                            logged_in = True

                            logged_in_user = user_id

                            name = df["username"][logged_in_user]

                            st.write(f"Welcome. You are logged in as user {name}") 

                            change_database(logged_in_user, "logged_in", 1)

                            page = "Betting"

                        else:
                            st.write("Wrong Password. Please try again!")    

                    else:

                        st.write("Username does not exist. Try again or create new user!")


            #new user

            st.subheader("")
            st.subheader("")

            st.subheader("Create a new User")
            col3, col4 = st.columns(2)

            username_new = col3.text_input("Select Username")
            
            password_new = col4.text_input("Select Password")

            st.subheader("")

            if st.button("Create User"):
                
                df = pd.read_csv("user base.csv", sep=";")

                if username_new in list(df["username"]):
                    
                    st.write("This username is already taken. Please try again with another one.")

                else:
                    
                    appender(username_new, password_new, 100)

                    st.write(f"A new user {username_new} has been created successfully!")

        if logged_in == True:

            df = pd.read_csv("user base.csv", sep=";")

            log_name = df["username"][logged_in_user]

            st.write(f"You are currently logged in as user {log_name}")

            if st.button("Logout"):

                if logged_in == False:

                    st.write ("You are already logged out!")
                
                if logged_in == True:

                    logged_in = False

                    change_database(logged_in_user, "logged_in", 0)

                    logged_in_user = -1

                    st.write("You were logged out successfully!")
