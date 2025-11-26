pipeline {
    agent any
    
    stages {
        stage('Checkout') {
            steps {
                echo "Checking out code from GitHub..."
            }
        }
        
        stage('Test') {
            steps {
                echo "Testing the pipeline..."
                sh 'pwd && ls -la'
            }
        }
        
        stage('Run Script') {
            steps {
                sh '''
                    echo "Running count_files.sh:"
                    ./count_files.sh
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline completed!"
        }
    }
}
