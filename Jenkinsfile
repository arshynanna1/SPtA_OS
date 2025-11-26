pipeline {
    agent any
    stages {
        stage('Test Script') {
            steps {
                checkout scm
                sh '''
                    chmod +x count_files.sh
                    ./count_files.sh
                    echo "Script works!"
                '''
            }
        }
        stage('Complete') {
            steps {
                echo "Lab 8: Jenkins Pipeline - Done"
                echo "Student: Arshyn Anna"
            }
        }
    }
}
