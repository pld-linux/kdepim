# TODO
# - subpackages for akregator, korganizer(?)
# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
%bcond_without	hidden_visibility	# pass '--fvisibility=hidden'
					# & '--fvisibility-inlines-hidden'
					# to g++
#
%define		_state		stable
%define		_minlibsevr	9:%{version}
%define		_minbaseevr	9:%{version}

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl):	Manad풽r informacji osobistej (PIM) dla KDE
Summary(ru):	晁錄鷗죈忘木 覲죔�碌李�� (PIM) 켈� KDE
Summary(uk):	晁錄鷗죈忘木 覲죔兩죈忘�� (PIM) 켈� KDE
Name:		kdepim
Version:	3.5.6
Release:	4
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{version}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	e37e6173fe9fd7f242c9502a4ae1d7de
Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-kmail_toolbars.patch
Patch2:		%{name}-kmail-vcardviewer.patch
Patch3:		kde-ac260-lt.patch
Patch4:		%{name}-kmail-toolbar.patch
BuildRequires:	autoconf
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bluez-libs-devel
BuildRequires:	boost-type_traits-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-dtd42-xml
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gpgme-devel >= 1:1.0.0
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libgnokii-devel
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	lockdev-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pilot-link-devel >= 0.12.1
BuildRequires:	qt-designer-libs
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildConflicts:	indexlib
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# subpackage akregator
Obsoletes:	akregator
#Obsoletes:	kdeaddons-konqueror
Obsoletes:	kdeaddons-kontact
Obsoletes:	kdepim-kontact
Obsoletes:	kdepim-korganizer
Obsoletes:	kdepim-kresources
Obsoletes:	kdepim-ksync
#Obsoletes:	kdepim-libkcal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
Summary(ru):	姸奸� 怒撲좌鞫漑 켈� kdepim
Summary(uk):	姸奸� 碌撲苟漑 켈� kdepim
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	indexlib-devel
Obsoletes:	kdepim-libkcal-devel
Conflicts:	kdenetwork-devel < 10:3.1.90

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

%package apidocs
Summary:	API documentation
Summary(pl):	Dokumentacja API
Group:		Documentation
Requires:	kdelibs >= 9:3.2.90

%description apidocs
Annotated reference of libkdepim, libkdenetwork, libkmailprivate,
libknodecommon and the other kdepim's programming interfaces':
- class lists
- class members
- namespaces

%description apidocs -l pl
Dokumentacja interfejs�w programowania libkdepim, libkdenetwork,
libkmailprivate, libknodecommon i innych z kdepim wraz z przypisami:
- listy klas i ich sk쿪dnik�w
- list� przestrzeni nazw (namespace)

%package -n kde-kio-groupwise
Summary:	Groupwise protocol service
Summary(pl):	Obs퀅ga protoko퀅 Groupwise
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description -n kde-kio-groupwise
Groupwise protocol service.

%description -n kde-kio-groupwise -l pl
Obs퀅ga protoko퀅 Groupwise.

%package -n kde-kio-imap4
Summary:	IMAP4 protocol service
Summary(pl):	Obs퀅ga protoko퀅 IMAP4
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kde-kio-newimap4 < 9:3.4.0

%description -n kde-kio-imap4
IMAP4 protocol service.

%description -n kde-kio-imap4 -l pl
Obs퀅ga protoko퀅 IMAP4.

%package kaddressbook
Summary:	Address book
Summary(pl):	Ksi굻ka adresowa
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs >= %{_minlibsevr}

%description kaddressbook
The KDE address book.

%description kaddressbook -l pl
Ksi굻ka adresowa dla KDE.

%package kalarm
Summary:	A personal alarm scheduler
Summary(pl):	Osobisty program do przypominania
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kalarm

%description kalarm
KAlarm is a personal alarm message, command and email scheduler. It
lets you set up personal alarm messages which pop up on the screen at
the chosen time, or you can schedule commands to be executed or emails
to be sent. Also includes an alarm daemon.

%description kalarm -l pl
KAlarm to osobisty program do planowania i przypominania poprzez
uruchomienie polecenia lub poczt� elektroniczn�. Umo퓄iwia ustawienie
w쿪snej wiadomo턢i alarmowej, kt�ra wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie polece� do wykonania lub poczty do
wys쿪nia. Zawiera tak풽 demona obs퀅guj켧ego przypominanie.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl):	Program do komunikacji mi�dzy PC a tel. kom�rkowym
Group:		X11/Applications
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= %{_minlibsevr}
Obsoletes:	kdepim-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo퓄iwia dost�p do telefonu kom�rkowego i pozwala na
synchronizacj� danych z telefonu z danymi na PC.

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s쿽wa "praca" w j�zyku punjambi) 턫edzi czas
sp�dzony na r璨nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
URL:		http://kmail.kde.org/
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kde-kio-imap4 >= %{epoch}:%{version}-%{release}
Requires:	kde-kio-pop3 >= %{_minbaseevr}
Requires:	kde-kio-smtp >= %{_minbaseevr}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kde-kio-sieve
Obsoletes:	kdenetwork-kmail
Obsoletes:	kdenetwork-korn
Obsoletes:	kdepim-ktnef

