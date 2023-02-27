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
              sh 'docker build -t anime/jenkins:0.1 .'
            }
        }
        stage('Running'){
            steps {
              sh 'docker run -d -p 8003:8080 anime/jenkins:0.1'
            }
        }	   
        stage('Login') {

		steps {
		    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
        
        stage('Push image to Hub'){
            steps{
		    sh 'docker push anime/jenkins:0.1'
	    }
        }
    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
