Summary:	Open BIOS parsing library
Summary(pl.UTF-8):	Biblioteka analizująca Open BIOS
Name:		libsmbios
Version:	2.3.0
Release:	1
License:	OSL v2.1 or GPL v2+
Group:		Libraries
Source0:	http://linux.dell.com/libsmbios/download/libsmbios/%{name}-%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	8f4bef657b04250f077f7ac5f2ecac2c
Patch0:		%{name}-sh.patch
Patch1:		%{name}-link.patch
URL:		http://linux.dell.com/libsmbios/main/index.html
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	cppunit-devel >= 1.9.6
BuildRequires:	doxygen
BuildRequires:	gettext-tools >= 0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 1:2.3
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
ExclusiveArch:	%{ix86} %{x8664} x32
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
Requires:	python-libsmbios = %{version}-%{release}

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

%package -n python-libsmbios
Summary:	Python interface to libsmbios C library
Summary(pl.UTF-8):	Interfejs Pythona do biblioteki C libsmbios
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-libsmbios
Python interface to libsmbios C library.

%description -n python-libsmbios -l pl.UTF-8
Interfejs Pythona do biblioteki C libsmbios.

%package -n yum-plugin-dellsysid
Summary:	YUM plugin to retrieve the Dell System ID
Summary(pl.UTF-8):	Wtyczka YUM-a do odczytu identyfikatorów komputerów firmy Dell (Dell System ID)
Group:		Applications/System
Requires:	python-libsmbios = %{version}-%{release}
Requires:	yum

%description -n yum-plugin-dellsysid
This package contains a YUM plugin which allows the use of certain
substitutions in yum repository configuration files on Dell systems.

%description -n yum-plugin-dellsysid -l pl.UTF-8
Ten pakiet zawiera wtyczkę YUM-a, pozwalającą na używanie określonych
podstawień w plikach konfiguracyjnych repozytoriów yum na komputerach
firmy Dell.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="%{rpmcppflags} -DLIBSMBIOS_ASSERT_CONFIG=1"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -pr src/include/{smbios,smbios_c} $RPM_BUILD_ROOT%{_includedir}

%py_postclean

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS COPYING COPYING-OSL ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/libsmbios.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmbios.so.2
%attr(755,root,root) %{_libdir}/libsmbios_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmbios_c.so.2

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/dellBiosUpdate-compat
%attr(755,root,root) %{_sbindir}/dellLEDCtl
%attr(755,root,root) %{_sbindir}/dellMediaDirectCtl
%attr(755,root,root) %{_sbindir}/smbios-*
%dir %{_sysconfdir}/libsmbios
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libsmbios/logging.conf
%{_datadir}/smbios-utils

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmbios.so
%attr(755,root,root) %{_libdir}/libsmbios_c.so
%{_libdir}/libsmbios.la
%{_libdir}/libsmbios_c.la
%{_includedir}/smbios
%{_includedir}/smbios_c
%{_pkgconfigdir}/libsmbios_c++.pc
%{_pkgconfigdir}/libsmbios_c.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmbios.a
%{_libdir}/libsmbios_c.a

%files -n python-libsmbios
%defattr(644,root,root,755)
%{py_sitescriptdir}/libsmbios_c

%files -n yum-plugin-dellsysid
%defattr(644,root,root,755)
%{_prefix}/lib/yum-plugins/dellsysid.py*
%config(noreplace) %verify(not md5 mtime size) /etc/yum/pluginconf.d/dellsysid.conf