%description kmail
This is electronic mail client for KDE with a huge amount of features:
- SMTP/maildir/POP3/IMAP support with SSL/TLS and pipelining
- address book
- automatic encryption using OpenPGP (PGP or GnuPG)
- powerful mail filters
- mailinglist aware nested mail folders
- on-demand downloading or deleting without downloading of big mails
  on a POP3 server
- full support for mails in all languages and charsets supported by Qt
- message search result presentation in virtual folders
- duplicate mail removal
- threading of messages
- spell checking as you type
- import of mail from other clients
- and more...

%description kmail -l pl
Program pocztowy dla KDE o olbrzymich mo퓄iwo턢iach, obejmuj켧ych:
- obs퀅g� SMTP/maildir/POP3/IMAP z SSL/TLS i pipeliningiem
- ksi굻k� adresow�
- automatyczne szyfrowanie przy u퓓ciu OpenPGP (PGP lub GnuPG)
- pot轅ne filtry pocztowe
- zagnie풼퓇ne skrzynki pocztowe z obs퀅g� list pocztowych
- 턢i켫anie na 엽danie lub usuwanie bez 턢i켫ania du퓓ch list�w z
  serwera POP3
- pe쿻� obs퀅g� list�w we wszystkich j�zykach i zestawach znak�w
  obs퀅giwanych przez Qt
- przeszukiwanie wiadomo턢i z prezentacj� w wirtualnych folderach
- usuwanie powt�rzonych list�w
- w켾kowanie wiadomo턢i
- kontrol� pisowni w locie
- import poczty z innych klient�w
- wiele wi�cej...

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik news�w dla KDE
Summary(pt_BR):	Leitor de not�cias (news) do KDE
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kde-kio-nntp >= %{_minbaseevr}
Requires:	kdebase-core >= %{_minbaseevr}
Obsoletes:	kdenetwork-knode

%description knode
KNode is an online newsreader (GKNSA compliant) for the K Desktop
Environment. It features:
- all basic features of a newsreader (read articles, post articles,
  threading ...)
- support for multiple newsservers
- reading and composing of MIME multipart messages
- inline display of attachments (text and images)
- support for sending mail via smtp
- customizable filters, fonts, colors
- full scoring
- and more...

%description knode -l pl
KNode to czytnik news�w zgodny ze specyfikacj� GKNSA przeznaczony dla
턳odowiska KDE. Jego mo퓄iwo턢i obejmuj�:
- wszystkie podstawowe cechy czytnika news�w (czytanie i wysy쿪nie
  artyku농w, w켾kowanie...)
- obs퀅g� wielu serwer�w news
- czytanie i tworzenie wielocz沅ciowych wiadomo턢i MIME
- wy턻ietlanie za낢cznik�w w tek턢ie (tekstowych i obrazk�w)
- konfigurowalne filtry, fonty i kolory
- pe쿻y scoring
- wiele wi�cej...

%description knode -l pt_BR
Leitor de not�cias (news) do KDE.

%package knotes
Summary:	Yellow cards
Summary(pl):	�車te karteczki
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na pulpicie notatki z opcj� wysy쿪nia.
Dodatkowo, aby m�c s퀅퓓� za przypominajk�, KNotes mo풽 wysy쿪� poczt�
i drukowa� notatki, a tak풽 przyjmowa� przeci켫anie nawet ze zdalnych
komputer�w.

%package konsolekalendar
Summary:	A command line ICard tool
Summary(pl):	Narz�dzie dost�pu do plik�w kalendarza z linii polece�
Group:		Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description konsolekalendar
KonsoleKalendar is a command line interface to KDE calendars. It lets
you view, insert, remove, or modify calendar events by way of the
command line or from a scripting language. Additionally,
KonsoleKalendar can export a KDE calendar to a variety of other
formats.

Main features of KonsoleKalendar:
- list calendar entries from a start date/time to end date/time
- insert/remove/modify calendar entries
- export calendar entries to other file formats

%description konsolekalendar -l pl
KonsoleKalendar to dzia쿪j켧y z linii polece� interfejs do kalendarzy
KDE. Pozwala ogl켨a�, wstawia�, usuwa� i modyfikowa� zdarzenia w
kalendarzu z linii polece� lub j�zyka skryptowego. Ponadto
KonsoleKalendar potrafi wyeksportowa� kalendarz KDE do wielu innych
format�w.

