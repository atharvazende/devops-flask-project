// pipeline {
//     agent any //Run on any available Jenkins agent/node

//     stages { //Pipeline is divided into logical stages. Each stage can have multiple steps.

//         stage('Clone') {
//             steps {
//                 echo 'Cloning Repository'
//             }
//         }

//         stage('Build') { //Represents one step in the CI/CD process.
//             steps { //Contains commands executed inside that stage.
//                 echo 'Building Application' //Prints message to build logs.
//             }
//         }

//         stage('Test') {
//             steps {
//                 echo 'Running Tests'
//             }
//         }
//     }
// }

pipeline {
    agent any

    environment {
        // Define environment variables here if needed
        IMAGE_NAME = "atharvazende/flask-app"
        IMAGE_TAG = "v1"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Build') {
            steps {
                echo 'Building Application'
            }
        }

        stage('Docker Build') {
            steps {
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Docker Login'){
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds', 
                        usernameVariable: 'DOCKER_USER',
                         passwordVariable: 'DOCKER_PASS'
                         )
                         ]) {
                    sh "echo $DOCKER_PASS | docker login -u $DOCKER_USER --password-stdin"
                }
            }
        }
        stage('Docker Push') {
            steps {
                sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
            }
        }
    }
}