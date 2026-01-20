
pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Pulling code from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t energy-devops .'
            }
        }

        stage('Run Energy App') {
            steps {
                sh 'docker run -i energy-devops'
            }
        }
    }

    post {
        success {
            echo 'CI pipeline completed successfully'
        }
        failure {
            echo 'CI pipeline failed'
        }
    }
}
