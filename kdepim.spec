#
# TODO (still on time?):
# - find out why cant this app find gtk+.h

%define		_state		snapshots
%define		_ver		3.1.93
%define		_snap		031114

Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ•Ω∫≈©≈æ »Ø∞Ê - PIM (∞≥¿Œ ¡§∫∏ ∞¸∏Æ)
Summary(pl):	Manadøer informacji osobistej (PIM) dla KDE
Summary(ru):	≈“”œŒ¡ÃÿŒŸ  –Ã¡Œ…“œ◊›…À (PIM) ƒÃ— KDE
Summary(uk):	≈“”œŒ¡ÃÿŒŸ  –Ã¡Œ’◊¡ÃÿŒ…À (PIM) ƒÃ— KDE
Name:		kdepim
Version:	%{_ver}.%{_snap}
Release:	1
Epoch:		3
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	b30dc8fd2e84fb5cb78cbd81f95dfa28
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	pilot-link-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Environment (KDE).

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Environment
(KDE).

%description -l ru
kdepim - ‹‘œ Œ¡¬œ“ ’‘…Ã…‘ ƒÃ— ’–“¡◊Ã≈Œ…— –≈“”œŒ¡ÃÿŒœ  …Œ∆œ“Õ¡√…≈  ƒÃ—
K Desktop Environment (KDE).

%description -l uk
kdepim - √≈ Œ¡¬¶“ ’‘…Ã¶‘ ƒÃ— À≈“’◊¡ŒŒ— –≈“”œŒ¡ÃÿŒœ¿ …Œ∆œ“Õ¡√¶§¿ ƒÃ— K
Desktop Environment (KDE).

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag≥Ûwkowe do KDE pim
Summary(uk):	Ê¡ Ã… “œ⁄“œ¬À… ƒÃ— kdepim
Summary(ru):	Ê¡ ÃŸ “¡⁄“¡¬œ‘À… ƒÃ— kdepim
Group:		X11/Development/Libraries
Obsoletes:	kdenetwork-devel < 10:3.1.90
Requires:	kdelibs-devel >= 9:%{version}
Requires:	%{name}-kaddressbook-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-kontact-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-korganizer-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkmailprivate = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag≥Ûwkowe potrzebne do budowy aplikacji
bazuj±cych na kdepim.

%description devel -l uk
„≈  –¡À≈‘ Õ¶”‘…‘ÿ ∆¡ Ã… ⁄¡«œÃœ◊À¶◊ Œ≈œ¬»¶ƒŒ¶ ƒÃ— –œ¬’ƒœ◊… –“œ«“¡Õ,
¬¡⁄œ◊¡Œ…» Œ¡ kdepim.

%description devel -l ru
¸‘œ‘ –¡À≈‘ ”œƒ≈“÷…‘ ∆¡ ÃŸ ⁄¡«œÃœ◊Àœ◊ Œ≈œ¬»œƒ…ÕŸ≈ ƒÃ— –œ”‘“œ≈Œ…—
–“œ«“¡ÕÕ, œ”Œœ◊¡ŒŒŸ» Œ¡ kdepim.

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi±øka adresowa
Group:		X11/Applications
Requires:	kdelibs-kabc >= 9:%{version}
Requires:	%{name}-kaddressbook-libs = %{epoch}:%{version}-%{release}

%description kaddressbook
Address Book.

%description kaddressbook -l pl
Ksi±øka adresowa.

%package kaddressbook-libs
Summary:	Address Book - shared libs
Summary(pl):	Ksi±øka adresowa - biblioteki wspÛ≥dzielone
Group:		X11/Libraries
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-kaddressbook < 3:3.1.92.031012

%description kaddressbook-libs
Address Book - shared libs.

%description kaddressbook-libs -l pl
Ksi±øka adresowa - biblioteki wspÛ≥dzielone.

%package kandy
Summary:	A communication program between mobile phone and PC
Summary(pl):	Program do komunikacji miÍdzy PC a tel. komÛrkowym
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umoøliwia dostÍp do telefonu komÛrkowego i pozwala na
synchronizacjÍ danych z telefonu z danymi na PC.

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s≥owa "praca" w jÍzyku punjambi) ∂ledzi czas
spÍdzony na rÛønych zajÍciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunkÛw wielu klientom.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Requires:	kdebase-mailnews >= 9:%{version}
Requires:	%{name}-libkmailprivate = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-kmail

