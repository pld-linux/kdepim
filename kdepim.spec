#
# TODO :
# - find out why cant this app find gtk+.h (stil on time for JPilot proxy)
# - bluetooth, gnokii, lockdev (more libs in BR)
# - Patching apropriate configure.in.in to not grumble about gpg{sm} and
#   build crypto stuff anyway
#
# Conditional build:
%bcond_without	apidocs		# prepare API documentation
%bcond_with     cvs             # use cvs checkouts instead of tarballs

%define		_state		snapshots
%define		_ver		3.2.91
%define		_snap		040523
%define		_packager	adgor

%define		_minlibsevr	9:3.2.90.040519
%define		_minbaseevr	9:3.2.90.040519

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ¥½ºÅ©Å¾ È¯°æ - PIM (°³ÀÎ Á¤º¸ °ü¸®)
Summary(pl):	Manad¿er informacji osobistej (PIM) dla KDE
Summary(ru):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÉÒÏ×ÝÉË (PIM) ÄÌÑ KDE
Summary(uk):	ðÅÒÓÏÎÁÌØÎÙÊ ÐÌÁÎÕ×ÁÌØÎÉË (PIM) ÄÌÑ KDE
Name:		kdepim
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		3
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
%if ! %{with cvs}
Source0:        ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
#Source0:	http://ep09.pld-linux.org/~%{_packager}/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:  53b213398dc488af5de57b74c6b3bbf5
%else
Source0:        kdesource.tar.gz
%endif
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
Patch2:		kde-common-QTDOCDIR.patch
BuildRequires:	automake
BuildRequires:	bison
%{?with_apidocs:BuildRequires:	doxygen}
BuildRequires:	ed
%{?with_apidocs:BuildRequires:	graphviz}
BuildRequires:	kdelibs-devel >= %{_minlibsevr}
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	pilot-link-devel
BuildRequires:	bluez-libs-devel
BuildRequires:	gpgme-devel
BuildRequires:	gnupg >= 1.2.2
BuildRequires:	lockdev-devel
BuildRequires:	libgnokii-devel
BuildRequires:	pcre-devel
BuildRequires:	qt-designer-libs
%{?with_apidocs:BuildRequires:	qt-doc}
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake >= 040511
BuildRequires:	zlib-devel
Requires:	%{name}-libs
Obsoletes:	kdepim-korganizer
Obsoletes:	kdepim-korganizer-libs 
#Obsoletes:	kdepim-libkcal
Obsoletes:	kdepim-kontact
# Will be replaced by kdeaddons-pim
#Obsoletes:	kdeaddons-kontact 
Obsoletes:	kdepim-kresources
BuildConflicts: kdepim-kontact-libs
BuildConflicts: kdepim-libkmailprivate
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
#Requires:	%{name}-kaddressbook-libs = %{epoch}:%{version}-%{release}
#Requires:	%{name}-kmail-libs = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libknodecommon = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libknotes_xmlrpc = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libktnef = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libs = %{epoch}:%{version}-%{release}
Conflicts:	kdenetwork-devel < 10:3.1.90
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
Group:		Development/Docs
Requires:	kdelibs >= 9:3.2.90

%description apidocs
API documentation.

%description apidocs -l pl
Dokumentacja API.

%package -n kde-kio-sieve
Summary:	KDE SIEVE protocol service
Summary(pl):	Obs³uga protoko³u SIEVE
Group:		X11/Libraries
#Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
Conflicts:	kdepim-kmail < 3:3.2.90.040210

%description -n kde-kio-sieve
KDE SIEVE protocol service.

%description -n kde-kio-sieve -l pl
Obs³uga protoko³u SIEVE.

%package -n kde-kio-newimap4
Summary:	New IMAP4 protocol service 
Summary(pl):	Nowa obs³uga protoko³u IMAP4
Group:		X11/Libraries
#Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}

%description -n kde-kio-newimap4
New IMAP4 protocol service.

%description -n kde-kio-newimap4 -l pl
Nowa obs³uga protoko³u IMAP4.


%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi±¿ka adresowa
Group:		X11/Applications
Requires:	kdelibs >= %{_minlibsevr}
#Requires:	%{name}-kaddressbook-libs = %{epoch}:%{version}-%{release}

%description kaddressbook
Address Book.

%description kaddressbook -l pl
Ksi±¿ka adresowa.

