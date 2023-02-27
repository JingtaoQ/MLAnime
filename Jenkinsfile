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
              sh 'docker build -t jingtaoqu/jenkins:latest .'
            }
        }
        stage('Running'){
            steps {
              sh 'docker run -d -p 8003:8080 jingtaoqu/jenkins:latest'
            }
        }	   
        stage('Login') {

		steps {
		    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
        
        stage('Push image to Hub'){
            steps{
		    sh 'docker push jingtaoqu/jenkins:latest'
	    }
        }
    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