%description kmail
This is electronic mail client for KDE. It is able to retrieve mail
from POP3 accounts and from local mailboxes.

This package contains version patched for better charset support.

%description kmail -l pl
Program pocztowy dla KDE. Potrafi odczytywaÊ pocztÍ z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj± programu z poprawion± obs≥ug± zestawÛw
znakÛw.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik newsÛw dla KDE
Summary(pt_BR):	Leitor de notÌcias (news) do KDE
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	kdebase-mailnews >= 9:%{version}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-knode

%description knode
This is a news reader for KDE. It has threading and everything else
you need to be happy reading your news.

%description knode -l pl
Czytnik newsÛw dla KDE. Obs≥uguje w±tki oraz killfile.

%description knode -l pt_BR
Leitor de notÌcias (news) do KDE.

%package knotes
Summary:	Yellow cards
Summary(pl):	ØÛ≥te karteczki
Group:		X11/Applications
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszczaÊ na pulpicie notatki z opcj± wysy≥ania.
Dodatkowo, aby mÛc s≥uøyÊ za przypominajkÍ, KNotes moøe wysy≥aÊ pocztÍ
i drukowaÊ notatki, a takøe przyjmowaÊ przeci±ganie nawet ze zdalnych
komputerÛw.

%package konsolekalendar
Summary:	A command line ICard tool
Summary(pl):	NarzÍdzie dostÍpu do plikÛw kalendarza z linii poleceÒ
Group:		Applications
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
NarzÍdzie dostÍpu do plikÛw kalendarza z linii poleceÒ.

%package kontact
Summary:	An integrated shell for the PIM apps
Summary(pl):	Zintegrowany system aplikacji PIM
Group:		X11/Applications
Requires:	%{name}-kontact-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-kaplan

%description kontact
An integrated shell for the PIM apps.

%description kontact -l pl
Zintegrowany system aplikacji PIM.

%package kontact-libs
Summary:	kontact - shared libs
Summary(pl):	kontact - biblioteki wspÛ≥dzielone
Group:		X11/Libraries
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-kontact < 3:3.1.92.031012

%description kontact-libs
kontact - shared libs.

%description kontact-libs -l pl
kontact - biblioteki wspÛ≥dzielone.

%package korganizer
Summary:	A complete calendar and scheduling progra
Summary(pl):	Kalendarz wraz z harmonogramem zadaÒ
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-korganizer-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdgantt = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-kalarm
Obsoletes:	kdepim-kgantt
Obsoletes:	kdepim-kitchensync
Obsoletes:	kdepim-ksync
Obsoletes:	korganizer

%description korganizer
A complete calendar and scheduling program, which supports information
interchange with other calendar applications through the industry
standard vCalendar file format.

%description korganizer -l pl
Kalendarz wraz z harmonogramem zadaÒ (KOrganizer), ktÛry wspiera
wymianÍ informacji z innymi tego typu aplikacjami poprzez standard
przemys≥owy (vCalendar).

%description korganizer -l ru
–œÃŒœ∆’ŒÀ√…œŒ¡ÃÿŒ¡— –“œ«“¡ÕÕ¡ À¡Ã≈Œƒ¡“— … –≈“”œŒ¡ÃÿŒœ«œ –Ã¡Œ…“œ◊›…À¡
(KOrganizer –œƒƒ≈“÷…◊¡≈‘ œ¬Õ≈Œ …Œ∆œ“Õ¡√…≈  ” ƒ“’«…Õ… –“œ«“¡ÕÕ¡Õ…
‘¡Àœ«œ “œƒ¡ ﬁ≈“≈⁄ ”‘¡Œƒ¡“‘ŒŸ  ∆œ“Õ¡‘ ∆¡ Ã¡ vCalendar)

