# TODO:
# - find out what's with libmal>=0.20 from http://jasonday.home.att.net/code/libmal/
# - find out why cant this app find gtk+.h

%define         _state          snapshots
%define         _ver		3.2
%define		_snap		030613
%define		_kdelibsminrel	0.%{_snap}.1


Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K µ•Ω∫≈©≈æ »Ø∞Ê - PIM (∞≥¿Œ ¡§∫∏ ∞¸∏Æ)
Summary(pl):	Manadøer informacji osobistej (PIM) dla KDE
Summary(ru):	≈“”œŒ¡ÃÿŒŸ  –Ã¡Œ…“œ◊›…À (PIM) ƒÃ— KDE
Summary(uk):	≈“”œŒ¡ÃÿŒŸ  –Ã¡Œ’◊¡ÃÿŒ…À (PIM) ƒÃ— KDE
Name:		kdepim
Version:	%{_ver}
Release:	0.%{_snap}.0.1
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://www.kernel.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
# Source0-md5:	3f5c723d13552bc3a694ddee14ca423b
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}-%{_kdelibsminrel}
BuildRequires:	pilot-link-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML
%define         _icondir        %{_datadir}/icons

%define         no_install_post_chrpath         1

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
Obsoletes:	kdenetwork-devel < 3.2
Requires:	%{name}-kaddressbook = %{version}-%{release}
Requires:	%{name}-korganizer = %{version}-%{release}
Requires:	%{name}-libmimelib = %{version}-%{release}

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
Requires:	kdelibs-kabc >= %{version}
Requires:	%{name}-libkdepim = %{version}-%{release}

%description kaddressbook
Address Book.

%description kaddressbook -l pl
Ksi±øka adresowa.

%package kandy
Summary:        A communication program between mobile phone and PC
Summary(pl):    Program do komunikacji miÍdzy PC a tel. komÛrkowym
Group:          X11/Applications
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdepim = %{version}-%{release}
Obsoletes:	%{name}-cellphone

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
Requires:	%{name}-korganizer = %{version}-%{release}

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s≥owa "praca" w jÍzyku punjambi) ∂ledzi czas
spÍdzony na rÛønych zajÍciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunkÛw wielu klientom.

%package kitchensync
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Applications
#Requires:	%{name}-korganizer = %{version}-%{release}

%description kitchensync
TODO.

%description kitchensync -l pl
TODO.

%package kmail
Summary:	KDE Mail client
Summary(pl):	Program pocztowy KDE
Summary(pt_BR):	Cliente / leitor de e-mails para o KDE
Group:		X11/Applications
Requires:	kdebase-mailnews >= %{version}
Requires:	%{name}-ktnef >= %{version}-%{release}
Requires:	%{name}-libkdenetwork >= %{version}-%{release}
Requires:	%{name}-libkdepim = %{version}-%{release}
Requires:	%{name}-libmimelib = %{version}-%{release}
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
Requires:	kdebase-core >= %{version}
Requires:	kdebase-mailnews >= %{version}
Requires:	%{name}-libkdenetwork >= %{version}-%{release}
Requires:	%{name}-libkdepim = %{version}-%{release}
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
Requires:	%{name}-korganizer = %{version}-%{release}

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
Summary:        A command line ICard tool
Summary(pl):    NarzÍdzie dostÍpu do plikÛw kalendarza z linii poleceÒ
Group:          Applications
Requires:	%{name}-korganizer = %{version}-%{release}

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
NarzÍdzie dostÍpu do plikÛw kalendarza z linii poleceÒ.

%package kontact
Summary:	An integrated shell for the PIM apps
Summary(pl):	Zintegrowany system aplikacji PIM
Group:          X11/Applications
Requires:       %{name}-kaddressbook = %{version}-%{release}
Requires:	%{name}-kmail = %{version}-%{release}
Requires:       %{name}-korganizer = %{version}-%{release}
Obsoletes:	%{name}-kaplan