G농wne mo퓄iwo턢i programu KonsoleKalendar:
- wypisywanie wpis�w kalendarza od daty pocz켾kowej do ko�cowej
- wstawianie/usuwanie/modyfikowanie wpis�w
- eksportowanie wpis�w kalendarza do innych format�w plik�w.

Narz�dzie dost�pu do plik�w kalendarza z linii polece�.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska펝ik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitora豫o da caixa de correio
Group:		X11/Applications
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj켧y liczb� wiadomo턢i w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitora豫o da caixa de correio.

%package kpilot
Summary:	A sync tool for palmtops
Summary(pl):	Narz�dzie do synchronizacji z palmtopami
Group:		X11/Applications
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	pilot-link
Obsoletes:	kdepim-kpalmdoc
Obsoletes:	kdepim-pilot
Obsoletes:	kpilot

%description kpilot
KPilot is an equivalent for the Palm Desktop software from Palm Inc,
which makes your Palm/Palm Pilot/Visor computer capable of exchanging
information with your KDE powered computer. KPilot doesn't replace the
Palm Desktop all by itself. It connects and integrates a number of
fine KDE 3.x applications into a package that can do everything the
Palm Desktop can, and more.

KPilot has plugins that can exchange information between your Palm and
other applications like KOrganizer or POP3/SMTP mail servers. In
KPilot you can display and edit your contacts, write notes or install
new programs on your Palm.

It supports:
- Palm Pilot, m100, m500, Zire, Tungsten series
- Handspring Visor and Treo series
- Sony Cli� series (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c,
  T675c, 665c)
- and Garmin iQue 3600
- others might work, but have not been tested

%description kpilot -l pl
KPilot to odpowiednik oprogramowania Palm Desktop firmy Palm Inc,
umo퓄iwiaj켧y wymian� informacji mi�dzy urz켨zeniami Palm, Palm Pilot
i Visor a komputerem z KDE. KPilot jako taki nie zast�puje Palm
Desktop - 낢czy i integruje wiele aplikacji KDE 3.x w pakiet, kt�rym
mo퓆a zrobi� tyle samo, a nawet wi�cej, co przy u퓓ciu Palm Desktop.

KPilot ma wtyczki do wymiany informacji mi�dzy Palmem a innymi
aplikacjami, takimi jak KOrganizer albo serwery POP3/SMTP. W KPilocie
mo퓆a wy턻ietla� i modyfikowa� kontakty, pisa� notatki lub instalowa�
nowe programy na Palmie.

Obs퀅guje urz켨zenia serii:
- Palm Pilot, m100, m500, Zire, Tungsten
- Handspring Visor i Treo
- Sony Cli� (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c, T675c, 665c)
- Garmin iQue 3600
- mog� dzia쿪� tak풽 inne, ale nie by퀉 testowane.

%description kpilot -l ru
略�俓讀 켈� 譚洸碌炚憫촁� � 3com Palm Pilots � 遝勒텁燉梏苽 � 炚苽
掠同銶戇陸苽,

%description kpilot -l uk
略�迲讀 켈� 譚洸碌過憫챈� � 3com Palm Pilots 讀 撞稽踏�苽 � 炚苽
妗�戇碌佶�.

%package libs
Summary:	Shared kdepim libraries
Summary(pl):	Wsp車dzielone biblioteki kdepim
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kdepim-kmail-libs = %{epoch}:%{version}-%{release}
Provides:	kdepim-libkdenetwork = %{epoch}:%{version}-%{release}
Provides:	kdepim-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	indexlib
Obsoletes:	kdenetwork
Obsoletes:	kdepim-commonlibs
Obsoletes:	kdepim-kaddressbook-libs
Obsoletes:	kdepim-kgantt
Obsoletes:	kdepim-kmail-libs
Obsoletes:	kdepim-kontact-libs
Obsoletes:	kdepim-korganizer-libs
Obsoletes:	kdepim-libkcal
Obsoletes:	kdepim-libkdenetwork
Obsoletes:	kdepim-libkdepim
Obsoletes:	kdepim-libkmailprivate
Obsoletes:	kdepim-libknodecommon
Obsoletes:	kdepim-libknotes_xmlrpc
Obsoletes:	kdepim-libkpilot
Obsoletes:	kdepim-libksieve
Obsoletes:	kdepim-libktnef
Obsoletes:	kdepim-libmimelib
Conflicts:	akregator < 3.4.0

%description libs
Libraries shared between PIM applications in KDE, which include:
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib and more

%description libs -l pl
Biblioteki wsp車dzielone pomi�dzy aplikacjami PIM w KDE, m.in.
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib.

