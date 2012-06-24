#
# Conditional build:
%bcond_without	apidocs		# do not prepare API documentation
#
%define		_state		unstable
%define		_kdever		3.80.2
%define		_minlibsevr	9:3.80.2
%define		_minbaseevr	9:3.80.2

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K ����ũž ȯ�� - PIM (���� ���� ����)
Summary(pl):	Manad�er informacji osobistej (PIM) dla KDE
Summary(ru):	������������ ����������� (PIM) ��� KDE
Summary(uk):	������������ ������������ (PIM) ��� KDE
Name:		kdepim
Version:	3.80.2
Release:	1
Epoch:		9
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# Source0-md5:	44b123e24579d306446f4fd35549b575
#Patch100: %{name}-branch.diff
#Patch0: kde-common-PLD.patch
#Patch1: %{name}-kmail_toolbars.patch
#Patch2: %{name}-iconsidepane-showtext.diff
#Patch3: %{name}-notru64.patch
BuildRequires:	QtSql-devel
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	bluez-libs-devel
BuildRequires:	cyrus-sasl-devel
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
BuildRequires:	flex
#BuildRequires:	gnupg >= 1.2.2
BuildRequires:	gnupg-agent
BuildRequires:	gpgme-devel >= 1:1.0.0
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libgnokii-devel
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	lockdev-devel
BuildRequires:	openssl-devel
BuildRequires:	pcre-devel
BuildRequires:	pilot-link-devel
BuildRequires:	qt-designer-libs
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	qt4-qmake
BuildRequires:	rpmbuild(macros) >= 1.129
#BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
BuildConflicts:	kdepim-kontact-libs
BuildConflicts:	kdepim-libkmailprivate
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
# subpackage akregator
Obsoletes:	akregator
#Obsoletes:	kdeaddons-konqueror
Obsoletes:	kdeaddons-kontact
Obsoletes:	kdepim-kontact
Obsoletes:	kdepim-korganizer
Obsoletes:	kdepim-korganizer-libs
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
kdepim - ��� ����� ������ ��� ���������� ������������ ����������� ���
K Desktop Environment (KDE).

%description -l uk
kdepim - �� ��¦� ���̦� ��� ��������� ������������ �������æ�� ��� K
Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag��wkowe do KDE pim
Summary(ru):	����� ���������� ��� kdepim
Summary(uk):	����� �������� ��� kdepim
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs-devel >= %{_minlibsevr}
Obsoletes:	kdepim-libkcal-devel
Conflicts:	kdenetwork-devel < 10:3.1.90

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe potrzebne do budowy aplikacji
bazuj�cych na kdepim.

%description devel -l uk
��� ����� ͦ����� ����� �������˦� ����Ȧ�Φ ��� �������� �������,
��������� �� kdepim.

%description devel -l ru
���� ����� �������� ����� ���������� ����������� ��� ����������
��������, ���������� �� kdepim.

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
- listy klas i ich sk�adnik�w
- list� przestrzeni nazw (namespace)

%package -n kde-kio-groupwise
Summary:	Groupwise protocol service
Summary(pl):	Obs�uga protoko�u Groupwise
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description -n kde-kio-groupwise
Groupwise protocol service.

%description -n kde-kio-groupwise -l pl
Obs�uga protoko�u Groupwise.

%package -n kde-kio-imap4
Summary:	IMAP4 protocol service
Summary(pl):	Obs�uga protoko�u IMAP4
Group:		X11/Libraries
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kde-kio-newimap4 < 9:3.4.0

%description -n kde-kio-imap4
IMAP4 protocol service.

%description -n kde-kio-imap4 -l pl
Obs�uga protoko�u IMAP4.

%package kaddressbook
Summary:	Address book
Summary(pl):	Ksi��ka adresowa
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdelibs >= %{_minlibsevr}

%description kaddressbook
The KDE address book.

