# TODO: - Work on kaplan
#	- Backport .desktop and icon files for Kaplan from recent CVS
#	- Correct Russian descriptions (for those who understand russian, it is
#	  clear that H (N) is written in lowercase instead uppercase
#	- Recheck dependencies

%define         _state          stable
%define         _ver		3.1.2

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl):	Manad풽r informacji osobistej (PIM) dla KDE
Summary(ru):	晁錄鷗죈忘木 覲죔�碌李�� (PIM) 켈� KDE
Summary(uk):	晁錄鷗죈忘木 覲죔兩죈忘�� (PIM) 켈� KDE
Name:		kdepim
Version:	%{_ver}
Release:	1
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_ver}/src/%{name}-%{version}.tar.bz2
# Source0-md5: af83c92cd27fc8f84bb28dffd274ada3
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%define         no_install_post_chrpath         1

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE). 

%description -l ru
kdepim - 卜� 适쫏� 略�俓� 켈� 徠怒隆턱�� 斤錄鷗죈忘銶 �廣菊皐촁탱 켈�
K Desktop Environment (KDE).

%description -l uk
kdepim - 쳔 适짝� 略�迲� 켈� 愾論陸鑛� 斤錄鷗죈忘舅 �廣菊皐챈ㅐ 켈� K
Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag농wkowe do KDE pim
Summary(uk):	姸奸� 碌撲苟漑 켈� kdepim
Summary(ru):	姸奸� 怒撲좌鞫漑 켈� kdepim
Group:		X11/Development/Libraries

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag농wkowe potrzebne do budowy aplikacji
bazuj켧ych na kdepim.

%description devel -l uk
矢� 僅愾� 稽戇�潼 팁奸� 憫하卿率┹ 壙苟홀켑� 켈� 饉쫬켓慄 妗逑怒�,
쩝博陸炚� 适 kdepim.

%description devel -l ru
璜鞫 僅愾� 遝컵壟�� 팁奸� 憫하卿率窘 壙苟훰케梏� 켈� 饉戇碌턱��
妗逑怒袴, 鞠卦陸鑛謨 适 kdepim.

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi굻ka adresowa
Group:		X11/Applications
Requires:	%{name} = %{version}-%{release}

%description kaddressbook
Address Book.

%description kaddressbook -l pl
Ksi굻ka adresowa.

%package kalarm
Summary:	Alarm
Summary(pl):	Alarm
Group:		X11/Applications                       
Requires:	%{name} = %{version}-%{release}

%description kalarm
Reminder Message Scheduler.

%description kalarm -l pl
Nastawianie przypominania o zdarzeniach.

%package kandy
Summary:        A communication program between mobile phone and PC
Summary(pl):    Program do komunikacji mi�dzy PC a tel. kom�rkowym
Group:          X11/Applications
Obsoletes:	%{name}-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo퓄iwia dost�p do telefonu kom�rkowego i pozwala na
synchronizacj� danych z telefonu z danymi na PC.

%package kaplan
Summary:        An integrated PIM application
Summary(pl):    Zintegrowany PIM
Group:          X11/Applications
Requires:	kdenetwork-kmail >= %{version}
Requires:       %{name}-knotes = %{version}-%{release}
Requires:	%{name}-kaddressbook = %{version}-%{release}
Requires:       %{name}-korganizer = %{version}-%{release}

%description kaplan
Kaplan is a PIM application, which integrates the knotes, kmail,
korganizer, kaddressbook parts.

%description kaplan -l pl
Kaplan jest aplikacj� PIM integruj켧� funkcjonalno뜻 knotes, kmail,
korganizer i kaddressbook.

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications                                                

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s쿽wa "praca" w j�zyku punjambi) 턫edzi czas
sp�dzony na r璨nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w wielu klientom.

%package kgantt
Summary:        A library to display and manage Gantt diagrams
Summary(pl):    Biblioteka do rysowania diagram�w Gantta zarz켨zania nimi
Group:          X11/Libraries

%description kgantt
A library to display and manage Gantt diagrams.

%description kgantt -l pl
Biblioteka do rysowania diagram�w Gantta zarz켨zania nimi.

%package knotes
Summary:	Yellow cards
Summary(pl):	�車te karteczki
Group:		X11/Applications                                                

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na desktopie notatki z opcj� wysy쿪nia.
Dodatkowo, aby m�c s퀅퓓� za przypominajk�, KNotes mo풽 wysy쿪� poczt�
i drukowa� notatki, a tak풽 przyjmowa� przeci켫anie nawet ze zdalnych
komputer�w.

%package konsolekalendar
Summary:        A command line ICard tool
Summary(pl):    Narz�dzie dost�pu do plik�w kalendarza z linii polece� 
Group:          Applications

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
Narz�dzie dost�pu do plik�w kalendarza z linii polece�.

