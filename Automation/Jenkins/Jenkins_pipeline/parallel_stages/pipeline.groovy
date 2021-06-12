// testing groovy script to do parallel runs using parallel feature 
pipeline {
   agent any
   stages {
      stage('Parallel Stage') {
         steps {
            parallel (

               "Taskone" : {
                  bat 'python C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Selenium\\python\\Jenkins_pipeline\\parallel_stages\\script1.py'
               },
            
               "Tasktwo" : {
               bat 'python C:\\Users\\532975\\Documents\\Automation\\GitHub\\Automation\\Selenium\\python\\Jenkins_pipeline\\\\parallel_stages\\script2.py'
               }
            )
          }
      }
   }
}