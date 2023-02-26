pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                echo '开始拉取代码...'
                cleanWs()
                git branch: '$BRANCH_NAME', credentialsId: '1b458187-1203-4ef5-8f9a-97fe7576e4b1', url: 'http://gitea:3000/root/my-multibranch-pipeline.git'
            }
        }
        stage('Build') {
            steps {
                echo '开始构建代码...'
            }
        }
        stage('Archive') {
            steps {
                echo '开始打包文件...'
                archiveArtifacts '**/*'
            }
        }
        stage('Deploy') {
            steps {
                echo '开始部署文件...'
                sshPublisher(publishers: [sshPublisherDesc(configName: 'nginx', transfers: [sshTransfer(cleanRemote: false, excludes: '', execCommand: 'nginx -s reload', execTimeout: 120000, flatten: false, makeEmptyDirs: false, noDefaultExcludes: false, patternSeparator: '[, ]+', remoteDirectory: '$BRANCH_NAME', remoteDirectorySDF: false, removePrefix: '', sourceFiles: '**/*')], usePromotionTimestamp: false, useWorkspaceInPromotion: false, verbose: false)])
            }
        }
    }
    triggers {
        pollSCM 'H/2 * * * *'
    }
}
