pipeline {
   agent any
    
    parameters {
  choice choices: ['chrome', 'ie'], description: 'browser names', name: 'browser'
   choice choices: ['qae', 'qaa'], description: 'env url', name: 'url'
}
   stages {
      stage('Build') {
         steps {
            echo 'Building'
            echo browser
            echo url
         }
      }
      
    stage('Test') {
         steps {
            echo 'Testing'
            echo 'hello'
            
         }
      }


   }
}
