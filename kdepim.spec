#
# Todo
#	- Deps verifying	
#

%define         _state          snapshots
%define         _ver		3.2
%define		_snap		030317

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - PIM (°³ÀÎ Á¤º¸ °ü¸®)
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË (PIM) ÄÌÑ KDE
Summary(uk):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË (PIM) ÄÌÑ KDE
Name:		kdepim
Version:	%{_ver}
Release:	0.%{_snap}.0.4
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%define         no_install_post_chrpath         1

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Enviromnent (KDE).

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Enviromnent
(KDE). 

%description -l ru
kdepim - ÜÔÏ ÎÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÐÅÒÓÏÎÁÌØÎÏÊ ÉÎÆÏÒÍÁÃÉÅÊ ÄÌÑ
K Desktop Enviromnent (KDE).

%description -l uk
kdepim - ÃÅ ÎÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÐÅÒÓÏÎÁÌØÎÏÀ ÉÎÆÏÒÍÁÃ¦¤À ÄÌÑ K
Desktop Enviromnent (KDE).

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
Pakiet ten zawiera pliki nag³ówkowe potzrebne do budowy aplikacji
bazuj±cych na kdepim.

%description devel -l uk
ãÅÊ ÐÁËÅÔ Í¦ÓÔÉÔØ ÆÁÊÌÉ ÚÁÇÏÌÏ×Ë¦× ÎÅÏÂÈ¦ÄÎ¦ ÄÌÑ ÐÏÂÕÄÏ×É ÐÒÏÇÒÁÍ,
ÂÁÚÏ×ÁÎÉÈ ÎÁ kdepim.

%description devel -l ru
üÔÏÔ ÐÁËÅÔ ÓÏÄÅÒÖÉÔ ÆÁÊÌÙ ÚÁÇÏÌÏ×ËÏ× ÎÅÏÂÈÏÄÉÍÙÅ ÄÌÑ ÐÏÓÔÒÏÅÎÉÑ
ÐÒÏÇÒÁÍÍ, ÏÓÎÏ×ÁÎÎÙÈ ÎÁ kdepim.

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi±¿ka adresowa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kaddressbook
Address Book

%description kaddressbook -l pl
Ksi±¿ka adresowa

%package kalarm
Summary:	Alarm
Summary(pl):	Alarm
Group:		X11/Applications                       
Requires:	%{name} = %{version}-%{release}

%description kalarm
Reminder Message Scheduler

%description kalarm -l pl
Nastawianie przypominania o zdarzeniach

%package kandy
Summary:        A communication program between mobile phone and PC
Summary(pl):    Program do komunikacji miêdzy PC a tel. komórkowym.
Group:          X11/Applications
Obsoletes:	%{name}-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo¿liwia dostêp do telefonu komórkowego i pozwala na
synchronizacjê danych z telefonu z danymi na PC.

#package kaplan
#Summary:        An integrated PIM application
#Summary(pl):    Zintegrowany PIM
#Group:          X11/Applications
#Requires:	%{name}-kmail >= %{version}
#Requires:       %{name}-knotes = %{version}-%{release}
#Requires:	%{name}-kaddressbook = %{version}-%{release}
#Requires:       %{name}-korganizer = %{version}-%{release}

##%description kaplan
#Kaplan is a PIM application, whcih integrates the knotes, kmail,
#korganizer, kaddressbook parts.

#%description kaplan -l pl
#Kaplan jest aplikacj± PIM integruj±c± funkcjonalno¶æ knotes, kmail,
#korganizer i kaddressbook.

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications                                                

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s³owa "praca" w jêzyku punjambi) ¶ledzi czas
spêdzony na ró¿nych zajêciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunków wielu klientom.

%package kgantt
Summary:        A library to display and manage Gantt diagrams
Summary(pl):    Biblioteka do rysowania diagramów Gantta zarz±dzania nimi
Group:          X11/Libraries

%description kgantt
A library to display and manage Gantt diagrams.

%description kgantt -l pl
Biblioteka do rysowania diagramów Gantta zarz±dzania nimi.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Requires:	kdebase-mailnews
Requires:	kdelibs >= %{version}
Requires:	%{name}-libkdenetwork >= %{version}
Obsoletes:	kdenetwork-kmail

%description kmail
This is electronic mail client for KDE. It is able to retrievie mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description kmail -l pl
Program pocztowy dla KDE. Potrafi odczytywaæ pocztê z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów
znaków.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik newsów dla KDE
Summary(pt_BR):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	kdebase-mailnews
Requires:	kdelibs >= %{version}
Requires:	%{name}-libkdenetwork >= %{version}
Obsoletes:	kdenetwork-knode

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description knode -l pl
Czytnik newsów dla KDE. Obs³uguje w±tki oraz killfile.

%description knode -l pt_BR
Leitor de notícias (news) do KDE.


%package knotes
Summary:	Yellow cards
Summary(pl):	¯ó³te karteczki
Group:		X11/Applications                                                

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszczaæ na desktopie notatki z opcj± wysy³ania.
Dodatkowo, aby móc s³u¿yæ za przypominajkê, KNotes mo¿e wysy³aæ pocztê
i drukowaæ notatki, a tak¿e przyjmowaæ przeci±ganie nawet ze zdalnych
komputerów.

