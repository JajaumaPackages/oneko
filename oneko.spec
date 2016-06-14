Name:		oneko
Summary: 	Cat chases the cursor
Version:	1.2
Release:	8%{?dist}
License:	Public Domain
Group:		Amusements/Graphics
# Modified Source to remove BSD images, due to copyright.
# Source0:	http://www.daidouji.com/oneko/distfiles/oneko-1.2.sakura.5.tar.gz
Source0:	oneko-1.2.sakura.5.noBSD.tar.gz
Source1:	oneko.desktop
Source2:	oneko.png
URL:		http://www.daidouji.com/oneko/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Patch0:		oneko-1.2.sakura.5-nobsd.patch
BuildRequires:	libX11-devel, imake, libXext-devel
BuildRequires:	desktop-file-utils

%description
A cat (neko) chases the cursor (now a mouse) around the screen while you 
work. Alternatively, a dog chases a bone.

%prep
%setup -q -n %{name}-%{version}.sakura.5
%patch0 -p1

%build
xmkmf -a
make CFLAGS="$RPM_OPT_FLAGS -Dlinux -D_POSIX_C_SOURCE=199309L-D_POSIX_SOURCE -D_XOPEN_SOURCE -D_BSD_SOURCE -D_SVID_SOURCE -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -DFUNCPROTO=15 -DNARROWPROTO -DSHAPE "

%install
rm -rf $RPM_BUILD_ROOT
make DESTDIR=$RPM_BUILD_ROOT install

mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mkdir -p $RPM_BUILD_ROOT%{_mandir}/ja/man1
install -p -m0644 oneko.man $RPM_BUILD_ROOT%{_mandir}/man1
install -p -m0644 oneko.man.jp $RPM_BUILD_ROOT%{_mandir}/ja/man1/oneko.man
mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications
mkdir -p $RPM_BUILD_ROOT%{_datadir}/pixmaps
install -p -m0644 %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/pixmaps
desktop-file-install --vendor fedora                            \
        --dir $RPM_BUILD_ROOT%{_datadir}/applications         \
        %{SOURCE1}
mv README README.jp
mv README-SUPP README-SUPP.jp

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README.jp README-NEW README-SUPP.jp sample.resource
%{_bindir}/oneko
%{_datadir}/applications/fedora-oneko.desktop
%{_datadir}/pixmaps/oneko.png
%{_mandir}/ja/man1/*
%{_mandir}/man1/*

%changelog
* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Thu Feb 26 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 19 2008 Fedora Release Engineering <rel-eng@fedoraproject.org> - 1.2-6
- Autorebuild for GCC 4.3

* Fri Aug 24 2007 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-5
- rebuild for BuildID

* Thu Sep 14 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-4
- FC-6 rebuild

* Tue Mar  7 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-3
- remove includedir macro, not needed
- rename japanese man page to not have .jp extension

* Thu Jan 19 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-2
- use _includedir macro
- remove _i386_ hardcode
- fix blatant typo in patch
- rename docs to jp
- use -p for install
- remove xorg-x11-proto-devel, unnecessary

* Wed Jan 18 2006 Tom "spot" Callaway <tcallawa@redhat.com> 1.2-1
- Initial package for Fedora Extras