%description kaddressbook -l pl
Ksi��ka adresowa dla KDE.

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
uruchomienie polecenia lub poczt� elektroniczn�. Umo�liwia ustawienie
w�asnej wiadomo�ci alarmowej, kt�ra wyskoczy na ekranie o wybranym
czasie albo zaszeregowanie polece� do wykonania lub poczty do
wys�ania. Zawiera tak�e demona obs�uguj�cego przypominanie.

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
KArm (nazwa pochodzi od s�owa "praca" w j�zyku punjambi) �ledzi czas
sp�dzony na r�nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
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
Program pocztowy dla KDE o olbrzymich mo�liwo�ciach, obejmuj�cych:
- obs�ug� SMTP/maildir/POP3/IMAP z SSL/TLS i pipeliningiem
- ksi��k� adresow�
- automatyczne szyfrowanie przy u�yciu OpenPGP (PGP lub GnuPG)
- pot�ne filtry pocztowe
- zagnie�d�one skrzynki pocztowe z obs�ug� list pocztowych
- �ci�ganie na ��danie lub usuwanie bez �ci�gania du�ych list�w z
  serwera POP3
- pe�n� obs�ug� list�w we wszystkich j�zykach i zestawach znak�w
  obs�ugiwanych przez Qt
- przeszukiwanie wiadomo�ci z prezentacj� w wirtualnych folderach
- usuwanie powt�rzonych list�w
- w�tkowanie wiadomo�ci
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
�rodowiska KDE. Jego mo�liwo�ci obejmuj�:
- wszystkie podstawowe cechy czytnika news�w (czytanie i wysy�anie
  artyku��w, w�tkowanie...)
- obs�ug� wielu serwer�w news
- czytanie i tworzenie wielocz�ciowych wiadomo�ci MIME
- wy�wietlanie za��cznik�w w tek�cie (tekstowych i obrazk�w)
- konfigurowalne filtry, fonty i kolory
- pe�ny scoring
- wiele wi�cej...

%description knode -l pt_BR
Leitor de not�cias (news) do KDE.