%package konsolekalendar
Summary:        A command line ICard tool
Summary(pl):    Narzêdzie dostêpu do plików kalendarza z linii poleceñ 
Group:          Applications

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
Narzêdzie dostêpu do plików kalendarza z linii poleceñ.

%package kontact
Summary:	An integrated shell for the PIM apps
Summary(pl):	Zintegrowany system aplikacji PIM
Group:          X11/Applications
Requires:	%{name}-kmail
#Requires:       %{name}-knode
Requires:       %{name}-korganizer
Requires:       %{name}-knotes
Requires:       %{name}-kaddressbook
Obsoletes:	%{name}-kaplan

%description kontact
An integrated shell for the PIM apps.

%description kontact -l pl
Zintegrowany system aplikacji PIM.

%package korganizer
Summary:        A complete calendar and scheduling progra
Summary(pl):    Kalendarz wraz z harmonogramem zadañ
Group:          X11/Applications

%description korganizer
A complete calendar and scheduling program, which supports information
interchange with other calendar applications through the industry
standard vCalendar file format.

%description korganizer -l pl
Kalendarz wraz z harmonogramem zadañ (KOrganizer), który wspiera
wymianê informacji z innymi tego typu aplikacjami poprzez standard
przemys³owy (vCalendar).

%description korganizer -l ru
ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÁÑ ÐÒÏÇÒÁÍÍÁ ËÁÌÅÎÄÁÒÑ É ÐÅÒÓÏÎÁÌØÎÏÇÏ ÐÌÁÎÉÒÏ×ÝÉËÁ
(KOrganizer ÐÏÄÄÅÒÖÉ×ÁÅÔ ÏÂÍÅÎ ÉÎÆÏÒÍÁÃÉÅÊ Ó ÄÒÕÇÉÍÉ ÐÒÏÇÒÁÍÍÁÍÉ
ÔÁËÏÇÏ ÒÏÄÁ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÙÊ ÆÏÒÍÁÔ ÆÁÊÌÁ vCalendar)

%description korganizer -l uk
ÐÏ×ÎÏÆÕÎËÃ¦ÏÎÁÌØÎÁ ÐÒÏÇÒÁÍÁ ËÁÌÅÎÄÁÒÁ ÔÁ ÐÅÒÓÏÎÁÌØÎÏÇÏ 
ÐÌÁÎÕ×ÁÌØÎÉËÁ (KOrganizer Ð¦ÄÔÒÉÍÕ¤ ÏÂÍ¦Î ÉÎÆÏÒÍÁÃ¦¤À Ú ¦ÎÛÉÍÉ
ÐÒÏÇÒÁÍÁÍÉ ÔÁËÏÇÏ ÒÏÄÕ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÉÊ ÆÏÒÍÁÔ ÆÁÊÌÕ vCalendar)

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska¼nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdelibs >= %{version}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj±cy ilo¶æ wiadomo¶ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitoração da caixa de correio.

%package kpilot
Summary:        A sync tool for palmtops
Summary(pl):    Narzêdzie do synchronizacji z palmtopami
Group:          X11/Applications
Requires:	pilot-link
Obsoletes:	%{name}-pilot

%description kpilot
Synchronization tool for 3Com Palm Pilots and compatible devices.

%description kpilot -l pl
Narzêdzie do synchronizacji z 3Com Palm Pilotem i zgodnymi
urz±dzeniami.

%description kpilot -l ru
ÕÔÉÌÉÔÁ ÄÌÑ ÓÉÎÈÒÏÎÉÚÁÃÉÉ Ó 3com Palm Pilots É ÓÏ×ÍÅÓÔÉÍÙÍÉ
Ó ÎÉÍÉ ÕÓÔÒÏÊÓÔ×ÁÍÉ,

%description kpilot -l uk
ÕÔÉÌ¦ÔÁ ÄÌÑ ÓÉÎÈÒÏÎ¦ÚÁÃ¦§ Ú 3com Palm Pilots ÔÁ ÓÕÍ¦ÓÎÉÍÉ Ú 
ÎÉÍÉ ÐÒÉÓÔÒÏÑÍÉ.

%package ksync
Summary:        A library for syncing stuff
Summary(pl):    Biblioteka do synchronizacji rzeczy
Group:          X11/Libraries

%description ksync
libksync is a generic library for syncing collections of data entries
like calenders, bookmarks, contacts, mail folders etc.

%description ksync -l pl
libksync jest standardow± bibliotek± do synchronizacji zbiorów danych
jak np. kalendarze, zak³adki, kontakty, foldery pocztowe itp.

%package libkdenetwork
Summary:        A network library
Summary(pl):    Biblioteka sieciowa
Group:          X11/Libraries
Obsoletes:	kdenetwork
Provides:	kdenetwork = 3.2

%description libkdenetwork

%description libkdenetwork -l pl

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	if [ -d $plik ]; then
	echo $plik
	sed -ie 's/\[nb\]/\[no\]/g' $plik
	fi
