%define		_state		stable
%define		_ver		3.2.3

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - PIM (°³ÀÎ Á¤º¸ °ü¸®)
Summary(pl):	Manad¿er informacji osobistej (PIM) dla KDE
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË (PIM) ÄÌÑ KDE
Summary(uk):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË (PIM) ÄÌÑ KDE
Name:		kdepim
Version:	%{_ver}
Release:	0.2
Epoch:		3
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	http://download.kde.org/%{_state}/%{_ver}/src/%{name}-%{_ver}.tar.bz2
Source0:	http://ep09.pld-linux.org/~djurban/kde/%{name}-%{version}.tar.bz2
# Source0-md5:	10249b56cbc4c67dc4093b9f968604b9
Patch100:	%{name}-branch.diff
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	automake
BuildRequires:	unsermake >= 040511
BuildRequires:	bison
BuildRequires:	docbook-dtd41-sgml
BuildRequires:	docbook-utils
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	pilot-link-devel
BuildRequires:	pcre-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildConflicts:	kdepim-mimelib
BuildConflicts:	kdepim-libkcal
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-korganizer-libs
BuildConflicts:	kdepim-kaddressbook-libs
BuildConflicts:	kdepim-libksieve
BuildConflicts:	kdepim-libktnef
BuildConflicts:	kdepim-ktnef
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
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-kaddressbook-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kontact-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-korganizer-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkmailprivate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-devel < 10:3.1.90

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

%package kaddressbook
Summary:	Address book
Summary(pl):	Ksi±¿ka adresowa
Group:		X11/Applications
Requires:	kdelibs >= 9:%{version}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

%description kaddressbook
The KDE address book.

%description kaddressbook -l pl
Ksi±¿ka adresowa dla KDE.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl):	Program do komunikacji miêdzy PC a tel. komórkowym
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-libkmailprivate = %{epoch}:%{version}-%{release}
Requires:	kdebase-mailnews >= 9:%{version}
Obsoletes:	kdenetwork-kmail
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
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}
Requires:	kdebase-mailnews >= 9:%{version}
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
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

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
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

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

%package kontact
Summary:	An integrated shell for the PIM apps
Summary(pl):	Zintegrowany system aplikacji PIM
Group:		X11/Applications
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-kaplan

%description kontact
An integrated workplace for the KDE PIM apps.

%description kontact -l pl
Zintegrowane biurko dla aplikacji PIM w KDE.

%package korganizer
Summary:	A complete calendar and scheduling program
Summary(pl):	Kalendarz wraz z harmonogramem zadañ
Group:		X11/Applications
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	kdebase-core >= 9:%{version}
Obsoletes:	kdepim-kalarm
Obsoletes:	kdepim-kgantt
Obsoletes:	kdepim-kitchensync
Obsoletes:	kdepim-ksync
Obsoletes:	korganizer

%description korganizer
A complete calendar and scheduling program, which supports information
interchange with other calendar applications through the industry
standard vCalendar and iCalendar file format.

%description korganizer -l pl
Kalendarz wraz z harmonogramem zadañ (KOrganizer), który wspiera
wymianê informacji z innymi tego typu aplikacjami poprzez standard
przemys³owy (vCalendar i iCalendar).

%description korganizer -l ru
ÐÏÌÎÏÆÕÎËÃÉÏÎÁÌØÎÁÑ ÐÒÏÇÒÁÍÍÁ ËÁÌÅÎÄÁÒÑ É ÐÅÒÓÏÎÁÌØÎÏÇÏ ÐÌÁÎÉÒÏ×ÝÉËÁ
(KOrganizer ÐÏÄÄÅÒÖÉ×ÁÅÔ ÏÂÍÅÎ ÉÎÆÏÒÍÁÃÉÅÊ Ó ÄÒÕÇÉÍÉ ÐÒÏÇÒÁÍÍÁÍÉ
ÔÁËÏÇÏ ÒÏÄÁ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÙÊ ÆÏÒÍÁÔ ÆÁÊÌÁ vCalendar)

