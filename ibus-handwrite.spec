Summary:	IBus handwrite project
Summary(pl.UTF-8):	Moduł IBus do pisma ręcznego
Name:		ibus-handwrite
Version:	3.0.0
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/microcai/ibus-handwrite/releases
Source0:	https://github.com/microcai/ibus-handwrite/releases/download/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	70869d907c6634616893cd0510ee078f
URL:		https://github.com/microcai/ibus-handwrite
BuildRequires:	gettext-tools >= 0.16.1
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	ibus-devel >= 1.3
BuildRequires:	pkgconfig
BuildRequires:	zinnia-devel
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
