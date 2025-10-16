Name:           count_files
Version:        1.0
Release:        1%{?dist}
Summary:        Script that counts files in the /etc directory
Group:          Applications/System
License:        GPL
URL:            https://github.com/arshynanna1/SPtA_OS
Source0:        count_files.sh
BuildArch:      noarch

%description
This package counts the number of files in the /etc directory.

%prep
%setup -q


%install
mkdir -p %{buildroot}/%{_bindir}
install -m 0755 %{SOURCE0} %{buildroot}/%{_bindir}/count_files.sh

%files
%{_bindir}/count_files.sh