%description korganizer -l uk
ÐÏ×ÎÏÆÕÎËÃ¦ÏÎÁÌØÎÁ ÐÒÏÇÒÁÍÁ ËÁÌÅÎÄÁÒÁ ÔÁ ÐÅÒÓÏÎÁÌØÎÏÇÏ ÐÌÁÎÕ×ÁÌØÎÉËÁ
(KOrganizer Ð¦ÄÔÒÉÍÕ¤ ÏÂÍ¦Î ÉÎÆÏÒÍÁÃ¦¤À Ú ¦ÎÛÉÍÉ ÐÒÏÇÒÁÍÁÍÉ ÔÁËÏÇÏ
ÒÏÄÕ ÞÅÒÅÚ ÓÔÁÎÄÁÒÔÎÉÊ ÆÏÒÍÁÔ ÆÁÊÌÕ vCalendar)

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska¼nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdebase-desktop >= 9:%{version}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}
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

%package libkdenetwork
Summary:	Network libraries
Summary(pl):	Biblioteki sieciowa
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdenetwork
Obsoletes:	kdepim-libmimelib

%description libkdenetwork
Libraries shared between applications that were moved to the KDE PIM
suite from the Kdenetwork module. It contains support for mail reading
and MIME attachments.

%description libkdenetwork -l pl
Biblioteki dzielone miêdzy aplikacjami, które zosta³y przeniesione do
zestawu KDE PIM z modulu Kdenetwork. Zawieraj± obs³ugê czytania poczty
i za³±czników MIME.

%package libkdepim
Summary:	kdepim libraries
Summary(pl):	Biblioteki kdepim
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim
Obsoletes:	kdepim-korganizer-libs
Obsoletes:	kdepim-kontact-libs
Obsoletes:	kdepim-kaddressbook-libs
Obsoletes:	kdepim-libkcal
Obsoletes:	kdepim-kaddressbook < 3:3.1.92.031012
Obsoletes:	kdepim-libkdgantt
Obsoletes:	kdepim-kresources

%description libkdepim
Libraries shared between applications in kdepim that provide:
- embedding of adressbook and IMAP support for it
- support for reading and writing the iCalendar and vCalendar formats
- KOrganizer and kontact embedding/accessing
- displaying and managing Gantt diagrams used by the project view
  plugin of KOrganizer.

%description libkdepim -l pl
Biblioteki dzielone miêdzy aplikacjami w kdepim zapewniaj±ce:
- osadzanie ksi±¿ki adresowej i obs³ugê IMAP dla niej
- obs³ugê czytania i pisania w formatach iCalendar i vCalendar
- osadzanie i dostêp do KOrganizera i kontacta
- wy¶wietlanie i zarz±dzanie diagramami Gantta u¿ywanymi we wtyczce do
  ogl±dania projektów KOrganizera.

%package libkmailprivate
Summary:	kmailprivate libraries
Summary(pl):	Biblioteki kmailprivate
Group:		X11/Libraries
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-libksieve
Obsoletes:	kdepim-libktnef

%description libkmailprivate
Libraries providing mail reading and writing engine, Microsoft TNEF
attachements support and sieve protocol.

%description libkmailprivate -l pl
Biblioteki dostarczaj±ce silnik do czytania i pisania poczty oraz
obs³ugê za³±czników Microsoft TNEF i protoko³u sieve.

%package libkpilot
Summary:	kpilot library
Summary(pl):	Biblioteka kpilot
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim

%description libkpilot
Library for KPilot - the KDE application for exchanging data with
palmtops.

%description libkpilot -l pl
Biblioteka dla KPilota - aplikacji KDE do wymiany danych z palmtopami.

%prep
%setup -q -n %{name}-%{version}
%patch100 -p1
%patch0 -p1
%patch1 -p1

%build
z=kpilot/conduits/configure.in.in
grep -v KPILOT_CHECK_PISOCK $z > $z.1
mv $z.1 $z
sed -i -e "s,SUBDIRS=vcf,SUBDIRS=vcf rfc822," kfile-plugins/Makefile.am

cp %{_datadir}/automake/config.sub admin
export kde_htmldir=%{_kdedocdir}
export kde_libs_htmldir=%{_kdedocdir}
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f admin/Makefile.common cvs

%configure \
	--with-qt-libraries=%{_libdir} \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian/man
