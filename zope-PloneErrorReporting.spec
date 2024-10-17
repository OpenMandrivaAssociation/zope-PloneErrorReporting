%define Product PloneErrorReporting
%define product ploneerrorreporting
%define name    zope-%{Product}
%define version 1.1
%define release %mkrel 6

%define zope_minver	2.7
%define plone_minver	2.0
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	PloneErrorReporting facilitate the submission of useful bug reports to Plone
License:	GPL
Group:		System/Servers
URL:        https://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{Product}-%{version}.tar.gz
Requires:	zope >= %{zope_minver}
Requires:	zope >= %{plone_minver}
Provides:	plone-PloneErrorReporting == %{version}
Obsoletes:	plone-PloneErrorReporting
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
PloneErrorReporting replaces default_error_message and 
prefs_error_log_showEntry with pages that facilitate the 
submission of useful bug reports to Plone.  It is designed 
with the goal of improving the information provided by bug 
reporters.

%prep
%setup -c -q

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-,root,root)
%{software_home}/Products/*