%prep
%setup -q
%patch100 -p0
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Calendar;/' \
	korganizer/korganizer.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kpilot/kpilot/kpilotdaemon.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kpilot/kpilot/kpilot.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kpilot/conduits/docconduit/kpalmdoc.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;ContactManagement;/' \
	kaddressbook/kaddressbook.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;X-PIM;/' \
	kontact/src/Kontact.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Email;/' \
	kmail/KMail.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Network;News;/' \
	knode/KNode.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kmobile/kmobile.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kandy/src/kandy.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Applet;/' \
	knotes/knotes.desktop
%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	ktnef/gui/ktnef.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

# change annoyance-filter path (required by autodetect in kmail)
%{__sed} -i -e 's,\($HOME/\.annoyance-filter/annoyance-filter\)\(.*\),annoyance-filter\2,g' \
	kmail/kmail.antispamrc

rm -f configure

%build
# speedup
if [ ! -f configure ]; then
	cp %{_datadir}/automake/config.sub admin
	%{__make} -f admin/Makefile.common cvs
fi

%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
	--disable-final \
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
	--enable-indexlib \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
	--with-gpg=/usr/bin/gpg \
	--with-gpgsm=/usr/bin/gpgsm \
	--enable-newdistrlists \
	--with-distribution="PLD Linux Distribution" \
	--with-qt-libraries=%{_libdir}

%{__make}
%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT
rm -f *.lang

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

%find_lang	akregator	--with-kde
%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	konsolekalendar	--with-kde
%find_lang	kontact		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	korn		--with-kde
%find_lang	kleopatra	--with-kde
cat kleopatra.lang >> kmail.lang
%find_lang	kpilot		--with-kde
%find_lang	ktnef		--with-kde
cat ktnef.lang >> kmail.lang
%find_lang	kwatchgnupg	--with-kde
cat kwatchgnupg.lang >> kmail.lang
%find_lang	multisynk	--with-kde

> %{name}.lang
cat akregator.lang	>> %{name}.lang
cat kontact.lang	>> %{name}.lang
cat korganizer.lang	>> %{name}.lang
# TODO
cat multisynk.lang	>> %{name}.lang

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

# remove checked files
rm $RPM_BUILD_ROOT%{_datadir}/applnk/{Applications/kalarm,Utilities/{kandy,karm,kmailcvt}}.desktop
rm $RPM_BUILD_ROOT%{_iconsdir}/locolor/{16x16/apps/ktnef,32x32/apps/ktnef}.png

