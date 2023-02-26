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
        

    }
  triggers{
       githubPush()
  }
}
