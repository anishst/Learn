// testing groovy script timeout
pipeline {
  agent any
  stages {
        stage('Deploy') {
          steps {
            timeout(time:5, unit: 'SECONDS') {
              // sh 'sleep 3' 
              powershell "Start-Sleep -Seconds 3"
            }
          }
    }
  }
}
