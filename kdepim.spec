# TODO:
# - find out what's with libmal>=0.20 from http://jasonday.home.att.net/code/libmal/
# - find out why cant this app find gtk+.h

%define         _state          snapshots
%define         _ver		3.2
%define		_snap		030502
%define		_kdelibsminrel	0.%{_snap}.1


Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K ����ũž ȯ�� - PIM (���� ���� ����)
Summary(pl):	Manad�er informacji osobistej (PIM) dla KDE
Summary(ru):	������������ ����������� (PIM) ��� KDE
Summary(uk):	������������ ������������ (PIM) ��� KDE
Name:		kdepim
Version:	%{_ver}
Release:	0.%{_snap}.1
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
#Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{name}-%{_snap}.tar.bz2
Source0:	http://team.pld.org.pl/~adgor/kde/%{name}-%{_snap}.tar.bz2
Patch0:		%{name}-kmail_toolbars.patch
Patch1:		%{name}-vcategories.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}-%{_kdelibsminrel}
BuildRequires:	pilot-link-devel
BuildRequires:	sed >= 4.0
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        %{_docdir}/kde/HTML

%define         no_install_post_chrpath         1

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
Summary(uk):	����� �������� ��� kdepim
Summary(ru):	����� ���������� ��� kdepim
Group:		X11/Development/Libraries
Obsoletes:	kdenetwork-devel < 3.2
Requires:	%{name}-kaddressbook = %{version}-%{release}
Requires:	%{name}-korganizer = %{version}-%{release}
Requires:	%{name}-libmimelib = %{version}-%{release}

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

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi��ka adresowa
Group:		X11/Applications
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdepim = %{version}-%{release}

%description kaddressbook
Address Book.

%description kaddressbook -l pl
Ksi��ka adresowa.

%package kandy
Summary:        A communication program between mobile phone and PC
Summary(pl):    Program do komunikacji mi�dzy PC a tel. kom�rkowym
Group:          X11/Applications
Requires:	kdebase-core >= %{version}
Requires:	%{name}-libkdepim = %{version}-%{release}
Obsoletes:	%{name}-cellphone

%description kandy
Kandy provides access to your mobile phone and allows to sync the data
on the phone with the data on your desktop computer.

%description kandy -l pl
Kandy umo�liwia dost�p do telefonu kom�rkowego i pozwala na
synchronizacj� danych z telefonu z danymi na PC.

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
KArm (nazwa pochodzi od s�owa "praca" w j�zyku punjambi) �ledzi czas
sp�dzony na r�nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w wielu klientom.

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
Program pocztowy dla KDE. Potrafi odczytywa� poczt� z kont POP3 jak i
lokalnych skrzynek.

Ten pakiet zawiera wersj� programu z poprawion� obs�ug� zestaw�w
znak�w.

%description kmail -l pt_BR
Poderoso cliente / leitor de e-mails para o KDE.

%package knode
Summary:	KDE News Reader
Summary(pl):	Czytnik news�w dla KDE
Summary(pt_BR):	Leitor de not�cias (news) do KDE
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
Czytnik news�w dla KDE. Obs�uguje w�tki oraz killfile.

%description knode -l pt_BR
Leitor de not�cias (news) do KDE.

%package knotes
Summary:	Yellow cards
Summary(pl):	��te karteczki
Group:		X11/Applications
Requires:	%{name}-korganizer = %{version}-%{release}

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na desktopie notatki z opcj� wysy�ania.
Dodatkowo, aby m�c s�u�y� za przypominajk�, KNotes mo�e wysy�a� poczt�
i drukowa� notatki, a tak�e przyjmowa� przeci�ganie nawet ze zdalnych
komputer�w.

%package konsolekalendar
Summary:        A command line ICard tool
Summary(pl):    Narz�dzie dost�pu do plik�w kalendarza z linii polece�
Group:          Applications
Requires:	%{name}-korganizer = %{version}-%{release}

%description konsolekalendar
Command line tool for accessing calendar files.

%description konsolekalendar -l pl
Narz�dzie dost�pu do plik�w kalendarza z linii polece�.

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
Summary(pl):    Kalendarz wraz z harmonogramem zada�
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
Kalendarz wraz z harmonogramem zada� (KOrganizer), kt�ry wspiera
wymian� informacji z innymi tego typu aplikacjami poprzez standard
przemys�owy (vCalendar).

%description korganizer -l ru
������������������� ��������� ��������� � ������������� ������������
(KOrganizer ������������ ����� ����������� � ������� �����������
������ ���� ����� ����������� ������ ����� vCalendar)

