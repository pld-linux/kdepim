%define		_ver		3.0.1
#define		_sub_ver
%define		_rel		1

%{?_sub_ver:	%define	_version	%{_ver}%{_sub_ver}}
%{!?_sub_ver:	%define	_version	%{_ver}}
%{?_sub_ver:	%define	_release	0.%{_sub_ver}.%{_rel}}
%{!?_sub_ver:	%define	_release	%{_rel}}
%{!?_sub_ver:	%define	_ftpdir	stable}
%{?_sub_ver:	%define	_ftpdir	unstable/kde-%{version}%{_sub_ver}}

Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Name:		kdepim
Version:	%{_version}
Release:	%{_release}
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_ftpdir}/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	zlib-devel
BuildRequires:	bison
BuildRequires:	pilot-link-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Enviromnent (KDE) kdepim contains the following
applications:

KOrganizer: a complete calendar and scheduling program. KOrganizer
supports information interchange with other calendar applications
through the industry standard vCalendar file format.

Empath: an E-Mail client

abbrowser: an address book reader

kpilot: Syncronization tool for 3com Palm Pilots and compatible
devices

twister: A PIM client

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Enviromnent
(KDE). kdepim zawiera nastepujace programy:

KOrganizer: kalendarz wraz z harmonogramem zadan. KOrganizer wspiera
wymiane informacji z innymi tego typu aplikacjami poprzez standard
przemyslowy vCalendar.

Empath: klient E-Mail.

abbrowser: czytnik ksiazki adresowej

kpilot: narzedzie do synchronizacji z 3Com Palm Pilot'em i
kompatybilnymi urzadzeniami.

twister: klient PIM.

%package devel
Summary:	Development files for KDE pim
Summary:	Pliki nag³owkowe do KDE pim
Group:		X11/Development/Libraries

%description devel
Development files for KDE pim.

%description devel -l pl
Pliki nag³owkowe do KDE pim.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
        CPPFLAGS="`pkg-config libpng12 --cflags`"
fi

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}{/Office/PIMs,/Settings/KDE}

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/[!K]* $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Office/PIMs/}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%{_libdir}/kde3/libabbrowserconduit.la
%{_libdir}/kde3/libabbrowserconduit.so.*.*.*
%{_libdir}/kde3/libexpenseconduit.la
%{_libdir}/kde3/libexpenseconduit.so.*.*.*
%{_libdir}/kde3/libknotesconduit.la
%{_libdir}/kde3/libknotesconduit.so.*.*.*
%{_libdir}/kde3/libnullconduit.la
%{_libdir}/kde3/libnullconduit.so.*.*.*
%{_libdir}/kde3/libpopmailconduit.la
%{_libdir}/kde3/libpopmailconduit.so.*.*.*
%{_libdir}/kde3/libvcalconduit.la
%{_libdir}/kde3/libvcalconduit.so.*.*.*

%{_libdir}/kde3/libkcm_alarmdaemonctrl.??
%{_libdir}/kde3/libkorg_datenums.??
%{_libdir}/kde3/libkorg_holidays.??
%{_libdir}/kde3/libkorg_projectview.??
%{_libdir}/kde3/libkorg_webexport.??

%{_datadir}/apps/*
%{_datadir}/autostart/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/config/*
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Settings/KDE/System/*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.??
%{_libdir}/kde3/libabbrowserconduit.so
%{_libdir}/kde3/libexpenseconduit.so
%{_libdir}/kde3/libknotesconduit.so
%{_libdir}/kde3/libnullconduit.so
%{_libdir}/kde3/libpopmailconduit.so
%{_libdir}/kde3/libvcalconduit.so
