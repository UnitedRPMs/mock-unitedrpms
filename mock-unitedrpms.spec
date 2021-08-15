%global commit0 093040f61023bd9ef4e99102721480f45f85e01c
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})
%global gver .git%{shortcommit0}

Name:           mock-unitedrpms
Version:        1.0
Release:        25%{?dist}
Summary:        Mock config files for the UnitedRPMs

Group:          Development/Tools
License:        MIT
URL:            https://github.com/UnitedRPMs/mock-unitedrpms
Source0:        https://github.com/UnitedRPMs/mock-unitedrpms/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildArch:      noarch
Requires:       mock >= 1.2.19
Requires:       mock-core-configs

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
#config(noreplace) {_sysconfdir}/mock/unitedrpms*.cfg
%{_sysconfdir}/mock/unitedrpms*.cfg


%changelog

* Thu Aug 12 2021 David Va <davidva AT tuta DOT io> 1.0-25
- Rawhide F36 template enabled

* Wed Apr 07 2021 David Va <davidva AT tuta DOT io> 1.0-24
- Rawhide F35 template enabled

* Tue May 26 2020 David Va <davidva AT tuta DOT io> 1.0-23
- New chroot fixes

* Thu Apr 09 2020 David Va <davidva AT tuta DOT io> 1.0-22
- Changed to use_bootstrap 

* Sat Feb 22 2020 David Va <davidva AT tuta DOT io> 1.0-21
- Rebuilt

* Thu Feb 20 2020 David Va <davidva AT tuta DOT io> 1.0-20
- Rawhide bump

* Fri Feb 07 2020 David Va <davidva AT tuta DOT io> 1.0-19
- Rawhide F33 template enabled

* Fri Aug 30 2019 David Va <davidva AT tuta DOT io> 1.0-18
- Rawhide F32 template enabled

* Sat Apr 06 2019 David Va <davidva AT tuta DOT io> 1.0-17
- Rawhide template enabled

* Wed Mar 13 2019 David Va <davidva AT tuta DOT io> 1.0-16
- F31 enabled

* Wed Feb 13 2019 David Va <davidva AT tuta DOT io> 1.0-15
- Rawhide fix
- F27 deleted

* Mon Oct 29 2018 David Va <davidva AT tuta DOT io> 1.0-14
- Added mock-core-configs dependency

* Mon Aug 20 2018 David Va <davidva AT tuta DOT io> 1.0-13
- Added mock config for F30

* Wed Jun 27 2018 David Va <davidva AT tuta DOT io> 1.0-12
- Enabled use_host_resolv

* Thu May 10 2018 David Vásquez <davidva AT tutanota DOT com> 1.0-11
- Provided fedora-29 configs to F29

* Wed Mar 21 2018 David Vásquez <davidva AT tutanota DOT com> 1.0-10
- Provided fedora-29 configs as symlinks to fedora-rawhide

* Wed Mar 07 2018 David Vásquez <davidva AT tutanota DOT com> 1.0-9
- F29 enabled

* Fri Jan 12 2018 David Vásquez <davidva AT tutanota DOT com> 1.0-8
- Networking enabled 

* Fri Sep 22 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-7.git337d3e7
- Updated to 1.0-7.git337d3e7
- Disabled bootstrap_container

* Fri Sep 22 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-5.git0094340
- Updated to 1.0-5.git0094340

* Fri Aug 25 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-4.git82a55dd
- Updated to 1.0-4.git82a55dd

* Sat Jul 22 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-3.git39ba597
- Updated to 1.0-3.git39ba597

* Fri Jun 23 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-2.git2b2a42b
- Updated to 1.0-2.git2b2a42b

* Fri May 19 2017 David Vásquez <davidva AT tutanota DOT com> 1.0-1.git04eec84
- Initial build