%description korganizer -l uk
���������æ������� �������� ��������� �� �������������
������������� (KOrganizer Ц�����դ ��ͦ� �������æ�� � ������
���������� ������ ���� ����� ����������� ������ ����� vCalendar)

%package korn
Summary:	KDE 'biff' application
Summary(pl):	Wska�nik skrzynki pocztowej dla KDE
Summary(pt_BR):	Miniaplicativo de monitora��o da caixa de correio
Group:		X11/Applications
Requires:	kdebase-kicker >= %{version}
Requires:	%{name}-libmimelib = %{version}-%{release}
Obsoletes:	kdenetwork-korn

%description korn
A simple program showing number of mails in your folders.

%description korn -l pl
Programik pokazuj�cy ilo�� wiadomo�ci w wybranych folderach
pocztowych.

%description korn -l pt_BR
Miniaplicativo de monitora��o da caixa de correio.

%package kpilot
Summary:        A sync tool for palmtops
Summary(pl):    Narz�dzie do synchronizacji z palmtopami
Group:          X11/Applications
Requires:	%{name}-korganizer = %{version}-%{release}
Requires:	pilot-link
Obsoletes:	%{name}-kpalmdoc
Obsoletes:	%{name}-pilot

%description kpilot
Synchronization tool for 3Com Palm Pilots and compatible devices.

%description kpilot -l pl
Narz�dzie do synchronizacji z 3Com Palm Pilotem i zgodnymi
urz�dzeniami.

%description kpilot -l ru
������� ��� ������������� � 3com Palm Pilots � ������������
� ���� ������������,

%description kpilot -l uk
���̦�� ��� ������Φ��æ� � 3com Palm Pilots �� ��ͦ����� �
���� ����������.

%package ksync
Summary:        A library for syncing stuff
Summary(pl):    Biblioteka do synchronizacji rzeczy
Group:          X11/Libraries
Requires:	%{name}-korganizer = %{version}-%{release}

%description ksync
libksync is a generic library for syncing collections of data entries
like calenders, bookmarks, contacts, mail folders etc.

%description ksync -l pl
libksync jest standardow� bibliotek� do synchronizacji zbior�w danych
jak np. kalendarze, zak�adki, kontakty, foldery pocztowe itp.

%package ktnef
Summary:        A viewer/extractor for TNEF files
Summary(pl):    Konwerter/ekstraktor plik�w TNEF
Group:          X11/Applications
Requires:	kdebase-core >= %{version}
Obsoletes:	kdenetwork-korn

%description ktnef
A viewer/extractor for TNEF files.

%description ktnef -l pl
Konwerter/ekstraktor plik�w TNEF.

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
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name}

%description libkdepim
TODO

%description libkdepim -l pl
TODO

%package libmimelib
Summary:	TODO
Summary(pl):	TODO
Group:		X11/Libraries
Requires:	kdelibs >= %{version}-%{_kdelibsminrel}
Obsoletes:	%{name}

%description libmimelib
TODO

%description libmimelib -l pl
TODO

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

