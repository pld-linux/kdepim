# TODO
# - subpackages for akregator, korganizer(?)
# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
%bcond_with	hidden_visibility	# pass '--fvisibility=hidden'
					# & '--fvisibility-inlines-hidden'
					# to g++ 
#
%define		_state		stable
%define		_kdever		3.5
%define		_ver		3.5.0

%define		_minlibsevr	9:3.5.0
%define		_minbaseevr	9:3.5.0

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - PIM (°³ÀÎ Á¤º¸ °ü¸®)
Summary(pl):	Manad¿er informacji osobistej (PIM) dla KDE
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË (PIM) ÄÌÑ KDE
Summary(uk):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË (PIM) ÄÌÑ KDE
Name:		kdepim
Version:	%{_ver}
Release:	7
Epoch:		9
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{_ver}.tar.bz2
# Source0-md5:	e19a2a40e422ecd483884ce6e9ac8925
Icon:		kde-pim.xpm
Patch100:	%{name}-branch.diff
Patch0:		kde-common-PLD.patch
Patch1:		%{name}-kmail_toolbars.patch
Patch2:		%{name}-alpha.patch
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bluez-libs-devel
BuildRequires:	cyrus-sasl-devel
BuildRequires:	docbook-dtd42-xml
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
%{?with_hidden_visibility:BuildRequires:	gcc-c++ >= 5:4.1.0-0.20051206r108118.1}
BuildRequires:	gpgme-devel >= 1:1.0.0
BuildRequires:	gnupg-agent
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libgnokii-devel
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	lockdev-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pilot-link-devel
%{?with_hidden_visibility:BuildRequires:	qt-devel >= 6:3.3.5.051113-1}
BuildRequires:	qt-designer-libs
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
BuildConflicts:	indexlib
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# subpackage akregator
Obsoletes:	akregator
Obsoletes:	kdeaddons-kontact
Obsoletes:	kdepim-kontact
Obsoletes:	kdepim-korganizer
Obsoletes:	kdepim-korganizer-libs
Obsoletes:	kdepim-kresources
Obsoletes:	kdepim-ksync
#Obsoletes:	kdeaddons-konqueror
#Obsoletes:	kdepim-libkcal
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%description -l ru
kdepim - ÜÔÏ ÎÁÂÏÒ ÕÔÉÌÉÔ ÄÌÑ ÕÐÒÁ×ÌÅÎÉÑ ÐÅÒÓÏÎÁÌØÎÏÊ ÉÎÆÏÒÍÁÃÉÅÊ ÄÌÑ
K Desktop Environment (KDE).

%description -l uk
kdepim - ÃÅ ÎÁÂ¦Ò ÕÔÉÌ¦Ô ÄÌÑ ËÅÒÕ×ÁÎÎÑ ÐÅÒÓÏÎÁÌØÎÏÀ ÉÎÆÏÒÍÁÃ¦¤À ÄÌÑ K
Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag³ówkowe do KDE pim
Summary(uk):	æÁÊÌÉ ÒÏÚÒÏÂËÉ ÄÌÑ kdepim
Summary(ru):	æÁÊÌÙ ÒÁÚÒÁÂÏÔËÉ ÄÌÑ kdepim
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= %{_minlibsevr}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Conflicts:	kdenetwork-devel < 10:3.1.90
Obsoletes:	indexlib-devel
Obsoletes:	kdepim-libkcal-devel

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
Dokumentacja interfejsów programowania libkdepim, libkdenetwork,
libkmailprivate, libknodecommon i innych z kdepim wraz z przypisami:
- listy klas i ich sk³adników
- listê przestrzeni nazw (namespace)

%package -n kde-kio-groupwise
Summary:	Groupwise protocol service
Summary(pl):	Obs³uga protoko³u Groupwise
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description -n kde-kio-groupwise
Groupwise protocol service.

%description -n kde-kio-groupwise -l pl
Obs³uga protoko³u Groupwise.

%package -n kde-kio-imap4
Summary:	IMAP4 protocol service
Summary(pl):	Obs³uga protoko³u IMAP4
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kde-kio-newimap4 < 9:3.4.0

%description -n kde-kio-imap4
IMAP4 protocol service.

%description -n kde-kio-imap4 -l pl
Obs³uga protoko³u IMAP4.

%package kaddressbook
Summary:	Address book
Summary(pl):	Ksi±¿ka adresowa
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description kaddressbook
The KDE address book.

%description kaddressbook -l pl
Ksi±¿ka adresowa dla KDE.