%package knotes
Summary:	Yellow cards
Summary(pl):	��te karteczki
Group:		X11/Applications
Requires:	%{name}-libs = %{epoch}:%{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na pulpicie notatki z opcj� wysy�ania.
Dodatkowo, aby m�c s�u�y� za przypominajk�, KNotes mo�e wysy�a� poczt�
i drukowa� notatki, a tak�e przyjmowa� przeci�ganie nawet ze zdalnych
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
KonsoleKalendar to dzia�aj�cy z linii polece� interfejs do kalendarzy
KDE. Pozwala ogl�da�, wstawia�, usuwa� i modyfikowa� zdarzenia w
kalendarzu z linii polece� lub j�zyka skryptowego. Ponadto
KonsoleKalendar potrafi wyeksportowa� kalendarz KDE do wielu innych
format�w.

G��wne mo�liwo�ci programu KonsoleKalendar:
- wypisywanie wpis�w kalendarza od daty pocz�tkowej do ko�cowej
- wstawianie/usuwanie/modyfikowanie wpis�w
- eksportowanie wpis�w kalendarza do innych format�w plik�w.

Narz�dzie dost�pu do plik�w kalendarza z linii polece�.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska�nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitora��o da caixa de correio
Group:		X11/Applications
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Requires:	kdebase-desktop >= %{_minbaseevr}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj�cy liczb� wiadomo�ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitora��o da caixa de correio.

%package libs
Summary:	Shared kdepim libraries
Summary(pl):	Wsp�dzielone biblioteki kdepim
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Provides:	kdepim-kmail-libs = %{epoch}:%{version}-%{release}
Provides:	kdepim-libkdenetwork = %{epoch}:%{version}-%{release}
Provides:	kdepim-libkdepim = %{epoch}:%{version}-%{release}
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
Biblioteki wsp�dzielone pomi�dzy aplikacjami PIM w KDE, m.in.
libkdenetwork, libkdepim, libkmailprivate, libknodecommon, libkpilot,
libksieve, libmimelib.

%prep
%setup -q

#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Calendar;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	korganizer/korganizer.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kpilot/kpilot/kpilotdaemon.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kpilot/kpilot/kpilot.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kpilot/conduits/docconduit/kpalmdoc.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;ContactManagement;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kaddressbook/kaddressbook.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;X-PIM;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kontact/src/Kontact.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;Email;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kmail/KMail.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Network;News;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	knode/KNode.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
#	kmobile/kmobile.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Office;PDA;/' \
#	-e 's/Terminal=0/Terminal=false/' \
#	kandy/src/kandy.desktop
#%{__sed} -i -e 's/Categories=.*/Categories=Qt;KDE;Utility;Applet;/' \
#	knotes/knotes.desktop
#%{__sed} -i -e 's/Terminal=0/Terminal=false/' \
#	karm/support/karm.desktop \
#	knotes/knotes.desktop \
#	konsolekalendar/konsolekalendar.desktop \
#	korn/KOrn.desktop
#%{__sed} -i -e '/\[Desktop Entry\]/aEncoding=UTF-8' \
#	-e 's/Terminal=0/Terminal=false/' \
#	ktnef/gui/ktnef.desktop
#for f in `find . -name \*.desktop`; do
#	if grep -q '^Categories=.*[^;]$' $f; then
#		sed -i -e 's/\(^Categories=.*$\)/\1;/' $f
#	fi
#	if grep -q '\[ven\]' $f; then
#		sed -i -e 's/\[ven\]/[ve]/' $f

#	fi
#done

# change annoyance-filter path (required by autodetect in kmail)
#%{__sed} -i -e 's,\($HOME/\.annoyance-filter/annoyance-filter\)\(.*\),annoyance-filter\2,g' \
#	kmail/kmail.antispamrc

%build
mkdir build
cd build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	../
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	kde_libs_htmldir=%{_kdedocdir}

rm -rf $RPM_BUILD_ROOT%{_iconsdir}/locolor

# Debian manpages
#install -d $RPM_BUILD_ROOT%{_mandir}/man1
#cd debian/man
#if [ -f alarmd.sgml ]; then
#	%{__sed} -i -e 's/alarmd/kalarmd/' -e 's/ALARMD/KALARMD/' alarmd.sgml
#	mv -f alarmd.sgml kalarmd.sgml
#fi
#for f in *.man ; do
#	base="$(basename $f .man)"
#	install ${base}.man $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
#done
#cd -

#%find_lang	akregator	--with-kde
#%find_lang	kaddressbook	--with-kde
#%find_lang	kalarm		--with-kde
#%find_lang	kalarmd		--with-kde
#cat kalarmd.lang >> kalarm.lang
#%find_lang	kandy		--with-kde
#%find_lang	karm		--with-kde
#%find_lang	kmail		--with-kde
#%find_lang	knode		--with-kde
#%find_lang	knotes		--with-kde
#%find_lang	konsolekalendar	--with-kde
#%find_lang	kontact		--with-kde
#%find_lang	korganizer	--with-kde
#%find_lang	korn		--with-kde
#%find_lang	kleopatra	--with-kde
#cat kleopatra.lang >> kmail.lang
#%find_lang	kpilot		--with-kde
#%find_lang	ktnef		--with-kde
#cat ktnef.lang >> kmail.lang
#%find_lang	kwatchgnupg	--with-kde
#cat kwatchgnupg.lang >> kmail.lang
#%find_lang	multisynk	--with-kde

#> %{name}.lang
#cat akregator.lang	>> %{name}.lang
#cat kontact.lang	>> %{name}.lang
#cat korganizer.lang	>> %{name}.lang
#cat kalarmd.lang	>> %{name}.lang
# TODO
#cat multisynk.lang	>> %{name}.lang

# Omit apidocs entries
#sed -i 's/.*apidocs.*//' *.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs			-p /sbin/ldconfig
%postun	libs			-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# -f %{name}.lang
%defattr(644,root,root,755)
#%doc README.Kolab
%attr(755,root,root) %{_bindir}/akregator
%attr(755,root,root) %{_bindir}/*groupwarewizard
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/kode
%attr(755,root,root) %{_bindir}/kabcclient
%attr(755,root,root) %{_bindir}/kontact
%attr(755,root,root) %{_bindir}/kxml_compiler
%attr(755,root,root) %{_bindir}/kagenda
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer
%attr(755,root,root) %{_bindir}/ktimetracker
%attr(755,root,root) %{_bindir}/kung
%attr(755,root,root) %{_bindir}/kwsdl_compiler
%attr(755,root,root) %{_bindir}/kxforms
%attr(755,root,root) %{_bindir}/schematest
%attr(755,root,root) %{_bindir}/sloxwizard
%{_libdir}/kde4/kabc_groupdav.la
%attr(755,root,root) %{_libdir}/kde4/kabc_groupdav.so*
%{_libdir}/kde4/kabc_slox.la
%attr(755,root,root) %{_libdir}/kde4/kabc_slox.so
%{_libdir}/kde4/kabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde4/kabc_xmlrpc.so
%{_libdir}/kde4/kcal_groupdav.la
%attr(755,root,root) %{_libdir}/kde4/kcal_groupdav.so*
%{_libdir}/kde4/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde4/kcal_kabc.so
%{_libdir}/kde4/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde4/kcal_remote.so
%{_libdir}/kde4/kcal_resourcefeatureplan.la
%attr(755,root,root) %{_libdir}/kde4/kcal_resourcefeatureplan.so*
%{_libdir}/kde4/kcal_slox.la
%attr(755,root,root) %{_libdir}/kde4/kcal_slox.so
%{_libdir}/kde4/kcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde4/kcal_xmlrpc.so
%{_libdir}/kde4/kcm_apptsummary.la
%attr(755,root,root) %{_libdir}/kde4/kcm_apptsummary.so
%{_prefix}/lib/kde4/kcm_todosummary.la
%attr(755,root,root) %{_prefix}/lib/kde4/kcm_todosummary.so
%{_libdir}/kde4/kcm_kmailsummary.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kmailsummary.so
%{_libdir}/kde4/kcm_kontact.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kontact.so
%{_libdir}/kde4/kcm_kontactsummary.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kontactsummary.so
%{_libdir}/kde4/kcm_korganizer.la
%attr(755,root,root) %{_libdir}/kde4/kcm_korganizer.so
%{_libdir}/kde4/kcm_sdsummary.la
%attr(755,root,root) %{_libdir}/kde4/kcm_sdsummary.so
%{_libdir}/kde4/kfile_ics.la
%attr(755,root,root) %{_libdir}/kde4/kfile_ics.so
%{_libdir}/kde4/libakregatorpart.la
%attr(755,root,root) %{_libdir}/kde4/libakregatorpart.so*
%{_libdir}/kde4/libakregator_mk4storage_plugin.la
%attr(755,root,root) %{_libdir}/kde4/libakregator_mk4storage_plugin.so
%{_libdir}/kde4/libkontact_akregator.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_akregator.so
%{_libdir}/kde4/libkontact_journalplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_journalplugin.so
%{_libdir}/kde4/libkontact_kaddressbookplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_kaddressbookplugin.so
%{_libdir}/kde4/libkontact_karm.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_karm.so
%{_libdir}/kde4/libkontact_kmailplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_kmailplugin.so
%{_libdir}/kde4/libkontact_knodeplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_knodeplugin.so
%{_libdir}/kde4/libkontact_knotesplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_knotesplugin.so
%{_libdir}/kde4/libkontact_korganizerplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_korganizerplugin.so
%{_libdir}/kde4/libkontact_todoplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_todoplugin.so
%{_libdir}/kde4/libkontact_specialdatesplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_specialdatesplugin.so
%{_libdir}/kde4/libkontact_summaryplugin.la
%attr(755,root,root) %{_libdir}/kde4/libkontact_summaryplugin.so
%{_libdir}/kde4/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde4/libkorg_*.so
%{_libdir}/kde4/libkorganizerpart.la
%attr(755,root,root) %{_libdir}/kde4/libkorganizerpart.so
%{_libdir}/kde4/plugins/designer/kdepimwidgets.la
%attr(755,root,root) %{_libdir}/kde4/plugins/designer/kdepimwidgets.so
%{_datadir}/apps/akregator
%{_datadir}/apps/kconf_update/korganizer.upd
%{_datadir}/apps/kdepimwidgets
%{_datadir}/apps/kxforms
%{_datadir}/apps/kontact
%{_datadir}/apps/kontactsummary
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/libkdepim
%{_datadir}/apps/libkholidays
%{_datadir}/apps/libkleopatra
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/akregator.kcfg
%{_datadir}/config.kcfg/custommimeheader.kcfg
%{_datadir}/config.kcfg/egroupware.kcfg
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/kontact.kcfg
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/config.kcfg/pimemoticons.kcfg
%{_datadir}/config.kcfg/replyphrases.kcfg
%{_datadir}/config.kcfg/slox.kcfg
%{_datadir}/config.kcfg/kxforms.kcfg
%{_datadir}/services/akregator_mk4storage_plugin.desktop
%{_datadir}/services/akregator_part.desktop
%{_datadir}/services/feed.protocol
%{_datadir}/services/kcmkmailsummary.desktop
%{_datadir}/services/kcmkontactsummary.desktop
%{_datadir}/services/kcmsdsummary.desktop
%{_datadir}/services/kfile_ics.desktop
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/kontact
%{_datadir}/services/kontactconfig.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/korganizer_*.desktop
%{_datadir}/services/kresources/kabc/kabc_*.desktop
%{_datadir}/services/kresources/kcal
%{_datadir}/services/kresources/alarms
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/akregator_plugin.desktop
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/kaddressbookimprotocol.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_datadir}/servicetypes/korgprintplugin.desktop
%{_desktopdir}/kde/Kontact.desktop
%{_desktopdir}/kde/akregator.desktop
%{_desktopdir}/kde/korganizer.desktop
%{_desktopdir}/kde/korganizer-import.desktop
%{_desktopdir}/kde/groupwarewizard.desktop
%{_desktopdir}/kde/kwsdl_compiler.desktop
%{_iconsdir}/*/*/apps/akregator*
%{_iconsdir}/*/*/*/rss_tag.png
%{_iconsdir}/*/*/apps/kontact.png
%{_iconsdir}/*/*/actions/kontact_*.png
%{_iconsdir}/*/*/*/korganizer.png
%{_iconsdir}/crystalsvg/22x22/actions/button_fewer.png
%{_iconsdir}/crystalsvg/22x22/actions/button_more.png

#%{_mandir}/man1/akregator.1*
#%{_mandir}/man1/ical2vcal.1*
#%{_mandir}/man1/kdeopt*.1*
#%{_mandir}/man1/kitchensync*.1*
#%{_mandir}/man1/korga*.1*
#%{_mandir}/man1/kontact*.1*
#%{_mandir}/man1/ksync*.1*
#%{_mandir}/man1/*wizard.1*

###### should be separate pac. ???
%attr(755,root,root) %{_bindir}/akonadi*
%attr(755,root,root) %{_libdir}/libakonadi.so.1.0.0
%attr(755,root,root) %{_libdir}/libakonadicomponents.so.1.0.0
%attr(755,root,root) %{_libdir}/libakonadiprivate.so
%attr(755,root,root) %{_libdir}/libakonadiresources.so.1.0.0
%attr(755,root,root) %{_libdir}/libakonadisearchprovider.so.1.0.0
%{_datadir}/apps/akonadi

%files devel
%defattr(644,root,root,755)
%{_includedir}/kdepimmacros.h
%{_includedir}/kdepimprotocols.h
%{_includedir}/akonadi
%{_includedir}/akregator
%{_includedir}/calendar
%{_includedir}/gpgme++
%{_includedir}/index
%{_includedir}/kabc
%{_includedir}/kaddressbook
%{_includedir}/kcal
%{_includedir}/kleo
%{_includedir}/kmail
%{_includedir}/kontact
%{_includedir}/korganizer
%{_includedir}/ksieve
%{_includedir}/libakonadi
%{_includedir}/libakonadiresources
%{_includedir}/libkholiday_ng
%{_includedir}/mimelib
%{_includedir}/qgpgme
%{_libdir}/libkaddressbook.so
%{_libdir}/libkmime.so
%{_libdir}/libkorganizer.so
%{_libdir}/libkorganizer_eventviewer.so
%{_libdir}/libkorganizer_calendar.so
%{_libdir}/libkpgp.so
%{_datadir}/apps/cmake/modules/FindKode.cmake
%{_datadir}/apps/cmake/modules/KodeMacros.cmake

#%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
#%{_kdedocdir}/en/%{name}-apidocs
#%endif

%files -n kde-kio-imap4
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/kde4/kio_imap4.so
%{_datadir}/services/imap4.protocol
%{_datadir}/services/imaps.protocol

%files -n kde-kio-groupwise
%defattr(644,root,root,755)
%{_datadir}/config.kcfg/groupwise.kcfg

%files kaddressbook
%defattr(644,root,root,755)
# -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/kde4/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kabconfig.so
%{_libdir}/kde4/kcm_kabcustomfields.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kabcustomfields.so
%{_libdir}/kde4/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kabldapconfig.so
%{_libdir}/kde4/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde4/kfile_vcf.so
%{_libdir}/kde4/ldifvcardthumbnail.la
%attr(755,root,root) %{_libdir}/kde4/ldifvcardthumbnail.so
%{_libdir}/kde4/libkaddrbk_cardview.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_cardview.so
%{_libdir}/kde4/libkaddrbk_cryptosettings.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_cryptosettings.so
%{_libdir}/kde4/libkaddrbk_distributionlist.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_distributionlist.so
%{_libdir}/kde4/libkaddrbk_iconview.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_iconview.so
%{_libdir}/kde4/libkaddrbk_resourceselection.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_resourceselection.so
%{_libdir}/kde4/libkaddrbk_tableview.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_tableview.so
%{_libdir}/kde4/libkaddrbk_*_xxport.la
%attr(755,root,root) %{_libdir}/kde4/libkaddrbk_*_xxport.so
%{_libdir}/kde4/libkaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde4/libkaddressbookpart.so
%{_datadir}/apps/kaddressbook
%{_datadir}/services/kaddressbook
%{_datadir}/services/kabconfig.desktop
%{_datadir}/services/kabcustomfields.desktop
%{_datadir}/services/kabldapconfig.desktop
%{_datadir}/services/kcmapptsummary.desktop
%{_datadir}/services/kcmtodosummary.desktop
%{_datadir}/services/ldifvcardthumbnail.desktop
%{_datadir}/servicetypes/dbuscalendar.desktop

%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_*.desktop
%{_desktopdir}/kde/kaddressbook.desktop
%{_iconsdir}/*/*/*/kaddressbook.png
#%{_mandir}/man1/kaddressbook*.1*
#%{_mandir}/man1/kabc2mutt*.1*

%files kalarm
%defattr(644,root,root,755)
# -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%{_datadir}/apps/kalarm
%{_datadir}/autostart/kalarm*.desktop
%{_libdir}/kde4/kalarm_*.la
%attr(755,root,root) %{_libdir}/kde4/kalarm_*.so
%{_desktopdir}/kde/kalarm.desktop
%{_desktopdir}/kde/kalarmd.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
%{_iconsdir}/*/*/*/file.png
%{_iconsdir}/*/*/*/message.png
%{_iconsdir}/*/*/*/new_from_template.png
%{_iconsdir}/*/*/*/playsound.png
%{_iconsdir}/*/*/*/kalarm_disabled.png
#%{_mandir}/man1/kalarm*.1*

%files karm
%defattr(644,root,root,755)
# -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_libdir}/kde4/libkarmpart.la
%attr(755,root,root) %{_libdir}/kde4/libkarmpart.so
%{_datadir}/apps/karm
%{_datadir}/services/karm_part.desktop
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png
%{_datadir}/apps/karmpart/karmui.rc

%files kmail
%defattr(644,root,root,755)
# -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail*
%attr(755,root,root) %{_bindir}/kleopatra
%attr(755,root,root) %{_bindir}/kwatchgnupg
%attr(755,root,root) %{_bindir}/indexlib-config
%{_libdir}/kde4/kcm_kmail.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kmail.so
%{_libdir}/kde4/kcm_kleopatra.la
%attr(755,root,root) %{_libdir}/kde4/kcm_kleopatra.so
%{_libdir}/kde4/libkmail_bodypartformatter_application_octetstream.la
%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_application_octetstream.so
%{_libdir}/kde4/libkmail_bodypartformatter_text_calendar.la
%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_calendar.so
%{_libdir}/kde4/libkmail_bodypartformatter_text_vcard.la
%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_vcard.so
%{_libdir}/kde4/libkmail_bodypartformatter_text_xdiff.la
%attr(755,root,root) %{_libdir}/kde4/libkmail_bodypartformatter_text_xdiff.so
%{_libdir}/kde4/libkmailpart.la
%attr(755,root,root) %{_libdir}/kde4/libkmailpart.so*
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kmail*.sh
%{_datadir}/apps/kconf_update/kmail.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp-3.1-upgrade-address-data.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/kpgp.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-signature.pl
%attr(755,root,root) %{_datadir}/apps/kconf_update/upgrade-transport.pl
%{_datadir}/apps/kleopatra
%{_datadir}/apps/kmailcvt
%{_datadir}/apps/kmail
%{_datadir}/apps/kwatchgnupg
%{_datadir}/config/kmail.antispamrc
%{_datadir}/config/kmail.antivirusrc
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/services/kmail_*.desktop
%{_datadir}/services/kleopatra_*.desktop
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
%{_libdir}/kde4/kio_mbox.la
%attr(755,root,root) %{_libdir}/kde4/kio_mbox.so
%{_datadir}/services/mbox.protocol
# kio-sieve
%{_libdir}/kde4/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde4/kio_sieve.so
%{_datadir}/services/sieve.protocol
#%{_mandir}/man1/kmail*.1*
#%{_mandir}/man1/kwatchgnupg*.1*
#%{_mandir}/man1/kleopatra*.1*
# ktnef
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png
%{_iconsdir}/*/*/*/ktnef_extract_*.png

%files knode
%defattr(644,root,root,755)
# -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_libdir}/kde4/kcm_knode.la
%attr(755,root,root) %{_libdir}/kde4/kcm_knode.so
%{_libdir}/kde4/libknodepart.la
%attr(755,root,root) %{_libdir}/kde4/libknodepart.so*
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_datadir}/services/knode_*.desktop
%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png
#%{_mandir}/man1/knode*.1*

