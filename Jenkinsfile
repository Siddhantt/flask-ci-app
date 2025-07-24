pipeline {
  agent any

  environment {
    DOCKER_IMAGE = "siddhant271299/flask-ci-app"
  }

  stages {
    stage('Checkout') {
      steps {
        git 'https://github.com/Siddhantt/flask-ci-app.git'
      }
    }

    stage('SonarQube Analysis') {
      steps {
        withSonarQubeEnv('SonarQube') {
          sh 'sonar-scanner'
        }
      }
    }

    stage('Build Docker Image') {
      steps {
        sh 'docker build -t $DOCKER_IMAGE .'
      }
    }

    stage('Scan with Trivy') {
      steps {
        sh 'trivy image $DOCKER_IMAGE'
      }
    }

    stage('Push to DockerHub') {
      steps {
        withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
          sh '''
            echo "$DOCKER_PASS" | docker login -u "$DOCKER_USER" --password-stdin
            docker push $DOCKER_IMAGE
          '''
        }
      }
    }
  }
}
