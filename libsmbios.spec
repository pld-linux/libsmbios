Summary:	Open BIOS parsing library
Summary(pl.UTF-8):	Biblioteka analizująca Open BIOS
Name:		libsmbios
Version:	2.2.26
Release:	1
License:	OSL v2.1 or GPL v2+
Group:		Libraries
Source0:	http://linux.dell.com/libsmbios/download/libsmbios/%{name}-%{version}/%{name}-%{version}.tar.bz2
# Source0-md5:	8ae63da74912deffa5b6b2602879c7a9
Patch0:		%{name}-sh.patch
Patch1:		%{name}-link.patch
URL:		http://linux.dell.com/libsmbios/main/index.html
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	cppunit-devel >= 1.9.6
BuildRequires:	doxygen
BuildRequires:	gettext-devel >= 0.14
BuildRequires:	libstdc++-devel
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python >= 2.3
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
%patch1 -p1

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
CPPFLAGS="-DLIBSMBIOS_ASSERT_CONFIG=1"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cp -rf src/include/{smbios,smbios_c} $RPM_BUILD_ROOT%{_includedir}

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
# or %files -n python-libsmbios ?
%{py_sitescriptdir}/libsmbios_c

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

# %files -n yum-*?
#%{_libdir}/yum-plugins/dellsysid.py*
#%config(noreplace) %verify(not md5 mtime size) /etc/yum/dellsysid.conf
