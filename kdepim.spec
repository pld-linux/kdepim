#
# TODO:
# - make separate subpackages
# - separate packages: pilot, cellphone, karm, knotes.
#
Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - PIM (°³ÀÎ Á¤º¸ °ü¸®)
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË (PIM) ÄÌÑ KDE
Summary(uk):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË (PIM) ÄÌÑ KDE
Name:		kdepim
Version:	3.0.4
Release:	2
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-no_versioned_modules.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
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

- KOrganizer - a complete calendar and scheduling program (KOrganizer
  supports information interchange with other calendar applications
  through the industry standard vCalendar file format),
- Empath - an E-Mail client,
- abbrowser - an address book reader,
- kpilot - Syncronization tool for 3com Palm Pilots and compatible
  devices,
- twister - A PIM client.

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Enviromnent
(KDE). kdepim zawiera nastêpujace programy:

- KOrganizer - kalendarz wraz z harmonogramem zadañ (KOrganizer
  wspiera wymianê informacji z innymi tego typu aplikacjami poprzez
  standard przemys³owy vCalendar),
- Empath - klient E-Mail,
- abbrowser - czytnik ksiazki adresowej,
- kpilot - narzedzie do synchronizacji z 3Com Palm Pilot'em i
  kompatybilnymi urzadzeniami.
- twister - klient PIM.

%description -l ru
kdepim - ÜÔÏ ÎÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÐÅÒÓÏÎÁÌØÎÏÊ ÉÎÆÏÒÍÁÃÉÅÊ ÄÌÑ
K Desktop Enviromnent (KDE). kdepim ÓÏÄÅÒÖÉÔ ÓÌÅÄÕÀÝÉÅ ÐÒÏÇÒÁÍÍÙ:

- KOrganizer - ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÁÑ ÐÒÏÇÒÁÍÍÁ ËÁÌÅÎÄÁÒÑ É ÐÅÒÓÏÎÁÌØÎÏÇÏ
  ÐÌÁÎÉÒÏ×ÝÉËÁ (KOrganizer ÐÏÄÄÅÒÖÉ×ÁÅÔ ÏÂÍÅÎ ÉÎÆÏÒÍÁÃÉÅÊ Ó ÄÒÕÇÉÍÉ
  ÐÒÏÇÒÁÍÍÁÍÉ ÔÁËÏÇÏ ÒÏÄÁ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÙÊ ÆÏÒÍÁÔ ÆÁÊÌÁ vCalendar)
- abbrowser - ÐÒÏÇÒÁÍÍÁ ÄÌÑ ÞÔÅÎÉÑ ÁÄÒÅÓÎÏÊ ËÎÉÇÉ,
- kpilot - ÕÔÉÌÉÔÁ ÄÌÑ ÓÉÎÈÒÏÎÉÚÁÃÉÉ Ó 3com Palm Pilots É ÓÏ×ÍÅÓÔÉÍÙÍÉ
  Ó ÎÉÍÉ ÕÓÔÒÏÊÓÔ×ÁÍÉ,

%description -l uk
kdepim - ÃÅ ÎÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÐÅÒÓÏÎÁÌØÎÏÀ ÉÎÆÏÒÍÁÃ¦¤À ÄÌÑ K
Desktop Enviromnent (KDE). kdepim Í¦ÓÔÉÔØ ÔÁË¦ ÐÒÏÇÒÁÍÉ:

- KOrganizer - ÐÏ×ÎÏÆÕÎËÃ¦ÏÎÁÌØÎÁ ÐÒÏÇÒÁÍÁ ËÁÌÅÎÄÁÒÁ ÔÁ ÐÅÒÓÏÎÁÌØÎÏÇÏ
  ÐÌÁÎÕ×ÁÌØÎÉËÁ (KOrganizer Ð¦ÄÔÒÉÍÕ¤ ÏÂÍ¦Î ÉÎÆÏÒÍÁÃ¦¤À Ú ¦ÎÛÉÍÉ
  ÐÒÏÇÒÁÍÁÍÉ ÔÁËÏÇÏ ÒÏÄÕ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÉÊ ÆÏÒÍÁÔ ÆÁÊÌÕ vCalendar),
