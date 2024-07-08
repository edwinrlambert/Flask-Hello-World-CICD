pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "hello-cicd"
    }

    stages {
        stage("Checkout") {
            steps {
                checkout scm
            }
        }

        stage("Check Docker") {
            steps {
                script {
                    // Check if Docker is installed
                    try {
                        sh "docker --version"
                        echo "docker is installed."
                    } catch (Exception e) {
                        echo "Docker is not installed."
                        error "Stopping build because Docker is not installed."
                    }

                    // Check if Jenkins can run Docker commands.
                    try {
                        sh "docker info"
                        echo "Jenkins has permission to access Docker."
                    } catch (Exception e) {
                        echo "jenkins does not have permission to access Docker."
                        error "Stopping build because Jenkins cannot access Docker."
                    }
                }
            }
        }

        stage("Build Docker Image") {
            steps {
                script {
                    dockerImage = docker.build(env.DOCKER_IMAGE)
                }
            }
        }

        stage("Run Tests") {
            steps {
                script {
                    dockerImage.inside {
                        sh "python -m unittest discover -s tests"
                    }
                }
            }
        }

        
    }
}