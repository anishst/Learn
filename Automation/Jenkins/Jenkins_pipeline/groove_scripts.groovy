// Groovy script  - works
pipeline {
   agent any

   stages {
      stage('Hello') {
          
        //   define env vars
            environment {
        // Crendential dependencies.  UsernamePassword credentials automatically set _USR and _PSW variables.
        KEY = credentials("HLAS")
        USER_ID = "${KEY_USR}"
        PSWD = "${KEY_PSW}"
        }
         steps {
            // bat 'pytest -v -s C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Selenium\\python\\Jenkins_pipeline\\main_script.py'
            bat 'python  C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Selenium\\python\\Jenkins_pipeline\\get_command_args.py $Env:USER_ID $Env:PSWD'
            
         }
      }
   }
}