pipeline {
    agent any

    stages {

        stage('Clone') {
            steps {
                git 'https://github.com/jyothsna-jarugulla/student-feedback-system.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t feedback-app .'
            }
        }

        stage('Deploy') {
            steps {
                sh 'ansible-playbook ansible/deploy.yml'
            }
        }

    }
}
