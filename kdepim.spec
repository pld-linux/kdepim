# TODO (still on time?):
# - find out why cant this app find gtk+.h
# Conditional build:
%bcond_with  i18n    # build i18n subpackages - not used in this branch
#
%define		_state		snapshots
%define		_ver		3.2.90
%define		_snap		040206

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
Source0:	http://ep09.pld-linux.org/~adgor/kde/%{name}-%{_snap}.tar.bz2
##%% Source0-md5:	657a61e0f3d90d2afec3820e77f81306
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	ed
BuildRequires:	kdelibs-devel >= 9:%{version}
BuildRequires:	libmal-devel >= 0.31
BuildRequires:	pilot-link-devel
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
BuildRequires:	zlib-devel
BuildRequires:	pcre-devel
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
Requires:	kdelibs >= 9:%{version}
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
Requires:	%{name}-libkdgantt = %{epoch}:%{version}-%{release}
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

%package kresources
Summary:        Additional kresources definitions
Summary(pl):    Dodatkowe definicje kresources
Group:          X11/Applications
Requires:       kdelibs >= 9:%{version}

%description kresources
Additional kresources definitions.

%description kresources -l pl
Dodatkowe definicje kresources.

%package kresources-devel
Summary:        Additional kresources definitions
Summary(pl):    Dodatkowe definicje kresources
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{epoch}:%{version}-%{release}

%description kresources-devel
Additional kresources definitions.

%description kresources-devel -l pl
Dodatkowe definicje kresources.

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

%package libkcal-devel
Summary:        libkcal header files
Summary(pl):    Naglowki libkcal
Group:          X11/Libraries
Requires:       kdelibs-devel >= 9:%{version}
Requires:       %{name}-libkcal = %{epoch}:%{version}-%{release}
Obsoletes:      kdepim

%description libkcal-devel
libkcal header files.

%description libkcal-devel -l pl
Naglowki libkcal.

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
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
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

%package i18n
Summary:	Internationalization and localization files for kdepim
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla pakietÛw kdepim
Group:		X11/Applications
Requires:	kdelibs-i18n >= 9:%{version}

%description i18n
Common internationalization and localization files for kdepim.

%description i18n -l pl
WspÛ≥dzielone pliki umiÍdzynarodawiaj±ce dla pakietÛw kdepim.

%package kaddressbook-i18n
Summary:	Internationalization and localization files for kaddressbook
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla kaddressbook
Group:		X11/Applications
Requires:	%{name}-kaddressbook = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description kaddressbook-i18n
Internationalization and localization files for kaddressbook.

%description kaddressbook-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla kaddressbook.

%package kandy-i18n
Summary:	Internationalization and localization files for kandy
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla kandy
Group:		X11/Applications
Requires:	%{name}-kandy = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}

%description kandy-i18n
Internationalization and localization files for kandy.

%description kandy-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla kandy.

%package karm-i18n
Summary:	Internationalization and localization files for karm
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla karm
Group:		X11/Applications
Requires:	%{name}-karm = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim-i18n = %{epoch}:%{version}-%{release}

%description karm-i18n
Internationalization and localization files for karm.

%description karm-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla karm.

%package kmail-i18n
Summary:	Internationalization and localization files for kmail
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla kmaila
Group:		X11/Applications
Requires:	%{name}-kmail = %{epoch}:%{version}-%{release}
Requires:	%{name}-ktnef-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libksieve-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-mailnews-i18n >= 9:%{version}

%description kmail-i18n
Internationalization and localization files for kmail.

%description kmail-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla kmaila.

%package knode-i18n
Summary:	Internationalization and localization files for knode
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla knode
Group:		X11/Applications
Requires:	%{name}-knode = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdepim-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-core-i18n >= 9:%{version}
Requires:	kdebase-mailnews-i18n >= 9:%{version}

%description knode-i18n
Internationalization and localization files for knode.

%description knode-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla knode.

%package knotes-i18n
Summary:	Internationalization and localization files for knotes
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla knotes
Group:		X11/Applications
Requires:	%{name}-knotes = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}

%description knotes-i18n
Internationalization and localization files for knotes.

%description knotes-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla knotes.

%package konsolekalendar-i18n
Summary:	Internationalization and localization files for konsolekalendar
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla konsolekalendara
Group:		X11/Applications
Requires:	%{name}-konsolekalendar = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}

%description konsolekalendar-i18n
Internationalization and localization files for konsolekalendar.

%description -l pl konsolekalendar-i18n
Pliki umiÍdzynarodawiaj±ce dla konsolekalendara.

%package kontact-i18n
Summary:	Internationalization and localization files for kontact
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla kontacta
Group:		X11/Applications
Requires:	%{name}-kontact = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}

