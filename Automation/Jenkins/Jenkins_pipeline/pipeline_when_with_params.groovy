pipeline {
    agent any
    parameters {
          choice  choices: ['greeting' , 'silence'],  description: '',name: 'REQUESTED_ACTION'
          choice  choices: ['ie' , 'chrome'],  description: '',name: 'BROWSER'
    }

    stages {
        stage ('Speak') {
            when {
                // Only say hello if a "greeting" is requested
                expression { params.REQUESTED_ACTION == 'greeting' }
            }
            steps {
                echo "Hello, Anish!"
            }
        }


        stage ('Speak Chrome') {
            when {
                // Only run if chrome is requested
                expression { params.BROWSER == 'chrome' }
            }
            steps {
                echo "Running Chrome Tests"
            }
        }
        }
}