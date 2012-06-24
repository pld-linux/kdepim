# TODO:
# - make separate subpackages

%define         _state          unstable
%define         _kdever         kde-3.1-beta1

Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	������������ ����������� (PIM) ��� KDE
Summary(uk):	������������ ������������ (PIM) ��� KDE
Name:		kdepim
Version:	3.0.8
Release:	3
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/%{_state}/%{_kdever}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-am.patch
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        /usr/share/doc/kde/HTML

%description
kdepim is a collection of Personal Information Management (PIM) tools
for the K Desktop Enviromnent (KDE) kdepim contains the following
applications:

- KOrganizer - a complete calendar and scheduling program (KOrganizer
  supports information interchange with other calendar applications
  through the industry standard vCalendar file format),
- Empath - an E-Mail client,
- abbrowser - an address book reader,
- kpilot - Syncronization tool for 3com Palm Pilots and compatible
  devices,
- twister - A PIM client.

%description -l pl
kdepim jest jest zestawem aplikacji PIM dla K Desktop Enviromnent
(KDE). kdepim zawiera nast�pujace programy:

- KOrganizer - kalendarz wraz z harmonogramem zada� (KOrganizer
  wspiera wymian� informacji z innymi tego typu aplikacjami poprzez
  standard przemys�owy vCalendar),
- Empath - klient E-Mail,
- abbrowser - czytnik ksiazki adresowej,
- kpilot - narzedzie do synchronizacji z 3Com Palm Pilot'em i
  kompatybilnymi urzadzeniami.
- twister - klient PIM.

%description -l ru
kdepim - ��� ����� ������ ��� ���������� ������������ ����������� ���
K Desktop Enviromnent (KDE). kdepim �������� ��������� ���������:

- KOrganizer - ������������������� ��������� ��������� � �������������
  ������������ (KOrganizer ������������ ����� ����������� � �������
  ����������� ������ ���� ����� ����������� ������ ����� vCalendar)
- abbrowser - ��������� ��� ������ �������� �����,
- kpilot - ������� ��� ������������� � 3com Palm Pilots � ������������
  � ���� ������������,

%description -l uk
kdepim - �� ��¦� ���̦� ��� ��������� ������������ �������æ�� ��� K
Desktop Enviromnent (KDE). kdepim ͦ����� ��˦ ��������:

- KOrganizer - ���������æ������� �������� ��������� �� �������������
  ������������� (KOrganizer Ц�����դ ��ͦ� �������æ�� � ������
  ���������� ������ ���� ����� ����������� ������ ����� vCalendar),
- abbrowser - �������� ��� ������� ������ϧ �����,
- kpilot - ���̦�� ��� ������Φ��æ� � 3com Palm Pilots �� ��ͦ����� �
  ���� ����������.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag��wkowe do KDE pim
Summary(uk):	����� �������� ��� kdepim
Summary(ru):	����� ���������� ��� kdepim
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}
Requires:	%{name}-common = %{version}
Requires:	%{name}-kaddressbook = %{version}
Requires:	%{name}-kalarm = %{version}

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag��wkowe potzrebne do budoway aplikacji
bazuj�cych na kdepim.

%description devel -l uk
��� ����� ͦ����� ����� �������˦� ����Ȧ�Φ ��� �������� �������,
��������� �� kdepim.

%description devel -l ru
���� ����� �������� ����� ���������� ����������� ��� ����������
��������, ���������� �� kdepim.

%package common
Summary:	Common files
Summary(pl):	Pliki wsp�lne
Group:		X11/Applications

%description common
Common files

%description common
Pliki wsp�lne

%package kaddressbook
Summary:	Address Book
Summary(pl):	Ksi��ka adresowa
Group:		X11/Applications
Requires:	%{name}-common = %{version}

%description kaddressbook
Address Book

%description kaddressbook
Ksi��ka adresowa

%package karm
Summary:	Personal timetracker
Summary(pl):	Osobisty czasomierz
Group:		X11/Applications                                                

%description karm
Personal timetracker

%description karm
Osobisty czasomierz

%package kalarm
Summary:	Alarm
Summary(pl):	Alarm
Group:		X11/Applications                       
Requires:	%{name}-common = %{version}

%description kalarm
Reminder Message Scheduler

%description kalarm
Nastawianie przypominania o zdarzeniach

%package knotes
Summary:	Yellow cards
Summary(pl):	��te karteczki
Group:		X11/Applications                                                

%description knotes
Yellow cards

%description knotes
��te karteczki

%prep
%setup -q
%patch0 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Office/PIMs

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

ALD=$RPM_BUILD_ROOT%{_applnkdir}
mv $ALD/{Applications/*,Office/PIMs}
mv $ALD/Utilities/{More/*,.}

#bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

#programs="empath kalarm kalarmd kalarmdgui kandy karm kgantt knotes \
#korganizer kpilot ksync libkcal twister"
programs="kandy korganizer kpilot"

> kdepim.lang
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdepim.lang
done

%find_lang kaddressbook		--with-kde
%find_lang kalarm               --with-kde
%find_lang kalarmd              --with-kde
cat kalarmd.lang >> kalarm.lang
%find_lang karm			--with-kde
%find_lang knotes               --with-kde

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%files -f kdepim.lang
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/?[!n][!bdl][!m]*
%attr(755,root,root) %{_libdir}/????[!acd]*.la
%attr(755,root,root) %{_libdir}/????[!acd]*.so.*
%attr(755,root,root) %{_libdir}/kde3/kfile*
%attr(755,root,root) %{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so.*
%attr(755,root,root) %{_libdir}/kde3/libkorg*
%{_datadir}/apps/?[!n][!dl][!m]*
%{_datadir}/autostart/korg*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_pixmapsdir}/*/*/*/?[!n][!dl][!m]*
%{_applnkdir}/.hidden/*
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Utilities/?[!n][!dl][!m]*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/kde3/*conduit.so

%files common
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libkdepim.la
%attr(755,root,root) %{_libdir}/libkdepim.so.*

%files kaddressbook -f kaddressbook.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kabc2mutt
%attr(755,root,root) %{_bindir}/kaddressbook
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart*
%{_datadir}/apps/kaddressbook
%{_pixmapsdir}/*/*/*/kaddressbook.png
%{_applnkdir}/Utilities/kaddressbook.desktop

%files kalarm -f kalarm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kalarm*
%attr(755,root,root) %{_libdir}/libkalarmd.la
%attr(755,root,root) %{_libdir}/libkalarmd.so.*
%attr(755,root,root) %{_libdir}/libkcal*.la
%attr(755,root,root) %{_libdir}/libkcal*.so.*
%{_datadir}/apps/kalarm*
%{_datadir}/autostart/kalarm*
%{_pixmapsdir}/*/*/*/kalarm.png
%{_applnkdir}/Utilities/kalarm.desktop

%files karm -f karm.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/karm
%{_datadir}/apps/karm
%{_pixmapsdir}/*/*/*/karm.png
%{_applnkdir}/Utilities/karm.desktop

%files knotes -f knotes.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/knotes
%{_datadir}/apps/knotes
%{_datadir}/config/*
%{_pixmapsdir}/*/*/*/knotes.png
%{_applnkdir}/Utilities/knotes.desktop
