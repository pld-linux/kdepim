# TODO: - Work on kaplan
#	- Backport .desktop and icon files for Kaplan from recent CVS
#	- Correct Russian descriptions (for those who understand russian, it is
#	  clear that H (N) is written in lowercase instead uppercase
#	- Recheck dependencies

%define         _state          unstable
%define         _kdever         kde-3.1-rc3

Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	Персональный планировщик (PIM) для KDE
Summary(uk):	Персональный планувальник (PIM) для KDE
Name:		kdepim
Version:	3.0.99
Release:	1
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
#Patch0:		%{name}-am.patch
#Patch1:		%{name}-kalarm.patch
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

%define         no_install_post_chrpath         1

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Enviromnent (KDE).

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Enviromnent
(KDE). 

%description -l ru
kdepim - это набор утилит для управления персональной информацией для
K Desktop Enviromnent (KDE).

%description -l uk
kdepim - це наб╕р утил╕т для керування персональною информац╕╓ю для K
Desktop Enviromnent (KDE).

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

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi╠©ka adresowa
Group:		X11/Applications
Requires:	%{name} = %{version}

%description kaddressbook
Address Book

%description kaddressbook -l pl
Ksi╠©ka adresowa

%package kalarm
Summary:	Alarm
Summary(pl):	Alarm
Group:		X11/Applications                       
Requires:	%{name} = %{version}

%description kalarm
Reminder Message Scheduler

%description kalarm -l pl
Nastawianie przypominania o zdarzeniach

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications                                                

%package kandy
Summary:        A communication program between mobile phone and PC
Summary(pl):    Program do komunikacji miЙdzy PC a tel. komСrkowym.
Group:          X11/Applications

%description kandy
Kandy provides access to your mobile phone and allows to sync the data on the
phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo©liwia dostЙp do telefonu komСrkowego i pozwala na synchronizacjЙ danych
z telefonu z danymi na PC.

%package kaplan
Summary:        An integrated PIM application
Summary(pl):    Zintegrowany PIM
Group:          X11/Applications
Requires:	kdenetwork-kmail = %{version}
Requires:       %{name}-knotes = %{version}
Requires:	%{name}-kaddressbook = %{version}
Requires:       %{name}-korganizer = %{version}

%description kaplan
Kaplan is a PIM application, whcih integrates the knotes, kmail, korganizer,  
kaddressbook parts.

%description kaplan -l pl
Kaplan jest aplikacj╠ PIM integruj╠c╠ funkcjonalno╤Ф knotes, kmail, korganizer,
kaddressbook.

%description karm
Personal timetracker

%description karm -l pl
Osobisty czasomierz

%package knotes
Summary:	Yellow cards
Summary(pl):	╞СЁte karteczki
Group:		X11/Applications                                                

%description knotes
Yellow cards

%description knotes -l pl
╞СЁte karteczki

%package konsolekalendar
Summary:        A command line ICard tool
Summary(pl):    NarzЙdzie dostepu do plikow kalendarza z linii polecen. 
Group:          Applications

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
NarzЙdzie dostepu do plikow kalendarza z linii polecen.

%package korganizer
Summary:        A complete calendar and scheduling progra
Summary(pl):    Kalendarz wraz z harmonogramem zadaЯ
Group:          X11/Applications

%description korganizer
A complete calendar and scheduling program, which  
supports information interchange with other calendar applications 
through the industry standard vCalendar file format.

%description korganizer -l pl
Kalendarz wraz z harmonogramem zadaЯ (KOrganizer), ktСry 
wspiera wymianЙ informacji z innymi tego typu aplikacjami poprzez
standard przemysЁowy (vCalendar).

%description korganizer -l ru
<lost>

%description korganizer -l uk
повнофункц╕ональна програма календара та персонального 
планувальника (KOrganizer п╕дтриму╓ обм╕н информац╕╓ю з ╕ншими
програмами такого роду через стандартний формат файлу vCalendar)

%package kpilot
Summary:        A sync tool for palmtops
Summary(pl):    NArzЙdzie do synchronizacji z palmtopami
Group:          X11/Applications
Requires:	pilot-link

%description kpilot
Syncronization tool for 3com Palm Pilots and compatible 
devices

