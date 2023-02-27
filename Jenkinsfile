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

        stage('Merge feature to main') {
            steps {
                sh 'git checkout feature'
                sh 'git pull origin feature'
                sh 'git checkout main'
                sh 'git pull origin main'
                sh 'git merge feature'
                sh 'git push origin main'
            }
            post {
                always {
                    script {
                        def currentBuildResult = currentBuild.result ?: 'SUCCESS'
                        if (currentBuildResult == 'SUCCESS') {
                            echo 'Feature branch merged into main branch successfully'
                        } else {
                            echo 'Feature branch merge failed'
                        }
                    }
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
