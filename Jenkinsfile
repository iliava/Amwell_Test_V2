pipeline {
  environment {
    imagename = "amwell_test"
    dockerImage = ''
  }
  agent any
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
