pipeline {
  environment {
    imagename = "amwell_test"
    registryCredential = 'IliaVa'
    dockerImage = ''
    tag = "${env.BUILD_NUMBER}"
  }
  agent any
  stages {
    stage('Cloning Git') {
      steps {
        git([url: 'https://github.com/iliava/Amwell_Test_V2.git', branch: 'main', credentialsId: 'iliava'])

      }
    }
    stage("Env Variables") {
            steps {
                echo "The build number is ${env.BUILD_NUMBER}"
                echo "You can also use \${BUILD_NUMBER} -> ${BUILD_NUMBER}"
                sh 'echo "I can access $BUILD_NUMBER in shell command as well."'
            }
        }
    stage('Building image') {
      steps{
        script {
          dockerImage = docker.build imagename:tag
           sh '''#!/bin/bash
                    docker stop $(docker ps -q --filter ancestor=amwell_test )
                    docker run -d -p 5000:5000 amwell_test
                '''
        }
      }
    }
  }
}
