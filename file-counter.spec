Name:           file-counter
Version:        1.0
Release:        1
Summary:        Count files in /etc directory

License:        MIT
URL:            https://github.com/arshynanna1/SPtA_OS
Source0:        count_files.sh

BuildArch:      noarch
Requires:       bash

%description
Bash script to calculate amount of files in /etc directory

%install
mkdir -p %{buildroot}/usr/local/bin
install -m 755 %{SOURCE0} %{buildroot}/usr/local/bin/file-counter

%files
/usr/local/bin/file-counter

%changelog
* Wed Oct 16 2024 anyashka <anyashka> - 1.0-1
- First RPM build
