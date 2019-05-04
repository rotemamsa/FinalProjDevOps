pipeline{
    agent any
    stages{
        stage("GIT clone or pull"){
            steps{
			
			//	def exists = fileExists 'dir("${JENKINS_HOME}/workspace/devOpsPipe/FinalProjDevOps/dockerTest.py")'
			//	echo exists
			//	if (exists) {
					echo 'git init'
					bat 'git init'
					echo 'git pull'
					bat 'git pull https://github.com/rotemamsa/FinalProjDevOps.git'
			//	}
			//	else{
			//		echo 'git clone'
			//	    dir('./FinalProjDevOps')
			//	    bat 'git clone https://github.com/rotemamsa/FinalProjDevOps.git'
			//	}
		    }
        }
        stage("run docker-compose"){
            steps{
                echo 'docker-machine start'
                bat 'docker-machine start default'
               	sleep (time:30, unit:"SECONDS") 
                echo 'docker-compose up'
                bat 'docker-compose up -d'
             	sleep (time:30, unit:"SECONDS") 

            }
        }
         stage("run selenium test"){
            steps{
                echo 'run selenium test '
                bat 'python dockerTest.py'
            }
        }
}
}