%package kaddressbook-libs
Summary:	Address Book - shared libs
Summary(pl):	Ksi±¿ka adresowa - biblioteki wspó³dzielone
Group:		X11/Libraries
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kaddressbook < 3:3.1.92.031012

%description kaddressbook-libs
Address Book - shared libs.

%description kaddressbook-libs -l pl
Ksi±¿ka adresowa - biblioteki wspó³dzielone.

%package kalarm
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
#Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}

%description kalarm
TODO.

%description kalarm -l pl
TODO.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl):	Program do komunikacji miêdzy PC a tel. komórkowym
Group:		X11/Applications
Requires:	kdebase-core >= %{_minlibsevr}
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
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
#Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

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
Requires:	kdebase-core >= %{_minbaseevr}
Requires:	kde-kio-imap4 >= %{_minbaseevr}
Requires:	kde-kio-pop3 >= %{_minbaseevr}
Requires:	kde-kio-smtp >= %{_minbaseevr}
#Requires:	%{name}-kmail-libs = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-kmail

%description kmail
This is electronic mail client for KDE. It is able to retrieve mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description kmail -l pl
Program pocztowy dla KDE. Potrafi odczytywaæ pocztê z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs³ug± zestawów
znaków.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package kmail-libs
Summary:	kmailprivate library
Summary(pl):	Biblioteka kmailprivate
Group:		X11/Libraries
#Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-libkmailprivate

%description kmail-libs
kdmailprivate library.

%description kmail-libs -l pl
Biblioteka kmailprivate.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik newsów dla KDE
Summary(pt_BR):	Leitor de notícias (news) do KDE
Group:		X11/Applications
Requires:	kde-kio-nntp >= %{_minbaseevr}
Requires:	kdebase-core >= %{_minbaseevr}
#Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
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
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}

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
#Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
Narzêdzie dostêpu do plików kalendarza z linii poleceñ.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska¼nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoração da caixa de correio
Group:		X11/Applications
Requires:	kdebase-kicker >= %{_minbaseevr}
#Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
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
#Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
#Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}
Requires:	pilot-link
Obsoletes:	kdepim-kpalmdoc
Obsoletes:	kdepim-pilot
Obsoletes:	kpilot

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

%package ktnef
Summary:	A viewer/extractor for TNEF files
Summary(pl):	Przegl±darka/ekstraktor plików TNEF
Group:		X11/Applications
Requires:	kdebase-core >= %{_minbaseevr}
#Requires:	%{name}-libktnef = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-korn

%description ktnef
A viewer/extractor for TNEF files.

%description ktnef -l pl
Przegl±darka/ekstraktor plików TNEF.

%package libkcal
Summary:	kcal library
Summary(pl):	Biblioteka kcal
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkcal
kcal library.

%description libkcal -l pl
Biblioteka kcal.

%package libkdenetwork
Summary:	A network library
Summary(pl):	Biblioteka sieciowa
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdenetwork

%description libkdenetwork
A network library.

%description libkdenetwork -l pl
Biblioteka sieciowa.

%package libkdepim
Summary:	kdepim library
Summary(pl):	Biblioteka kdepim
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkdepim
kdepim library.

%description libkdepim -l pl
Biblioteka kdepim.

%package libknodecommon
Summary:	knodecommon library
Summary(pl):	Biblioteka knodecommon
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libknodecommon
knodecommon library.

%description libknodecommon -l pl
Biblioteka knodecommon.

%package libknotes_xmlrpc
Summary:	knotes_xmlrpc library
Summary(pl):	Biblioteka knotes_xmlrpc
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libknotes_xmlrpc
knotes_xmlrpc library.

%description libknotes_xmlrpc -l pl
Biblioteka knotes_xmlrpc.

%package libkpilot
Summary:	kpilot library
Summary(pl):	Biblioteka kpilot
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libkpilot
kpilot library.

%description libkpilot -l pl
Biblioteka kpilot.

%package libksieve
Summary:	ksieve library
Summary(pl):	Biblioteka ksieve
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libksieve
ksieve library.

%description libksieve -l pl
Biblioteka ksieve.

%package libktnef
Summary:	ktnef library
Summary(pl):	Biblioteka ktnef
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}
Obsoletes:	kdepim-ktnef < 3:3.1.92.031012

%description libktnef
ksieve ktnef.

%description libktnef -l pl
Biblioteka ktnef.

