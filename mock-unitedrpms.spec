%global gitdate 20170519
%global commit0 44019727be2a005a63cb9070682293d0bfdff201
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           mock-unitedrpms
Version:        1.0
Release:        1%{?gver}%{?dist}
Summary:        Mock config files for the UnitedRPMs

Group:          Development/Tools
License:        MIT
URL:            https://unitedrpms.github.io/
Source0:	https://github.com/UnitedRPMs/mock-unitedrpms/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
Requires:       mock >= 1.2.19

%description
Mock config files for the UnitedRPMs Project


%prep
%autosetup -n %{name}-%{commit0} 


%build
#Nothing to build


%install
mkdir -p %{buildroot}%{_sysconfdir}/mock
install -pm 0644 etc/mock/unitedrpms*.cfg %{buildroot}%{_sysconfdir}/mock


%files
%defattr(-,root,root,-)
%config(noreplace) %{_sysconfdir}/mock/unitedrpms*.cfg


%changelog
* Fri May 19 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-1git1234567
- Initial build
