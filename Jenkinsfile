pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhubpwd')
    }
  stages {
	stage('Merge feature to main') {
                steps {
                sh 'git checkout main'
                sh 'git merge origin/feature'
                sh 'git pull origin main'
                sh 'git merge origin/feature'
                sh 'git push origin main'
                }
            }
  	stage('Login') {

		steps {
		    sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
			}
		}
        
        stage('Push image to Hub'){
            steps{
		    sh 'docker push jingtaoqu/anime:frontend'
	    }
        }
      }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
