pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('animepwd')
    }

    stages {
        stage('Build and test feature branch') {
            when {
                branch 'feature/*'
            }
            steps {
                sh 'npm install'
                sh 'npm run test'
            }
        }
        stage('Build and Unit Test') {
            steps {
                sh 'mvn clean install'
            }
        }
        stage('Building') {
            steps {
              sh 'pip3 install -r requirements.txt'
            }
        }
        stage('Testing') {
            steps {
              sh 'python -m unittest'
            }
        }
        stage('Deploying'){
            steps {
              sh 'docker build -t jingtaoqu/project0117:latest .'
            }
        }
    }
  triggers{
       githubPush()
  }
}
