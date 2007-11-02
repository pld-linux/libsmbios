Summary:	Open BIOS parsing library
Summary(pl.UTF-8):	Biblioteka analizująca Open BIOS
Name:		libsmbios
Version:	0.13.11
Release:	1
License:	OSL v2.1 or GPL v2+
Group:		Libraries
Source0:	http://linux.dell.com/libsmbios/download/libsmbios/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1a522211eee051fce227350faab3e63f
Patch0:		%{name}-link.patch
URL:		http://linux.dell.com/libsmbios/main/index.html
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	cppunit-devel >= 1.9.6
BuildRequires:	doxygen
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel
ExclusiveArch:	%{ix86} %{x8664}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsmbios is a library and utilities that can be used by client
programs to get information from standard BIOS tables, such as the
SMBIOS table.

%description -l pl.UTF-8
libsmbios to biblioteka i narzędzia, które mogą wykorzystywać
programy klienckie do uzyskania informacji ze standardowych tablic
BIOS-u, takich jak tablica SMBIOS.

%package progs
Summary:	libsmbios tools
Summary(pl.UTF-8):	Narzędzia libsmbios
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}

%description progs
libsmbios tools.

%description progs -l pl.UTF-8
Narzędzia libsmbios.

%package devel
Summary:	Header files and development documentation for libsmbios
Summary(pl.UTF-8):	Pliki nagłówkowe i dokumentacja do libsmbios
Summary(ru.UTF-8):	Хедеры для разработки программ с использованием libsmbios
Summary(uk.UTF-8):	Хедери для розробки програм з використанням libsmbios
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel
# for libsmbiosxml only
#Requires:	libxml2-devel

%description devel
Header files and development documentation for libsmbios.

%description devel -l pl.UTF-8
Pliki nagłówkowe i dokumentacja do libsmbios.

%description devel -l ru.UTF-8
Хедеры для разработки программ с использованием libsmbios.

%description devel -l uk.UTF-8
Хедери для розробки програм з використанням libsmbios.

%package static
Summary:	Static libsmbios libraries
Summary(pl.UTF-8):	Biblioteki statyczne libsmbios
Summary(ru.UTF-8):	Статические библиотеки для разработки программ с использованием libsmbios
Summary(uk.UTF-8):	Статичні бібліотеки для розробки програм з використанням libsmbios
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsmbios libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libsmbios.

%description static -l ru.UTF-8
Статические библиотеки для разработки программ с использованием
libsmbios.

%description static -l uk.UTF-8
Статичні бібліотеки для розробки програм з використанням libsmbios.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
CPPFLAGS="-DLIBSMBIOS_ASSERT_CONFIG=1"
# ${!varname} bashism
bash %configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf include/smbios $RPM_BUILD_ROOT%{_includedir}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-OSL ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libsmbios.so.*.*.*
%attr(755,root,root) %{_libdir}/libsmbiosxml.so.*.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/*

%files devel
%defattr(644,root,root,755)
%doc doc/interface/html
%attr(755,root,root) %{_libdir}/libsmbios.so
%attr(755,root,root) %{_libdir}/libsmbiosxml.so
%{_libdir}/libsmbios.la
%{_libdir}/libsmbiosxml.la
%{_includedir}/smbios

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmbios.a
%{_libdir}/libsmbiosxml.a
