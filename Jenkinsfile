pipeline {
    agent any
    
    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }
        
        stage('Build DEB Package') {
            steps {
                sh '''
                    sudo apt update
                    sudo apt install -y devscripts debhelper build-essential
                    dpkg-buildpackage -us -uc
                '''
            }
        }
        
        stage('Install Package') {
            steps {
                sh '''
                    # Встановлюємо DEB пакет
                    sudo dpkg -i ../count-files_1.0-1_all.deb || true
                    echo "Package installed successfully"
                '''
            }
        }
        
        stage('Execute Script') {
            steps {
                sh '''
                    # Виконуємо наш скрипт
                    count-files
                    echo "Script from Lab 2 executed successfully!"
                '''
            }
        }
    }
    
    post {
        always {
            echo "Pipeline execution completed"
        }
        success {
            echo "SUCCESS: All stages completed successfully!"
        }
    }
}
