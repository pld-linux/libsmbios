Summary:	Open BIOS parsing libs
Name:		libsmbios
Version:	0.13.6
Release:	1
License:	GPL/OSL
Group:		Libraries
Source0:	http://linux.dell.com/libsmbios/download/libsmbios/%{name}-%{version}/libsmbios-0.13.6.tar.gz
# Source0-md5:	cab4267585bb5c8707510c27026d5a3b
URL:		http://linux.dell.com/libsmbios/main/index.html
BuildRequires:	cppunit-devel
BuildRequires:	doxygen
BuildRequires:	libxml2-devel
ExclusiveArch:	%{x8664} %{ix86}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsmbios is a library and utilities that can be used by client
programs to get information from standard BIOS tables, such as the
SMBIOS table.

%package progs
Summary:	libsmbios tools
Summary(pl.UTF-8):	Narzędzia libsmbios
Group:		Development/Libraries
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

%build
CPPFLAGS="-DLIBSMBIOS_ASSERT_CONFIG=1"
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sysconfdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS COPYING* ChangeLog NEWS README TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_aclocaldir}/*.m4
%{_pkgconfigdir}/*.pc
%{_mandir}/man3/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
