from flask import Flask, render_template, request, redirect, session, flash, url_for
import openai
import os
from chatgpt import chatgpt
import db_user 
import db_joke
import bert_model
import json

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

# Set up the OpenAI API key
openai.api_key = os.getenv("OPEN_AI_KEY")

@app.route("/")
def start():
    return redirect("/first")

@app.route("/first")
def first():
    return render_template("first.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        session["username"] = username
        if username == 'admin' and db_user.login_user(username, password):
            return redirect("/admin_options")
        elif db_user.login_user(username, password):
            return redirect("/home")
        else:
            flash('Wrong Username or Password, Please Enter Again')
            return render_template("login.html", error="Invalid login credentials.")
    return render_template("login.html")


@app.route("/signup", methods=["GET", "POST"])
def signup():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        age = request.form["age"]
        gender = request.form["gender"]
        country = request.form["country"]
        fav_comedian = request.form["fav_comedian"]
        personality = request.form["personality"]
        if db_user.get_user_info_by_username(username):
            flash("The username is used")
            return render_template("signup.html")
        else:
            db_user.create_user(username, password, age, gender, country, fav_comedian, personality)
            return redirect("/login")
    return render_template("signup.html")


@app.route('/admin_options')
def admin_options():
    return render_template('admin_options.html')

@app.route('/database')
def show_users():
    users = db_user.get_all_user()
    jokes = db_joke.get_all_jokes()
    return render_template('database.html', users=users, jokes=jokes)

@app.route('/delete_user', methods=['POST'])
def delete_user():
    db_user.delete_user_by_username(username = request.form['username'])
    return redirect("/database")

@app.route('/delete_all_users', methods=['POST'])
def delete_all_users():
    db_user.delete_all_users()
    return redirect("/database")

@app.route('/delete_all_jokes', methods=['POST'])
def delete_all_jokes():
    db_joke.delete_all_jokes()
    return redirect("/database")

@app.route("/home", methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        keyword = request.form["keyword"]
        return redirect(url_for('result', keyword=keyword))
    return render_template('home.html')


@app.route('/result', methods=['GET','POST'])
def result():
    # Check if the user is logged in
    username = session.get('username', None)

    if request.method == 'POST':
        keyword = request.form["keyword"]
        
        # Check if the keyword has changed
        if 'keyword' in session and session['keyword'] == keyword:
            # print("keyword3: ", keyword)
            jokes = session.get('generated_jokes', [])  # Retrieve the jokes from the session
            ratings = session.get('generated_ratings', [])  # Retrieve the jokes from the session
        else:
            # Keyword has changed, so generate new jokes
            session['keyword'] = keyword  # Store the new keyword in the session

            _, _, age, gender, country, fav_comedian, _ = db_user.get_user_info_by_username(username)

            if fav_comedian is None:
                prompt = f"give me 7 jokes about {keyword} for a {age} years old {gender} who stays in {country}"
            else:
                prompt = f"give me 7 jokes about {keyword} for a {age} years old {gender} who stays in {country} using {fav_comedian} style"

            # get jokes from gpt
            gen_jokes = chatgpt(prompt)
            # get bert rating
            gen_ratings = bert_model.bert_rating(gen_jokes)
            # sort jokes based on rating and get top 5 
            jokes, ratings = bert_model.top_5_jokes(gen_jokes, gen_ratings)

            # Store the generated jokes in the session
            session['generated_jokes'] = jokes 
            session['generated_ratings'] = ratings 
            
        if "submit_button" in request.form:
            for j in range(len(jokes)):  # Assuming there are 5 jokes
                joke = jokes[j]
                rating = ratings[j]
                
                funny_rating = int(request.form.get(f'rate_{j+1}', 0))
                offensive_rating = int(request.form.get(f'rate_offensive{j+1}', 0))
                surprise_rating = int(request.form.get(f'rate_surprise{j+1}', 0))
                # Get the reality radio input value
                reality_rep_value = request.form.get(f'radio{j+1}', 'Yes')  # Default to 'Yes' if not provided
                # Set reality_rep_rating to 0 if the value is 'No'
                reality_rep_rating = 0 if reality_rep_value == 'No' else 1

                # Insert the ratings into your database
                db_joke.insert_joke(joke, keyword, rating, funny_rating, offensive_rating, surprise_rating, reality_rep_rating, username) 
            return render_template("home.html", confirmation_message="Thank you for your ratings!")  # Redirect to the home page
    return render_template('result.html', response=jokes, keyword=keyword)


with open('fixed_jokes.json', 'r', encoding='utf-8') as file:
    data = json.load(file)  
fixed_jokes = data['fixed_jokes']

@app.route('/participants', methods=['GET','POST'])
def participants():
    # Check if the user is logged in
    username = session.get('username', None)
    print("Username2: ", username)
    keyword = None
    jokes = None
    bert_rating = "No need"

    # Check if the user has submitted the ratings form
    if request.method == 'POST' and "submit_button" in request.form:
        for category in fixed_jokes:
            jokes = category['jokes']
            keyword = category['keyword']  # Get the keyword for this category
            
            for joke in jokes:
                print(joke)
                funny_rating = int(request.form.get(f'rate_{joke}', 0))
                offensive_rating = int(request.form.get(f'rate_offensive_{joke}', 0))
                surprise_rating = int(request.form.get(f'rate_surprise_{joke}', 0))
                reality_rep_value = request.form.get(f'radio_{joke}', 'Yes')
                reality_rep_rating = 0 if reality_rep_value == 'No' else 1

                # Store the ratings in the database, along with the keyword
                db_joke.insert_joke(joke, keyword, bert_rating, funny_rating, offensive_rating, surprise_rating, reality_rep_rating, username)

        return render_template("home.html", confirmation_message="Thank you for your ratings!")

    return render_template('participants.html', jokes=fixed_jokes, keyword=keyword)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
