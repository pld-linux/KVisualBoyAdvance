Summary:	KVisualBoyAdvance - simple graphical frontend to the VisualBoyAdvance emulator
Summary(pl.UTF-8):   KVisualBoyAdvance - nakładka graficzna na emulator VisualBoyAdvance
Name:		KVisualBoyAdvance
Version:	0.3.1
Release:	1
License:	GPL v2
Group:		Applications/Emulators
Source0:	http://download.softpedia.ro/linux/kvisualboyadvance-%{version}.tar.gz
# Source0-md5:	72e4e44ad17d349ae0fde9db0c90a112
URL:		http://www.kde-apps.org/content/show.php?content=10210
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-devel
BuildRequires:	qt-devel
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	VisualBoyAdvance
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KVisualBoyAdvance ("KVBA") is a simple graphical frontend to the
VisualBoyAdvance emulator, which lets you play Game Boy Advance(TM)
games under Linux.

%description -l pl.UTF-8
KVisualBoyAdvance ("KVBA") jest nakładką graficzną na emulator
VisualBoyAdvance, który pozwala grać w gry przeznaczone dla Game Boy
Advance(TM) pod Linuksem.

%prep
%setup -q -n kvisualboyadvance-%{version}

%build
%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir}

install -d $RPM_BUILD_ROOT%{_desktopdir}/kde
mv -f $RPM_BUILD_ROOT{%{_datadir}/applnk/Utilities,%{_desktopdir}/kde}/kvisualboyadvance.desktop

%find_lang kvisualboyadvance --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f kvisualboyadvance.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kvisualboyadvance
%{_datadir}/apps/kvisualboyadvance
%{_desktopdir}/kvisualboyadvance.desktop
%{_iconsdir}/*/*/*/kvisualboyadvance.png
# ???
%{_iconsdir}/*/*/*/hi*/app-kvisualboyadvance.png_
