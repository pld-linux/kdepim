# TODO:
# - make separate subpackages

%define         _state          unstable                                        
%define         _kdever         kde-3.1-beta1      

Summary:	Personal Information Management (PIM) for KDE
Summary(pl):	Manadzer informacji osobistej (PIM) dla KDE
Summary(ru):	Персональный планировщик (PIM) для KDE
Summary(uk):	Персональный планувальник (PIM) для KDE
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
(KDE). kdepim zawiera nastЙpujace programy:

- KOrganizer - kalendarz wraz z harmonogramem zadaЯ (KOrganizer
  wspiera wymianЙ informacji z innymi tego typu aplikacjami poprzez
  standard przemysЁowy vCalendar),
- Empath - klient E-Mail,
- abbrowser - czytnik ksiazki adresowej,
- kpilot - narzedzie do synchronizacji z 3Com Palm Pilot'em i
  kompatybilnymi urzadzeniami.
- twister - klient PIM.

%description -l ru
kdepim - это набор утилит для управления персональной информацией для
K Desktop Enviromnent (KDE). kdepim содержит следующие программы:

- KOrganizer - полнофункциональная программа календаря и персонального
  планировщика (KOrganizer поддерживает обмен информацией с другими
  программами такого рода через стандартный формат файла vCalendar)
- abbrowser - программа для чтения адресной книги,
- kpilot - утилита для синхронизации с 3com Palm Pilots и совместимыми
  с ними устройствами,

%description -l uk
kdepim - це наб╕р утил╕т для керування персональною информац╕╓ю для K
Desktop Enviromnent (KDE). kdepim м╕стить так╕ програми:

- KOrganizer - повнофункц╕ональна програма календара та персонального
  планувальника (KOrganizer п╕дтриму╓ обм╕н информац╕╓ю з ╕ншими
  програмами такого роду через стандартний формат файлу vCalendar),
- abbrowser - програма для читання адресно╖ книги,
- kpilot - утил╕та для синхрон╕зац╕╖ з 3com Palm Pilots та сум╕сними з
  ними пристроями.

%package devel
Summary:	Development files for KDE pim
Summary(pl):	Pliki nagЁСwkowe do KDE pim
Summary(uk):	Файли розробки для kdepim
Summary(ru):	Файлы разработки для kdepim
Group:		X11/Development/Libraries

%description devel
This package contains header files needed if you wish to build
applications based on kdepim.

%description devel -l pl
Pakiet ten zawiera pliki nagЁСwkowe potzrebne do budoway aplikacji
bazuj╠cych na kdepim.

%description devel -l uk
Цей пакет м╕стить файли заголовк╕в необх╕дн╕ для побудови програм,
базованих на kdepim.

%description devel -l ru
Этот пакет содержит файлы заголовков необходимые для построения
программ, основанных на kdepim.

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
