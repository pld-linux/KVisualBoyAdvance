Summary:	KVisualBoyAdvance - simple graphical frontend to the VisualBoyAdvance emulator
Summary(pl):	KVisualBoyAdvance - nak³adka graficzna na emulator VisualBoyAdvance
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
Requires:	VisualBoyAdvance
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
KVisualBoyAdvance ( "KVBA" ) is a simple graphical frontend to the
VisualBoyAdvance emulator, which lets you play Game Boy Advance(Tm)
games under Linux.

%description -l pl
KVisualBoyAdvance ( "KVBA" ) jest nak³adk± graficzn± na emulator
VisualBoyAdvance, który pozwala graæ gry przeznaczone dla Game Boy
Advance(Tm) pod Linuxem.

%prep
%setup -q -n kvisualboyadvance-%{version}

%build
%configure \
	--disable-rpath

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/kvisualboyadvance
%{_datadir}/applnk/Utilities/kvisualboyadvance.desktop
%{_datadir}/apps/kvisualboyadvance/kvisualboyadvanceui.rc
%{_docdir}/HTML/en/kvisualboyadvance/index.*
%{_iconsdir}/*/*/*/hi*/app-kvisualboyadvance.png_
%{_iconsdir}/*/*/*/kvisualboyadvance.png