mv $ALD/{Settings,KDE-Settings}
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

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%{_libdir}/libkaddressbook.la
%attr(755,root,root) %{_libdir}/libkaddressbook.so.*
%{_libdir}/kde3/kcm_kabconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabconfig.so
%{_libdir}/kde3/kcm_kabldapconfig.la
%attr(755,root,root) %{_libdir}/kde3/kcm_kabldapconfig.so
%{_libdir}/kde3/kfile_vcf.la
%attr(755,root,root) %{_libdir}/kde3/kfile_vcf.so
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
%{_datadir}/services/kaddressbook
%{_datadir}/services/kfile_vcf.desktop
%{_datadir}/servicetypes/dcopaddressbook.desktop
%{_datadir}/servicetypes/kaddressbook_extension.desktop
%{_datadir}/servicetypes/kaddressbook_view.desktop
%{_datadir}/servicetypes/kaddressbook_xxport.desktop
%{_applnkdir}/KDE-Settings/Components/kabconfig.desktop
%{_applnkdir}/KDE-Settings/Components/kabldapconfig.desktop
%{_desktopdir}/kaddressbook.desktop
%{_pixmapsdir}/*/*/*/kaddressbook.png

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
%{_libdir}/libkpinterfaces.la
%attr(755,root,root) %{_libdir}/libkpinterfaces.so.*
%{_libdir}/kde3/libkp*plugin.la
%attr(755,root,root) %{_libdir}/kde3/libkp*plugin.so
%{_datadir}/apps/kp*plugin
%{_datadir}/apps/kontact
%{_datadir}/services/kp*plugin.*
%{_datadir}/servicetypes/kontactplugin.desktop
%{_pixmapsdir}/crystalsvg/*/apps/kontact.png
%{_desktopdir}/Kontact.desktop

%files korganizer -f korganizer.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_bindir}/korgac
%attr(755,root,root) %{_bindir}/korganizer*
%attr(755,root,root) %{_bindir}/ical2vcal
%attr(755,root,root) %{_bindir}/simplealarmdaemon
%{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_libdir}/libkdgantt.la
%attr(755,root,root) %{_libdir}/libkdgantt.so.*
%{_libdir}/libkgantt.la
%attr(755,root,root) %{_libdir}/libkgantt.so.*
%{_libdir}/libknewstuff.la
%attr(755,root,root) %{_libdir}/libknewstuff.so.*
%{_libdir}/libkorganizer.la
%attr(755,root,root) %{_libdir}/libkorganizer.so.*
%{_libdir}/libkpimexchange.la
%attr(755,root,root) %{_libdir}/libkpimexchange.so.*
%{_libdir}/kde3/kcal_dir.la
%attr(755,root,root) %{_libdir}/kde3/kcal_dir.so
%{_libdir}/kde3/kcal_kabc.la
%attr(755,root,root) %{_libdir}/kde3/kcal_kabc.so
%{_libdir}/kde3/kcal_remote.la
%attr(755,root,root) %{_libdir}/kde3/kcal_remote.so
%{_libdir}/kde3/libkcm_kcalendars.la
%attr(755,root,root) %{_libdir}/kde3/libkcm_kcalendars.so
%{_libdir}/kde3/libkorg_*.la
%attr(755,root,root) %{_libdir}/kde3/libkorg_*.so
%{_libdir}/kde3/resourcecalendarexchange.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarexchange.so
%{_libdir}/kde3/resourcecalendarimap.la
%attr(755,root,root) %{_libdir}/kde3/resourcecalendarimap.so
%{_datadir}/apps/kalarm*
%{_datadir}/apps/kgantt
%{_datadir}/apps/korganizer
%{_datadir}/apps/kresources
%{_datadir}/autostart/kalarm*.desktop
%{_datadir}/autostart/korgac.desktop
%{_datadir}/services/korganizer
%{_datadir}/servicetypes/calendardecoration.desktop
%{_datadir}/servicetypes/calendarplugin.desktop
%{_datadir}/servicetypes/dcopcalendar.desktop
%{_datadir}/servicetypes/korganizerpart.desktop
%{_datadir}/services/webcal.protocol
%{_applnkdir}/.hidden/kalarmd.desktop
%{_applnkdir}/KDE-Settings/Components/kcalendars.desktop
%{_desktopdir}/kalarm.desktop
%{_desktopdir}/korganizer.desktop
%{_pixmapsdir}/[!l]*/*/*/kalarm.png
%{_pixmapsdir}/*/*/*/korganizer*.png

%files korn
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/korn
%{_desktopdir}/KOrn.desktop
%{_pixmapsdir}/*/*/*/korn.png

%files kpilot -f kpilot.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kpalmdoc
%attr(755,root,root) %{_bindir}/kpilot*
%{_libdir}/libkpilot.la
%attr(755,root,root) %{_libdir}/libkpilot.so.*
%{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so*
%{_datadir}/apps/kpilot
%{_datadir}/services/*conduit.desktop
%{_datadir}/servicetypes/kpilotconduit.desktop
%{_desktopdir}/kpalmdoc.desktop
%{_desktopdir}/kpilot*.desktop
%{_pixmapsdir}/*/*/apps/kpalmdoc.png
%{_pixmapsdir}/[!l]*/*/*/kpilot*.png

%files ksync
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ksync
%{_libdir}/libksync.la
%attr(755,root,root) %{_libdir}/libksync.so.*
%{_datadir}/apps/ksync

%files ktnef
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/ktnef
%{_libdir}/libktnef.la
%attr(755,root,root) %{_libdir}/libktnef.so.*
%{_datadir}/apps/ktnef
%{_datadir}/mimelnk/application/ms-tnef.desktop
%{_desktopdir}/ktnef.desktop
%{_pixmapsdir}/hicolor/*/apps/ktnef.png

%files libkdenetwork
%doc libkdenetwork/{AUTHORS*,CLASSTREE*,DESIGN.kmime,README}
%defattr(644,root,root,755)
%{_libdir}/libkdenetwork.la
%attr(755,root,root) %{_libdir}/libkdenetwork.so.*

%files libkdepim
%defattr(644,root,root,755)
%doc README*
%{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*

%files libmimelib
%doc mimelib/{Changes,README*,Tutorial}
%defattr(644,root,root,755)
%{_libdir}/libmimelib.la
%attr(755,root,root) %{_libdir}/libmimelib.so.*
