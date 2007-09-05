%define name	repoview
%define version 0.6.0
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:        Creates a set of static HTML pages in a yum repository
Group:          Networking/WWW
License:        GPL
URL:            http://linux.duke.edu/projects/mini/%{name}
Source0:        http://linux.duke.edu/projects/mini/%{name}/download/%{name}-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}
BuildArch:      noarch
Requires:       python >= 2.2
Requires:       python-kid >= 0.6.3
Requires:       python-elementtree

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
