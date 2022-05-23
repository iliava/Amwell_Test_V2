pipeline {
  environment {
    imagename = "amwell_test"
    registryCredential = 'IliaVa'
    dockerImage = ''
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/iliava/Amwell_Test_V2.git', branch: 'main', credentialsId: 'iliava'])

      }
    }
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
  }
}
