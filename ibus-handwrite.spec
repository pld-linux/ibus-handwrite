Summary:	IBus handwrite project
Name:		ibus-handwrite
Version:	2.1.3
Release:	2
License:	GPL v2+
Group:		Libraries
Source0:	http://ibus-handwrite.googlecode.com/files/%{name}-%{version}.tar.gz
# Source0-md5:	887a6b44f01f3eaff45b0af1a996d4cc
URL:		http://code.google.com/p/ibus-handwrite/
BuildRequires:	ibus-devel
BuildRequires:	gtk+2-devel
BuildRequires:	gtkglext-devel
BuildRequires:	zinnia-devel
Requires:	ibus
Requires:	zinnia-tomoe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus handwrite project.

%prep
%setup -q

%build
%configure \
	--enable-zinnia \
	--with-zinnia-tomoe=%{_datadir}/zinnia/model/tomoe

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-handwrite
%{_datadir}/ibus-handwrite
%{_datadir}/ibus/component/handwrite-*.xml