%description kontact-i18n
Internationalization and localization files for kontact.

%description kontact-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla kontacta.

%package korganizer-i18n
Summary:	Internationalization and localization files for korganizer
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla korganizera
Group:		X11/Applications
Requires:	%{name}-korganizer = %{epoch}:%{version}-%{release}
Requires:	%{name}-kgantt-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-korganizer-libs-i18n = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}

%description korganizer-i18n
Internationalization and localization files for korganizer.

%description korganizer-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla korganizera.

%package korn-i18n
Summary:	Internationalization and localization files for korn
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla korna
Group:		X11/Applications
Requires:	%{name}-korn = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkdenetwork-i18n = %{epoch}:%{version}-%{release}
Requires:	kdebase-kicker-i18n >= 9:%{version}

%description korn-i18n
Internationalization and localization files for korn.

%description korn-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla korna.

%package kpilot-i18n
Summary:	Internationalization and localization files for kpilot
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla kpilota
Group:		X11/Applications
Requires:	%{name}-kpilot = %{epoch}:%{version}-%{release}
Requires:	%{name}-libkcal-i18n = %{epoch}:%{version}-%{release}

%description kpilot-i18n
Internationalization and localization files for kpilot.

%description kpilot-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla kpilota.

%package libkdepim-i18n
Summary:	Internationalization and localization files for libkdepim
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla libkdepim
Group:		X11/Applications
Requires:	%{name}-libkdepim = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libkdepim-i18n
Internationalization and localization files for libkdepim.

%description libkdepim-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla libkdepim.

%package libkdenetwork-i18n
Summary:	Internationalization and localization files for libkdenetwork
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla libkdenetwork
Group:		X11/Applications
Requires:	%{name}-libkdenetwork = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libkdenetwork-i18n
Internationalization and localization files for libkdenetwork.

%description libkdenetwork-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla libkdenetwork.

%package libksieve-i18n
Summary:	Internationalization and localization files for libksieve
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla libksieve
Group:		X11/Applications
Requires:	%{name}-libksieve = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libksieve-i18n
Internationalization and localization files for libksieve.

%description libksieve-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla libksieve.

%package korganizer-libs-i18n
Summary:	Internationalization and localization files for korganizer-libs
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla korganizer-libs
Group:		X11/Applications
Requires:	%{name}-korganizer-libs = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}
Obsoletes:	kdepim-kgantt-i18n

%description korganizer-libs-i18n
Internationalization and localization files for korganizer-libs.

%description korganizer-libs-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla korganizer-libs.

%package libkcal-i18n
Summary:	Internationalization and localization files for libkcal
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla libkcal
Group:		X11/Applications
Requires:	%{name}-libkcal = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libkcal-i18n
Internationalization and localization files for libkcal.

%description libkcal-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla libkcal.

%package ktnef-i18n
Summary:	Internationalization and localization files for ktnef
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla ktnef
Group:		X11/Applications
Requires:	%{name}-ktnef = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description ktnef-i18n
Internationalization and localization files for ktnef.

%description ktnef-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla ktnef.

%package libkdgantt-i18n
Summary:	Internationalization and localization files for libkdgantt
Summary(pl):	Pliki umiÍdzynarodawiaj±ce dla libkdgantt
Group:		X11/Applications
Requires:	%{name}-libkdgantt = %{epoch}:%{version}-%{release}
Requires:	%{name}-i18n = %{epoch}:%{version}-%{release}

%description libkdgantt-i18n
Internationalization and localization files for libkdgantt.

%description libkdgantt-i18n -l pl
Pliki umiÍdzynarodawiaj±ce dla libkdgantt.

%prep
%setup -q -n %{name}-%{_snap}
%patch0 -p1
%patch1 -p1

%build
cp /usr/share/automake/config.sub admin

export UNSERMAKE=/usr/share/unsermake/unsermake

%{__make} -f admin/Makefile.common cvs

%configure \
	--disable-rpath \
	--with-qt-libraries=%{_libdir}

%{__make} -C kpilot/conduits/vcalconduit korganizerConduit.h

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

# Debian manpages
install -d $RPM_BUILD_ROOT%{_mandir}/man1
cd debian
%{__perl} -pi -e 's/alarmd/kalarmd/;s/ALARMD/KALARMD/' alarmd.sgml
mv -f alarmd.sgml kalarmd.sgml
for f in *.sgml ; do
	base="$(basename $f .sgml)"
	upper="$(echo ${base} | tr a-z A-Z)"
	db2man $f
	install ${upper}.1 $RPM_BUILD_ROOT%{_mandir}/man1/${base}.1
done
cd ..

