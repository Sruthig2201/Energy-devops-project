pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Code checked out from GitHub'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t energy-devops .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run --rm energy-devops'
            }
        }
    }
}