%description kpilot -l pl
Narzedzie do synchronizacji z 3Com Palm Pilot'em i 
kompatybilnymi urzadzeniami.

%description kpilot -l ru
утилита для синхронизации с 3com Palm Pilots и совместимыми
с ними устройствами,

%description kpilot -l uk
утил╕та для синхрон╕зац╕╖ з 3com Palm Pilots та сум╕сними з 
ними пристроями.

%package ksync
Summary:        A library for syncing stuff
Summary(pl):    Biblioteka do synchronizacji rzeczy
Group:          X11/Libraries

%description ksync
libksync is a generic library for syncing collections of data entries like
calenders, bookmarks, contacts, mail folders etc.

%description ksync -l pl
libksync jest standardow╠ bibliotek╠ do synchronizacji zbiorСw danych jak np. 
kalendarze, zakЁadki, kontakty, foldery pocztowe itp.

%package kgantt
Summary:        A library to display and manage Gantt diagrams
Summary(pl):    Biblioteka do wy╤wietlania i zarz╠dzania diagramami Gantta
Group:          X11/Libraries

%description kgantt
A library to display and manage Gantt diagrams

%description kgantt -l pl
Biblioteka do wy╤wietlania i zarz╠dzania diagramami Gantta

%prep
%setup -q
#%patch0 -p1
#%patch1 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final

%{__make}

cd kaplan
%{__make}
cd .. 

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cd kaplan
%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT
cd ..

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Applications/*,Office/PIMs}
mv $ALD/Utilities/{More/*,.}

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
cat kalarmd.lang >> kalarm.lang
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	knotes		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	kpilot		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_libdir}/kde3/kfile*.*
%attr(755,root,root) %{_libdir}/libkdepim.*
%attr(755,root,root) %{_libdir}/libkcal*.*
%attr(755,root,root) %{_libdir}/libkpimexchange.*
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/webcal.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/*

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
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_libdir}/libkalarmd.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart
%{_pixmapsdir}/*/*/*/kalarm.png
%{_applnkdir}/.hidden/*
%{_applnkdir}/Office/PIMs/kalarm.desktop
%{_applnkdir}/Utilities/kalarm.desktop


%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_applnkdir}/Utilities/kandy.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_pixmapsdir}/*/*/*/karm.png
%{_applnkdir}/Utilities/karm.desktop

%files kaplan
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaplan
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.*
%attr(755,root,root) %{_libdir}/libkpinterfaces*.*
%{_datadir}/apps/kaplan
%{_datadir}/apps/kp*plugin
%{_datadir}/services/kp*plugin.*
%{_datadir}/servicetypes/kaplanplugin.desktop
#%{_pixmapsdir}/*/*/*/kaplan.png
%{_applnkdir}/Utilities/kandy.desktop

%files kgantt
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkgantt*.*
%{_datadir}/apps/kgantt

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_pixmapsdir}/*/*/*/knotes.png
%{_applnkdir}/Utilities/knotes.desktop

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar


%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_libdir}/libknewstuff*.*
%attr(755,root,root) %{_libdir}/libkorganizer*.*
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.*
%{_datadir}/apps/korganizer
%{_datadir}/services/korganizer
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_pixmapsdir}/*/*/*/korganizer*.png
%{_applnkdir}/Office/PIMs/korganizer.desktop

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpilot*
%attr(755,root,root) %{_libdir}/libkpilot*.*
%attr(755,root,root) %{_libdir}/kde3/*conduit.*
%{_datadir}/apps/kpilot
%{_datadir}/services/expense-conduit.desktop
%{_datadir}/services/abbrowser_conduit.desktop
%{_datadir}/services/knotes-conduit.desktop
%{_datadir}/services/null-conduit.desktop
%{_datadir}/services/popmail-conduit.desktop
%{_datadir}/services/time_conduit.desktop
%{_datadir}/services/todo-conduit.desktop
%{_datadir}/services/vcal-conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_pixmapsdir}/*/*/*/kpilot*.png
%{_applnkdir}/Utilities/kpilot*.desktop

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%attr(755,root,root) %{_libdir}/libksync*.*
%{_datadir}/apps/ksync
