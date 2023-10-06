from flask import Flask


app = Flask(__name__)


@app.route('/')
def team_name():
    return '<p>Team 4<br/>Team Members: Hamou Kamber and Sigdel Alina</p>'




if __name__ == '__main__':
    app.run()