%package kalarm
Summary:	A personal alarm scheduler
Summary(pl):	Osobisty program do przypominania
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description kalarm
KAlarm is a personal alarm message, command and email scheduler. It
lets you set up personal alarm messages which pop up on the screen at
the chosen time, or you can schedule commands to be executed or emails
to be sent. Also includes an alarm daemon.

%description kalarm -l pl
KAlarm to osobisty program do planowania i przypominania poprzez
uruchomienie polecenia lub poczt± elektroniczn±. Umo¿liwia ustawienie
w³asnej wiadomo¶ci alarmowej, która wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie poleceñ do wykonania lub poczty do
wys³ania. Zawiera tak¿e demona obs³uguj±cego przypominanie.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl):	Program do komunikacji miêdzy PC a tel. komórkowym
Group:		X11/Applications
Requires:	kdebase-core >= %{_minlibsevr}
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo¿liwia dostêp do telefonu komórkowego i pozwala na
synchronizacjê danych z telefonu z danymi na PC.

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
KArm (nazwa pochodzi od s³owa "praca" w jêzyku punjambi) ¶ledzi czas
spêdzony na ró¿nych zajêciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunków wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
URL:		http://kmail.kde.org/
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	kde-kio-imap4 >= %{epoch}:%{version}-%{release}
Requires:	kde-kio-pop3 >= %{_minbaseevr}
Requires:	kde-kio-smtp >= %{_minbaseevr}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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
Program pocztowy dla KDE o olbrzymich mo¿liwo¶ciach, obejmuj±cych:
- obs³ugê SMTP/maildir/POP3/IMAP z SSL/TLS i pipeliningiem
- ksi±¿kê adresow±
- automatyczne szyfrowanie przy u¿yciu OpenPGP (PGP lub GnuPG)
- potê¿ne filtry pocztowe
- zagnie¿d¿one skrzynki pocztowe z obs³ug± list pocztowych
- ¶ci±ganie na ¿±danie lub usuwanie bez ¶ci±gania du¿ych listów z
  serwera POP3
- pe³n± obs³ugê listów we wszystkich jêzykach i zestawach znaków
  obs³ugiwanych przez Qt
- przeszukiwanie wiadomo¶ci z prezentacj± w wirtualnych folderach
- usuwanie powtórzonych listów
- w±tkowanie wiadomo¶ci
- kontrolê pisowni w locie
- import poczty z innych klientów
- wiele wiêcej...

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik newsów dla KDE
Summary(pt_BR):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	kde-kio-nntp >= %{_minbaseevr}
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
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
KNode to czytnik newsów zgodny ze specyfikacj± GKNSA przeznaczony dla
¶rodowiska KDE. Jego mo¿liwo¶ci obejmuj±:
- wszystkie podstawowe cechy czytnika newsów (czytanie i wysy³anie
  artyku³ów, w±tkowanie...)
- obs³ugê wielu serwerów news
- czytanie i tworzenie wieloczê¶ciowych wiadomo¶ci MIME
- wy¶wietlanie za³±czników w tek¶cie (tekstowych i obrazków)
- konfigurowalne filtry, fonty i kolory
- pe³ny scoring
- wiele wiêcej...

%description knode -l pt_BR
Leitor de notícias (news) do KDE.

%package knotes
Summary:	Yellow cards
Summary(pl):	¯ó³te karteczki
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszczaæ na pulpicie notatki z opcj± wysy³ania.
Dodatkowo, aby móc s³u¿yæ za przypominajkê, KNotes mo¿e wysy³aæ pocztê
i drukowaæ notatki, a tak¿e przyjmowaæ przeci±ganie nawet ze zdalnych
komputerów.

%package konsolekalendar
Summary:	A command line ICard tool
Summary(pl):	Narzêdzie dostêpu do plików kalendarza z linii poleceñ
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
KonsoleKalendar to dzia³aj±cy z linii poleceñ interfejs do kalendarzy
KDE. Pozwala ogl±daæ, wstawiaæ, usuwaæ i modyfikowaæ zdarzenia w
kalendarzu z linii poleceñ lub jêzyka skryptowego. Ponadto
KonsoleKalendar potrafi wyeksportowaæ kalendarz KDE do wielu innych
formatów.

G³ówne mo¿liwo¶ci programu KonsoleKalendar:
- wypisywanie wpisów kalendarza od daty pocz±tkowej do koñcowej
- wstawianie/usuwanie/modyfikowanie wpisów
- eksportowanie wpisów kalendarza do innych formatów plików.