%{__perl} -pi -e 's/alarmd/kalarmd/;s/ALARMD/KALARMD/' alarmd.sgml
[ -f alarmd.sgml -a ! -f kalarmd.sgml ] && mv -f alarmd.sgml kalarmd.sgml
for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done
cd ../..

%clean
rm -rf $RPM_BUILD_ROOT

%post	libkdenetwork		-p /sbin/ldconfig
%postun	libkdenetwork		-p /sbin/ldconfig

%post	libkdepim		-p /sbin/ldconfig
%postun	libkdepim		-p /sbin/ldconfig

%post	libkmailprivate		-p /sbin/ldconfig
%postun	libkmailprivate		-p /sbin/ldconfig

%post	libkpilot		-p /sbin/ldconfig
%postun	libkpilot		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
##%lang(en) %{_kdedocdir}/en/%{name}-apidocs
%attr(755,root,root) %{_libdir}/libkabinterfaces.so
%attr(755,root,root) %{_libdir}/libkaddressbook.so
%attr(755,root,root) %{_libdir}/libkalarmd.so
%attr(755,root,root) %{_libdir}/libkcal.so
%attr(755,root,root) %{_libdir}/libkdenetwork.so
%attr(755,root,root) %{_libdir}/libkdepim.so
%attr(755,root,root) %{_libdir}/libkgantt.so
%attr(755,root,root) %{_libdir}/libkmailprivate.so
%attr(755,root,root) %{_libdir}/libknewstuff.so
%attr(755,root,root) %{_libdir}/libkontact.so
%attr(755,root,root) %{_libdir}/libkorganizer.so
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so
%attr(755,root,root) %{_libdir}/libkpilot.so
%attr(755,root,root) %{_libdir}/libkpimexchange.so
%attr(755,root,root) %{_libdir}/libkpinterfaces.so
%attr(755,root,root) %{_libdir}/libksieve.so
%attr(755,root,root) %{_libdir}/libksync.so
%attr(755,root,root) %{_libdir}/libktnef.so
%attr(755,root,root) %{_libdir}/libmimelib.so
%attr(755,root,root) %{_libdir}/libkdgantt.so
%{_includedir}/*
# kitchensync part
#%attr(755,root,root) %{_libdir}/libdummykonnector.so
#%attr(755,root,root) %{_libdir}/libkitchensyncui.so
#%attr(755,root,root) %{_libdir}/libkonnector.so
#%attr(755,root,root) %{_libdir}/libksharedfile.so
#%attr(755,root,root) %{_libdir}/libksync2.so
#%attr(755,root,root) %{_libdir}/liblocalkonnector.so
#%attr(755,root,root) %{_libdir}/libqtopiakonnector.so
#%{_includedir}/kitchensync
#%{_includedir}/ksharedfile.h

%files kaddressbook
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde3/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%{_libdir}/kde3/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_libdir}/kde3/ldifvcardthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/ldifvcardthumbnail.so
%{_libdir}/kde3/libkaddrbk_cardview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_cardview.so
%{_libdir}/kde3/libkaddrbk_distributionlist.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_distributionlist.so
%{_libdir}/kde3/libkaddrbk_iconview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_iconview.so
%{_libdir}/kde3/libkaddrbk_location.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_location.so
%{_libdir}/kde3/libkaddrbk_merge.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_merge.so
%{_libdir}/kde3/libkaddrbk_tableview.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_tableview.so
%{_libdir}/kde3/libkaddrbk_*_xxport.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_*_xxport.so
%{_libdir}/kde3/libkaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_datadir}/services/kabconfig.desktop
%{_datadir}/services/kabldapconfig.desktop
%{_datadir}/services/kaddressbook
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/ldifvcardthumbnail.desktop
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_datadir}/servicetypes/kaddressbook_xxport.desktop
%{_desktopdir}/kde/kaddressbook.desktop
%{_iconsdir}/*/*/*/kaddressbook.png
%{_kdedocdir}/en/kaddressbook

%files kandy
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop
%{_mandir}/man1/kandy.1*
%{_kdedocdir}/en/kandy

%files karm
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png
%{_kdedocdir}/en/karm

%files kmail
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kgpgcertmanager
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_libdir}/kde3/libkmailpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmailpart.so*
%attr(755,root,root) %{_libdir}/kde3/kfile_rfc822.so
%{_libdir}/kde3/kfile_rfc822.la
%{_datadir}/apps/kconf_update/k[!n]*
%{_datadir}/apps/kconf_update/u*
%{_datadir}/apps/kgpgcertmanager/kgpgcertmanagerui.rc
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
%{_datadir}/services/kfile_rfc822.desktop
%{_datadir}/services/sieve.protocol
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde/KMail.desktop
#%{_iconsdir}/*/*/actions/mark_as_spam.png
%{_iconsdir}/*/*/apps/kmail.png
%{_iconsdir}/*/*/apps/kmailcvt.png
%{_iconsdir}/*/*/apps/kmaillight.png
%{_kdedocdir}/en/kmail
%{_kdedocdir}/en/kgpgcertmanager

