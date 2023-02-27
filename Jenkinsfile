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

        stage('Deploying') {
            steps {
                sh 'docker build -t jingtaoqu/anime:frontend .'
            }
        }

        stage('Running') {
            steps {
                sh 'docker run -d -p 8003:8080 jingtaoqu/anime:frontend'
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
    
    post {
        always {
            sh 'docker logout'
        }
    }
}
 }
