Summary:	Tool for converting WordPerfect Graphics file into OpenDocument Graphics format
Name:		wpg2odg
Version:	0.1.0
Release:	1
License:	LGPL v2+
Group:		Applications
URL:		http://libwpg.sourceforge.net/
Source0:	http://dl.sourceforge.net/libwpg/%{name}-%{version}.tar.gz
# Source0-md5:	6309293ad531f4ac98abb31de5c4c54d
BuildRequires:	libwpg-devel >= 0.0.1
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tool for converting WordPerfect Graphics file into OpenDocument
Graphics format.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/wpg2odg
%attr(755,root,root) %{_bindir}/wpg2odgbatch.pl
