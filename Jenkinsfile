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
          dockerImage = docker.build imagename
           sh '''#!/bin/bash

                    docker ps
                    docker stop $(docker ps -q --filter ancestor=amwell_test )
                    ls
                '''
        }
      }
    }
  }
}
