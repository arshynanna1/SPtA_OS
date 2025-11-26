# Laboratory Work #5 Report
## DEB Package Creation

### Student: Arshyn Anna

### What was done:
Created a DEB package for Ubuntu/Debian that installs the file counting script.

### Files created in debian/ folder:
- control - package information and dependencies
- rules - build instructions  
- changelog - version history
- compat - compatibility version
- install - installation rules
- source/format - package format

### Package details:
- Name: count-files
- Version: 1.0-1
- Installs script to: /usr/bin/count-files

### Build command:
dpkg-buildpackage -us -uc

### Result:
DEB package successfully created and ready for installation on Debian/Ubuntu systems.

### Date: November 2024
