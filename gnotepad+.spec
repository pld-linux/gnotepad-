%define name gnotepad+
%define version 1.1.3
%define release 1
%define prefix /usr

Summary: Simple but versatile editor for X11.

Name: %{name}
Version: %{version}
Release: %{release}
Group: Applications/Editors
Copyright: Freely distributable
Url: http://members.xoom.com/ackahn/gnp
Source: %{name}-%{version}.tar.gz
Source1: gnotepad+.desktop
BuildRoot:	/tmp/%{name}-%{version}-root
Requires: gtk+ >= 1.1.13 glib >= 1.1.13

%changelog

* Tue Apr 01 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.3

* Fri Mar 19 1999 Michael Fulbright <drmike@redhat.com>
- strip binaries

* Fri Mar 12 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.2
- doesnt work with GNOME session management, disabling GNOME support

* Sun Mar 06 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.1

* Fri Feb 19 1999 Michael Fulbright <drmike@redhat.com>
- version 1.1.0

* Fri Jan 22 1999 Michael Fulbright <drmike@redhat.com>
- first attempt at spec file

%description
gnotepad+ is an easy-to-use, yet fairly feature-rich, simple text editor
for systems running X11 and using GTK+. It is designed for as little
bloat as possible, while still providing many of the common features found
in a modern GUI-based text editor.

%prep
%setup

%build
CFLAGS="$RPM_OPT_FLAGS" \
./configure %{_target} \
	--prefix=%{prefix} \
	--disable-gnome
make

%install
if [ -d $RPM_BUILD_ROOT ]; then rm -r $RPM_BUILD_ROOT; fi
mkdir -p $RPM_BUILD_ROOT%{prefix}
make prefix=$RPM_BUILD_ROOT%{prefix} install

mkdir -p $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications
install -c -m 664 %{SOURCE1} $RPM_BUILD_ROOT%{prefix}/share/gnome/apps/Applications

# strip binaries
strip `file $RPM_BUILD_ROOT/%{prefix}/bin/* | awk -F':' '/executable/ { print $1 }'`

%files
%doc AUTHORS NEWS README TODO ChangeLog
%attr(755,root,root) %{prefix}/bin/gnp
%{prefix}/man/man1/gnp.1
%{prefix}/share/gnome/apps/Applications/gnotepad+.desktop
%{prefix}/share/gnotepad+

%clean
rm -r $RPM_BUILD_ROOT
