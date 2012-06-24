#
# TODO:
# - make separate subpackages
# - separate packages: pilot, cellphone, karm, knotes.
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K ����ũž ȯ�� - PIM (���� ���� ����)
Summary(pl):	Zarz�dca informacji osobistych (PIM) dla KDE
Summary(ru):	������������ ����������� (PIM) ��� KDE
Summary(uk):	������������ ������������ (PIM) ��� KDE
Name:		kdepim
Version:	3.0.4
Release:	3
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.bz2
# generated from kde-i18n
Source1:	kde-i18n-%{name}-%{version}.tar.bz2
Patch0:		%{name}-desktop.patch
Patch1:		%{name}-no_versioned_modules.patch
Patch2:		%{name}-desktop_2.patch
BuildRequires:	awk
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	zlib-devel
Requires:	kdelibs >= %{version}
Obsoletes:	korganizer
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define         _htmldir        %{_datadir}/doc/kde/HTML

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

%package pilot
Summary:	KDE support for synchronizing data with a Palm(tm) or compatible PDA
Summary(pl):	KDE - obs�uga synchronizacji danych z Palmem(tm) lub kompatybilnym PDA
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pilot
KDE support for synchronizing data with a Palm(tm) or compatible PDA.

%description pilot -l pl
KDE - obs�uga synchronizacji danych z Palmem(tm) lub kompatybilnym
PDA.

%package cellphone
Summary:	KDE support for synchronizing data with cellphones
Summary(pl):	KDE - obs�uga synchronizacji danych z telefonami kom�rkowymi
Group:		X11/Applications
Requires:	%{name} = %{version}

%description cellphone
KDE support for synchronizing data with cellphones.

%description cellphone -l pl
KDE - obs�uga synchronizacji danych z telefonami kom�rkowymi.

%package karm
Summary:	Time tracking tool
Summary(pl):	Narz�dzie do �ledzenia czasu
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	karm

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s�owa "praca" w j�zyku punjambi) �ledzi czas
sp�dzony na r�nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w r�nym klientom.

%package knotes
Summary:	Post-It notes on the desktop
Summary(pl):	Notatki na desktopie, kt�re mo�na wysy�a�
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	knotes

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na desktopie notatki z opcj� wysy�ania.
Dodatkowo, aby m�c s�u�y� za przypominajk�, KNotes mo�e wysy�a� poczt�
i drukowa� notatki, a tak�e przyjmowa� przeci�ganie nawet ze zdalnych
komputer�w.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag��wkowe do KDE pim
Summary(uk):	����� �������� ��� kdepim
Summary(ru):	����� ���������� ��� kdepim
Group:		X11/Development/Libraries

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

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure \
	--enable-final \
	--%{?debug:en}%{!?debug:dis}able-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/{Office/PIMs,Settings/KDE}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_applnkdir}/Settings/[!K]* $RPM_BUILD_ROOT%{_applnkdir}/Settings/KDE/
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications/*,Office/PIMs/}
install libkcal/.libs/libkcal.so.2.*.* $RPM_BUILD_ROOT%{_libdir}
install kpilot/lib/.libs/libkpilot.so.0.*.* $RPM_BUILD_ROOT%{_libdir}

# create in toplevel %%{_pixmapsdir} links to icons
for i in $RPM_BUILD_ROOT%{_pixmapsdir}/hicolor/48x48/apps/{kalarm,karm,knotes,korganizer,kpilot}.png
do
%if %{?_with_pixmapsubdirs:1}%{!?_with_pixmapsubdirs:0}
	ln -sf `echo $i | sed "s:^$RPM_BUILD_ROOT%{_pixmapsdir}/::"` $RPM_BUILD_ROOT%{_pixmapsdir}	
%else
	cp -af $i $RPM_BUILD_ROOT%{_pixmapsdir}
%endif
done

%if %{!?_with_pixmapsubdirs:1}%{?_with_pixmapsubdirs:0}
# moved
rm -f $RPM_BUILD_ROOT%{_pixmapsdir}/*color/??x??/*/{kalarm,karm,knotes,korganizer,kpilot}.png \
%endif

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT

for f in `find $RPM_BUILD_ROOT%{_applnkdir} -name '.directory' -o -name '*.desktop'` ; do
	awk -v F=$f '/^Icon=/ && !/\.xpm$/ && !/\.png$/ { $0 = $0 ".png";} { print $0; } END { if(F == ".directory") print "Type=Directory"; }' < $f > $f.tmp
	mv -f $f{.tmp,}
done

# not compiled: programs="empath ksync twister"
programs="kalarm kalarmd kalarmdgui kandy karm kgantt knotes korganizer kpilot libkcal"
> kdepim.lang
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdepim.lang
done

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files -f kdepim.lang
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.so.*.*.*

%{_libdir}/kde3/libabbrowserconduit.la
%{_libdir}/kde3/libabbrowserconduit.so
%{_libdir}/kde3/libexpenseconduit.la
%{_libdir}/kde3/libexpenseconduit.so
%{_libdir}/kde3/libknotesconduit.la
%{_libdir}/kde3/libknotesconduit.so
%{_libdir}/kde3/libnullconduit.la
%{_libdir}/kde3/libnullconduit.so
%{_libdir}/kde3/libpopmailconduit.la
%{_libdir}/kde3/libpopmailconduit.so
%{_libdir}/kde3/libtodoconduit.la
%{_libdir}/kde3/libtodoconduit.so*
%{_libdir}/kde3/libvcalconduit.la
%{_libdir}/kde3/libvcalconduit.so

%{_libdir}/kde3/libkcm_alarmdaemonctrl.??
%{_libdir}/kde3/libkorg_datenums.??
%{_libdir}/kde3/libkorg_holidays.??
%{_libdir}/kde3/libkorg_projectview.??
%{_libdir}/kde3/libkorg_webexport.??

%{_datadir}/apps/*
%{_datadir}/autostart/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/config/*
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Settings/KDE/System/*
%{_applnkdir}/Utilities/*
%{_pixmapsdir}/*/*/*/*.png
%{_pixmapsdir}/*.png

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.??
