#
# TODO:
# - make separate subpackages
# - separate packages: pilot, cellphone, karm, knotes.
#
Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K ╣╔╫╨е╘е╬ х╞╟Ф - PIM (╟Ёюн а╓╨╦ ╟Э╦╝)
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	Персональный планировщик (PIM) для KDE
Summary(uk):	Персональный планувальник (PIM) для KDE
Name:		kdepim
Version:	3.0.3
Release:	6
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-fix-knotes-crash.patch
Patch1:		%{name}-desktop.patch
Patch2:		%{name}-no_versioned_modules.patch
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
(KDE). kdepim zawiera nastЙpujace programy:

- KOrganizer - kalendarz wraz z harmonogramem zadaЯ (KOrganizer
  wspiera wymianЙ informacji z innymi tego typu aplikacjami poprzez
  standard przemysЁowy vCalendar),
- Empath - klient E-Mail,
- abbrowser - czytnik ksiazki adresowej,
- kpilot - narzedzie do synchronizacji z 3Com Palm Pilot'em i
  kompatybilnymi urzadzeniami.
- twister - klient PIM.

%description -l ru
kdepim - это набор утилит для управления персональной информацией для
K Desktop Enviromnent (KDE). kdepim содержит следующие программы:

- KOrganizer - полнофункциональная программа календаря и персонального
  планировщика (KOrganizer поддерживает обмен информацией с другими
  программами такого рода через стандартный формат файла vCalendar)
- abbrowser - программа для чтения адресной книги,
- kpilot - утилита для синхронизации с 3com Palm Pilots и совместимыми
  с ними устройствами,

%description -l uk
kdepim - це наб╕р утил╕т для керування персональною информац╕╓ю для K
Desktop Enviromnent (KDE). kdepim м╕стить так╕ програми:

- KOrganizer - повнофункц╕ональна програма календара та персонального
  планувальника (KOrganizer п╕дтриму╓ обм╕н информац╕╓ю з ╕ншими
  програмами такого роду через стандартний формат файлу vCalendar),
- abbrowser - програма для читання адресно╖ книги,
- kpilot - утил╕та для синхрон╕зац╕╖ з 3com Palm Pilots та сум╕сними з
  ними пристроями.

%package pilot
Summary:	KDE support for synchronizing data with a Palm(tm) or compatible PDA
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pilot
KDE support for synchronizing data with a Palm(tm) or compatible PDA.

%package cellphone
Summary:	KDE support for synchronizing data with cellphones
Group:		X11/Applications
Requires:	%{name} = %{version}

%description cellphone
KDE support for synchronizing data with cellphones. Install
%{name}-cellphone if you want to use %{name} and have a cellphone.

%package karm
Summary:	Time tracking tool
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	karm

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%package knotes
Summary:	Post-It notes on the desktop
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	knotes

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nagЁСwkowe do KDE pim
Summary(uk):	Файли розробки для kdepim
Summary(ru):	Файлы разработки для kdepim
Group:		X11/Development/Libraries

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe potzrebne do budoway aplikacji
bazuj╠cych na kdepim.

%description devel -l uk
Цей пакет м╕стить файли заголовк╕в необх╕дн╕ для побудови програм,
базованих на kdepim.

%description devel -l ru
Этот пакет содержит файлы заголовков необходимые для построения
программ, основанных на kdepim.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

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
%{_libdir}/kde3/libtodoconduit.so
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
%{_libdir}/kde3/libabbrowserconduit.so
%{_libdir}/kde3/libexpenseconduit.so
%{_libdir}/kde3/libknotesconduit.so
%{_libdir}/kde3/libnullconduit.so
%{_libdir}/kde3/libpopmailconduit.so
%{_libdir}/kde3/libvcalconduit.so
