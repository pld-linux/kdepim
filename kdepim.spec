#
# TODO:
# - make separate subpackages
# - separate packages: pilot, cellphone, karm, knotes.
#
# Conditional build:
# _with_pixmapsubdirs - leave different depth/resolution icons
#
%define		_with_pixmapsubdirs	1
Summary:	Personal Information Management (PIM) for KDE
Summary(ko):	K 데스크탑 환경 - PIM (개인 정보 관리)
Summary(pl):	Zarz켨ca informacji osobistych (PIM) dla KDE
Summary(ru):	晁錄鷗죈忘木 覲죔�碌李�� (PIM) 켈� KDE
Summary(uk):	晁錄鷗죈忘木 覲죔兩죈忘�� (PIM) 켈� KDE
Name:		kdepim
Version:	3.0.5a
Release:	0.2
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
  standard przemys쿽wy vCalendar),
- Empath - klient E-Mail,
- abbrowser - czytnik ksiazki adresowej,
- kpilot - narzedzie do synchronizacji z 3Com Palm Pilot'em i
  kompatybilnymi urzadzeniami.
- twister - klient PIM.

%description -l ru
kdepim - 卜� 适쫏� 略�俓� 켈� 徠怒隆턱�� 斤錄鷗죈忘銶 �廣菊皐촁탱 켈�
K Desktop Enviromnent (KDE). kdepim 遝컵壟�� 畓탠藍憤� 妗逑怒袴�:

- KOrganizer - 饉勍軀來塏�鷗죈忘죙 妗逑怒袴� 個謙匡죠� � 斤錄鷗죈忘逑�
  覲죔�碌李�個 (KOrganizer 饉컴텀禮陸텃 苟考� �廣菊皐촁탱 � 켠朗�苽
  妗逑怒袴죌� 讀蓋하 碌컨 使瑙� 戇죔컨鹿槐� 팥魯죤 팁奸� vCalendar)
- abbrowser - 妗逑怒袴� 켈� 師턱�� 좔瑙踏銶 芥�핀,
- kpilot - 略�俓讀 켈� 譚洸碌炚憫촁� � 3com Palm Pilots � 遝勒텁燉梏苽
  � 炚苽 掠同銶戇陸苽,

%description -l uk
kdepim - 쳔 适짝� 略�迲� 켈� 愾論陸鑛� 斤錄鷗죈忘舅 �廣菊皐챈ㅐ 켈� K
Desktop Enviromnent (KDE). kdepim 稽戇�潼 讀閘 妗逑怒苽:

- KOrganizer - 饉肋軀來塏┩适景适 妗逑怒皐 個謙匡죠� 讀 斤錄鷗죈忘逑�
  覲죔兩죈忘�個 (KOrganizer 揆켬虜鼓� 苟稽� �廣菊皐챈ㅐ � ┧排苽
  妗逑怒皐苽 讀蓋하 碌켭 使瑙� 戇죔컨鹿炚� 팥魯죤 팁奸� vCalendar),
- abbrowser - 妗逑怒皐 켈� 司讀鑛� 좔瑙踏垢 芥�핀,
- kpilot - 略�迲讀 켈� 譚洸碌過憫챈� � 3com Palm Pilots 讀 撞稽踏�苽 �
  炚苽 妗�戇碌佶�.

%package pilot
Summary:	KDE support for synchronizing data with a Palm(tm) or compatible PDA
Summary(pl):	KDE - obs퀅ga synchronizacji danych z Palmem(tm) lub kompatybilnym PDA
Group:		X11/Applications
Requires:	%{name} = %{version}

%description pilot
KDE support for synchronizing data with a Palm(tm) or compatible PDA.

%description pilot -l pl
KDE - obs퀅ga synchronizacji danych z Palmem(tm) lub kompatybilnym
PDA.

%package cellphone
Summary:	KDE support for synchronizing data with cellphones
Summary(pl):	KDE - obs퀅ga synchronizacji danych z telefonami kom�rkowymi
Group:		X11/Applications
Requires:	%{name} = %{version}

%description cellphone
KDE support for synchronizing data with cellphones.

%description cellphone -l pl
KDE - obs퀅ga synchronizacji danych z telefonami kom�rkowymi.

%package karm
Summary:	Time tracking tool
Summary(pl):	Narz�dzie do 턫edzenia czasu
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	karm

%description karm
KArm - Punjambi language for "work" - tracks time spent on various
tasks. It is useful for tracking hours to be billed to different
clients.

%description karm -l pl
KArm (nazwa pochodzi od s쿽wa "praca" w j�zyku punjambi) 턫edzi czas
sp�dzony na r璨nych zaj�ciach. Jest przydatny przy obliczaniu godzin
do wystawiania rachunk�w r璨nym klientom.

%package knotes
Summary:	Post-It notes on the desktop
Summary(pl):	Notatki na desktopie, kt�re mo퓆a wysy쿪�
Group:		X11/Applications
Requires:	%{name} = %{version}
Obsoletes:	knotes

%description knotes
KNotes allows you to place Post-It notes on your desktop. In addition
to serving as a reminder, KNotes can mail and print your notes, and
accept drag and drop even from remote sites.

%description knotes -l pl
KNotes pozwala umieszcza� na desktopie notatki z opcj� wysy쿪nia.
Dodatkowo, aby m�c s퀅퓓� za przypominajk�, KNotes mo풽 wysy쿪� poczt�
i drukowa� notatki, a tak풽 przyjmowa� przeci켫anie nawet ze zdalnych
komputer�w.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nag농wkowe do KDE pim
Summary(uk):	姸奸� 碌撲苟漑 켈� kdepim
Summary(ru):	姸奸� 怒撲좌鞫漑 켈� kdepim
Group:		X11/Development/Libraries

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nag농wkowe potrzebne do budowy aplikacji
bazuj켧ych na kdepim.

%description devel -l uk
矢� 僅愾� 稽戇�潼 팁奸� 憫하卿率┹ 壙苟홀켑� 켈� 饉쫬켓慄 妗逑怒�,
쩝博陸炚� 适 kdepim.

%description devel -l ru
璜鞫 僅愾� 遝컵壟�� 팁奸� 憫하卿率窘 壙苟훰케梏� 켈� 饉戇碌턱��
妗逑怒袴, 鞠卦陸鑛謨 适 kdepim.

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
