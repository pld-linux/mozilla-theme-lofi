Summary:	Minimalistic theme based on old-style Modern theme
Summary(pl):	Minimalistyczny motyw bazuj±cy na starym motywie Modern
Name:		mozilla-theme-lofi
Version:	1.7
%define		_realname	lofi
%define	fver	%(echo %{version} | tr -d .)
Release:	1
License:	GPL
Group:		X11/Applications/Networking
Source0:	http://downloads.mozdev.org/themes/themes/%{_realname}-%{fver}.jar
# Source0-md5:	90e64184f8ec97917ae270415ba1056a
Source1:	%{_realname}-installed-chrome.txt
URL:		http://themes.mozdev.org/themes/lofi.html
Requires(post,postun):	textutils
Requires:	mozilla >= 1.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{_realname}-%{version}-root-%(id -u -n)

%define		_chromedir	%{_datadir}/mozilla/chrome

%description
Minimalistic theme based on old-style Modern theme.

%description -l pl
Minimalistyczny motyw bazuj±cy na starym motywie Modern Mozilli.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_chromedir}

install %{SOURCE0} $RPM_BUILD_ROOT%{_chromedir}/%{_realname}.jar
install %{SOURCE1} $RPM_BUILD_ROOT%{_chromedir}/

%clean
rm -rf $RPM_BUILD_ROOT

%post
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%postun
umask 022
cat %{_chromedir}/*-installed-chrome.txt >%{_chromedir}/installed-chrome.txt

%files
%defattr(644,root,root,755)
%{_chromedir}/%{_realname}.jar
%{_chromedir}/%{_realname}-installed-chrome.txt