rm -f $RPM_BUILD_ROOT%{_libdir}/kde3/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs			-p /sbin/ldconfig
%postun	libs			-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.Kolab
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/exchangewizard
%attr(755,root,root) %{_bindir}/*groupwarewizard
%attr(755,root,root) %{_bindir}/groupwisewizard
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/kode
%attr(755,root,root) %{_bindir}/kolabwizard
%attr(755,root,root) %{_bindir}/kontact
%attr(755,root,root) %{_bindir}/kxml_compiler
%attr(755,root,root) %{_bindir}/kitchensync
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ksync
%attr(755,root,root) %{_bindir}/multisynk
%attr(755,root,root) %{_bindir}/networkstatustestservice
%attr(755,root,root) %{_bindir}/sloxwizard

%attr(755,root,root) %{_libdir}/libkabckonnector.so
%attr(755,root,root) %{_libdir}/libkcalkonnector.so
%attr(755,root,root) %{_libdir}/liblocalkonnector.so
%attr(755,root,root) %{_libdir}/libqtopiakonnector.so
%attr(755,root,root) %{_libdir}/libremotekonnector.so

%attr(755,root,root) %{_libdir}/kde3/conduit_memofile.so
%attr(755,root,root) %{_libdir}/kde3/conduit_notepad.so
%attr(755,root,root) %{_libdir}/kde3/kabc_groupdav.so
%attr(755,root,root) %{_libdir}/kde3/kabc_groupwise.so
%attr(755,root,root) %{_libdir}/kde3/kabc_kolab.so
%attr(755,root,root) %{_libdir}/kde3/kabc_newexchange.so
%attr(755,root,root) %{_libdir}/kde3/kabc_slox.so
%attr(755,root,root) %{_libdir}/kde3/kabc_xmlrpc.so
#%attr(755,root,root) %{_libdir}/kde3/kcal_blogging.so
%attr(755,root,root) %{_libdir}/kde3/kcal_groupdav.so
%attr(755,root,root) %{_libdir}/kde3/kcal_groupwise.so
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%attr(755,root,root) %{_libdir}/kde3/kcal_kolab.so
%attr(755,root,root) %{_libdir}/kde3/kcal_local.so
%attr(755,root,root) %{_libdir}/kde3/kcal_localdir.so
%attr(755,root,root) %{_libdir}/kde3/kcal_newexchange.so
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%attr(755,root,root) %{_libdir}/kde3/kcal_resourcefeatureplan.so
%attr(755,root,root) %{_libdir}/kde3/kcal_slox.so
%attr(755,root,root) %{_libdir}/kde3/kcal_xmlrpc.so
#%attr(755,root,root) %{_libdir}/kde3/kcm_kabsummary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kmailsummary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kontact.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactknt.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactsummary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_korganizer.so
%attr(755,root,root) %{_libdir}/kde3/kcm_korgsummary.so
%attr(755,root,root) %{_libdir}/kde3/kcm_sdsummary.so
%attr(755,root,root) %{_libdir}/kde3/kded_networkstatus.so
%attr(755,root,root) %{_libdir}/kde3/kfile_ics.so
%attr(755,root,root) %{_libdir}/kde3/libakregatorpart.so*
#%attr(755,root,root) %{_libdir}/kde3/libkded_ksharedfile.so
%attr(755,root,root) %{_libdir}/kde3/libexchangewizard.so
%attr(755,root,root) %{_libdir}/kde3/libgroupwisewizard.so*
%attr(755,root,root) %{_libdir}/kde3/libakregator_mk4storage_plugin.so
%attr(755,root,root) %{_libdir}/kde3/libkitchensyncpart.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_akregator.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_journalplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_kaddressbookplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_karm.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmailplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_knodeplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_knotesplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_korganizerplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_todoplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_kpilotplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_multisynk.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_newstickerplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_specialdatesplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_summaryplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkontact_weatherplugin.so
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%attr(755,root,root) %{_libdir}/kde3/libkorganizerpart.so
%attr(755,root,root) %{_libdir}/kde3/libksfilter_addressbook.so
%attr(755,root,root) %{_libdir}/kde3/libksfilter_calendar.so
%attr(755,root,root) %{_libdir}/kde3/libksync_backup.so
%attr(755,root,root) %{_libdir}/kde3/libksync_debugger.so
%attr(755,root,root) %{_libdir}/kde3/libksync_pluckerpart.so
%attr(755,root,root) %{_libdir}/kde3/libksync_restore.so
%attr(755,root,root) %{_libdir}/kde3/libksync_syncerpart.so
%attr(755,root,root) %{_libdir}/kde3/libksync_viewer.so
%attr(755,root,root) %{_libdir}/kde3/libmultisynkpart.so
%attr(755,root,root) %{_libdir}/kde3/liboverviewpart.so
%attr(755,root,root) %{_libdir}/kde3/libegroupwarewizard.so*
%attr(755,root,root) %{_libdir}/kde3/libkolabwizard.so*
%attr(755,root,root) %{_libdir}/kde3/libsloxwizard.so*
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kdepimwidgets.so
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kpartsdesignerplugin.so
%{_datadir}/apps/akregator
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/kdepimwidgets
%{_datadir}/apps/kgantt
%{_datadir}/apps/kitchensync
%{_datadir}/apps/konqueror/servicemenus/kitchensync-pluck-rdf.desktop
%{_datadir}/apps/konqueror/servicemenus/kitchensync-pluck.desktop
%{_datadir}/apps/kontact
%{_datadir}/apps/kontactsummary
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/ksync
%{_datadir}/apps/kdepim
%{_datadir}/apps/multisynk
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/customtemplates_kfg.kcfg
%{_datadir}/config.kcfg/egroupware.kcfg
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config.kcfg/memofileconduit.kcfg
%{_datadir}/config.kcfg/mk4config.kcfg
%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/slox.kcfg
%{_datadir}/config.kcfg/templatesconfiguration_kfg.kcfg

#%{_datadir}/mimelnk/kdedevice/cellphone.desktop
#%{_datadir}/mimelnk/kdedevice/pda.desktop
%{_datadir}/services/akregator_mk4storage_plugin.desktop
%{_datadir}/services/akregator_part.desktop
%{_datadir}/services/feed.protocol
#%{_datadir}/services/kcmkabsummary.desktop
%{_datadir}/services/kcmkmailsummary.desktop
%{_datadir}/services/kcmkontactknt.desktop
%{_datadir}/services/kcmkontactsummary.desktop
%{_datadir}/services/kcmkorgsummary.desktop
%{_datadir}/services/kcmsdsummary.desktop
%{_datadir}/services/kded/networkstatus.desktop
%{_datadir}/services/kfile_ics.desktop
%{_datadir}/services/kitchensync
%{_datadir}/services/kontact
%{_datadir}/services/kontactconfig.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/korganizer_*.desktop
%{_datadir}/services/kresources/kabc/imap.desktop
%{_datadir}/services/kresources/kabc/kabc_groupdav.desktop
%{_datadir}/services/kresources/kabc/kabc_groupwise.desktop
%{_datadir}/services/kresources/kabc/kabc_newexchange.desktop
%{_datadir}/services/kresources/kabc/kabc_opengroupware.desktop
%{_datadir}/services/kresources/kabc/kabc_slox.desktop
%{_datadir}/services/kresources/kabc/kabc_xmlrpc.desktop
%{_datadir}/services/kresources/kabc/kolab.desktop
%{_datadir}/services/kresources/kabc/kabc_ox.desktop
%{_datadir}/services/kresources/kcal
%{_datadir}/services/kresources/kcal_manager.desktop
%{_datadir}/services/kresources/konnector
%{_datadir}/services/kresources/konnector_manager.desktop
%{_datadir}/services/overview.desktop
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/akregator_plugin.desktop
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/filter.desktop
%{_datadir}/servicetypes/kaddressbookimprotocol.desktop
%{_datadir}/servicetypes/kitchensync.desktop
%{_datadir}/servicetypes/konnector.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_datadir}/servicetypes/korgprintplugin.desktop
%{_desktopdir}/kde/Kontact.desktop
%{_desktopdir}/kde/akregator.desktop
%{_desktopdir}/kde/korganizer.desktop
%{_desktopdir}/kde/multisynk.desktop
%{_desktopdir}/kde/groupwarewizard.desktop
%{_iconsdir}/*/*/apps/akregator*
%{_iconsdir}/*/*/*/korganizer*.png
%{_iconsdir}/*/*/apps/multisynk.png
%{_iconsdir}/*/*/apps/kontact.png
%{_iconsdir}/*/*/actions/kontact_*.png
%{_iconsdir}/*/*/actions/*rss*
%{_iconsdir}/crystalsvg/22x22/actions/button_fewer.png
%{_iconsdir}/crystalsvg/22x22/actions/button_more.png

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/indexlib-config
%{_includedir}/KNotesIface.h
%{_includedir}/KNotesAppIface.h
%{_includedir}/kdepimmacros.h
%{_includedir}/kmailIface.h
%{_includedir}/kmailicalIface.h
%{_includedir}/kmailpartIface.h
%{_includedir}/akregator
%{_includedir}/calendar
%{_includedir}/gpgme++
%{_includedir}/index
%{_includedir}/kabc/kabc_resourcexmlrpc.h
%{_includedir}/kabc/kcal_resourcexmlrpc.h
%{_includedir}/kaddressbook
%{_includedir}/kdepim
%{_includedir}/kgantt
%{_includedir}/kitchensync
%{_includedir}/kleo
%{_includedir}/kmail
%{_includedir}/kontact
%{_includedir}/korganizer
%{_includedir}/kpilot
%{_includedir}/ksieve
%{_includedir}/ktnef
%{_includedir}/libemailfunctions
%{_includedir}/libkcal
%{_includedir}/mimelib
%{_includedir}/qgpgme
%{_libdir}/libgpgme++.so
%{_libdir}/libkabc_groupdav.so
%{_libdir}/libindex.so
%{_libdir}/libkabc_groupwise.so
%{_libdir}/libkabc_newexchange.so
%{_libdir}/libkabc_slox.so
%{_libdir}/libkabc_xmlrpc.so
%{_libdir}/libkabckolab.so
%{_libdir}/libkabinterfaces.so
%{_libdir}/libkaddressbook.so
%{_libdir}/libkcal.so
%{_libdir}/libkcal_groupdav.so
%{_libdir}/libkcal_groupwise.so
%{_libdir}/libkcal_newexchange.so
%{_libdir}/libkcal_resourcefeatureplan.so
%{_libdir}/libkcal_resourceremote.so
%{_libdir}/libkcal_slox.so
%{_libdir}/libkcal_xmlrpc.so
%{_libdir}/libkcalkolab.so
%{_libdir}/libkdepim.so
%{_libdir}/libkgantt.so
%{_libdir}/libkgroupwarebase.so
%{_libdir}/libkgroupwaredav.so
%{_libdir}/libkholidays.so
%{_libdir}/libkitchensyncui.so
%{_libdir}/libkleopatra.so
%{_libdir}/libkmime.so
%{_libdir}/libknotes_xmlrpc.so
%{_libdir}/libknoteskolab.so
%{_libdir}/libkocorehelper.so
%{_libdir}/libkode.so
%{_libdir}/libkonnector.so
%{_libdir}/libkontact.so
%{_libdir}/libkorganizer.so
%{_libdir}/libkorganizer_eventviewer.so
%{_libdir}/libkorganizer_calendar.so
%{_libdir}/libkorg_stdprinting.so
%{_libdir}/libkpgp.so
%{_libdir}/libmultisynk.so
%{_libdir}/libkpilot.so
%{_libdir}/libkpimexchange.so
%{_libdir}/libkpimidentities.so
%{_libdir}/libkpinterfaces.so
%{_libdir}/libksieve.so
%{_libdir}/libksync.so
%{_libdir}/libksync2.so
%{_libdir}/libktnef.so
%{_libdir}/libmimelib.so
%{_libdir}/libqgpgme.so

%{_libdir}/*.la

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files -n kde-kio-imap4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_imap4.so
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol

%files -n kde-kio-groupwise
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde3/kio_groupwise.so
%{_datadir}/config.kcfg/groupwise.kcfg
%{_datadir}/services/groupwise.protocol
%{_datadir}/services/groupwises.protocol

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kabcustomfields.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%attr(755,root,root) %{_libdir}/kde3/ldifvcardthumbnail.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cardview.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cryptosettings.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_distributionlist.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_iconview.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_resourceselection.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_tableview.so
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_*_xxport.so
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_datadir}/services/kabconfig.desktop
%{_datadir}/services/kabcustomfields.desktop
%{_datadir}/services/kabldapconfig.desktop
%{_datadir}/services/kaddressbook
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/ldifvcardthumbnail.desktop
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_contacteditorwidget.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_datadir}/servicetypes/kaddressbook_xxport.desktop
%{_desktopdir}/kde/kaddressbook.desktop
%{_iconsdir}/*/*/*/kaddressbook.png

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*.desktop
%{_desktopdir}/kde/kalarm.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%attr(755,root,root) %{_libdir}/kde3/libkarmpart.so
%{_datadir}/apps/karm
%{_datadir}/apps/karmpart
%{_datadir}/services/karm_part.desktop
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmail_antivir.sh
%attr(755,root,root) %{_bindir}/kmail_clamav.sh
%attr(755,root,root) %{_bindir}/kmail_fprot.sh
%attr(755,root,root) %{_bindir}/kmail_sav.sh
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kleopatra
%attr(755,root,root) %{_bindir}/kwatchgnupg
%attr(755,root,root) %{_libdir}/kde3/kcm_kmail.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kleopatra.so
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_application_octetstream.so
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_calendar.so
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_vcard.so
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_xdiff.so
%attr(755,root,root) %{_libdir}/kde3/libkmailpart.so*
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.sh
%{_datadir}/apps/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-signature.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-transport.pl
%{_datadir}/apps/kleopatra
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
%{_datadir}/apps/kwatchgnupg
%{_datadir}/apps/libkleopatra
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_datadir}/config/libkleopatrarc
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/services/kmail_config_accounts.desktop
%{_datadir}/services/kmail_config_appearance.desktop
%{_datadir}/services/kmail_config_composer.desktop
%{_datadir}/services/kmail_config_identity.desktop
%{_datadir}/services/kmail_config_misc.desktop
%{_datadir}/services/kmail_config_security.desktop
%{_datadir}/services/kleopatra_config_appear.desktop
%{_datadir}/services/kleopatra_config_dirserv.desktop
%{_datadir}/services/kleopatra_config_dnorder.desktop
%{_datadir}/servicetypes/dcopimap.desktop
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde/KMail.desktop
%{_desktopdir}/kde/kmail_view.desktop
# hidden (todo)
%{_desktopdir}/kde/kleopatra_import.desktop
%{_iconsdir}/*/*/apps/kmail.*
%{_iconsdir}/*/*/apps/kmailcvt.*
%{_iconsdir}/*/*/apps/kmaillight.*
# TODO
%{_iconsdir}/*/*/apps/gpg.png
%{_iconsdir}/*/*/apps/gpgsm.png
# kio-mbox
%attr(755,root,root) %{_libdir}/kde3/kio_mbox.so
%{_datadir}/services/mbox.protocol
# kio-sieve
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_datadir}/services/sieve.protocol
# ktnef
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%attr(755,root,root) %{_libdir}/kde3/kcm_knode.so
%attr(755,root,root) %{_libdir}/kde3/libknodepart.so*
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_datadir}/services/knode_config_accounts.desktop
%{_datadir}/services/knode_config_appearance.desktop
%{_datadir}/services/knode_config_cleanup.desktop
%{_datadir}/services/knode_config_identity.desktop
%{_datadir}/services/knode_config_post_news.desktop
%{_datadir}/services/knode_config_privacy.desktop
%{_datadir}/services/knode_config_read_news.desktop
%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%attr(755,root,root) %{_libdir}/kde3/knotes_kolab.so
%attr(755,root,root) %{_libdir}/kde3/knotes_local.so
%attr(755,root,root) %{_libdir}/kde3/knotes_xmlrpc.so
%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knoteconfig.kcfg
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%dir %{_datadir}/services/kresources/knotes
%{_datadir}/services/kresources/knotes/imap.desktop
%{_datadir}/services/kresources/knotes/local.desktop
%{_datadir}/services/kresources/knotes/knotes_xmlrpc.desktop
%{_datadir}/services/kresources/knotes/kolabresource.desktop
%{_datadir}/services/kresources/knotes_manager.desktop
%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png