%package libmimelib
Summary:	mimelib library, based on mimepp library
Summary(pl):	Biblioteka mimelib oparta na bibliotece mimepp
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libmimelib
mimelib library, based on mimepp library.

%description libmimelib -l pl
Biblioteka mimelib oparta na bibliotece mimepp.

%package libs
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Requires:	kdelibs >= %{_minlibsevr}

%description libs
TODO.

%description libs -l pl
TODO.

%prep
%if ! %{with cvs}
%setup -q -n %{name}-%{_snap} 
%else
%setup -q -n %{name} -D
%endif
%patch0 -p1
%patch1 -p1
%patch2 -p1

echo "KDE_OPTIONS = nofinal" >> kitchensync/kitchensync/backup/Makefile.am
echo "KDE_OPTIONS = nofinal" >> korganizer/Makefile.am

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final \
	--with-qt-libraries=%{_libdir}

%{__make}

%{?with_apidocs:%{__make} apidox}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian/man
if [ -f alarmd.sgml ]; then
	%{__perl} -pi -e 's/alarmd/kalarmd/;s/ALARMD/KALARMD/' alarmd.sgml
	mv -f alarmd.sgml kalarmd.sgml
fi	
for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done
cd -

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
cat kalarmd.lang >> kalarm.lang
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	konsolekalendar	--with-kde
%find_lang	kontact		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	korn		--with-kde
%find_lang	kgpgcertmanager	--with-kde
cat kgpgcertmanager.lang >> kmail.lang
%find_lang	kpilot		--with-kde
%find_lang	ktnef		--with-kde
%find_lang	kwatchgnupg	--with-kde
cat kwatchgnupg.lang >> kmail.lang

> %{name}.lang
cat kontact.lang	>> %{name}.lang
cat korganizer.lang	>> %{name}.lang
cat kalarmd.lang	>> %{name}.lang

# Omit apidocs entries
sed -i 's/.*apidocs.*//' *.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	kaddressbook-libs	-p /sbin/ldconfig
%postun	kaddressbook-libs	-p /sbin/ldconfig

%post	kmail-libs		-p /sbin/ldconfig
%postun	kmail-libs		-p /sbin/ldconfig

%post	libkcal			-p /sbin/ldconfig
%postun	libkcal			-p /sbin/ldconfig

%post	libkdenetwork		-p /sbin/ldconfig
%postun	libkdenetwork		-p /sbin/ldconfig

%post	libkdepim		-p /sbin/ldconfig
%postun	libkdepim		-p /sbin/ldconfig

%post	libknodecommon		-p /sbin/ldconfig
%postun	libknodecommon		-p /sbin/ldconfig

%post	libknotes_xmlrpc	-p /sbin/ldconfig
%postun	libknotes_xmlrpc	-p /sbin/ldconfig

%post	libkpilot		-p /sbin/ldconfig
%postun	libkpilot		-p /sbin/ldconfig

%post	libksieve		-p /sbin/ldconfig
%postun	libksieve		-p /sbin/ldconfig

%post	libktnef		-p /sbin/ldconfig
%postun	libktnef		-p /sbin/ldconfig

%post	libmimelib		-p /sbin/ldconfig
%postun	libmimelib		-p /sbin/ldconfig