%description kontact
An integrated shell for the PIM apps.

%description kontact -l pl
Zintegrowany system aplikacji PIM.

%package korganizer
Summary:        A complete calendar and scheduling progra
Summary(pl):    Kalendarz wraz z harmonogramem zadaÒ
Group:          X11/Applications
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdenetwork = %{version}-%{release}
Requires:	%{name}-libkdepim = %{version}-%{release}
Obsoletes:	%{name}-kalarm
Obsoletes:	%{name}-kgantt
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

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wskaºnik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitoraÁ„o da caixa de correio
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
Requires:	%{name}-libmimelib = %{version}-%{release}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj±cy liczbÍ wiadomo∂ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitoraÁ„o da caixa de correio.

%package kpilot
Summary:        A sync tool for palmtops
Summary(pl):    NarzÍdzie do synchronizacji z palmtopami
Group:          X11/Applications
Requires:	%{name}-korganizer = %{version}-%{release}
Requires:	pilot-link
Obsoletes:	%{name}-kpalmdoc
Obsoletes:	%{name}-pilot

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

%package ksync
Summary:        A library for syncing stuff
Summary(pl):    Biblioteka do synchronizacji rzeczy
Group:          X11/Libraries
Requires:	%{name}-korganizer = %{version}-%{release}

%description ksync
libksync is a generic library for syncing collections of data entries
like calendars, bookmarks, contacts, mail folders etc.

%description ksync -l pl
libksync jest standardow± bibliotek± do synchronizacji zbiorÛw danych
jak np. kalendarze, zak≥adki, kontakty, foldery pocztowe itp.

%package ktnef
Summary:        A viewer/extractor for TNEF files
Summary(pl):    Konwerter/ekstraktor plikÛw TNEF
Group:          X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:	kdenetwork-korn

%description ktnef
A viewer/extractor for TNEF files.

%description ktnef -l pl
Konwerter/ekstraktor plikÛw TNEF.

%package libkdenetwork
Summary:	A network library
Summary(pl):	Biblioteka sieciowa
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	kdenetwork

%description libkdenetwork
A network library.

%description libkdenetwork -l pl
Biblioteka sieciowa.

%package libkdepim
Summary:	kdepim library
Summary(pl):	Biblioteka kdepim
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name}

%description libkdepim
kdepim library.

%description libkdepim -l pl
Biblioteka kdepim.

%package libmimelib
Summary:	mimelib library, based on mimepp library
Summary(pl):	Biblioteka mimelib oparta na bibliotece mimepp
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name}

%description libmimelib
mimelib library, based on mimepp library.

%description libmimelib -l pl
Biblioteka mimelib oparta na bibliotece mimepp.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build

for plik in `find ./ -name *.desktop` ; do
	if [ -d $plik ]; then
	echo $plik
	sed -ie 's/\[nb\]/\[no\]/g' $plik
	fi
done

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT\
	kde_appsdir=%{_applnkdir} \
	kde_htmldir=%{_htmldir}

install -d $RPM_BUILD_ROOT%{_desktopdir}

ALD=$RPM_BUILD_ROOT%{_applnkdir}