%if %{with i18n}
if [ -f "%{SOURCE1}" ] ; then
	bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT
	for f in $RPM_BUILD_ROOT%{_datadir}/locale/*/LC_MESSAGES/*.mo; do
		if [ "`file $f | sed -e 's/.*,//' -e 's/message.*//'`" -le 1 ] ; then
			rm -f $f
		fi
	done
else
	echo "No i18n sources found and building --with i18n. FIXIT!"
	exit 1
fi
%endif

%find_lang	kaddressbook	--with-kde
%find_lang	kalarm		--with-kde
%find_lang	kalarmd		--with-kde
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
%find_lang	kpilot		--with-kde

cat kalarm.lang >> korganizer.lang
cat kalarmd.lang >> korganizer.lang
cat kgpgcertmanager.lang >> kmail.lang

%if %{with i18n}
%find_lang alarmdaemonctrl	--with-kde
cat alarmdaemonctrl.lang >> korganizer.lang
%find_lang kalarmdgui		--with-kde
cat kalarmdgui.lang >> korganizer.lang
%find_lang ksync           --with-kde
cat ksync.lang >> korganizer.lang
%find_lang libcalendarresources --with-kde
cat libcalendarresources.lang >> korganizer.lang

%find_lang kmailcvt      --with-kde
cat kmailcvt.lang >> kmail.lang
%find_lang kfile_rfc822 --with-kde
cat kfile_rfc822.lang >> kmail.lang
%find_lang kio_sieve --with-kde
cat kio_sieve.lang >> kmail.lang

%find_lang kabc2mutt      --with-kde
cat kabc2mutt.lang >> kaddressbook.lang
%find_lang kcmkabconfig   --with-kde
cat kcmkabconfig.lang >> kaddressbook.lang
%find_lang kfile_vcf      --with-kde
cat kfile_vcf.lang >> kaddressbook.lang

# Not packaging kmobile, it was disabled by coolo
%find_lang kdgantt --with-kde
%find_lang ktnef --with-kde

%find_lang libkcal --with-kde
%find_lang libkcalsystem --with-kde
cat libkcalsystem.lang >> libkcal.lang

%find_lang libkdenetwork --with-kde
%find_lang libkdepim --with-kde
%find_lang libksieve --with-kde
%find_lang libksync --with-kde
mv {libksync,korganizer-libs}.lang
%find_lang kgantt --with-kde
cat kgantt.lang >> korganizer-libs.lang
%find_lang libkpimexchange --with-kde
cat libkpimexchange.lang >> korganizer-libs.lang
%find_lang desktop_kdepim --with-kde
%endif

files="\
	kaddressbook \
	kandy \
	karm \
	kmail \
	knode \
	knotes \
	konsolekalendar \
	kontact \
	korganizer \
	korn \
	kpilot"

for i in $files; do
	> ${i}_en.lang
        echo "%defattr(644,root,root,755)" > ${i}_en.lang
	grep en\/ ${i}.lang|grep -v apidocs >> ${i}_en.lang
	grep -v apidocs $i.lang|grep -v en\/ > ${i}.lang.1
	mv ${i}.lang.1 ${i}.lang
done

# Workaround for empty en docdirs. They are empty because all en docs are
# in the  base non-i18n package
# Grep them out

durne=`ls -1 *.lang|grep -v _en`

for i in $durne; 
do
	echo $i >> control
	grep -v en\/ $i|grep -v apidocs >> ${i}.1
	if [ -f ${i}.1 ] ; then
		mv ${i}.1 ${i}
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

%post	kresources		-p /sbin/ldconfig
%postun	kresources		-p /sbin/ldconfig

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

%if %{with i18n}
%files i18n -f desktop_kdepim.lang
%files kaddressbook-i18n -f kaddressbook.lang
%files kandy-i18n -f kandy.lang
%files karm-i18n -f karm.lang
%files kmail-i18n -f kmail.lang
%files knode-i18n -f knode.lang
%files knotes-i18n -f knotes.lang
%files konsolekalendar-i18n -f konsolekalendar.lang
%files kontact-i18n -f kontact.lang
%files korganizer-i18n -f korganizer.lang
%files korn-i18n -f korn.lang
%files kpilot-i18n -f kpilot.lang
%files libkdepim-i18n -f libkdepim.lang
%files libkdenetwork-i18n -f libkdenetwork.lang
%files libksieve-i18n -f libksieve.lang
%files korganizer-libs-i18n -f korganizer-libs.lang
%files libkcal-i18n -f libkcal.lang
%files ktnef-i18n -f ktnef.lang
%files libkdgantt-i18n -f kdgantt.lang
%endif

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

%files kaddressbook -f kaddressbook_en.lang
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

