%global commit0 82a55dde65dd9ab49773f513446b253f344162c0
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           mock-unitedrpms
Version:        1.0
Release:        4%{?gver}%{?dist}
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
install -pm 0644 unitedrpms*.cfg %{buildroot}%{_sysconfdir}/mock


%files
%defattr(-,root,root,-)
#%config(noreplace) %{_sysconfdir}/mock/unitedrpms*.cfg
%{_sysconfdir}/mock/unitedrpms*.cfg


%changelog

* Fri Aug 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-4.git82a55dd
- Updated to 1.0-4.git82a55dd

* Sat Jul 22 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-3.git39ba597
- Updated to 1.0-3.git39ba597

* Fri Jun 23 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-2.git2b2a42b
- Updated to 1.0-2.git2b2a42b

* Fri May 19 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-1.git04eec84
- Initial build
