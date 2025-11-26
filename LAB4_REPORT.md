# Laboratory Work #4 Report
## RPM Package Creation

### Student: Arshyn Anna
### Date: November 2024

### Objective:
Create an RPM package that includes the file counting script for Red Hat-based Linux distributions.

### Implementation:

#### SPEC File Location: `rpm/count_files.spec`

#### Package Specifications:
- **Name:** count_files
- **Version:** 1.0
- **Release:** 1
- **Architecture:** noarch
- **License:** GPL

#### SPEC File Content:
\`\`\`spec
Name: count_files
Version: 1.0
Release: 1%{?dist}
Summary: Count files in /etc directory
License: GPL
URL: https://github.com/arshynanna1/SPtA_OS
Source0: count_files.sh

%description
This package counts the number of files in the /etc directory.

%prep

%build

%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/count_files.sh

%files
%{_bindir}/count_files.sh
\`\`\`

### Build Process:
- Created SPEC file with proper RPM structure
- Configured installation path to /usr/bin
- Set executable permissions for the script
- Designed as architecture-independent package (noarch)

### Key RPM Sections:
- **%description:** Package functionality description
- **%install:** File installation instructions
- **%files:** List of files included in package

### Verification:
- SPEC file syntax validated
- Package structure follows RPM standards
- Ready for automated building in CI/CD pipeline

### Development Status:
RPM package specification completed and ready for building.
