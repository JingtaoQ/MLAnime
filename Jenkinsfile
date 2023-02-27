pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhubpwd')
    }


    stages {
        stage('Building') {
            steps {
              sh 'pip3 install -r requirements.txt'
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
            stage('Merge feature to main') {
                steps {
                sh 'git checkout -b main'
                sh 'git merge feature'
                sh 'git push origin main'
                }
            }




    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
