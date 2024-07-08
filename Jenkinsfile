pipeline {
    agent any
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("hello-cicd")
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    docker.image("hello-cicd").run("-p 5000:5000")
                }
            }
        }
    }
}
