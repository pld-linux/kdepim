# TODO:
# - make separate subpackages

%define         _state          unstable
%define         _kdever         kde-3.1-beta1

Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	Персональный планировщик (PIM) для KDE
Summary(uk):	Персональный планувальник (PIM) для KDE
Name:		kdepim
Version:	3.0.8
Release:	3
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

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

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nagЁСwkowe do KDE pim
Summary(uk):	Файли розробки для kdepim
Summary(ru):	Файлы разработки для kdepim
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-common = %{version}
Requires:	%{name}-kaddressbook = %{version}
Requires:	%{name}-kalarm = %{version}

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

%package common
Summary:	Common files
Summary(pl):	Pliki wspСlne
Group:		X11/Applications

%description common
Common files

%description common
Pliki wspСlne

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi╠©ka adresowa
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kaddressbook
Address Book

%description kaddressbook
Ksi╠©ka adresowa

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications                                                

%description karm
Personal timetracker

%description karm
Osobisty czasomierz

%package kalarm
Summary:	Alarm
Summary(pl):	Alarm
Group:		X11/Applications                       
Requires:	%{name}-common = %{version}

%description kalarm
Reminder Message Scheduler

%description kalarm
Nastawianie przypominania o zdarzeniach

%package knotes
Summary:	Yellow cards
Summary(pl):	╞СЁte karteczki
Group:		X11/Applications                                                

%description knotes
Yellow cards

%description knotes
╞СЁte karteczki

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Applications/*,Office/PIMs}
mv $ALD/Utilities/{More/*,.}

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#programs="empath kalarm kalarmd kalarmdgui kandy karm kgantt knotes \
#korganizer kpilot ksync libkcal twister"
programs="kandy korganizer kpilot"

> kdepim.lang
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdepim.lang
done

%find_lang kaddressbook		--with-kde
%find_lang kalarm               --with-kde
%find_lang kalarmd              --with-kde
cat kalarmd.lang >> kalarm.lang
%find_lang karm			--with-kde
%find_lang knotes               --with-kde

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%files -f kdepim.lang
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/?[!n][!bdl][!m]*
%attr(755,root,root) %{_libdir}/????[!acd]*.la
%attr(755,root,root) %{_libdir}/????[!acd]*.so.*
%attr(755,root,root) %{_libdir}/kde3/kfile*
%attr(755,root,root) %{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so.*
%attr(755,root,root) %{_libdir}/kde3/libkorg*
%{_datadir}/apps/?[!n][!dl][!m]*
%{_datadir}/autostart/korg*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_pixmapsdir}/*/*/*/?[!n][!dl][!m]*
%{_applnkdir}/.hidden/*
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Utilities/?[!n][!dl][!m]*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/kde3/*conduit.so

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart*
%{_datadir}/apps/kaddressbook
%{_pixmapsdir}/*/*/*/kaddressbook.png
%{_applnkdir}/Utilities/kaddressbook.desktop

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%attr(755,root,root) %{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*
%{_pixmapsdir}/*/*/*/kalarm.png
%{_applnkdir}/Utilities/kalarm.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_pixmapsdir}/*/*/*/karm.png
%{_applnkdir}/Utilities/karm.desktop

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_pixmapsdir}/*/*/*/knotes.png
%{_applnkdir}/Utilities/knotes.desktop
