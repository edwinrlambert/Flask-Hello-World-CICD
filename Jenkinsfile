pipeline {
    agent any
    environment {
        // Update this with your Docker Hub username and the repository name
        DOCKER_IMAGE = 'edwinrlambert/hello-cicd'

        // Specify the path to your kubeconfig file correctly for a Windows machine.
        KUBECONFIG = 'C:\\Users\\user\\.kube\\config'
    }
    stages {
        stage('Test') {
            steps {
                script {
                    bat "python -m unittest discover -s tests"
                }
            }
        }
        stage('Build') {
            steps {
                script {
                    bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                    bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Now using 'hello-cicd' as the container name as per your deployment details
                    bat "kubectl set image deployment/hello-cicd hello-cicd=${DOCKER_IMAGE}:${BUILD_NUMBER} -n hello-cicd-namespace"
                }
            }
        }
    }
}