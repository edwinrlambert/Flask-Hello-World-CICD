pipeline {
    agent any
    environment {
        // Update this with your Docker Hub username and the repository name
        DOCKER_IMAGE = 'edwinrlambert/hello-cicd'

        // Specify the path to your kubeconfig file correctly for a Windows machine.
        KUBECONFIG = 'C:\\Users\\user\\.kube\\config'
    }
    stages {
        stage('Build') {
            steps {
                script {
                    // Using 'bat' instead of 'sh' for Windows batch command execution
                    // Ensure Docker CLI and kubectl are available in your system PATH.
                    bat "docker build -t ${DOCKER_IMAGE}:${BUILD_NUMBER} ."
                    bat "docker push ${DOCKER_IMAGE}:${BUILD_NUMBER}"
                }
            }
        }
        stage('Deploy') {
            steps {
                script {
                    // Ensure kubectl is configured and has access to your Kubernetes cluster.
                    // Update the deployment command accordingly if needed.
                    bat "kubectl set image deployment/hello-cicd hello-cicd=${DOCKER_IMAGE}:${BUILD_NUMBER} --record"
                }
            }
        }
    }
}
