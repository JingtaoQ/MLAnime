pipeline{
 agent any
 environment {
        DOCKERHUB_CREDENTIALS=credentials('animepwd')
    }
 stages {
        stage('Build') {
            steps{
                sh 'docker build -t anime:0.1 .'
            }
        }
        stage('login') {
            steps{
                sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
            }
        }
        stage('push') {
            steps{
                sh 'docker push anime:0.1'
            }
        }
    }
 post {
     always {
        echo 'end'
     }
 }
}