%package korganizer
Summary:        A complete calendar and scheduling progra
Summary(pl):    Kalendarz wraz z harmonogramem zada�
Group:          X11/Applications

%description korganizer
A complete calendar and scheduling program, which supports information
interchange with other calendar applications through the industry
standard vCalendar file format.

%description korganizer -l pl
Kalendarz wraz z harmonogramem zada� (KOrganizer), kt�ry wspiera
wymian� informacji z innymi tego typu aplikacjami poprzez standard
przemys쿽wy (vCalendar).

%description korganizer -l ru
饉勍軀來塏�鷗죈忘죙 妗逑怒袴� 個謙匡죠� � 斤錄鷗죈忘逑� 覲죔�碌李�個
(KOrganizer 饉컴텀禮陸텃 苟考� �廣菊皐촁탱 � 켠朗�苽 妗逑怒袴죌�
讀蓋하 碌컨 使瑙� 戇죔컨鹿槐� 팥魯죤 팁奸� vCalendar)

%description korganizer -l uk
饉肋軀來塏┩适景适 妗逑怒皐 個謙匡죠� 讀 斤錄鷗죈忘逑� 
覲죔兩죈忘�個 (KOrganizer 揆켬虜鼓� 苟稽� �廣菊皐챈ㅐ � ┧排苽
妗逑怒皐苽 讀蓋하 碌켭 使瑙� 戇죔컨鹿炚� 팥魯죤 팁奸� vCalendar)

%package kpilot
Summary:        A sync tool for palmtops
Summary(pl):    Narz�dzie do synchronizacji z palmtopami
Group:          X11/Applications
Requires:	pilot-link
Obsoletes:	%{name}-pilot

%description kpilot
Synchronization tool for 3Com Palm Pilots and compatible devices.

%description kpilot -l pl
Narz�dzie do synchronizacji z 3Com Palm Pilotem i zgodnymi
urz켨zeniami.

%description kpilot -l ru
略�俓讀 켈� 譚洸碌炚憫촁� � 3com Palm Pilots � 遝勒텁燉梏苽
� 炚苽 掠同銶戇陸苽,

%description kpilot -l uk
略�迲讀 켈� 譚洸碌過憫챈� � 3com Palm Pilots 讀 撞稽踏�苽 � 
炚苽 妗�戇碌佶�.

%package ksync
Summary:        A library for syncing stuff
Summary(pl):    Biblioteka do synchronizacji rzeczy
Group:          X11/Libraries

%description ksync
libksync is a generic library for syncing collections of data entries
like calenders, bookmarks, contacts, mail folders etc.

%description ksync -l pl
libksync jest standardow� bibliotek� do synchronizacji zbior�w danych
jak np. kalendarze, zak쿪dki, kontakty, foldery pocztowe itp.

%prep
%setup -q

%build
kde_appsdir="%{_applnkdir}"; export kde_appsdir
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

for plik in `find ./ -name *.desktop` ; do
	echo $plik
	sed -i -e 's/\[nb\]/\[no\]/g' $plik
done

%configure \
	--enable-final

%{__make}

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
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*
%{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/webcal.protocol

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde3/libkaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_applnkdir}/Utilities/kaddressbook.desktop
%{_pixmapsdir}/*/*/*/kaddressbook.png

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/korgac
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart
%{_applnkdir}/.hidden/*
%{_applnkdir}/Office/PIMs/kalarm.desktop
%{_applnkdir}/Utilities/kalarm.desktop
%{_pixmapsdir}/[!l]*/*/*/kalarm.png

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_applnkdir}/Utilities/kandy.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_applnkdir}/Utilities/karm.desktop
%{_pixmapsdir}/*/*/*/karm.png

%files kaplan
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kaplan
%{_libdir}/kde3/libkp*plugin.la
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.so
%{_libdir}/libkpinterfaces*.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*
%{_datadir}/apps/kaplan
%{_datadir}/apps/kp*plugin
%{_datadir}/services/kp*plugin.*
%{_datadir}/servicetypes/kaplanplugin.desktop
%{_applnkdir}/Office/PIMs/Kaplan.desktop
%{_pixmapsdir}/*/*/*/kaplan.png

%files kgantt
%defattr(644,root,root,755)
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*
%{_datadir}/apps/kgantt

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_applnkdir}/Utilities/knotes.desktop
%{_pixmapsdir}/*/*/*/knotes.png

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar

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

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*
%{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so
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
%{_applnkdir}/Utilities/kpilot*.desktop
%{_pixmapsdir}/[!l]*/*/*/kpilot*.png

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*
%{_datadir}/apps/ksync