%post	libs			-p /sbin/ldconfig
%postun	libs			-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
# kolabwizard
%doc README.Kolab
%attr(755,root,root) %{_bindir}/kolabwizard
%attr(755,root,root) %{_bindir}/*groupwarewizard
# kitchensync part
%attr(755,root,root) %{_bindir}/kitchensync
%{_libdir}/libdummykonnector.la
%attr(755,root,root) %{_libdir}/libdummykonnector.so
%{_libdir}/liblocalkonnector.la
%attr(755,root,root) %{_libdir}/liblocalkonnector.so
%{_libdir}/libqtopiakonnector.la
%attr(755,root,root) %{_libdir}/libqtopiakonnector.so
%{_libdir}/libremotekonnector.la
%attr(755,root,root) %{_libdir}/libremotekonnector.so
%{_libdir}/kde3/libkded_ksharedfile.la
%attr(755,root,root) %{_libdir}/kde3/libkded_ksharedfile.so
%{_libdir}/kde3/libkitchensyncpart.la
%attr(755,root,root) %{_libdir}/kde3/libkitchensyncpart.so
%{_libdir}/kde3/libksync_backup.la
%attr(755,root,root) %{_libdir}/kde3/libksync_backup.so
%{_libdir}/kde3/libksync_debugger.la
%attr(755,root,root) %{_libdir}/kde3/libksync_debugger.so
%{_libdir}/kde3/libksync_restore.la
%attr(755,root,root) %{_libdir}/kde3/libksync_restore.so
%{_libdir}/kde3/libksync_syncerpart.la
%attr(755,root,root) %{_libdir}/kde3/libksync_syncerpart.so
%{_libdir}/kde3/libksync_viewer.la
%attr(755,root,root) %{_libdir}/kde3/libksync_viewer.so
%{_libdir}/kde3/liboverviewpart.la
%attr(755,root,root) %{_libdir}/kde3/liboverviewpart.so
%{_datadir}/apps/kitchensync/ksyncgui.rc
%{_datadir}/apps/kitchensync/pics/opie.png
%{_datadir}/services/kded/ksharedfile.desktop
%{_datadir}/mimelnk/kdedevice/cellphone.desktop
%{_datadir}/mimelnk/kdedevice/pda.desktop
%{_datadir}/services/kitchensync/backup.desktop
%{_datadir}/services/kitchensync/debugger.desktop
%{_datadir}/services/kitchensync/restore.desktop
%{_datadir}/services/kitchensync/syncerpart.desktop
%{_datadir}/services/kitchensync/viewer.desktop
%dir %{_datadir}/services/kresources/konnector
%{_datadir}/services/kresources/konnector/dummykonnector.desktop
%{_datadir}/services/kresources/konnector/localkonnector.desktop
%{_datadir}/services/kresources/konnector/qtopia.desktop
%{_datadir}/services/kresources/konnector/remotekonnector.desktop
%{_datadir}/services/overview.desktop
%{_datadir}/servicetypes/kitchensync.desktop
%{_datadir}/servicetypes/konnector.desktop
# kontact part
%attr(755,root,root) %{_bindir}/kontact
%{_libdir}/kde3/kcm_kabsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabsummary.so
%{_libdir}/kde3/kcm_kmailsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmailsummary.so
%{_libdir}/kde3/kcm_kontactsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactsummary.so
%{_libdir}/kde3/kcm_korgsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_korgsummary.so
%{_libdir}/kde3/libkontact_kaddressbookplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kaddressbookplugin.so
%{_libdir}/kde3/libkontact_kmailplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kmailplugin.so
%{_libdir}/kde3/libkontact_knodeplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knodeplugin.so
%{_libdir}/kde3/libkontact_knotesplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_knotesplugin.so
%{_libdir}/kde3/libkontact_kpilotplugin.la
%attr(755,root,root) %{_libdir}/kde3/libkontact_kpilotplugin.so
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
%{_datadir}/services/kcmkabsummary.desktop
%{_datadir}/services/kcmkmailsummary.desktop
%{_datadir}/services/kcmkontactsummary.desktop
%{_datadir}/services/kcmkorgsummary.desktop
%{_datadir}/services/kontact
%{_datadir}/services/kontactconfig.desktop
%{_datadir}/servicetypes/kontactplugin.desktop
%{_desktopdir}/kde/Kontact.desktop
%{_iconsdir}/crystalsvg/*/apps/kontact.png
# korganizer part
#%attr(755,root,root) %{_bindir}/ghns
#%attr(755,root,root) %{_bindir}/khotnewstuff
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
%{_datadir}/apps/kgantt
##%{_datadir}/apps/knewstuff
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/ksync
%{_datadir}/autostart/korgac.desktop
##%{_datadir}/config/khotnewstuffrc
%{_datadir}/config.kcfg/kolab.kcfg
%{_datadir}/config.kcfg/korganizer.kcfg
%{_datadir}/services/korganizer_configcolors.desktop
%{_datadir}/services/korganizer_configfonts.desktop
%{_datadir}/services/korganizer_configfreebusy.desktop
%{_datadir}/services/korganizer_configgroupautomation.desktop
%{_datadir}/services/korganizer_configgroupscheduling.desktop
%{_datadir}/services/korganizer_configmain.desktop
%{_datadir}/services/korganizer_configtime.desktop
%{_datadir}/services/korganizer_configviews.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_desktopdir}/kde/korganizer.desktop
##%{_iconsdir}/crystalsvg/*/actions/knewstuff.png
%{_iconsdir}/*/*/*/korganizer*.png
%{_mandir}/man1/ical2vcal.1*
%{_mandir}/man1/korganizer.1*
# kresources part
%{_libdir}/kde3/kabc_imap.la
%attr(755,root,root) %{_libdir}/kde3/kabc_imap.so
%{_libdir}/kde3/kabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kabc_xmlrpc.so
%{_libdir}/kde3/kcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_xmlrpc.so
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_datadir}/services/kresources/kabc/imap.desktop
%{_datadir}/services/kresources/kabc/kabc_xmlrpc.desktop
# libkcal part
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

