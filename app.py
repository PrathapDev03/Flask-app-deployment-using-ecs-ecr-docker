from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    return f"Welcome {username}! ECS + ECR + Docker Deployment Successful"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)