%description korganizer -l uk
–œ◊Œœ∆’ŒÀ√¶œŒ¡ÃÿŒ¡ –“œ«“¡Õ¡ À¡Ã≈Œƒ¡“¡ ‘¡ –≈“”œŒ¡ÃÿŒœ«œ
–Ã¡Œ’◊¡ÃÿŒ…À¡ (KOrganizer –¶ƒ‘“…Õ’§ œ¬Õ¶Œ …Œ∆œ“Õ¡√¶§¿ ⁄ ¶Œ€…Õ…
–“œ«“¡Õ¡Õ… ‘¡Àœ«œ “œƒ’ ﬁ≈“≈⁄ ”‘¡Œƒ¡“‘Œ…  ∆œ“Õ¡‘ ∆¡ Ã’ vCalendar)

%package korganizer-libs
Summary:	korganizer - shared libs
Summary(pl):	korganizer - biblioteki wspÛ≥dzielone
Group:		X11/Libraries
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Obsoletes:	%{name}-korganizer < 3:3.1.92.031012
Obsoletes:	%{name}-commonlibs

%description korganizer-libs
korganizer - shared libs.

%description korganizer-libs -l pl
korganizer - biblioteki wspÛ≥dzielone.

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wskaºnik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoraÁ„o da caixa de correio
Group:		X11/Applications
Requires:	kdebase-kicker >= 9:%{version}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj±cy liczbÍ wiadomo∂ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitoraÁ„o da caixa de correio.

%package kpilot
Summary:	A sync tool for palmtops
Summary(pl):	NarzÍdzie do synchronizacji z palmtopami
Group:		X11/Applications
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkpilot = %{epoch}:%{version}-%{release}
Requires:	pilot-link
Obsoletes:	kdepim-kpalmdoc
Obsoletes:	kdepim-pilot
Obsoletes:	kpilot

%description kpilot
Synchronization tool for 3Com Palm Pilots and compatible devices.

%description kpilot -l pl
NarzÍdzie do synchronizacji z 3Com Palm Pilotem i zgodnymi
urz±dzeniami.

%description kpilot -l ru
’‘…Ã…‘¡ ƒÃ— ”…Œ»“œŒ…⁄¡√…… ” 3com Palm Pilots … ”œ◊Õ≈”‘…ÕŸÕ…
” Œ…Õ… ’”‘“œ ”‘◊¡Õ…,

%description kpilot -l uk
’‘…Ã¶‘¡ ƒÃ— ”…Œ»“œŒ¶⁄¡√¶ß ⁄ 3com Palm Pilots ‘¡ ”’Õ¶”Œ…Õ… ⁄
Œ…Õ… –“…”‘“œ—Õ….

%package ktnef
Summary:	A viewer/extractor for TNEF files
Summary(pl):	Konwerter/ekstraktor plikÛw TNEF
Group:		X11/Applications
Requires:	kdebase-core >= 9:%{version}
Requires:	%{name}-libktnef = %{epoch}:%{version}-%{release}
Obsoletes:	kdenetwork-korn

%description ktnef
A viewer/extractor for TNEF files.

%description ktnef -l pl
Przegl±darka/ekstraktor plikÛw TNEF.

%package libkcal
Summary:	kcal library
Summary(pl):	Biblioteka kcal
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim

%description libkcal
kcal library.

%description libkcal -l pl
Biblioteka kcal.

%package libkdenetwork
Summary:	A network library
Summary(pl):	Biblioteka sieciowa
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdenetwork

%description libkdenetwork
A network library.

%description libkdenetwork -l pl
Biblioteka sieciowa.

%package libkdepim
Summary:	kdepim library
Summary(pl):	Biblioteka kdepim
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim

%description libkdepim
kdepim library.

%description libkdepim -l pl
Biblioteka kdepim.

%package libkdgantt
Summary:	A kdgantt library
Summary(pl):	Biblioteka kdgantt
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-korganizer-libs < 3.1.92.031029

%description libkdgantt
A kdgantt library.

%description libkdgantt -l pl
Biblioteka kdgantt.

%package libkdgantt-devel
Summary:	A kdgantt library - header files
Summary(pl):	Biblioteka kdgantt - pliki nag≥Ûwkowe
Group:		X11/Development/Libraries
Requires:	kdelibs-devel >= 9:%{version}
Obsoletes:	%{name}-devel < 3.1.92.031029

%description libkdgantt-devel
A kdgantt library - header files.

%description libkdgantt-devel -l pl
Biblioteka kdgantt - pliki nag≥Ûwkowe.

