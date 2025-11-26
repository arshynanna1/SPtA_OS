pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Build and Install') {
            steps {
                sh '''
                    echo "Building DEB package..."
                    dpkg-buildpackage -us -uc
                    
                    echo "Installing package..."
                    sudo dpkg -i ../count-files_1.0-1_all.deb
                '''
            }
        }
        
        stage('Run Script') {
            steps {
                sh '''
                    echo "Executing count-files script:"
                    count-files
                    echo "Script completed successfully!"
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline finished"
        }
    }
}
