// using global variables across stages

def report_list = []
def msgstring = ""
pipeline {
    agent any
    parameters { choice(name: 'RUN', choices: ['DEV', 'QA', 'BUILD'], description: '') }
    stages {
        stage('Dev') {
            when {
                expression { params.RUN == 'DEV'}
            }
            steps {
                echo 'Dev test'

                script {
                    report_list.add("<li>Dev</li> URL for build ${currentBuild.number}; build URL: ${env.BUILD_URL}")
                }
            }
        }
        stage ('QA'){
            steps{
                catchError(buildResult: 'FAILURE', stageResult: 'FAILURE'){
                    echo  "QA steps "
                        script {
                        report_list.add("<li>QA</li> URL for ${currentBuild.number}; build URL: ${env.BUILD_URL}")
                    }
                }

            }
        }
        stage ('Build'){
            steps{
                script {
                    report_list.add("<li>BUILD</li> URL for ${currentBuild.number}; build URL: ${env.BUILD_URL}")
                }
            }
        }
    }
    post{
        always {

            echo "all done!"
            sh "echo ${currentBuild.number}"
            script{
                msgstring = """<h2>report</h2>\
                test run details - Duration: ${currentBuild.durationString}"""
                report_list.each {
                    msgstring = msgstring + """$it<br/>"""
                    println(msgstring)
                }

            }
            // msg to be send to ms teams; slack etc.
            echo "${msgstring}"
        }
    }
}