pipeline {
  environment {
    imagename = "amwell_test"
    dockerImage = ''
  }
  agent any
  stages {
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Run New Container') {
      steps{
        script {
          sh "docker run --name $imagename.$BUILD_NUMBER -d -p 5000:5000 $imagename:$BUILD_NUMBER"
        }
      }
    }
  }
}
