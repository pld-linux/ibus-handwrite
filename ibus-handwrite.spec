Summary:	IBus handwrite project
Summary(pl.UTF-8):	Moduł IBus do pisma ręcznego
Name:		ibus-handwrite
Version:	2.1.4
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: http://code.google.com/p/ibus-handwrite/downloads/list
Source0:	http://ibus-handwrite.googlecode.com/files/%{name}-%{version}.tar.bz2
# Source0-md5:	4aafbee7ec20883c7ab94f8fdfad8917
URL:		http://code.google.com/p/ibus-handwrite/
BuildRequires:	gettext-devel >= 0.16.1
BuildRequires:	gtk+2-devel >= 2:2.10
BuildRequires:	gtkglext-devel
BuildRequires:	ibus-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	zinnia-devel
Requires:	gtk+2 >= 2:2.10
Requires:	ibus >= 1.3
Requires:	zinnia-tomoe
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
IBus handwrite project.

%description -l pl.UTF-8
Moduł IBus do pisma ręcznego.

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
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libexecdir}/ibus-engine-handwrite
%{_datadir}/ibus-handwrite
%{_datadir}/ibus/component/handwrite-*.xml
