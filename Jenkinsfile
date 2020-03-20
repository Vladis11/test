pipeline {
    agent any
    environment {
        PATH="/var/jenkins_home/miniconda3/bin:$PATH"
    }
    stages {
    	stage('Build Environment') {
    		steps {
    			sh '''conda create --yes -n ${BUILD_TAG} python
                      source activate ${BUILD_TAG} 
                      pip install nose coverage nosexcover pylint
          		'''   		
    		}   		
    	}      
        stage ('Test') {
            steps {
				sh '''
					  source activate ${BUILD_TAG}
			          nosetests -sv --with-xunit --xunit-file=nosetests.xml --with-xcoverage --xcoverage-file=coverage.xml			         
		        '''
            	
            }
        }
        stage ('Pylint Static Code Analysis') {
        	steps {
        		sh '''
					  source activate ${BUILD_TAG}
					  pylint --generate-rcfile > .pylintrc
					  pylint --rcfile=.pylintrc $(find . -iname "*.py" -print) -r n --msg-template="{path}:{line}: [{msg_id}({symbol}), {obj}] {msg}" > pylint-report.txt || exit 0			         
		        '''
        	}
        	
        }
        stage('SonarQube analysis') {
            steps {
                script {
                  scannerHome = tool 'sonar'
                }
                withSonarQubeEnv('sonar') {
                  sh "${scannerHome}/bin/sonar-scanner"
                }
            }
        }
               
    }
    post {
        always {
            sh 'conda remove --yes -n ${BUILD_TAG} --all'
        }
    }

}
