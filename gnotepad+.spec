Summary:	Simple but versatile editor for X11
Name:		gnotepad+
Version:	1.2.2
Release:	1
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source0:	http://download.sourceforge.net/gnotepad/%{name}-%{version}.tar.gz
URL:		http://gnotepad.sourceforge.net/
BuildRequires:	gnome-libs-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text editor
for systems running X11 and using GTK+. It is designed for as little bloat
as possible, while still providing many of the common features found in a
modern GUI-based text editor.

%prep
%setup -q

%build
gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT
make install \
	DESTDIR=$RPM_BUILD_ROOT \
	Applicationsdir=%{_applnkdir}/Editors

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS NEWS README TODO ChangeLog

%find_lang %{name} --with-gnome

%clean
rm -r $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/gnp
%{_mandir}/man1/*
%{_applnkdir}/Editors/gnotepad+.desktop
%{_datadir}/gnotepad+
