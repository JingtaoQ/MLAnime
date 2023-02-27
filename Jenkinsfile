pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }


        stage('Merge to main') {
            when {
                branch 'feature/*'
            }
            steps {
                sh 'git checkout main'
                sh 'git merge origin/${env.BRANCH_NAME}'
                sh 'git push origin main'
            }
        }
    }

    post {
        always {
            sh 'git checkout ${env.BRANCH_NAME}'
            sh 'git pull origin ${env.BRANCH_NAME}'
            sh 'git fetch --tags'
        }
    }
}
