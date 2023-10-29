## Guide to set up and run our web application

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