%files knode
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_libdir}/kde3/libknodepart.la
%attr(755,root,root) %{_libdir}/kde3/libknodepart.so*
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png
%{_kdedocdir}/en/knode

%files knotes
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knotes.kcfg
%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png
%{_kdedocdir}/en/knotes

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/kde/konsolekalendar.desktop
%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png
%{_kdedocdir}/en/konsolekalendar

%files kontact
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%{_libdir}/kde3/libkontact_kaddressbookplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kaddressbookplugin.so
# kitchensync kontact plugin
#%{_libdir}/kde3/libkontact_kitchensync.la
#%attr(755,root,root) %{_libdir}/kde3/libkontact_kitchensync.so
%{_libdir}/kde3/libkontact_kmailplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmailplugin.so
%{_libdir}/kde3/libkontact_knodeplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knodeplugin.so
%{_libdir}/kde3/libkontact_knotesplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knotesplugin.so
%{_libdir}/kde3/libkontact_summaryplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_summaryplugin.so
%{_libdir}/kde3/libkontact_weatherplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_weatherplugin.so
%{_libdir}/kde3/kcm_kontact.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontact.so
%{_libdir}/kde3/libkontact_korganizerplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_korganizerplugin.so
%{_libdir}/kde3/libkontact_todoplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_todoplugin.so
%{_datadir}/apps/kontact
%{_datadir}/apps/kontactsummary
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/services/kontact
%{_datadir}/services/kontactconfig.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{_desktopdir}/kde/Kontact.desktop
%{_iconsdir}/crystalsvg/*/apps/kontact.png
%{_kdedocdir}/en/kontact

%files korganizer
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ghns
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/khotnewstuff
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ksync
%attr(755,root,root) %{_bindir}/ical2vcal
%{_libdir}/kde3/kcm_korganizer.la
%attr(755,root,root) %{_libdir}/kde3/kcm_korganizer.so
%{_libdir}/kde3/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%{_libdir}/kde3/libkorganizerpart.la
%attr(755,root,root) %{_libdir}/kde3/libkorganizerpart.so
#%{_libdir}/kde3/resourcecalendarexchange.la
#%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_datadir}/apps/kalarm*
%{_datadir}/apps/kgantt
%{_datadir}/apps/knewstuff
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/ksync
%{_datadir}/autostart/kalarm*.desktop
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config/khotnewstuffrc
%{_datadir}/services/configcolors.desktop
%{_datadir}/services/configfonts.desktop
%{_datadir}/services/configfreebusy.desktop
%{_datadir}/services/configgroupautomation.desktop
%{_datadir}/services/configgroupscheduling.desktop
%{_datadir}/services/configmain.desktop
%{_datadir}/services/configtime.desktop
%{_datadir}/services/configviews.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_desktopdir}/kde/kalarm.desktop
%{_desktopdir}/kde/korganizer.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
%{_iconsdir}/crystalsvg/*/actions/knewstuff.png
%{_iconsdir}/*/*/*/korganizer*.png
%{_mandir}/man1/ical2vcal.1*
%{_mandir}/man1/kalarmd.1*
%{_mandir}/man1/korganizer.1*
%{_kdedocdir}/en/korganizer
%{_kdedocdir}/en/kalarm
%{_kdedocdir}/en/kcontrol/kalarmd
# kitchensync part
#%attr(755,root,root) %{_bindir}/kitchensync
#%attr(755,root,root) %{_bindir}/simplealarmdaemon
#%{_libdir}/kde3/libkded_ksharedfile.la
#%attr(755,root,root) %{_libdir}/kde3/libkded_ksharedfile.so
#%{_libdir}/kde3/libkitchensyncpart.la
#%attr(755,root,root) %{_libdir}/kde3/libkitchensyncpart.so
#%{_libdir}/kde3/libksync_backup.la
#%attr(755,root,root) %{_libdir}/kde3/libksync_backup.so
#%{_libdir}/kde3/libksync_debugger.la
#%attr(755,root,root) %{_libdir}/kde3/libksync_debugger.so
#%{_libdir}/kde3/libksync_syncerpart.la
#%attr(755,root,root) %{_libdir}/kde3/libksync_syncerpart.so
#%{_libdir}/kde3/liboverviewpart.la
#%attr(755,root,root) %{_libdir}/kde3/liboverviewpart.so
#%{_datadir}/apps/kitchensync
#%{_datadir}/mimelnk/kdedevice/cellphone.desktop
#%{_datadir}/mimelnk/kdedevice/pda.desktop
#%{_datadir}/services/kded/ksharedfile.desktop
#%{_datadir}/services/kitchensync
#%{_datadir}/services/overview.desktop
#%{_datadir}/services/kresources/konnector
#%{_datadir}/servicetypes/kitchensync.desktop
#%{_datadir}/servicetypes/konnector.desktop

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png
%{_kdedocdir}/en/korn

