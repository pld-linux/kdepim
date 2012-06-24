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
Release:	1
Epoch:		2
License:	GPL
Vendor:		The KDE Team
Group:		X11/Applications
Source0:	%{name}-%{version}.%{_snapshot}.tar.bz2
# generated from kde-i18n
#Source1:	kde-i18n-%{name}-%{version}.tar.bz2
BuildRequires:	bison
BuildRequires:	kdelibs-devel >= %{version}
BuildRequires:	pilot-link-devel
BuildRequires:	qt-devel >= 3.0.5
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
Pakiet ten zawiera pliki nag��wkowe potzrebne do budoway aplikacji
bazuj�cych na kdepim.

%description devel -l uk
��� ����� ͦ����� ����� �������˦� ����Ȧ�Φ ��� �������� �������,
��������� �� kdepim.

%description devel -l ru
���� ����� �������� ����� ���������� ����������� ��� ����������
��������, ���������� �� kdepim.

%prep
%setup -q

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
programs="kaddressbook kalarm kalarmd kandy karm knotes korganizer kpilot"

> kdepim.lang
for i in $programs; do
	%find_lang $i --with-kde
	cat $i.lang >> kdepim.lang
done

%clean
%{!?_without_clean:rm -rf $RPM_BUILD_ROOT}

%files -f kdepim.lang
%defattr(644,root,root,755)
%doc README*
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/*.la
%attr(755,root,root) %{_libdir}/*.so.*
%attr(755,root,root) %{_libdir}/kde3/kfile*
%attr(755,root,root) %{_libdir}/kde3/*conduit.la
%attr(755,root,root) %{_libdir}/kde3/*conduit.so.*
%attr(755,root,root) %{_libdir}/kde3/libkaddressbookpart*
%attr(755,root,root) %{_libdir}/kde3/libkorg*
%{_datadir}/apps/*
%{_datadir}/autostart/*
%{_datadir}/services/*
%{_datadir}/servicetypes/*
%{_datadir}/config/*
%{_pixmapsdir}/*/*/*/*.png
%{_applnkdir}/.hidden/kalarmd.desktop
%{_applnkdir}/Office/PIMs/*
%{_applnkdir}/Utilities/*

%files devel
%defattr(644,root,root,755)
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/kde3/*conduit.so
