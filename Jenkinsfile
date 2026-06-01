pipeline {
    agent any

    environment {
        IMAGE_NAME     = "jenkins-pipeline-app"
        IMAGE_TAG      = "1.0.${BUILD_NUMBER}"
        CONTAINER_NAME = "pipeline-app"
        APP_PORT       = "5000"
    }

    stages {

        stage('Setup Network') {
            steps {
                sh 'docker network create jenkins_network || true'
                sh 'docker network connect jenkins_network jenkins || true'
            }
        }

        stage('Build') {
            steps {
                echo '📦 Installing dependencies...'
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                echo '🧪 Running tests...'
                sh '''
                    . venv/bin/activate
                    pytest tests/ -v --tb=short
                '''
            }
            post {
                always { echo '✅ Test stage complete.' }
            }
        }

        stage('Docker Build') {
            steps {
                echo '🐳 Building Docker image...'
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
                sh "docker tag ${IMAGE_NAME}:${IMAGE_TAG} ${IMAGE_NAME}:latest"
            }
        }

        stage('Deploy') {
            steps {
                echo '🚀 Deploying container...'
                sh """
                    docker stop ${CONTAINER_NAME} || true
                    docker rm ${CONTAINER_NAME} || true
                    docker run -d --name ${CONTAINER_NAME} --network jenkins_network -p 8282:5000 --restart unless-stopped ${IMAGE_NAME}:${IMAGE_TAG}
                """
            }
        }

        stage('Health Check') {
            steps {
                echo '🔍 Waiting for app to start...'
                sh 'sleep 8'
                sh "curl -f http://pipeline-app:5000/health || exit 1"
                echo '✅ App is healthy!'
            }
        }
    }

    post {
        success { echo "🎉 Pipeline #${BUILD_NUMBER} succeeded!" }
        failure { echo "❌ Pipeline #${BUILD_NUMBER} failed." }
        always {
            echo '🧹 Cleaning up...'
            sh 'docker image prune -f || true'
        }
    }
}