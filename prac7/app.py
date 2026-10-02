from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)


#script
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'YOUR_GITHUB_REPOSITORY_URL'
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirement.txt'
            }
        }

        stage('Test') {
            steps {
                bat 'python -m pytest -v'
            }
        }

        stage('Deploy') {
            steps {
                bat 'echo Application deployed successfully'
            }
        }
    }
}