%files devel
%defattr(644,root,root,755)
%{_includedir}/KNotesIface.h
%{_includedir}/kmailIface.h
%{_includedir}/kmailicalIface.h
%{_includedir}/kmailpartIface.h
%{_includedir}/kabc/kcal_resourcexmlrpc.h
%{_includedir}/calendar
%{_includedir}/gpgme++
%{_includedir}/kaddressbook
%{_includedir}/kdepim
%{_includedir}/kgantt
%{_includedir}/kleo
#%{_includedir}/knewstuff
%{_includedir}/kontact
%{_includedir}/korganizer
%{_includedir}/kpilot
%{_includedir}/ksieve
%{_includedir}/ktnef
%{_includedir}/mimelib
%{_includedir}/qgpgme
%{_libdir}/libgpgme++.so
%{_libdir}/libkabinterfaces.so
%{_libdir}/libkaddressbook.so
%{_libdir}/libkalarmd.so
%{_libdir}/libkdenetwork.so
%{_libdir}/libkdepim.so
%{_libdir}/libkgantt.so
%{_libdir}/libkleopatra.so
%{_libdir}/libkmailprivate.so
#%{_libdir}/libknewstuff.so
%{_libdir}/libknodecommon.so
%{_libdir}/libknotes_xmlrpc.so
%{_libdir}/libkontact.so
%{_libdir}/libkorganizer.so
%{_libdir}/libkorganizer_eventviewer.so
%{_libdir}/libkpilot.so
%{_libdir}/libkpimexchange.so
%{_libdir}/libkpinterfaces.so
%{_libdir}/libksieve.so
%{_libdir}/libksync.so
%{_libdir}/libktnef.so
%{_libdir}/libmimelib.so
%{_libdir}/libqgpgme.so
# kitchensync part
%{_includedir}/kitchensync
%{_includedir}/ksharedfile.h
%{_libdir}/libkitchensyncui.so
%{_libdir}/libkonnector.so
%{_libdir}/libksharedfile.so
%{_libdir}/libksync2.so
# kresources-devel part
%{_includedir}/kabc/kabc_resourcexmlrpc.h
%{_libdir}/libkabc_xmlrpc.so
# libkcal-devel part
%{_includedir}/libkcal
%{_libdir}/libkcal.so
%{_libdir}/libkcal_imap.so
%{_libdir}/libkcal_xmlrpc.so

%if %{with apidocs}
%files apidocs
%defattr(644,root,root,755)
%{_kdedocdir}/en/%{name}%{!?with_cvs:-%{_snap}}-apidocs
%endif

%files -n kde-kio-sieve
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_datadir}/services/sieve.protocol

%files -n kde-kio-newimap4
%defattr(644,root,root,755)
%{_libdir}/kde3/kio_newimap4.la
%attr(755,root,root) %{_libdir}/kde3/kio_newimap4.so
%{_datadir}/services/newimap4.protocol
%{_datadir}/services/newimaps.protocol

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
%{_libdir}/kde3/libkaddrbk_instantmessaging.la
%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_instantmessaging.so
##%{_libdir}/kde3/libkaddrbk_location.la
##%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_location.so
#%{_libdir}/kde3/libkaddrbk_merge.la
#%attr(755,root,root) %{_libdir}/kde3/libkaddrbk_merge.so
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

%files kaddressbook-libs
%defattr(644,root,root,755)
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%{_libdir}/libkabinterfaces.la
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%{_datadir}/applnk/.hidden/kalarmd.desktop
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*.desktop
%{_desktopdir}/kde/kalarm.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
%{_mandir}/man1/kalarmd.1*

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop
%{_mandir}/man1/kandy.1*

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png

