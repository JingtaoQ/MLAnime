
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
              sh 'docker build -t jingtaoqu/anime:model .'
            }
        }
      stage('Volumne'){
        steps {
              sh 'docker volume create model'
              sh 'docker run -d --name=model --mount source=MLAnime,destination=/usr/share/nginx/model nginx:latest'
				}
      }
        stage('Running'){
            steps {
              sh 'docker run -d -p 8003:8080 jingtaoqu/anime:model'
            }
        }	   

			stage('Push to main') {
			            steps {
			              script {
			                def gitBranch = "${env.BRANCH_NAME}"
			                if (gitBranch == "main") {
			                  sh 'git push origin main'
			                } else {
			                  echo "Skipping push to main for branch: ${gitBranch}"
			                }
			              }
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