Narzêdzie dostêpu do plików kalendarza z linii poleceñ.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska¼nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdebase-desktop >= %{_minbaseevr}
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj±cy liczbê wiadomo¶ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitoração da caixa de correio.

%package kpilot
Summary:	A sync tool for palmtops
Summary(pl):	Narzêdzie do synchronizacji z palmtopami
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
- Sony Clié series (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c,
  T675c, 665c)
- and Garmin iQue 3600
- others might work, but have not been tested

%description kpilot -l pl
KPilot to odpowiednik oprogramowania Palm Desktop firmy Palm Inc,
umo¿liwiaj±cy wymianê informacji miêdzy urz±dzeniami Palm, Palm Pilot
i Visor a komputerem z KDE. KPilot jako taki nie zastêpuje Palm
Desktop - ³±czy i integruje wiele aplikacji KDE 3.x w pakiet, którym
mo¿na zrobiæ tyle samo, a nawet wiêcej, co przy u¿yciu Palm Desktop.

KPilot ma wtyczki do wymiany informacji miêdzy Palmem a innymi
aplikacjami, takimi jak KOrganizer albo serwery POP3/SMTP. W KPilocie
mo¿na wy¶wietlaæ i modyfikowaæ kontakty, pisaæ notatki lub instalowaæ
nowe programy na Palmie.

Obs³uguje urz±dzenia serii:
- Palm Pilot, m100, m500, Zire, Tungsten
- Handspring Visor i Treo
- Sony Clié (TJ35/E1, TJ25, T415, SJ120/333, S300, T625c, T675c, 665c)
- Garmin iQue 3600
- mog± dzia³aæ tak¿e inne, ale nie by³y testowane.

%description kpilot -l ru
ÕÔÉÌÉÔÁ ÄÌÑ ÓÉÎÈÒÏÎÉÚÁÃÉÉ Ó 3com Palm Pilots É ÓÏ×ÍÅÓÔÉÍÙÍÉ Ó ÎÉÍÉ
ÕÓÔÒÏÊÓÔ×ÁÍÉ,

%description kpilot -l uk
ÕÔÉÌ¦ÔÁ ÄÌÑ ÓÉÎÈÒÏÎ¦ÚÁÃ¦§ Ú 3com Palm Pilots ÔÁ ÓÕÍ¦ÓÎÉÍÉ Ú ÎÉÍÉ
ÐÒÉÓÔÒÏÑÍÉ.

%package libs
Summary:	Shared kdepim libraries
Summary(pl):	Wspó³dzielone biblioteki kdepim
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
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
Provides:	kdepim-libkdenetwork = %{epoch}:%{version}-%{release}
Provides:	kdepim-libkdepim = %{epoch}:%{version}-%{release}
Provides:	kdepim-kmail-libs = %{epoch}:%{version}-%{release}
Conflicts:	akregator < 3.4.0

%description libs
Libraries shared between PIM applications in KDE, which include:
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib and more

%description libs -l pl
Biblioteki wspó³dzielone pomiêdzy aplikacjami PIM w KDE, m.in.
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib.

%prep
%setup -q
%patch100 -p0
%patch0 -p1
#%patch1 -p1
%patch2 -p1

%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Calendar;/' \
	-e 's/Terminal=0/Terminal=false/' \
	korganizer/korganizer.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kpilot/kpilot/kpilotdaemon.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kpilot/kpilot/kpilot.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kpilot/conduits/docconduit/kpalmdoc.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;ContactManagement;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kaddressbook/kaddressbook.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;X-PIM;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kontact/src/Kontact.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Email;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kmail/KMail.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Network;News;/' \
	-e 's/Terminal=0/Terminal=false/' \
	knode/KNode.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	kmobile/kmobile.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
	-e 's/Terminal=0/Terminal=false/' \
	kandy/src/kandy.desktop
%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Applet;/' \
	knotes/knotes.desktop
%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
	karm/support/karm.desktop \
	knotes/knotes.desktop \
	konsolekalendar/konsolekalendar.desktop \
	korn/KOrn.desktop
%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
	-e 's/Terminal=0/Terminal=false/' \
	ktnef/gui/ktnef.desktop
for f in `find . -name \*.desktop`; do
	if grep -q '^Categories=.*[^;]$' $f; then
		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
	fi
	if grep -q '\[ven\]' $f; then
		sed -i -e 's/\[ven\]/[ve]/' $f
	fi
done

