// https://www.jenkins.io/doc/pipeline/steps/credentials-binding/
// https://www.jenkins.io/doc/book/pipeline/jenkinsfile/#for-secret-text-usernames-and-passwords-and-secret-files
pipeline {
   agent any

    environment {
        // store file in env var
        json_file = credentials('JSON_CONFIG_FILE')

    }
   stages {
      stage('Hello') {
         steps {
             dir('C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Jenkins\\Jenkins_pipeline\\secret_file_test'){
             // use local var
               withCredentials([file(credentialsId: 'JSON_CONFIG_FILE', variable: 'FILE')]) {
                  echo "%FILE%"
                  echo "%json_file%"
                  bat "python read_config.py"
                  }
             }
            echo 'Hello World'
         }
      }
   }
}
