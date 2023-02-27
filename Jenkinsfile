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
	stage('Merge feature branch to main') {
            steps {
                script {
                    def gitBranch = "${env.BRANCH_NAME}"
                    if (gitBranch != "main") {
                        // Fetch the latest changes from the main branch
                        sh 'git fetch origin main'

                        // Checkout the main branch
                        sh 'git checkout main'

                        // Merge the feature branch into the main branch
                        sh "git merge origin/${gitBranch}"

                        // Push the changes to the remote main branch
                        sh 'git push origin main'

                        // Checkout the feature branch again
                        sh "git checkout ${gitBranch}"
                    }
                }
            }
        }


    }
    
  post{
      always{
         sh 'docker logout'
      }
  }
}