# change annoyance-filter path (required by autodetect in kmail)
%{__sed} -i -e 's,\($HOME/\.annoyance-filter/annoyance-filter\)\(.*\),annoyance-filter\2,g' \
	kmail/kmail.antispamrc
cp %{_datadir}/automake/config.sub admin
#export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%build
%configure \
	--%{?debug:en}%{!?debug:dis}able-debug%{?debug:=full} \
	%{!?debug:--disable-rpath} \
%ifnarch alpha
	--enable-final \
%endif
	%{?with_hidden_visibility:--enable-gcc-hidden-visibility} \
	--enable-indexlib \
%if "%{_lib}" == "lib64"
	--enable-libsuffix=64 \
%endif
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
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian/man
if [ -f alarmd.sgml ]; then
	%{__sed} -i -e 's/alarmd/kalarmd/' -e 's/ALARMD/KALARMD/' alarmd.sgml
	mv -f alarmd.sgml kalarmd.sgml
fi
for f in *.man ; do
	base="$(basename $f .man)"
	install ${base}.man $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done
cd -

%find_lang	akregator	--with-kde
%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
#%find_lang	kalarmd		--with-kde
#cat kalarmd.lang >> kalarm.lang
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
#cat kalarmd.lang	>> %{name}.lang
# TODO
cat multisynk.lang	>> %{name}.lang

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

# remove checked files
rm $RPM_BUILD_ROOT%{_datadir}/applnk/{Applications/kalarm,Utilities/{kandy,karm,kmailcvt}}.desktop
rm $RPM_BUILD_ROOT%{_iconsdir}/locolor/{16x16/apps/{kpilot,ktnef},32x32/apps/ktnef}.png

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

%{_libdir}/libkabckonnector.la
%attr(755,root,root) %{_libdir}/libkabckonnector.so
%{_libdir}/libkcalkonnector.la
%attr(755,root,root) %{_libdir}/libkcalkonnector.so
%{_libdir}/liblocalkonnector.la
%attr(755,root,root) %{_libdir}/liblocalkonnector.so
%{_libdir}/libqtopiakonnector.la
%attr(755,root,root) %{_libdir}/libqtopiakonnector.so
%{_libdir}/libremotekonnector.la
%attr(755,root,root) %{_libdir}/libremotekonnector.so

