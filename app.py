from flask import Flask, render_template, request

# TODO: create new Flask app
app = Flask(__name__)
users=[]

@app.route("/")
def main_page():
    # TODO: return index.html
    return render_template('index.html')


# TODO: Add route for sign up
@app.route('/signup', methods= ['post'])
def sign_up():
    # TODO: get user input from request
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']

    if not user_exists(email=email, username=username, password=password):
        users.append(
            {
                'email': email,
                'username': username,
                'password': password
            }
        )
        return "<h2>New user has been created</h2>"
    else:
        return "<h2>This user already exists</h2>"

#not the same cpmment
def user_exists(email, username, password):
    # TODO: check for user if exists, you can use an array as your records.
    for user in users:
        if user['username'] == username or user['email'] == email:
            return True
    return False

    
app.run(debug=True)