%files kpilot
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
%{_datadir}/apps/kpilot
%{_datadir}/services/*conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_desktopdir}/kde/kpalmdoc.desktop
%{_desktopdir}/kde/kpilot*.desktop
%{_iconsdir}/*/*/apps/kpalmdoc.png
%{_iconsdir}/[!l]*/*/*/kpilot*.png
%{_mandir}/man1/kpilot.1*
%{_kdedocdir}/en/kpilot

%files libkdenetwork
%defattr(644,root,root,755)
%doc libkdenetwork/{AUTHORS*,CLASSTREE*,DESIGN.kmime,README}
%doc mimelib/{Changes,README*,Tutorial}
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*.*

%files libkdepim
%defattr(644,root,root,755)
%doc README*
%doc libkcal/{HACKING,README}
%{_libdir}/libkontact.la
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
%{_libdir}/libkcal.la
%attr(755,root,root) %{_libdir}/libkcal.so.*.*.*
%{_libdir}/kde3/kcal_imap.la
%attr(755,root,root) %{_libdir}/kde3/kcal_imap.so
%{_libdir}/kde3/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%{_libdir}/kde3/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%{_libdir}/kde3/kcal_local.la
%attr(755,root,root) %{_libdir}/kde3/kcal_local.so
%{_libdir}/kde3/kcal_localdir.la
%attr(755,root,root) %{_libdir}/kde3/kcal_localdir.so
%{_datadir}/services/kresources/kcal
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%{_libdir}/libkabinterfaces.la
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so.*.*.*
%{_libdir}/kde3/kabc_imap.la
%attr(755,root,root) %{_libdir}/kde3/kabc_imap.so
%{_datadir}/services/kresources/kabc/imap.desktop
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*.*.*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%{_libdir}/libkorganizer_eventviewer.la
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*.*.*
# kitchensync part
#%{_libdir}/libkitchensyncui.la
#%attr(755,root,root) %{_libdir}/libkitchensyncui.so.*.*.*
#%{_libdir}/libkonnector.la
#%attr(755,root,root) %{_libdir}/libkonnector.so.*.*.*
#%{_libdir}/libksharedfile.la
#%attr(755,root,root) %{_libdir}/libksharedfile.so.*.*.*
#%{_libdir}/libksync2.la
#%attr(755,root,root) %{_libdir}/libksync2.so.*.*.*

%files libkmailprivate
%defattr(644,root,root,755)
%{_libdir}/libkmailprivate.la
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*.*
%{_libdir}/libksieve.la
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*

%files libkpilot
%defattr(644,root,root,755)
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*
