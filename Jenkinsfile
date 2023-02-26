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
}
