Summary:	Simple but versatile editor for X11.
Name:		gnotepad+
Version:	1.1.4
Release:	4
License:	GPL
Group:		Applications/Editors
Group(pl):	Aplikacje/Edytory
Source:		http://ack.netpedia.net/gnp/%{name}-%{version}.tar.gz
Patch0:		gnotepad+-applnk.patch
URL:		http://members.xoom.com/ackahn/gnp/
BuildRequires:	gnome-libs-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text editor
for systems running X11 and using GTK+. It is designed for as little
bloat as possible, while still providing many of the common features found
in a modern GUI-based text editor.

%prep
%setup -q
%patch -p1

%build
automake
LDFLAGS="-s"; export LDFLAGS
%configure \
	--enable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	AUTHORS NEWS README TODO ChangeLog

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/gnp
%{_mandir}/man1/*
%{_datadir}/applnk/Applications/gnotepad+.desktop
%{_datadir}/gnotepad+
