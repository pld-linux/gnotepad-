Summary:	Simple but versatile editor for X11
Summary(pl):	Prosty ale wszechstronny edytor dlaa X11
Name:		gnotepad+
Version:	1.3.3
Release:	3
License:	GPL
Group:		Applications/Editors
Source0:	ftp://download.sourceforge.net/pub/sourceforge/gnotepad/%{name}-%{version}.tar.gz
URL:		http://gnotepad.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text
editor for systems running X11 and using GTK+. It is designed for as
little bloat as possible, while still providing many of the common
features found in a modern GUI-based text editor.

%description -l pl
gnotepad+ to prosty w u¿yci, maj±cy ju¿ sporo mo¿liwo¶ci, edytor
zwyk³ego tekstu dla systemów z X11 i GTK+. Zosta³ tak zaprojektowany,
by byæ mo¿liwie ma³ym, ale mieæ wiele mo¿liwo¶ci spotykanych we
wspó³czesnych edytorach tekstu z graficznym interfejsem u¿ytkownika.

%prep
%setup -q

%build
libtoolize --copy --force
gettextize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c -f
%configure \
	--enable-gnome
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Office/Editors

gzip -9nf AUTHORS NEWS README TODO ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/gnp
%{_mandir}/man1/*
%{_applnkdir}/Office/Editors/gnotepad+.desktop
%{_datadir}/gnotepad+
