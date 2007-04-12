%define product		PloneErrorReporting
%define version		1.0
%define release	        1

%define zope_minver	2.7
%define plone_minver	2.0

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Summary:	PloneErrorReporting facilitate the submission of useful bug reports to Plone
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/ploneerrorreporting/releases/%{version}/PloneErrorReporting-%{version}.tar.bz2
URL:		http://plone.org/products/ploneerrorreporting
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	zope >= %{plone_minver}

Provides:	plone-PloneErrorReporting == %{version}
Obsoletes:	plone-PloneErrorReporting

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
%defattr(0644, root, root, 0755)
%{software_home}/Products/*




