// testing groovy script try catch
pipeline {
  agent any
  stages {
    stage("Run unit tests"){
      steps {
        script {
          try {
              bat 'python C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Jenkins\\Jenkins_pipeline\\try_catch\\script1.py'
          }
          catch (all) {
            echo 'Something failed, I should sound the klaxons!'
            //currentBuild.result='FAILURE'
        }
          finally {
            echo "Testing try catch"
          }
        }
      }
    }

     stage('Error Steps') {
            steps {
                // will mark the build as success but stage as failure
                catchError(buildResult: 'SUCCESS', stageResult: 'FAILURE') {
                   bat 'python C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Jenkins\\Jenkins_pipeline\\try_catch\\script1.py'
                }
            }
        }
    stage ('Speak') {
      steps{
        bat 'python C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Jenkins\\Jenkins_pipeline\\\\try_catch\\script2.py'
      }
    }


  }
}