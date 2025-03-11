Summary:	Open BIOS parsing library
Summary(pl.UTF-8):	Biblioteka analizująca Open BIOS
Name:		libsmbios
Version:	2.4.3
Release:	5
License:	OSL v2.1 or GPL v2+
Group:		Libraries
#Source0Download: https://github.com/dell/libsmbios/releases
Source0:	https://github.com/dell/libsmbios/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	d27a0de66b04860e4e3e8d1bb338bf6a
Patch0:		%{name}-sh.patch
Patch1:		%{name}-link.patch
URL:		https://github.com/dell/libsmbios
BuildRequires:	autoconf >= 2.61
BuildRequires:	automake >= 1.6
BuildRequires:	cppunit-devel >= 1.9.6
BuildRequires:	doxygen
BuildRequires:	gettext-tools >= 0.14
BuildRequires:	help2man
BuildRequires:	libtool >= 2:1.5
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	python3 >= 1:3.2
BuildRequires:	rpmbuild(macros) >= 1.219
BuildRequires:	sed >= 4.0
ExclusiveArch:	%{ix86} %{x8664} x32
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsmbios is a library and utilities that can be used by client
programs to get information from standard BIOS tables, such as the
SMBIOS table.

%description -l pl.UTF-8
libsmbios to biblioteka i narzędzia, które mogą wykorzystywać programy
klienckie do uzyskania informacji ze standardowych tablic BIOS-u,
takich jak tablica SMBIOS.

%package progs
Summary:	libsmbios tools
Summary(pl.UTF-8):	Narzędzia libsmbios
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	python3-libsmbios = %{version}-%{release}

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

%package -n python3-libsmbios
Summary:	Python 3 interface to libsmbios C library
Summary(pl.UTF-8):	Interfejs Pythona 3 do biblioteki C libsmbios
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}
Requires:	python3-modules >= 1:3.2
Obsoletes:	python-libsmbios < 2.4.0
Obsoletes:	yum-plugin-dellsysid < 2.4.0

%description -n python3-libsmbios
Python 3 interface to libsmbios C library.

%description -n python3-libsmbios -l pl.UTF-8
Interfejs Pythona 3 do biblioteki C libsmbios.

%prep
%setup -q
%patch -P 0 -p1
%patch -P 1 -p1

%{__sed} -i -e '/AC_CONFIG_FILES(\[po\/Makefile\.in\])/d' configure.ac

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

# --for-msgfmt causes not to emit output for empty translations
%{__make} \
	MSGMERGE_FOR_MSGFMT_OPTION=

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# not installed by make install
cp -pr src/include/smbios_c $RPM_BUILD_ROOT%{_includedir}

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmbios*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc COPYING COPYING-OSL README.md
%attr(755,root,root) %{_libdir}/libsmbios_c.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmbios_c.so.2

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/smbios-*
%dir %{_sysconfdir}/libsmbios
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/libsmbios/logging.conf
%{_datadir}/smbios-utils
%{_mandir}/man1/smbios-*.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmbios_c.so
%{_includedir}/smbios_c
%{_pkgconfigdir}/libsmbios_c.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmbios_c.a

%files -n python3-libsmbios
%defattr(644,root,root,755)
%{py3_sitedir}/libsmbios_c
