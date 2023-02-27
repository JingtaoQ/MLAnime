pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('animepwd')
    }


    stages {
        stage('Building') {
            steps {
              sh 'pip3 install -r requirements.txt'
            }
        }
    stage('Testing') {
            steps {
              sh 'python3 test_app.py'
            }
        }

        stage('Deploying'){
            steps {
              sh 'docker build -t jingtaoqu/anime:frontend .'
            }
        }
        stage('Running'){
            steps {
              sh 'docker run -d -p 8003:8080 jingtaoqu/anime:frontend'
            }
        }	   

        
    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