%package libkmailprivate
Summary:	kmailprivate library
Summary(pl):	Biblioteka kmailprivate
Group:		X11/Libraries
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
Requires:	%{name}-libktnef = %{epoch}:%{version}-%{release}
Requires:	%{name}-libmimelib = %{epoch}:%{version}-%{release}

%description libkmailprivate
kdmailprivate library.

%description libkmailprivate -l pl
Biblioteka kmailprivate.

%package libkpilot
Summary:	kpilot library
Summary(pl):	Biblioteka kpilot
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim

%description libkpilot
kpilot library.

%description libkpilot -l pl
Biblioteka kpilot.

%package libksieve
Summary:	ksieve library
Summary(pl):	Biblioteka ksieve
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}

%description libksieve
ksieve library.

%description libksieve -l pl
Biblioteka ksieve.

%package libktnef
Summary:	ktnef library
Summary(pl):	Biblioteka ktnef
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	%{name}-ktnef < 3:3.1.92.031012

%description libktnef
ksieve ktnef.

%description libktnef -l pl
Biblioteka ktnef.

%package libmimelib
Summary:	mimelib library, based on mimepp library
Summary(pl):	Biblioteka mimelib oparta na bibliotece mimepp
Group:		X11/Libraries
Requires:	kdelibs >= 9:%{version}
Obsoletes:	kdepim

%description libmimelib
mimelib library, based on mimepp library.

%description libmimelib -l pl
Biblioteka mimelib oparta na bibliotece mimepp.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
for f in `find . -name \*.desktop | xargs grep -l '\[nb\]'` ; do
	echo -e ',s/\[nb\]=/[no]=/\n,w' | ed $f 2>/dev/null
done

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT\
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_kdedocdir}

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	konsolekalendar	--with-kde
%find_lang	korganizer	--with-kde
%find_lang	korn		--with-kde
%find_lang	kgpgcertmanager	--with-kde
%find_lang	kpilot		--with-kde

cat kalarm.lang >> korganizer.lang
cat kalarmd.lang >> korganizer.lang
cat kgpgcertmanager.lang >> kmail.lang

for f in *.lang; do
	if grep -q %{name}-%{_snap}-apidocs $f; then
		grep -v %{name}-%{_snap}-apidocs $f > $f.tmp
		mv $f.tmp $f
	fi
done

%clean
rm -rf $RPM_BUILD_ROOT

%post	kaddressbook-libs	-p /sbin/ldconfig
%postun	kaddressbook-libs	-p /sbin/ldconfig

%post	kontact-libs		-p /sbin/ldconfig
%postun	kontact-libs		-p /sbin/ldconfig

%post	korganizer-libs		-p /sbin/ldconfig
%postun	korganizer-libs		-p /sbin/ldconfig

%post	libkcal			-p /sbin/ldconfig
%postun	libkcal			-p /sbin/ldconfig

%post	libkdenetwork		-p /sbin/ldconfig
%postun	libkdenetwork		-p /sbin/ldconfig

%post	libkdepim		-p /sbin/ldconfig
%postun	libkdepim		-p /sbin/ldconfig

%post	libkdgantt		-p /sbin/ldconfig
%postun	libkdgantt		-p /sbin/ldconfig

%post	libkmailprivate		-p /sbin/ldconfig
%postun	libkmailprivate		-p /sbin/ldconfig

%post	libkpilot		-p /sbin/ldconfig
%postun	libkpilot		-p /sbin/ldconfig

%post	libksieve		-p /sbin/ldconfig
%postun	libksieve		-p /sbin/ldconfig

%post	libktnef		-p /sbin/ldconfig
%postun	libktnef		-p /sbin/ldconfig

