%define name	repoview
%define version 0.6.2
%define release 3

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Creates a set of static HTML pages in a yum repository
Group:          Networking/WWW
License:        GPL
URL:            https://linux.duke.edu/projects/mini/%{name}
Source0:        http://linux.duke.edu/projects/mini/%{name}/download/%{name}-%{version}.tar.gz
Requires:       python >= 2.2
Requires:       python-kid >= 0.6.3
Requires:       python-elementtree
BuildArch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
RepoView creates a set of static HTML pages in a yum repository for easy
browsing.


%prep
%setup -q
perl -pi \
	-e "s|^DEFAULT_TEMPLATEDIR =.*|DEFAULT_TEMPLATEDIR = '%{_datadir}/%{name}/templates'|g;" \
	repoview.py
perl -pi -e 'tr/\n//d' ChangeLog

%install
rm -rf %{buildroot}
mkdir -p -m 755                         \
    %{buildroot}/%{_datadir}/%{name} \
    %{buildroot}/%{_bindir}          \
    %{buildroot}/%{_mandir}/man8
install -m 755 repoview.py  %{buildroot}/%{_bindir}/repoview
install -m 644 repoview.8 %{buildroot}/%{_mandir}/man8
cp -rp templates %{buildroot}/%{_datadir}/%{name}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc README COPYING ChangeLog
%{_datadir}/%{name}
%{_bindir}/*
%{_mandir}/man*/*


%changelog
* Tue Sep 15 2009 Thierry Vignaud <tvignaud@mandriva.com> 0.6.2-2mdv2010.0
+ Revision: 442687
- rebuild

* Thu Jan 15 2009 Jérôme Soyer <saispo@mandriva.org> 0.6.2-1mdv2009.1
+ Revision: 329838
- New upstream release

* Fri Aug 01 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.1-4mdv2009.0
+ Revision: 260233
- rebuild

* Fri Jul 25 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.6.1-3mdv2009.0
+ Revision: 248374
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.6.1-1mdv2008.1
+ Revision: 115425
- new version

* Wed Sep 05 2007 Jérôme Soyer <saispo@mandriva.org> 0.6.0-1mdv2008.0
+ Revision: 79840
- New release 0.6.0
- Import repoview



* Sun Oct 09 2005 Michael Scherer <misc@mandriva.org> 0.4.1-1mdk
- New release 0.4.1

* Sat Oct 08 2005 Michael Scherer <misc@mandriva.org> 0.4-1mdk
- New release 0.4

* Sat Jul 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3- 4 
- properly quote variable

* Sat Jul 16 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-3mdk 
- don't mess with software internal version

* Wed Jul 13 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-2mdk 
- used mkrel

* Tue Jul 12 2005 Guillaume Rousse <guillomovitch@mandriva.org> 0.3-1mdk 
- first mdk release
