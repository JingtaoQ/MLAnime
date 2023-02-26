pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('animepwd')
    }

    stages {
        
        stage('Test feature branch') {
            when {
                branch 'feature/*'
            }
            steps {
                sh 'pip3 install -r requirements.txt'
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