%post	libmimelib		-p /sbin/ldconfig
%postun	libmimelib		-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%lang(en) %{_kdedocdir}/en/%{name}-%{_snap}-apidocs
%{_includedir}/KNotesIface.h
%{_includedir}/kmailIface.h
%{_includedir}/kmailicalIface.h
%{_includedir}/kmailpartIface.h
%{_includedir}/calendar
%{_includedir}/kaddressbook
%{_includedir}/kdepim
%{_includedir}/kgantt
%{_includedir}/knewstuff
%{_includedir}/kontact
%{_includedir}/korganizer
%{_includedir}/kpilot
%{_includedir}/ksieve
%{_includedir}/ktnef
%{_includedir}/mimelib
%{_libdir}/libkabinterfaces.so
%{_libdir}/libkaddressbook.so
%{_libdir}/libkalarmd.so
%{_libdir}/libkcal.so
%{_libdir}/libkdenetwork.so
%{_libdir}/libkdepim.so
%{_libdir}/libkgantt.so
%{_libdir}/libkmailprivate.so
%{_libdir}/libknewstuff.so
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
# kitchensync part
#%{_includedir}/kitchensync
#%{_includedir}/ksharedfile.h
#%{_libdir}/libdummykonnector.so
#%{_libdir}/libkitchensyncui.so
#%{_libdir}/libkonnector.so
#%{_libdir}/libksharedfile.so
#%{_libdir}/libksync2.so
#%{_libdir}/liblocalkonnector.so
#%{_libdir}/libqtopiakonnector.so

%files kaddressbook -f kaddressbook.lang
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

%files kaddressbook-libs
%defattr(644,root,root,755)
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%{_libdir}/libkabinterfaces.la
%attr(755,root,root) %{_libdir}/libkabinterfaces.so.*.*.*

%files kandy -f kandy.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop

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
%attr(755,root,root) %{_bindir}/kgpgcertmanager
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_libdir}/kde3/libkmailpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmailpart.so*
%{_datadir}/apps/kconf_update/k[!n]*
%{_datadir}/apps/kconf_update/u*
%{_datadir}/apps/kgpgcertmanager/kgpgcertmanagerui.rc
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
%{_datadir}/services/sieve.protocol
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde/KMail.desktop
%{_iconsdir}/*/*/actions/mark_as_spam.png
%{_iconsdir}/*/*/apps/kmail.png
%{_iconsdir}/*/*/apps/kmailcvt.png
%{_iconsdir}/*/*/apps/kmaillight.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_libdir}/kde3/libknodepart.la
%attr(755,root,root) %{_libdir}/kde3/libknodepart.so*
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png

%files konsolekalendar -f konsolekalendar.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar

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

%files kontact-libs
%defattr(644,root,root,755)
%{_libdir}/libkontact.la
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*

%files korganizer -f korganizer.lang
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
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_datadir}/apps/kalarm*
%{_datadir}/apps/kgantt
%{_datadir}/apps/knewstuff
%{_datadir}/apps/korgac
%{_datadir}/apps/korganizer
%{_datadir}/apps/ksync
%{_datadir}/autostart/kalarm*.desktop
%{_datadir}/autostart/korgac.desktop
%{_datadir}/config.kcfg/korganizer.kcfg
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
%{_applnkdir}/.hidden/kalarmd.desktop
%{_desktopdir}/kde/kalarm.desktop
%{_desktopdir}/kde/korganizer.desktop
%{_iconsdir}/[!l]*/*/*/kalarm.png
%{_iconsdir}/crystalsvg/*/actions/knewstuff.png
%{_iconsdir}/*/*/*/korganizer*.png
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

%files korganizer-libs
%defattr(644,root,root,755)
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

%files ktnef
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/kde/ktnef.desktop
%{_iconsdir}/hicolor/*/apps/ktnef.png

# TODO
%files libkcal
%defattr(644,root,root,755)
%doc libkcal/{HACKING,README}
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

%files libkdenetwork
%defattr(644,root,root,755)
%doc libkdenetwork/{AUTHORS*,CLASSTREE*,DESIGN.kmime,README}
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*.*

%files libkdepim
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*

%files libkdgantt
%defattr(644,root,root,755)
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so.*.*.*

%files libkdgantt-devel
%defattr(644,root,root,755)
%{_includedir}/KDGanttView.h
%{_includedir}/KDGanttViewEventItem.h
%{_includedir}/KDGanttViewItem.h
%{_includedir}/KDGanttViewSummaryItem.h
%{_includedir}/KDGanttViewTaskItem.h
%{_includedir}/KDGanttViewTaskLink.h
%{_includedir}/KDGanttViewTaskLinkGroup.h
%{_includedir}/KDXMLTools.h
%{_libdir}/libkdgantt.so

%files libkmailprivate
%defattr(644,root,root,755)
%{_libdir}/libkmailprivate.la
%attr(755,root,root) %{_libdir}/libkmailprivate.so.*.*.*

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
