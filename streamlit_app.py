import streamlit as st
import pandas as pd
from PIL import Image

def main():

with st.container():
    st.image(Image.open('logo.png'))
   
	
	"""Welcome to Nova´s Horseracing Track!"""

	st.title("Welcome to Nova´s own private Horseracing Track!")

	menu = ["Welcome", "Tutorial", "Login", "SignUp"]
	choice = st.sidebar.selectbox("Menu",menu)

	if choice == "Welcome":
		st.subheader("Glad to have you here!")
		st.write("After opening your own betting account, you will be able to take your money and bet it on our wide array of race horses and jockeys - ready?")
		st.write("You can use our menu on the left to navigate. If you haven´t done any betting so far, we suggest you go and check out our 'Tutorial' Section before you proceed to the race-track!")
	
	elif choice == "Tutorial":
		st.subheader("How to bet on horses? After this you can´t loose anymore!")
	
	elif choice == "Login":
		st.subheader("Login Section")

		username = st.sidebar.text_input("User Name")
		password = st.sidebar.text_input("Password",type='password')
		if st.sidebar.button("Login"):
			# if password == '12345':
			create_usertable()
			hashed_pswd = make_hashes(password)

			result = login_user(username,check_hashes(password,hashed_pswd))
			if result:

				st.success("Logged In as {}".format(username))

				task = st.selectbox("Task",["Add Post","Analytics","Profiles"])
				if task == "Add Post":
					st.subheader("Add Your Post")

				elif task == "Analytics":
					st.subheader("Analytics")
				elif task == "Profiles":
					st.subheader("User Profiles")
					user_result = view_all_users()
					clean_db = pd.DataFrame(user_result,columns=["Username","Password"])
					st.dataframe(clean_db)
			else:
				st.warning("Incorrect Username/Password")


	elif choice == "SignUp":
		st.subheader("Create New Account")
		new_user = st.text_input("Username")
		new_password = st.text_input("Password",type='password')

		if st.button("Signup"):
			create_usertable()
			add_userdata(new_user,make_hashes(new_password))
			st.success("You have successfully created a valid Account")
			st.info("Go to Login Menu to login")



if __name__ == '__main__':
	main()
