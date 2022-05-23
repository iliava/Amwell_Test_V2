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
           sh '''#!/bin/bash
              docker stop $(docker container ls -q --filter name=amwell_test*)
           '''
           sh "docker run --name $imagename.$BUILD_NUMBER -d -p 5000:5000 $imagename:$BUILD_NUMBER"
        }
      }
    }
    stage('Stop Old Container & Clean') {
      steps{
        script {
           sh '''#!/bin/bash
              docker stop $(docker container ls -q --filter name=amwell_test*)
              docker container prune -f
           '''
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