%files konsolekalendar -f konsolekalendar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/kde/konsolekalendar.desktop
%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png

%files korn -f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_libdir}/kconf_update_bin/korn-3-4-config_change
%{_datadir}/apps/kconf_update/korn-*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/korn-3-5*.pl
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/kpilot*
%attr(755,root,root) %{_libdir}/kde3/conduit_address.so
%attr(755,root,root) %{_libdir}/kde3/conduit_doc.so
%attr(755,root,root) %{_libdir}/kde3/conduit_knotes.so
%attr(755,root,root) %{_libdir}/kde3/conduit_popmail.so
%attr(755,root,root) %{_libdir}/kde3/conduit_mal.so
%attr(755,root,root) %{_libdir}/kde3/conduit_sysinfo.so
%attr(755,root,root) %{_libdir}/kde3/conduit_time.so
%attr(755,root,root) %{_libdir}/kde3/conduit_todo.so
%attr(755,root,root) %{_libdir}/kde3/conduit_vcal.so
%attr(755,root,root) %{_libdir}/kde3/kcm_kpilot.so
%attr(755,root,root) %{_libdir}/kde3/kfile_palm.so
%{_datadir}/apps/kconf_update/kpalmdoc.upd
%{_datadir}/apps/kconf_update/kpilot.upd
%{_datadir}/apps/kpilot
%{_datadir}/config.kcfg/abbrowserconduit.kcfg
%{_datadir}/config.kcfg/docconduit.kcfg
%{_datadir}/config.kcfg/knotesconduit.kcfg
%{_datadir}/config.kcfg/kpalmdoc.kcfg
%{_datadir}/config.kcfg/kpilot.kcfg
%{_datadir}/config.kcfg/kpilotlib.kcfg
%{_datadir}/config.kcfg/malconduit.kcfg
%{_datadir}/config.kcfg/popmail.kcfg
%{_datadir}/config.kcfg/sysinfoconduit.kcfg
%{_datadir}/config.kcfg/timeconduit.kcfg
%{_datadir}/config.kcfg/vcalconduitbase.kcfg
%{_datadir}/services/kfile_palm.desktop
%{_datadir}/services/kpilot_config.desktop
%{_datadir}/services/*conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_desktopdir}/kde/kpalmdoc.desktop
%{_desktopdir}/kde/kpilot*.desktop
%{_iconsdir}/*/*/apps/kpalmdoc.png
%{_iconsdir}/[!l]*/*/*/kpilot*.png

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakregatorprivate.so
%attr(755,root,root) %{_libdir}/libindex.so.*.*.*
%attr(755,root,root) %{_libdir}/libgpgme++.so.*.*.*
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_groupdav.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_groupwise.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_newexchange.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_slox.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabckolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_groupdav.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_groupwise.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_newexchange.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_resourcefeatureplan.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_slox.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcal_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkcalkolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
%attr(755,root,root) %{_libdir}/libkgroupwarebase.so.*.*.*
%attr(755,root,root) %{_libdir}/libkgroupwaredav.so.*.*.*
%attr(755,root,root) %{_libdir}/libkholidays.so.*.*.*
%attr(755,root,root) %{_libdir}/libkitchensyncui.so.*.*.*
%attr(755,root,root) %{_libdir}/libkleopatra.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmailprivate.so
%attr(755,root,root) %{_libdir}/libkmime.so.*.*.*
%attr(755,root,root) %{_libdir}/libknodecommon.so
%attr(755,root,root) %{_libdir}/libknotes_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libknoteskolab.so.*.*.*
%attr(755,root,root) %{_libdir}/libkocorehelper.so.*.*.*
%attr(755,root,root) %{_libdir}/libkode.so.*.*.*
%attr(755,root,root) %{_libdir}/libkonnector.so.*.*.*
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpgp.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpimidentities.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
%attr(755,root,root) %{_libdir}/libkslox.so.*.*.*
%attr(755,root,root) %{_libdir}/libksync.so.*.*.*
%attr(755,root,root) %{_libdir}/libksync2.so.*.*.*
%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
%attr(755,root,root) %{_libdir}/libqgpgme.so.*.*.*
%attr(755,root,root) %{_libdir}/libmultisynk.so.*.*.*
%{_datadir}/apps/libical
%{_datadir}/apps/libkdepim
%{_datadir}/apps/libkholidays