%files kandy -f kandy_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kandy*
%{_datadir}/apps/kandy
%{_datadir}/config.kcfg/kandy.kcfg
%{_desktopdir}/kde/kandy.desktop

%files karm -f karm_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_desktopdir}/kde/karm.desktop
%{_iconsdir}/*/*/*/karm.png

%files kmail -f kmail_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmail
%attr(755,root,root) %{_bindir}/kmailcvt
%attr(755,root,root) %{_bindir}/kgpgcertmanager
%{_libdir}/kde3/kcm_kmail.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kmail.so
%{_libdir}/kde3/kio_sieve.la
%attr(755,root,root) %{_libdir}/kde3/kio_sieve.so
%{_libdir}/kde3/libkmailpart.la
%attr(755,root,root) %{_libdir}/kde3/libkmailpart.so*
%{_datadir}/apps/kconf_update/k[!n]*
%{_datadir}/apps/kconf_update/u*
%{_datadir}/apps/kgpgcertmanager/kgpgcertmanagerui.rc
%{_datadir}/apps/kmail
%{_datadir}/apps/kmailcvt
%{_datadir}/services/kmail_config_appearance.desktop
%{_datadir}/services/kmail_config_composer.desktop
%{_datadir}/services/kmail_config_identity.desktop
%{_datadir}/services/kmail_config_misc.desktop
%{_datadir}/services/kmail_config_network.desktop
%{_datadir}/services/kmail_config_security.desktop
%{_datadir}/services/sieve.protocol
%{_datadir}/servicetypes/dcopmail.desktop
%{_desktopdir}/kde/KMail.desktop
#%{_iconsdir}/*/*/actions/mark_as_spam.png
%{_iconsdir}/*/*/apps/kmail.png
%{_iconsdir}/*/*/apps/kmailcvt.png
%{_iconsdir}/*/*/apps/kmaillight.png

%files knode -f knode_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knode
%{_libdir}/kde3/libknodepart.la
%attr(755,root,root) %{_libdir}/kde3/libknodepart.so*
%{_datadir}/apps/knode
%{_datadir}/services/knewsservice.protocol
%{_desktopdir}/kde/KNode.desktop
%{_iconsdir}/*/*/*/knode.png
%{_iconsdir}/*/*/*/knode2.png

%files knotes -f knotes_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_desktopdir}/kde/knotes.desktop
%{_iconsdir}/*/*/*/knotes.png

%files konsolekalendar -f konsolekalendar_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/konsolekalendar
%{_desktopdir}/kde/konsolekalendar.desktop
%{_iconsdir}/crystalsvg/*/*/konsolekalendar.png

%files kontact -f kontact_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kontact
%{_libdir}/kde3/kcm_kontactsummary.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kontactsummary.so
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
%{_datadir}/services/kcmkontactsummary.desktop
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

%files korganizer -f korganizer_en.lang
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
%{_datadir}/applnk/.hidden/kalarmd.desktop
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

%files korn -f korn_en.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/kde/KOrn.desktop
%{_iconsdir}/*/*/*/korn.png

%files kpilot -f kpilot_en.lang
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
%{_datadir}/services/kpilot_config.desktop
%{_datadir}/services/*conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_desktopdir}/kde/kpalmdoc.desktop
%{_desktopdir}/kde/kpilot*.desktop
%{_iconsdir}/*/*/apps/kpalmdoc.png
%{_iconsdir}/[!l]*/*/*/kpilot*.png

# TODO
%files kresources
%defattr(644,root,root,755)
%{_libdir}/libkabc_xmlrpc.la
%%attr(755,root,root) %{_libdir}/libkabc_xmlrpc.so.*.*.*
%{_libdir}/kde3/kabc_imap.la
%attr(755,root,root) %{_libdir}/kde3/kabc_imap.so
%{_libdir}/kde3/kabc_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kabc_xmlrpc.so
%{_libdir}/kde3/kcal_xmlrpc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_xmlrpc.so
%{_libdir}/kde3/knotes_imap.la
%attr(755,root,root) %{_libdir}/kde3/knotes_imap.so
%{_libdir}/kde3/knotes_local.la
%attr(755,root,root) %{_libdir}/kde3/knotes_local.so
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_datadir}/services/kresources/kabc/imap.desktop
%{_datadir}/services/kresources/kabc/kabc_xmlrpc.desktop
%{_datadir}/services/kresources/knotes/imap.desktop
%{_datadir}/services/kresources/knotes/local.desktop

%files kresources-devel
%defattr(644,root,root,755)
%{_includedir}/kabc/kabc_resourcexmlrpc.h
%{_libdir}/libkabc_xmlrpc.so

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

%files libkcal-devel
%defattr(644,root,root,755)
%{_includedir}/libkcal
%{_libdir}/libkcal.so

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
