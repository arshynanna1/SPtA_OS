# Laboratory Work #5 Report
## DEB Package Creation

### Student: Arshyn Anna
### Date: November 2024

### Objective:
Create a DEB package for the file counting script for Debian/Ubuntu systems.

### DEB Package Structure:
The package includes these files in debian/ directory:

- **debian/changelog** - Version history and changes
- **debian/compat** - Debhelper compatibility (version 13)  
- **debian/control** - Package metadata and dependencies
- **debian/install** - File installation instructions
- **debian/rules** - Build process configuration
- **debian/source/format** - Source code format (3.0 native)

### Package Information:
- **Name:** count-files
- **Version:** 1.0-1
- **Architecture:** all
- **License:** GPL-3.0

### Build Command:
\`\`\`bash
dpkg-buildpackage -us -uc
\`\`\`

### Testing:
- Package builds successfully
- Installs script to /usr/bin/count-files
- Script works after installation

### Status:
DEB package successfully created and tested.
