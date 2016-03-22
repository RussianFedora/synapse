Name:          synapse
Version:       0.2.99.2
Release:       1%{?dist}
Summary:       A semantic file launcher

License:       GPLv3+
URL:           https://launchpad.net/synapse-project
Source0:       https://launchpad.net/%{name}-project/0.3/%{version}/+download/%{name}-%{version}.tar.xz

BuildRequires: intltool >= 0.35.0
BuildRequires: /usr/bin/desktop-file-validate
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gdk-x11-3.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(gio-unix-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(json-glib-1.0)
BuildRequires: pkgconfig(keybinder-3.0) 
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(zeitgeist-2.0)
BuildRequires: vala-devel
BuildRequires: pkgconfig(rest-0.7)
BuildRequires: pkgconfig(appindicator3-0.1)

%description
Synapse is a semantic launcher written in Vala that you can use
to start applications as well as find and access relevant documents
and files by making use of the Zeitgeist engine.

%prep
%autosetup

%build
%configure --disable-static
%make_build V=1

%install
%make_install

%find_lang %{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/applications/%{name}.desktop

%post
/bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &> /dev/null || :
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :
fi

%posttrans
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &> /dev/null || :

%files -f %{name}.lang
%doc AUTHORS ChangeLog NEWS README
%license COPYING COPYING.GPL2 COPYING.LGPL2.1
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.svg
%{_mandir}/man1/%{name}.1*

%changelog
* Tue Mar 22 2016 Maxim Orlov <murmansksity@gmail.com> - 0.2.99.2-1.R
- Update to 0.2.99.2
- Use %%autosetup macro
- Add V=1 (Make the build verbose)

* Tue Aug 11 2015 Maxim Orlov <murmansksity@gmail.com> - 0.2.99.1-1.R
- Initial package.
