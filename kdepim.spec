Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Menad¿er informacji osobistej (PIM) dla KDE
Name:		kdepim
Version:	2.2.2
Release:	2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	zlib-devel
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
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE). kdepim zawiera nastêpuj±ce programy:

KOrganizer: kalendarz wraz z harmonogramem zadañ. KOrganizer wspiera
wymianê informacji z innymi tego typu aplikacjami poprzez standard
przemys³owy vCalendar.

Empath: klient E-Mail.

abbrowser: czytnik ksi±¿ki adresowej.

kpilot: narzêdzie do synchronizacji z 3Com Palm Pilotem i
kompatybilnymi urz±dzeniami.

twister: klient PIM.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag³ówkowe do KDE pim
Group:		X11/Development/Libraries

%description devel
Development files for KDE pim.

%description devel -l pl
Pliki nag³ówkowe do KDE pim.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs

mv -f $RPM_BUILD_ROOT%{_applnkdir}/{Applications,Office/PIMs}/korganizer.desktop

gzip -9nf README*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Utilities/*
%{_datadir}/autostart/alarmd.desktop
%{_datadir}/apps/*
%{_datadir}/config/*
%{_pixmapsdir}/*/*/apps/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so
