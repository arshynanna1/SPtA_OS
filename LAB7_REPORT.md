# Laboratory Work #7 Report
## Docker Container for Jenkins

### Student: Arshyn Anna
### Date: November 2024

### Objective:
Create a Dockerfile that runs Jenkins master with build tools for RPM and DEB package creation.

### Implementation:

#### Dockerfile Location: `docker/Dockerfile`

#### Dockerfile Content:
\`\`\`dockerfile
FROM jenkins/jenkins:lts

USER root

RUN apt-get update && \\
    apt-get install -y \\
    devscripts \\
    debhelper \\
    build-essential \\
    rpm \\
    git \\
    curl

RUN which dpkg-deb && which rpmbuild

RUN mkdir -p /home/jenkins/workspace
RUN chown jenkins:jenkins /home/jenkins/workspace

USER jenkins

RUN jenkins-plugin-cli --plugins \\
    git \\
    mailer \\
    ssh-slaves

EXPOSE 8080

CMD ["jenkins.sh"]
\`\`\`

### Docker Image Features:
- **Base Image:** Jenkins LTS (Long Term Support)
- **Build Tools Installed:**
  - devscripts, debhelper, build-essential (for DEB packages)
  - rpm (for RPM packages)
  - git, curl (for version control and downloads)

### Container Configuration:
- **User Management:** Runs as Jenkins user after tool installation
- **Workspace:** Created /home/jenkins/workspace directory
- **Ports:** Exposes 8080 for web interface and 50000 for agents
- **Plugins:** Pre-installed git, mailer, and ssh-slaves plugins

### Build Process:
\`\`\`bash
docker build -t jenkins-custom docker/
docker run -d -p 8080:8080 -p 50000:50000 --name jenkins jenkins-custom
\`\`\`

### Verification:
- Docker image builds successfully
- Jenkins starts and is accessible via web interface
- All build tools are available inside container
- Ready for CI/CD pipeline integration

### Purpose:
Provides a complete Jenkins environment with all necessary tools for building both RPM and DEB packages.
