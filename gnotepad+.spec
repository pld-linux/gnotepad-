Summary:	Simple but versatile editor for X11.
Name:		gnotepad+
Version:	1.1.2
Release:	1
Group:		Applications/Editors
Copyright:	Freely distributable
Url:		http://members.xoom.com/ackahn/gnp
Source:		%{name}-%{version}.tar.gz
Source1:	gnotepad+.desktop
BuildRoot:	/tmp/%{name}-%{version}-root
Requires:	gtk+ >= 1.1.13 glib >= 1.1.13

%define		_prefix	/usr/X11R6
%define		_mandir	/usr/X11R6/man

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text editor
for systems running X11 and using GTK+. It is designed for as little
bloat as possible, while still providing many of the common features found
in a modern GUI-based text editor.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target_platform} \
	--prefix=%{_prefix} \
	--disable-gnome
make

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_prefix}
make install prefix=$RPM_BUILD_ROOT%{_prefix}

install -d $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications
install -c %{SOURCE1} $RPM_BUILD_ROOT%{_datadir}/gnome/apps/Applications

strip $RPM_BUILD_ROOT/%{_bindir}/* || :

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* AUTHORS NEWS README TODO ChangeLog

%clean
rm -r $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {AUTHORS,NEWS,README,TODO,ChangeLog}.gz
%attr(755,root,root) %{_bindir}/gnp
%{_mandir}/man1/*
%{_datadir}/gnome/apps/Applications/gnotepad+.desktop
%{_datadir}/gnotepad+
