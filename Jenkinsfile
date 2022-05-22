pipeline {
  environment {
    imagename = "amwell_test"
    registryCredential = 'IliaVa'
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
          docker.build amwell_Flask
        }
      }
    }
    stage('Deploy Image') {
      steps{
        script {
          docker run -d -p 5000:5000 amwell_Flask
          }
        }
      }
    }
  }
}
