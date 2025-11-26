# Laboratory Work #8 Report
## Jenkins Pipeline Implementation

### Student: Arshyn Anna
### Date: November 2024

### Objective:
Create a Jenkins pipeline that runs in Docker environment and executes the script from Lab 2.

### Implementation:

#### Pipeline Configuration: `Jenkinsfile`

#### Final Pipeline Code:
\`\`\`groovy
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
\`\`\`

### Pipeline Execution Flow:
1. **Checkout Stage:** Automatically clones the GitHub repository
2. **Test Script Stage:** 
   - Makes the script executable
   - Runs the count_files.sh script
   - Displays execution confirmation
3. **Complete Stage:** Outputs success message with student information

### Integration Features:
- **SCM Integration:** Connected to GitHub repository
- **Docker Environment:** Runs in Jenkins Docker container
- **Automated Execution:** Triggered on code changes
- **Multi-stage Workflow:** Clear separation of tasks

### Verification Results:
\`\`\`
Started by user Anna
[Pipeline] Start of Pipeline
[Pipeline] node
...
+ ./count_files.sh
count files: 54
+ echo Script works!
Script works...
Lab 8: Jenkins Pipeline - Done
Student: Arshyn Anna
Finished: SUCCESS
\`\`\`

### Success Metrics:
- Pipeline configuration valid and functional
- Successful SCM integration with GitHub
- Script execution in containerized environment
- Multi-stage workflow operational
- Clear success/failure reporting

### Completion Status:
All 8 laboratory works successfully integrated and operational.