done

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_desktopdir}

ALD=$RPM_BUILD_ROOT%{_applnkdir}

install -d $ALD/{Office/PIMs,Settings/KDE}

mv -f $ALD/{Applications/[Kk]o*,Office/PIMs}
mv -f $ALD/Internet/K[!O]*.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/Internet/More/KOrn.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/{Settings/Components,Settings/KDE}
mv -f $ALD/{PIM/*,Settings/KDE/Components}
mv -f $ALD/Utilities/kaddressbook*.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/Utilities/k[!am]*.desktop $RPM_BUILD_ROOT%{_desktopdir}
mv -f $ALD/Utilities/More/*.desktop $RPM_BUILD_ROOT%{_desktopdir}

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
cat kalarmd.lang >> kalarm.lang
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	kpilot		--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/ktnef
%attr(755,root,root) %{_bindir}/simplealarmdaemon
%{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*
%{_libdir}/kde3/kcal_dir.la
%attr(755,root,root) %{_libdir}/kde3/kcal_dir.so
%{_libdir}/kde3/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%{_libdir}/kde3/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_libdir}/kde3/libkcm_kcalendars.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcalendars.so
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_libdir}/kde3/resourcecalendarimap.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarimap.so
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so*
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so*
%{_datadir}/apps/kresources
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_datadir}/services/doc_conduit.desktop
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/sieve.protocol
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{_applnkdir}/Settings/KDE/Components/kcalendars.desktop
%{_desktopdir}/kpalmdoc.desktop
%{_desktopdir}/ktnef.desktop
%{_pixmapsdir}/crystalsvg/*/apps/kpalmdoc.png
%{_pixmapsdir}/hicolor/*/apps/ktnef.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/kde3/*conduit.so

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde3/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%{_libdir}/kde3/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%{_libdir}/kde3/libkaddrbk_cardview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cardview.so
%{_libdir}/kde3/libkaddrbk_distributionlist.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_distributionlist.so
%{_libdir}/kde3/libkaddrbk_iconview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_iconview.so
%{_libdir}/kde3/libkaddrbk_location.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_location.so
%{_libdir}/kde3/libkaddrbk_tableview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_tableview.so
%{_libdir}/kde3/libkaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_datadir}/services/kaddressbook
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_applnkdir}/Settings/KDE/Components/kabconfig.desktop
%{_applnkdir}/Settings/KDE/Components/kabldapconfig.desktop
%{_desktopdir}/kaddressbook.desktop
%{_pixmapsdir}/*/*/*/kaddressbook.png

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/korgac
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart
%{_applnkdir}/.hidden/kalarmd.desktop
%{_desktopdir}/kalarm.desktop
%{_pixmapsdir}/[!l]*/*/*/kalarm.png

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_desktopdir}/kandy.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_desktopdir}/karm.desktop
%{_pixmapsdir}/*/*/*/karm.png

##%files kaplan
#%{_datadir}/servicetypes/kaplanplugin.desktop
#%{_applnkdir}/Office/PIMs/Kaplan.desktop
#%{_pixmapsdir}/*/*/*/kaplan.png

%files kgantt
%defattr(644,root,root,755)
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*
%{_datadir}/apps/kgantt

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kgpgcertmanager
#%attr(755,root,root) %{_bindir}/mail.local
%{_libdir}/kde3/libkmailpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmailpart.so*
#%{_libdir}/kde3/kfile_rfc822.la
#%attr(755,root,root) %{_libdir}/kde3/kfile_rfc822.so
%{_datadir}/apps/kconf_update/k[!n]*
%{_datadir}/apps/kconf_update/u*
%{_datadir}/apps/kgpgcertmanager/kgpgcertmanagerui.rc
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
#%{_datadir}/services/kfile_rfc822.desktop
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/KMail.desktop
%{_pixmapsdir}/*/*/*/kmail*.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_desktopdir}/KNode.desktop
%{_pixmapsdir}/*/*/*/knode.png

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_desktopdir}/knotes.desktop
%{_pixmapsdir}/*/*/*/knotes.png

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar

%files kontact
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%{_libdir}/kde3/libkp*plugin.la
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.so
%{_libdir}/libkpinterfaces*.la
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*
%{_datadir}/apps/kp*plugin
%{_datadir}/services/kp*plugin.*
%{_datadir}/apps/kontact
%{_pixmapsdir}/crystalsvg/*/apps/kontact.png
%{_applnkdir}/Office/PIMs/Kontact.desktop

%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ical2vcal
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*
%{_libdir}/kde3/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%{_datadir}/apps/korganizer
%{_datadir}/services/korganizer
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_applnkdir}/Office/PIMs/korganizer.desktop
%{_pixmapsdir}/*/*/*/korganizer*.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/KOrn.desktop
%{_pixmapsdir}/*/*/*/korn.png

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*
%{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so.*
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
%{_desktopdir}/kpilot*.desktop
%{_pixmapsdir}/[!l]*/*/*/kpilot*.png

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*
%{_datadir}/apps/ksync

%files libkdenetwork
%defattr(644,root,root,755)
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so*
