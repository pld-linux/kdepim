Summary:	K Desktop Environment - pim 
Summary(pl):	K Desktop Environment - pim
Name:		kdepim
Version:	2.1.1
Release:	1
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/distribution/generic/tar/src/%{name}-%{version}.tar.bz2
BuildRequires:	XFree86-devel
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	qt-devel >= 2.2
BuildRequires:	zlib-devel
Requires:	qt >= 2.2
Requires:	kdelibs >= %{version}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        %{_datadir}/doc/kde/HTML

%description
KDE pim

%description -l pl
Pakiet KDE pim.

%package devel
Summary:	Development files for KDE pim
Summary:	Pliki nag³owkowe do KDE pim
Group:		X11/Development/Libraries

%description devel
Development files for KDE pim.

%description -l pl devel
Pliki nag³owkowe do KDE pim.

%prep
%setup -q

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

export LDFLAGS
%configure2_13 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} DESTDIR=$RPM_BUILD_ROOT install


%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_libdir}/*.so.*
%{_applnkdir}/Applications/*
%{_applnkdir}/Utilities/*
%{_prefix}/share/apps/*
%{_prefix}/share/config/*
%doc
%{_prefix}/share/pixmaps/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/rmm/*.h
%{_libdir}/*.la