- abbrowser - ÐÒÏÇÒÁÍÁ ÄÌÑ ÞÉÔÁÎÎÑ ÁÄÒÅÓÎÏ§ ËÎÉÇÉ,
- kpilot - ÕÔÉÌ¦ÔÁ ÄÌÑ ÓÉÎÈÒÏÎ¦ÚÁÃ¦§ Ú 3com Palm Pilots ÔÁ ÓÕÍ¦ÓÎÉÍÉ Ú
  ÎÉÍÉ ÐÒÉÓÔÒÏÑÍÉ.

%package pilot
Summary:	KDE support for synchronizing data with a Palm(tm) or compatible PDA
Summary(pl):	KDE - obs³uga synchronizacji danych z Palmem(tm) lub kompatybilnym PDA
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pilot
KDE support for synchronizing data with a Palm(tm) or compatible PDA.

%description pilot -l pl
KDE - obs³uga synchronizacji danych z Palmem(tm) lub kompatybilnym
PDA.

%package cellphone
Summary:	KDE support for synchronizing data with cellphones
Summary(pl):	KDE - obs³uga synchronizacji danych z telefonami komórkowymi.
Group:		X11/Applications
Requires:	%{name} = %{version}

%description cellphone
KDE support for synchronizing data with cellphones.

%description cellphone -l pl
KDE - obs³uga synchronizacji danych z telefonami komórkowymi.

%package karm
Summary:	Time tracking tool
Summary(pl):	Narzêdzie do ¶ledzenia czasu
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	karm

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s³owa "praca" w jêzyku punjambi) ¶ledzi czas
spêdzony na ró¿nych zajêciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunków ró¿nym klientom.

%package knotes
Summary:	Post-It notes on the desktop
Summary(pl):	Notatki na desktopie, które mo¿na wysy³aæ
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	knotes

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszczaæ na desktopie notatki z opcj± wysy³ania.
Dodatkowo, aby móc s³u¿yæ za przypominajkê, KNotes mo¿e wysy³aæ pocztê
i drukowaæ notatki, a tak¿e przyjmowaæ przeci±ganie nawet ze zdalnych
komputerów.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag³ówkowe do KDE pim
Summary(uk):	æÁÊÌÉ ÒÏÚÒÏÂËÉ ÄÌÑ kdepim
Summary(ru):	æÁÊÌÙ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ kdepim
Group:		X11/Development/Libraries

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag³ówkowe potrzebne do budowy aplikacji
bazuj±cych na kdepim.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ ÚÁÇÏÌÏ×Ë¦× ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ,
ÂÁÚÏ×ÁÎÉÈ ÎÁ kdepim.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ
ÐÒÏÇÒÁÍÍ, ÏÓÎÏ×ÁÎÎÙÈ ÎÁ kdepim.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Office/PIMs,Settings/KDE}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/[!K]* $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications/*,Office/PIMs/}
install libkcal/.libs/libkcal.so.2.*.* $RPM_BUILD_ROOT%{_libdir}
install kpilot/lib/.libs/libkpilot.so.0.*.* $RPM_BUILD_ROOT%{_libdir}

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

programs="empath kalarm kalarmd kalarmdgui kandy karm kgantt knotes korganizer kpilot ksync libkcal twister"
> kdepim.lang
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdepim.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdepim.lang
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%{_libdir}/kde3/libabbrowserconduit.la
%{_libdir}/kde3/libabbrowserconduit.so
%{_libdir}/kde3/libexpenseconduit.la
%{_libdir}/kde3/libexpenseconduit.so
%{_libdir}/kde3/libknotesconduit.la
%{_libdir}/kde3/libknotesconduit.so
%{_libdir}/kde3/libnullconduit.la
%{_libdir}/kde3/libnullconduit.so
%{_libdir}/kde3/libpopmailconduit.la
%{_libdir}/kde3/libpopmailconduit.so
%{_libdir}/kde3/libtodoconduit.la
%{_libdir}/kde3/libtodoconduit.so*
%{_libdir}/kde3/libvcalconduit.la
%{_libdir}/kde3/libvcalconduit.so

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
%{_pixmapsdir}/*/*/*/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.??