install -d $ALD/KDE-Settings/Components
mv $ALD/{PIM/*,KDE-Settings/Components}

mv $ALD/Applications/[Kk]o*.desktop	$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Internet/K[!O]*.desktop		$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Internet/More/KOrn.desktop	$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Utilities/kaddressbook*.desktop	$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Utilities/k[!am]*.desktop	$RPM_BUILD_ROOT%{_desktopdir}
mv $ALD/Utilities/More/*.desktop	$RPM_BUILD_ROOT%{_desktopdir}

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
%find_lang	kandy		--with-kde
%find_lang	karm		--with-kde
%find_lang	kmail		--with-kde
%find_lang	knode		--with-kde
%find_lang	knotes		--with-kde
%find_lang	korganizer	--with-kde
%find_lang	kpilot		--with-kde

cat kalarm.lang >> korganizer.lang
cat kalarmd.lang >> korganizer.lang

%clean
rm -rf $RPM_BUILD_ROOT

%post	kaddressbook	-p /sbin/ldconfig
%postun	kaddressbook	-p /sbin/ldconfig

%post	kontact		-p /sbin/ldconfig
%postun	kontact		-p /sbin/ldconfig

%post	kitchensync	-p /sbin/ldconfig
%postun	kitchensync	-p /sbin/ldconfig

%post	korganizer	-p /sbin/ldconfig
%postun	korganizer	-p /sbin/ldconfig

%post	kpilot		-p /sbin/ldconfig
%postun	kpilot		-p /sbin/ldconfig

%post	ksync		-p /sbin/ldconfig
%postun	ksync		-p /sbin/ldconfig

%post	ktnef		-p /sbin/ldconfig
%postun	ktnef		-p /sbin/ldconfig

%post	libkdenetwork	-p /sbin/ldconfig
%postun	libkdenetwork	-p /sbin/ldconfig

%post	libkdepim	-p /sbin/ldconfig
%postun	libkdepim	-p /sbin/ldconfig

%post	libmimelib	-p /sbin/ldconfig
%postun	libmimelib	-p /sbin/ldconfig

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*.*.*
%{_libdir}/kde3/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%{_libdir}/kde3/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
%{_libdir}/kde3/ldifvcardthumbnail.la
%attr(755,root,root) %{_libdir}/kde3/ldifvcardthumbnail.so
%{_libdir}/kde3/libaddressbookpart.la
%attr(755,root,root) %{_libdir}/kde3/libaddressbookpart.so
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
%{_datadir}/services/addressbook.desktop
%{_datadir}/services/kaddressbook
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/services/ldifvcardthumbnail.desktop
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_datadir}/servicetypes/kaddressbook_xxport.desktop
%{_applnkdir}/KDE-Settings/Components/kabconfig.desktop
%{_applnkdir}/KDE-Settings/Components/kabldapconfig.desktop
%{_desktopdir}/kaddressbook.desktop
%{_icondir}/*/*/*/kaddressbook.png

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
%{_icondir}/*/*/*/karm.png

%files kitchensync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kitchensync
%{_libdir}/libagendakonnector.la
%attr(755,root,root) %{_libdir}/libagendakonnector.so.*.*.*
%{_libdir}/libdummykonnector.la
%attr(755,root,root) %{_libdir}/libdummykonnector.so.*.*.*
%{_libdir}/libkitchensyncui.la
%attr(755,root,root) %{_libdir}/libkitchensyncui.so.*.*.*
%{_libdir}/libkonnector.la
%attr(755,root,root) %{_libdir}/libkonnector.so.*.*.*
%{_libdir}/libksharedfile.la
%attr(755,root,root) %{_libdir}/libksharedfile.so.*.*.*
%{_libdir}/libqtopiakonnector.la
%attr(755,root,root) %{_libdir}/libqtopiakonnector.so.*.*.*
%{_libdir}/kde3/libkded_ksharedfile.la
%attr(755,root,root) %{_libdir}/kde3/libkded_ksharedfile.so
%{_libdir}/kde3/libksync_debugger.la
%attr(755,root,root) %{_libdir}/kde3/libksync_debugger.so
%{_libdir}/kde3/liboverviewpart.la
%attr(755,root,root) %{_libdir}/kde3/liboverviewpart.so
%{_datadir}/apps/kitchensync
%{_datadir}/mimelnk/kdedevice/cellphone.desktop
%{_datadir}/mimelnk/kdedevice/pda.desktop
%{_datadir}/services/kded/ksharedfile.desktop
%{_datadir}/services/kitchensync
%{_datadir}/services/overview.desktop
%{_datadir}/servicetypes/kitchensync.desktop
%{_datadir}/servicetypes/konnector.desktop

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
%{_desktopdir}/KMail.desktop
%{_icondir}/*/*/*/kmail*.png

%files knode -f knode.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_desktopdir}/KNode.desktop
%{_icondir}/*/*/*/knode.png

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_desktopdir}/knotes.desktop
%{_icondir}/*/*/*/knotes.png

%files konsolekalendar
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar

%files kontact
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%{_libdir}/libkontact.la
%attr(755,root,root) %{_libdir}/libkontact.so.*.*.*
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*.*.*
%{_libdir}/kde3/libkp*plugin.la
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.so
%{_libdir}/kde3/kcm_kontact.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontact.so
%{_datadir}/apps/kp*plugin
%{_datadir}/apps/kontact
%{_datadir}/apps/summaryviewpart
%{_datadir}/services/kp*plugin.*
%{_datadir}/servicetypes/kontactplugin.desktop
%{_applnkdir}/KDE-Settings/Components/kontactconfig.desktop
%{_desktopdir}/Kontact.desktop
%{_icondir}/crystalsvg/*/apps/kontact.png

%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/simplealarmdaemon
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*.*.*
%{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*.*.*
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so.*.*.*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*.*.*
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*.*.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*.*.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*.*.*
%{_libdir}/kde3/kcal_imap.la
%attr(755,root,root) %{_libdir}/kde3/kcal_imap.so
%{_libdir}/kde3/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%{_libdir}/kde3/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%{_libdir}/kde3/kcal_localdir.la
%attr(755,root,root) %{_libdir}/kde3/kcal_localdir.so
#%{_libdir}/kde3/libkcm_kcalendars.la
#%attr(755,root,root) %{_libdir}/kde3/libkcm_kcalendars.so
%{_libdir}/kde3/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%{_libdir}/kde3/liborganizerpart.la
%attr(755,root,root) %{_libdir}/kde3/liborganizerpart.so
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_datadir}/apps/kalarm*
%{_datadir}/apps/kgantt
%{_datadir}/apps/korganizer
%{_datadir}/apps/kresources
%{_datadir}/autostart/kalarm*.desktop
%{_datadir}/autostart/korgac.desktop
%{_datadir}/services/korganizer
%{_datadir}/services/kresources/kcal/imap.desktop
%{_datadir}/services/kresources/kcal/kabc.desktop
%{_datadir}/services/kresources/kcal/local.desktop
%{_datadir}/services/kresources/kcal/localdir.desktop
%{_datadir}/services/kresources/kcal/remote.desktop
%{_datadir}/services/organizer.desktop
%{_datadir}/services/webcal.protocol
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_applnkdir}/.hidden/kalarmd.desktop
#%{_applnkdir}/KDE-Settings/Components/kcalendars.desktop
%{_desktopdir}/kalarm.desktop
%{_desktopdir}/korganizer.desktop
%{_icondir}/[!l]*/*/*/kalarm.png
%{_icondir}/*/*/*/korganizer*.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/KOrn.desktop
%{_icondir}/*/*/*/korn.png

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*.*.*
%{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so*
%{_datadir}/apps/kpilot
%{_datadir}/services/*conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_desktopdir}/kpalmdoc.desktop
%{_desktopdir}/kpilot*.desktop
%{_icondir}/*/*/apps/kpalmdoc.png
%{_icondir}/[!l]*/*/*/kpilot*.png

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*.*.*
%{_datadir}/apps/ksync

%files ktnef
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*.*.*
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/ktnef.desktop
%{_icondir}/hicolor/*/apps/ktnef.png

%files libkdenetwork
%doc libkdenetwork/{AUTHORS*,CLASSTREE*,DESIGN.kmime,README}
%defattr(644,root,root,755)
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*.*.*

%files libkdepim
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*.*.*

%files libmimelib
%doc mimelib/{Changes,README*,Tutorial}
%defattr(644,root,root,755)
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*.*.*
