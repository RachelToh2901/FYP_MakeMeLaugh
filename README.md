## Guide to use our web application (End User Guide)

This section will provide a step by step guide on how to use the web application. To access to the web app online, they will need to use this ip address http://159.89.201.35/

#### 1. First page - Login/Signup

This is the first page of the web app. Users can choose to login or signup by clicking the button shown. First time users are required to sign up an account first before login. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/first_page.png "first_page screenshot")

#### 2. Signup

If users clicked on the ‘Signup’ button in the previous page, they will be led to this signup page. Users need to put in information requested in the sign up page. Once all information is filled up, users need to click on the ‘Signup’ button to sign up this account with the info given. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/signup_page.png "signup_page screenshot")

If users found out that they already have an account, users can click on the ‘Login’ text at the bottom to proceed to the login page. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/signup_button.png "signup_button screenshot")

#### 3. Login

Users are required to login first. They will need to input their username and password they provided during signup. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/login_page.png "login_page screenshot")

If a wrong username or password is given, an error message will pop up at the top of the page, and users need to re-enter their username and password. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/login_error_msg.png "login_error_msg screenshot")

#### 4. Enter Keyword

Users can enter a keyword to generate a joke related to the keyword entered. After entering the keyword, users need to press the ‘Generate Joke’ button to get the jokes. If users want to quit from the web app, users can click on the ‘Exit’ button to get back to the first page. 

*(Note: Please ignore the ‘Additional Jokes’ button, that’s for the joke annotation task)*

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/main_wo_keyword.png "main_wo_keyword screenshot")

Users must at least input a word into the black field to generate jokes. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/main_with_keyword.png "main_with_keyword screenshot")

#### 5. Rate Jokes

Users will receive 5 jokes related to the keyword entered. Users can give rating to the jokes, rating including the funny level of the joke, offensive level, surprise level, and can they relate the joke to the reality (reality representation). 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/result_page.png "result_page screenshot")

To submit the feedback/rating, users need to click on the ‘Submit’ button at the bottom of the page. If users want to get other jokes, users can click on the ‘Generate another joke’ button, this will lead the users to the previous page. Else if users want to quit, users can click on the ‘Exit’ button. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/result_page_buttons.png "result_page_buttons screenshot")


___


## Guide to set up and run our web application (Technical Guide)

#### 1. Clone project to local repository

To clone the project to local repository, use command 
git clone https://github.com/TohXiaoYing/MakeMeLaugh.git

However, this repo contains some large files. In order to push to GitHub, please use the Git Large File Storage (LFS) system. More information about LFS and its setup: https://git-lfs.com/


#### 2. Set up virtual environment

Virtual environments are very helpful and important for us to install only libraries needed for this project and make sure they don’t mess up with the main one. Besides, it is easier to identify necessary libraries needed for the project by using “pip list” in terminal code.

How to create and activate virtual environment:
1. Install virtual environment - `pip install virtualenv`

2. Create virtual environment **virtualenv [environmentname]** - `virtualenv myenv`

3. Activate virtual environment **[environmentname]\Scripts\activate**
    - Windows - `myenv\Scripts\activate`
    - Mac - `source ./myenv/bin/activate`

4. Deactivate virtual environment - `deactivate`

Once activate, you will see your virtual env at the terminal in bracket ().
If deactivated, the bracket will disappear.

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/virtualenv.png "virtualenv screenshot")


#### 3. Install libraries/packages

All the libraries or packages needed for this project are listed in **requirements.txt**. Install them using the command `pip install -r requirements.txt`. **Remember to do the installation in the virtual environment.**

After installation, you can use command `pip list` to check whether the libraries are installed correctly. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/pip_list.png "pip list screenshot")


#### 4. Create .env file

This project required GPT to generate jokes. Generate an OpenAI API key from the OpenAI website, then put the API key in this .env file. 

If you have created your own account in OpenAI, you can generate your own key, then you can run chatgpt through API. Can refer to this link to see how to generate your own API key: https://www.howtogeek.com/885918/how-to-get-an-openai-api-key/
This OpenAI API key is used in the chatgpt.py python file. The library `python-dotenv` is used to load values from a .env file. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/load_dotenv.png "load_dotenv screenshot")


#### 5. Run myApp.py

This file contains the Flask command. To start the web application, run the command python myApp.py in the terminal. Then you will see the output shown as below. `Ctrl+click` on the ip address given or copy paste it to the web browser to run the app. To stop the web app from running, just type `Ctrl+C` in the terminal. 

![alt text](https://github.com/TohXiaoYing/MakeMeLaugh/blob/main/images/python_myApp.png "python myApp screenshot")