%files knotes
%defattr(644,root,root,755)
# -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_libdir}/kde4/knotes_local.la
%attr(755,root,root) %{_libdir}/kde4/knotes_local.so
%{_libdir}/kde4/knotes_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde4/knotes_xmlrpc.so
%{_datadir}/apps/knotes
%{_datadir}/config.kcfg/knoteconfig.kcfg
%{_datadir}/config.kcfg/knotesglobalconfig.kcfg
%{_datadir}/services/kresources/knotes
%{_datadir}/services/kresources/knotes_manager.desktop
%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png
#%{_mandir}/man1/knotes*.1*

%files konsolekalendar
%defattr(644,root,root,755)
# -f konsolekalendar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/kde/konsolekalendar.desktop
%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png
#%{_mandir}/man1/konsolekalendar*.1*

%files korn
%defattr(644,root,root,755)
# -f korn.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_datadir}/apps/kconf_update/korn-*.upd
%attr(755,root,root) %{_datadir}/apps/kconf_update/korn-*.pl
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png
#%{_mandir}/man1/korn*.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libakregatorprivate.so*
%attr(755,root,root) %{_libdir}/libgpgme++.so.*.*.*
%attr(755,root,root) %{_libdir}/libindex.so.*.*.*
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*
%attr(755,root,root) %{_libdir}/kabc_groupdav.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_slox.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*
%attr(755,root,root) %{_libdir}/kcal_groupdav.so.*.*.*
%attr(755,root,root) %{_libdir}/kcal_resourcefeatureplan.so.*.*.*
%attr(755,root,root) %{_libdir}/libkmime.so.*
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_calendar.so.*.*.*
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%attr(755,root,root) %{_libdir}/libkpgp.so.*
%attr(755,root,root) %{_prefix}/lib/libkalarm_resources.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkcal_resourceremote.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkcal_slox.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkcal_xmlrpc.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkdepim.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkgroupwarebase.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkgroupwaredav.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkholidays.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkholidays_ng.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkleopatra.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkmailprivate.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libknodecommon.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libknotes_xmlrpc.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkocorehelper.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkode.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkontact.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkorg_stdprinting.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkorganizer_interfaces.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkpimidentities.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkpinterfaces.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkschema.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkschemawidgets.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libksieve.so.0.0.0
%attr(755,root,root) %{_prefix}/lib/libkslox.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libkxmlcommon.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libmimelib.so.1.1.0
%attr(755,root,root) %{_prefix}/lib/libqgpgme.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libschema.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libwscl.so.1.0.0
%attr(755,root,root) %{_prefix}/lib/libwsdl.so.1.0.0