%{_libdir}/kde3/conduit_memofile.la
%attr(755,root,root) %{_libdir}/kde3/conduit_memofile.so
%{_libdir}/kde3/conduit_notepad.la
%attr(755,root,root) %{_libdir}/kde3/conduit_notepad.so
%{_libdir}/kde3/kabc_groupdav.la
%attr(755,root,root) %{_libdir}/kde3/kabc_groupdav.so
%{_libdir}/kde3/kabc_groupwise.la
%attr(755,root,root) %{_libdir}/kde3/kabc_groupwise.so
%{_libdir}/kde3/kabc_kolab.la
%attr(755,root,root) %{_libdir}/kde3/kabc_kolab.so
%{_libdir}/kde3/kabc_newexchange.la
%attr(755,root,root) %{_libdir}/kde3/kabc_newexchange.so
%{_libdir}/kde3/kabc_slox.la
%attr(755,root,root) %{_libdir}/kde3/kabc_slox.so
%{_libdir}/kde3/kabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kabc_xmlrpc.so
%{_libdir}/kde3/kcal_blogging.la
%attr(755,root,root) %{_libdir}/kde3/kcal_blogging.so
%{_libdir}/kde3/kcal_groupdav.la
%attr(755,root,root) %{_libdir}/kde3/kcal_groupdav.so
%{_libdir}/kde3/kcal_groupwise.la
%attr(755,root,root) %{_libdir}/kde3/kcal_groupwise.so
%{_libdir}/kde3/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%{_libdir}/kde3/kcal_kolab.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kolab.so
%{_libdir}/kde3/kcal_local.la
%attr(755,root,root) %{_libdir}/kde3/kcal_local.so
%{_libdir}/kde3/kcal_localdir.la
%attr(755,root,root) %{_libdir}/kde3/kcal_localdir.so
%{_libdir}/kde3/kcal_newexchange.la
%attr(755,root,root) %{_libdir}/kde3/kcal_newexchange.so
%{_libdir}/kde3/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%{_libdir}/kde3/kcal_resourcefeatureplan.la
%attr(755,root,root) %{_libdir}/kde3/kcal_resourcefeatureplan.so
%{_libdir}/kde3/kcal_slox.la
%attr(755,root,root) %{_libdir}/kde3/kcal_slox.so
%{_libdir}/kde3/kcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_xmlrpc.so
#%{_libdir}/kde3/kcm_kabsummary.la
#%attr(755,root,root) %{_libdir}/kde3/kcm_kabsummary.so
%{_libdir}/kde3/kcm_kmailsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmailsummary.so
%{_libdir}/kde3/kcm_kontact.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontact.so
%{_libdir}/kde3/kcm_kontactknt.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactknt.so
%{_libdir}/kde3/kcm_kontactsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactsummary.so
%{_libdir}/kde3/kcm_korganizer.la
%attr(755,root,root) %{_libdir}/kde3/kcm_korganizer.so
%{_libdir}/kde3/kcm_korgsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_korgsummary.so
%{_libdir}/kde3/kcm_sdsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_sdsummary.so
%{_libdir}/kde3/kded_networkstatus.la
%attr(755,root,root) %{_libdir}/kde3/kded_networkstatus.so
%{_libdir}/kde3/kfile_ics.la
%attr(755,root,root) %{_libdir}/kde3/kfile_ics.so
%{_libdir}/kde3/libakregatorpart.la
%attr(755,root,root) %{_libdir}/kde3/libakregatorpart.so*
#%{_libdir}/kde3/libkded_ksharedfile.la
#%attr(755,root,root) %{_libdir}/kde3/libkded_ksharedfile.so
%{_libdir}/kde3/libexchangewizard.la
%attr(755,root,root) %{_libdir}/kde3/libexchangewizard.so
%{_libdir}/kde3/libgroupwisewizard.la
%attr(755,root,root) %{_libdir}/kde3/libgroupwisewizard.so*
%{_libdir}/kde3/libakregator_mk4storage_plugin.la
%attr(755,root,root) %{_libdir}/kde3/libakregator_mk4storage_plugin.so
%{_libdir}/kde3/libkitchensyncpart.la
%attr(755,root,root) %{_libdir}/kde3/libkitchensyncpart.so
%{_libdir}/kde3/libkontact_akregator.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_akregator.so
%{_libdir}/kde3/libkontact_journalplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_journalplugin.so
%{_libdir}/kde3/libkontact_kaddressbookplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kaddressbookplugin.so
%{_libdir}/kde3/libkontact_karm.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_karm.so
%{_libdir}/kde3/libkontact_kmailplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmailplugin.so
%{_libdir}/kde3/libkontact_knodeplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knodeplugin.so
%{_libdir}/kde3/libkontact_knotesplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knotesplugin.so
%{_libdir}/kde3/libkontact_korganizerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_korganizerplugin.so
%{_libdir}/kde3/libkontact_todoplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_todoplugin.so
%{_libdir}/kde3/libkontact_kpilotplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kpilotplugin.so
%{_libdir}/kde3/libkontact_multisynk.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_multisynk.so
%{_libdir}/kde3/libkontact_newstickerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_newstickerplugin.so
%{_libdir}/kde3/libkontact_specialdatesplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_specialdatesplugin.so
%{_libdir}/kde3/libkontact_summaryplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_summaryplugin.so
%{_libdir}/kde3/libkontact_weatherplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_weatherplugin.so
%{_libdir}/kde3/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%{_libdir}/kde3/libkorganizerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkorganizerpart.so
%{_libdir}/kde3/libksfilter_addressbook.la
%attr(755,root,root) %{_libdir}/kde3/libksfilter_addressbook.so
%{_libdir}/kde3/libksfilter_calendar.la
%attr(755,root,root) %{_libdir}/kde3/libksfilter_calendar.so
%{_libdir}/kde3/libksync_backup.la
%attr(755,root,root) %{_libdir}/kde3/libksync_backup.so
%{_libdir}/kde3/libksync_debugger.la
%attr(755,root,root) %{_libdir}/kde3/libksync_debugger.so
%{_libdir}/kde3/libksync_pluckerpart.la
%attr(755,root,root) %{_libdir}/kde3/libksync_pluckerpart.so
%{_libdir}/kde3/libksync_restore.la
%attr(755,root,root) %{_libdir}/kde3/libksync_restore.so
%{_libdir}/kde3/libksync_syncerpart.la
%attr(755,root,root) %{_libdir}/kde3/libksync_syncerpart.so
%{_libdir}/kde3/libksync_viewer.la
%attr(755,root,root) %{_libdir}/kde3/libksync_viewer.so
%{_libdir}/kde3/libmultisynkpart.la
%attr(755,root,root) %{_libdir}/kde3/libmultisynkpart.so
%{_libdir}/kde3/liboverviewpart.la
%attr(755,root,root) %{_libdir}/kde3/liboverviewpart.so
%{_libdir}/kde3/libegroupwarewizard.la
%attr(755,root,root) %{_libdir}/kde3/libegroupwarewizard.so*
%{_libdir}/kde3/libkolabwizard.la
%attr(755,root,root) %{_libdir}/kde3/libkolabwizard.so*
%{_libdir}/kde3/libsloxwizard.la
%attr(755,root,root) %{_libdir}/kde3/libsloxwizard.so*
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_libdir}/kde3/plugins/designer/kdepimwidgets.la
%attr(755,root,root) %{_libdir}/kde3/plugins/designer/kdepimwidgets.so
%{_libdir}/kde3/plugins/designer/kpartsdesignerplugin.la
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
%{_datadir}/apps/multisynk
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/egroupware.kcfg
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config.kcfg/memofileconduit.kcfg
%{_datadir}/config.kcfg/mk4config.kcfg
%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/slox.kcfg
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
#
%{_iconsdir}/crystalsvg/22x22/actions/button_fewer.png
%{_iconsdir}/crystalsvg/22x22/actions/button_more.png
#
%{_mandir}/man1/akregator.1*
%{_mandir}/man1/ical2vcal.1*
%{_mandir}/man1/kdeopt*.1*
%{_mandir}/man1/kitchensync*.1*
%{_mandir}/man1/korga*.1*
%exclude %{_mandir}/man1/korganizerIn.1*
%{_mandir}/man1/kontact*.1*
%{_mandir}/man1/ksync*.1*
%{_mandir}/man1/*wizard.1*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/indexlib-config
%{_includedir}/KNotesIface.h
%{_includedir}/KNotesAppIface.h
%{_includedir}/kdepimmacros.h
#%{_includedir}/ksharedfile.h
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
#%{_includedir}/libkdepim
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
%{_libdir}/libkcal_blogging.so
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
#%{_libdir}/libksharedfile.so
%{_libdir}/libksieve.so
%{_libdir}/libksync.so
%{_libdir}/libksync2.so
%{_libdir}/libktnef.so
%{_libdir}/libmimelib.so
%{_libdir}/libqgpgme.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}-apidocs
%endif

%files -n kde-kio-imap4
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_imap4.la
%attr(755,root,root) %{_libdir}/kde3/kio_imap4.so
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol

%files -n kde-kio-groupwise
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_groupwise.la
%attr(755,root,root) %{_libdir}/kde3/kio_groupwise.so
%{_datadir}/config.kcfg/groupwise.kcfg
%{_datadir}/services/groupwise.protocol
%{_datadir}/services/groupwises.protocol

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde3/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%{_libdir}/kde3/kcm_kabcustomfields.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabcustomfields.so
%{_libdir}/kde3/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_libdir}/kde3/ldifvcardthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/ldifvcardthumbnail.so
%{_libdir}/kde3/libkaddrbk_cardview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cardview.so
%{_libdir}/kde3/libkaddrbk_cryptosettings.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cryptosettings.so
%{_libdir}/kde3/libkaddrbk_distributionlist.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_distributionlist.so
%{_libdir}/kde3/libkaddrbk_iconview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_iconview.so
%{_libdir}/kde3/libkaddrbk_resourceselection.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_resourceselection.so
%{_libdir}/kde3/libkaddrbk_tableview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_tableview.so
%{_libdir}/kde3/libkaddrbk_*_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_*_xxport.so
%{_libdir}/kde3/libkaddressbookpart.la
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
%{_mandir}/man1/kaddressbook*.1*
%{_mandir}/man1/kabc2mutt*.1*

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*.desktop
%{_desktopdir}/kde/kalarm.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
%{_mandir}/man1/kalarm*.1*

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop
%{_mandir}/man1/kandy*.1*

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_libdir}/kde3/libkarmpart.la
%attr(755,root,root) %{_libdir}/kde3/libkarmpart.so
%{_datadir}/apps/karm
%{_datadir}/apps/karmpart
%{_datadir}/services/karm_part.desktop
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png
%{_mandir}/man1/karm*.1*

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
%{_libdir}/kde3/kcm_kmail.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmail.so
%{_libdir}/kde3/kcm_kleopatra.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kleopatra.so
%{_libdir}/kde3/libkmail_bodypartformatter_application_octetstream.la
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_application_octetstream.so
%{_libdir}/kde3/libkmail_bodypartformatter_text_calendar.la
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_calendar.so
%{_libdir}/kde3/libkmail_bodypartformatter_text_vcard.la
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_vcard.so
%{_libdir}/kde3/libkmail_bodypartformatter_text_xdiff.la
%attr(755,root,root) %{_libdir}/kde3/libkmail_bodypartformatter_text_xdiff.so
%{_libdir}/kde3/libkmailpart.la
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
%{_libdir}/kde3/kio_mbox.la
%attr(755,root,root) %{_libdir}/kde3/kio_mbox.so
%{_datadir}/services/mbox.protocol
# kio-sieve
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_datadir}/services/sieve.protocol
%{_mandir}/man1/kmail*.1*
%{_mandir}/man1/kwatchgnupg*.1*
%{_mandir}/man1/kleopatra*.1*
%{_mandir}/man1/korganizerIn.1*
# ktnef
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png
%{_mandir}/man1/ktnef*.1*

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_libdir}/kde3/kcm_knode.la
%attr(755,root,root) %{_libdir}/kde3/kcm_knode.so
%{_libdir}/kde3/libknodepart.la
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
%{_mandir}/man1/knode*.1*

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_libdir}/kde3/knotes_kolab.la
%attr(755,root,root) %{_libdir}/kde3/knotes_kolab.so
%{_libdir}/kde3/knotes_local.la
%attr(755,root,root) %{_libdir}/kde3/knotes_local.so
%{_libdir}/kde3/knotes_xmlrpc.la
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
%{_mandir}/man1/knotes*.1*

%files konsolekalendar -f konsolekalendar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/kde/konsolekalendar.desktop
%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png
%{_mandir}/man1/konsolekalendar*.1*

%files korn -f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_libdir}/kconf_update_bin/korn-3-4-config_change
%{_datadir}/apps/kconf_update/korn-*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/korn-3-5*.pl
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png
%{_mandir}/man1/korn*.1*

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/kde3/conduit_address.la
%attr(755,root,root) %{_libdir}/kde3/conduit_address.so
%{_libdir}/kde3/conduit_doc.la
%attr(755,root,root) %{_libdir}/kde3/conduit_doc.so
%{_libdir}/kde3/conduit_knotes.la
%attr(755,root,root) %{_libdir}/kde3/conduit_knotes.so
%{_libdir}/kde3/conduit_popmail.la
%attr(755,root,root) %{_libdir}/kde3/conduit_popmail.so
%{_libdir}/kde3/conduit_mal.la
%attr(755,root,root) %{_libdir}/kde3/conduit_mal.so
%{_libdir}/kde3/conduit_sysinfo.la
%attr(755,root,root) %{_libdir}/kde3/conduit_sysinfo.so
%{_libdir}/kde3/conduit_time.la
%attr(755,root,root) %{_libdir}/kde3/conduit_time.so
%{_libdir}/kde3/conduit_todo.la
%attr(755,root,root) %{_libdir}/kde3/conduit_todo.so
%{_libdir}/kde3/conduit_vcal.la
%attr(755,root,root) %{_libdir}/kde3/conduit_vcal.so
%{_libdir}/kde3/kcm_kpilot.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kpilot.so
%{_libdir}/kde3/kfile_palm.la
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
%{_mandir}/man1/kpilot*.1*
%{_mandir}/man1/kpalm*.1*

%files libs
%defattr(644,root,root,755)
%{_libdir}/libakregatorprivate.la
%attr(755,root,root) %{_libdir}/libakregatorprivate.so
%{_libdir}/libindex.la
%attr(755,root,root) %{_libdir}/libindex.so.*.*.*
%{_libdir}/libgpgme++.la
%attr(755,root,root) %{_libdir}/libgpgme++.so.*.*.*
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%{_libdir}/libkabc_groupdav.la
%attr(755,root,root) %{_libdir}/libkabc_groupdav.so.*.*.*
%{_libdir}/libkabc_groupwise.la
%attr(755,root,root) %{_libdir}/libkabc_groupwise.so.*.*.*
%{_libdir}/libkabc_newexchange.la
%attr(755,root,root) %{_libdir}/libkabc_newexchange.so.*.*.*
%{_libdir}/libkabc_slox.la
%attr(755,root,root) %{_libdir}/libkabc_slox.so.*.*.*
%{_libdir}/libkabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%{_libdir}/libkabckolab.la
%attr(755,root,root) %{_libdir}/libkabckolab.so.*.*.*
%{_libdir}/libkabinterfaces.la
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*
%{_libdir}/libkcal.la
%attr(755,root,root) %{_libdir}/libkcal.so.*.*.*
%{_libdir}/libkcal_blogging.la
%attr(755,root,root) %{_libdir}/libkcal_blogging.so.*.*.*
%{_libdir}/libkcal_groupdav.la
%attr(755,root,root) %{_libdir}/libkcal_groupdav.so.*.*.*
%{_libdir}/libkcal_groupwise.la
%attr(755,root,root) %{_libdir}/libkcal_groupwise.so.*.*.*
%{_libdir}/libkcal_newexchange.la
%attr(755,root,root) %{_libdir}/libkcal_newexchange.so.*.*.*
%{_libdir}/libkcal_resourcefeatureplan.la
%attr(755,root,root) %{_libdir}/libkcal_resourcefeatureplan.so.*.*.*
%{_libdir}/libkcal_resourceremote.la
%attr(755,root,root) %{_libdir}/libkcal_resourceremote.so.*.*.*
%{_libdir}/libkcal_slox.la
%attr(755,root,root) %{_libdir}/libkcal_slox.so.*.*.*
%{_libdir}/libkcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/libkcal_xmlrpc.so.*.*.*
%{_libdir}/libkcalkolab.la
%attr(755,root,root) %{_libdir}/libkcalkolab.so.*.*.*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
%{_libdir}/libkgroupwarebase.la
%attr(755,root,root) %{_libdir}/libkgroupwarebase.so.*.*.*
%{_libdir}/libkgroupwaredav.la
%attr(755,root,root) %{_libdir}/libkgroupwaredav.so.*.*.*
%{_libdir}/libkholidays.la
%attr(755,root,root) %{_libdir}/libkholidays.so.*.*.*
%{_libdir}/libkitchensyncui.la
%attr(755,root,root) %{_libdir}/libkitchensyncui.so.*.*.*
%{_libdir}/libkleopatra.la
%attr(755,root,root) %{_libdir}/libkleopatra.so.*.*.*
%{_libdir}/libkmailprivate.la
%attr(755,root,root) %{_libdir}/libkmailprivate.so
%{_libdir}/libkmime.la
%attr(755,root,root) %{_libdir}/libkmime.so.*.*.*
%{_libdir}/libknodecommon.la
%attr(755,root,root) %{_libdir}/libknodecommon.so
%{_libdir}/libknotes_xmlrpc.la
%attr(755,root,root) %{_libdir}/libknotes_xmlrpc.so.*.*.*
%{_libdir}/libknoteskolab.la
%attr(755,root,root) %{_libdir}/libknoteskolab.so.*.*.*
%{_libdir}/libkocorehelper.la
%attr(755,root,root) %{_libdir}/libkocorehelper.so.*.*.*
%{_libdir}/libkode.la
%attr(755,root,root) %{_libdir}/libkode.so.*.*.*
%{_libdir}/libkonnector.la
%attr(755,root,root) %{_libdir}/libkonnector.so.*.*.*
%{_libdir}/libkontact.la
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%{_libdir}/libkorg_stdprinting.la
%attr(755,root,root) %{_libdir}/libkorg_stdprinting.so.*.*.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%{_libdir}/libkorganizer_calendar.la
%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so.*.*.*
%{_libdir}/libkorganizer_eventviewer.la
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%{_libdir}/libkpgp.la
%attr(755,root,root) %{_libdir}/libkpgp.so.*.*.*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
%{_libdir}/libkpimidentities.la
%attr(755,root,root) %{_libdir}/libkpimidentities.so.*.*.*
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
#%{_libdir}/libksharedfile.la
#%attr(755,root,root) %{_libdir}/libksharedfile.so.*.*.*
%{_libdir}/libksieve.la
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
%{_libdir}/libkslox.la
%attr(755,root,root) %{_libdir}/libkslox.so.*.*.*
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*.*.*
%{_libdir}/libksync2.la
%attr(755,root,root) %{_libdir}/libksync2.so.*.*.*
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
%{_libdir}/libqgpgme.la
%attr(755,root,root) %{_libdir}/libqgpgme.so.*.*.*
%{_libdir}/libmultisynk.la
%attr(755,root,root) %{_libdir}/libmultisynk.so.*.*.*
%{_datadir}/apps/libical
%{_datadir}/apps/libkdepim
%{_datadir}/apps/libkholidays
