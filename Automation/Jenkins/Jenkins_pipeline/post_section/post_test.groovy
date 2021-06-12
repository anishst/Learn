pipeline {
    agent any
     environment {
      // Crendentials needed for scripts;
      // these needs to be set in Jenkins instance > Credentials for scripts to work
      MSTEAMS_HOOK = credentials("MSTEAMS_HOOK")
        }
    stages {
        stage('Example') {
            steps {
                echo 'Hello World'
            }
        }
    }
    post {
        always {
            echo 'I will always say Hello again!'
        }
        success {
                mail to: 'email',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong with ${env.BUILD_URL}"

            office365ConnectorSend (
            status: "SUCESS",
            //webhookUrl: "<url>",
            webhookUrl: "${MSTEAMS_HOOK}",
            color: '00ff00',
            message: "Test Successful: ${JOB_NAME} - ${BUILD_DISPLAY_NAME}<br>Pipeline duration: ${currentBuild.durationString}"
          )
        }
        failure {
          mail to: 'email',
             subject: "Failed Pipeline: ${currentBuild.fullDisplayName}",
             body: "Something is wrong with ${env.BUILD_URL}"

            office365ConnectorSend (
            status: "FAILED",
            //webhookUrl: "<url>",
            webhookUrl: "${MSTEAMS_HOOK}",
            color: 'd00000',
            message: "Test Failed: ${JOB_NAME} - ${BUILD_DISPLAY_NAME}<br>Pipeline duration: ${currentBuild.durationString}"
          )
        }
    }
}