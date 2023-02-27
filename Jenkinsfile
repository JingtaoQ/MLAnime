
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
              sh docker.image('my-docker-image').run('-v /path/to/model:/model')
              sh 'docker build -t jingtaoqu/anime:model .'
            }
        }
      stage('Volumne'){
        steps {
              sh 'docker volume create model'
              sh 'docker run -d --name=model --mount source=MLAnime/outputmodel.pkl,destination=/usr/share/nginx/model nginx:latest'
				}
      }
        stage('Running'){
            steps {
              sh 'docker run -d -p 8003:8080 jingtaoqu/anime:model'
            }
        }	   
        stage('Login') {

		steps {
		    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
        
        stage('Push image to Hub'){
            steps{
		    sh 'docker push jingtaoqu/anime:model'
	    }
        }
    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
}
