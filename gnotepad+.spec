Summary:	Simple but versatile editor for X11
Summary(pl):	Prosty ale wszechstronny edytor dla X11
Name:		gnotepad+
Version:	1.3.3
Release:	5
License:	GPL
Group:		Applications/Editors
Source0:	http://dl.sourceforge.net/gnotepad/%{name}-%{version}.tar.gz
# Source0-md5:	00f1de16e84cbbe65d85acc542b2791f
#Patch0:		%{name}-gdk_pixbuf.patch
URL:		http://gnotepad.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
#BuildRequires:	gtkhtml-devel
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text
editor for systems running X11 and using GTK+. It is designed for as
little bloat as possible, while still providing many of the common
features found in a modern GUI-based text editor.

%description -l pl
gnotepad+ to prosty w u¿yciu, maj±cy ju¿ sporo mo¿liwo¶ci edytor
zwyk³ego tekstu dla systemów z X11 i GTK+. Zosta³ tak zaprojektowany,
by byæ mo¿liwie ma³ym, ale mieæ wiele mo¿liwo¶ci spotykanych we
wspó³czesnych edytorach tekstu z graficznym interfejsem u¿ytkownika.

%prep
%setup -q
#%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
# does not compile with gtkhtml-1.0.
%configure \
	--enable-gnome \
	--enable-gtkhtml=no
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Editors

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{_bindir}/gnp
%{_mandir}/man1/*
%{_applnkdir}/Editors/gnotepad+.desktop
%{_datadir}/gnotepad+