%files kmail -f kmail.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
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
%{_datadir}/config/libkleopatrarc
%{_datadir}/config.kcfg/kmail.kcfg
%{_datadir}/services/kmail_config_appearance.desktop
%{_datadir}/services/kmail_config_composer.desktop
%{_datadir}/services/kmail_config_identity.desktop
%{_datadir}/services/kmail_config_misc.desktop
%{_datadir}/services/kmail_config_network.desktop
%{_datadir}/services/kmail_config_security.desktop
%{_datadir}/services/kleopatra_config_appear.desktop
%{_datadir}/services/kleopatra_config_dirserv.desktop
%{_datadir}/services/kleopatra_config_dnorder.desktop
%{_datadir}/servicetypes/dcopimap.desktop
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde/KMail.desktop
%{_desktopdir}/kde/kmail_view.desktop
%{_iconsdir}/*/*/apps/kmail.png
%{_iconsdir}/*/*/apps/kmailcvt.png
%{_iconsdir}/*/*/apps/kmaillight.png
# TODO
%{_iconsdir}/*/*/apps/gpg.png
%{_iconsdir}/*/*/apps/gpgsm.png

%files kmail-libs
%defattr(644,root,root,755)
# For kmail only?
%{_libdir}/libkleopatra.la
%attr(755,root,root) %{_libdir}/libkleopatra.so.*.*.*
#
%{_libdir}/libkmailprivate.la
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*.*

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

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_libdir}/kde3/knotes_imap.la
%attr(755,root,root) %{_libdir}/kde3/knotes_imap.so
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
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png

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
%{_mandir}/man1/kpilot.1*

%files ktnef -f ktnef.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png

%files libkcal
%defattr(644,root,root,755)
%doc libkcal/{HACKING,README}
%{_libdir}/libkcal.la
%attr(755,root,root) %{_libdir}/libkcal.so.*.*.*

%files libkdenetwork
%defattr(644,root,root,755)
%doc libkdenetwork/{AUTHORS*,CLASSTREE*,DESIGN.kmime,README}
%{_libdir}/libgpgme++.la
%attr(755,root,root) %{_libdir}/libgpgme++.so.*.*.*
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*.*
%{_libdir}/libqgpgme.la
%attr(755,root,root) %{_libdir}/libqgpgme.so.*.*.*

%files libkdepim
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*

%files libknodecommon
%defattr(644,root,root,755)
%{_libdir}/libknodecommon.la
%attr(755,root,root) %{_libdir}/libknodecommon.so.*.*.*

%files libknotes_xmlrpc
%defattr(644,root,root,755)
%{_libdir}/libknotes_xmlrpc.la
%attr(755,root,root) %{_libdir}/libknotes_xmlrpc.so.*.*.*

%files libkpilot
%defattr(644,root,root,755)
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*

%files libksieve
%defattr(644,root,root,755)
%{_libdir}/libksieve.la
%attr(755,root,root) %{_libdir}/libksieve.so.*.*.*

%files libktnef
%defattr(644,root,root,755)
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*

%files libmimelib
%defattr(644,root,root,755)
%doc mimelib/{Changes,README*,Tutorial}
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*

%files libs
%defattr(644,root,root,755)
%{_libdir}/kde3/libegroupwarewizard.la
%attr(755,root,root) %{_libdir}/kde3/libegroupwarewizard.so.*.*.*
%{_libdir}/kde3/libkolabwizard.la
%attr(755,root,root) %{_libdir}/kde3/libkolabwizard.so.*.*.*
# kitchensync part
%{_libdir}/libkitchensyncui.la
%attr(755,root,root) %{_libdir}/libkitchensyncui.so.0.0.0
%{_libdir}/libkonnector.la
%attr(755,root,root) %{_libdir}/libkonnector.so.0.0.0
%{_libdir}/libksharedfile.la
%attr(755,root,root) %{_libdir}/libksharedfile.so.0.0.0
%{_libdir}/libksync2.la
%attr(755,root,root) %{_libdir}/libksync2.so.0.0.0
# kontact-libs part
%{_libdir}/libkontact.la
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
# korganizer-libs part
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*.*.*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
##%{_libdir}/libknewstuff.la
##%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%{_libdir}/libkorganizer_eventviewer.la
%attr(755,root,root) %{_libdir}/libkorganizer_eventviewer.so.*.*.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*.*.*
# kresources part
%{_libdir}/libkabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%{_libdir}/libkcal_imap.la
%attr(755,root,root) %{_libdir}/libkcal_imap.so.*.*.*
%{_libdir}/libkcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/libkcal_xmlrpc.so.*.*.*
