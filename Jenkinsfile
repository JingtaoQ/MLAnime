pipeline {
    agent any

    stages {
        stage('Building') {
            steps {
              sh 'pip3 install -r requirement.txt'
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
