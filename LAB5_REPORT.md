# Laboratory Work #5 Report

## Topic: "Software Packaging: Creating DEB Package"

---

## Objective:
Master the methodology of creating DEB packages for Debian/Ubuntu-based Linux distributions. Learn to package custom scripts into a format suitable for distribution and installation through the package management system.

---

## Package Architecture:

### DEB Packaging Structure:
\`\`\`
debian/
├── changelog      # Version change history (maintainer scripts)
├── compat         # Debhelper compatibility version (13)
├── control        # Package metadata (dependencies, description)
├── install        # File installation instructions
├── rules          # Makefile for build process
└── source/
    └── format     # Source code format (3.0 native)
\`\`\`

---

## Implementation Stages:

### 1. Environment Preparation and Structure
- Initialization of \`debian/\` directory with appropriate subdirectories
- Installation of required tools: \`devscripts\`, \`debhelper\`, \`build-essential\`

### 2. Package Metadata Configuration
**File \`debian/control\` contains:**
- Package identification (Name, Version, Architecture)
- Build dependencies (Build-Depends)
- Functional description (Description)

### 3. Build Process Configuration
**File \`debian/rules\` defines:**
- Standard debhelper targets (\`dh $@\`)
- Custom installation rules (\`override_dh_auto_install\`)
- Copying source script to \`/usr/bin/\`

### 4. Package Building and Validation
\`\`\`bash
dpkg-buildpackage -us -uc  # Build without signing
\`\`\`
Validation of structure and dependencies correctness.

---

## Testing and Validation:

### Testing Procedure:
1. Package installation: \`sudo dpkg -i count-files_1.0-1_all.deb\`
2. Integration check: \`which count-files\`
3. Functional testing: \`count-files\`

### Test Results:
- Package successfully integrates with dpkg
- Script accessible via PATH (\`/usr/bin/count-files\`)
- Functionality correct: returns **97 files** in /etc

---

## Results:

### Obtained DEB Package:
- **Name:** \`count-files\`
- **Version:** \`1.0-1\`
- **Architecture:** \`all\`
- **Size:** ~5KB

### Functional Characteristics:
- Automatic installation to system PATH
- Validation through Ubuntu package manager
- Compatibility with package management system

---

## Conclusions:
DEB packaging is an effective method for software distribution in Debian-based systems. The created package complies with Ubuntu standards and can be used for automated script deployment in production environments.

---
**Performed by:** Arshyn Anna  
**Date:** November 26, 2024
