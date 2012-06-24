Summary:     Library for handling different jpeg files.
Summary(de): Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(fr): Biblioth�que pour g�rer diff�rents fichiers jpeg
Summary(pl): Biblioteka do manipulacji r�nymi plikami w formacie jpeg
Summary(tr): jpeg resimlerini i�leme kitapl���
Name:        libjpeg
Version:     6b
Release:     8
Copyright:   distributable
Group:       Libraries
Source0:     ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
Buildroot:   /tmp/%{name}-%{version}-root

%description
This package is a library of functions that manipulate jpeg images

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von 
jpeg-Bildern.

%description -l fr
Biblioth�que de fonctions qui manipulent des images jpeg

%description -l pl
Ten pakiet zawiera bibliotek� funkcji do manipulacji plikami jpeg.

%description -l tr
Bu paket, jpeg �ekillerini i�lemek i�in kitapl�klar ve basit istemciler i�erir.

%package devel
Summary:     header files for developing programs using libjpeg
Summary(de): Header zum Entwickeln von Programmen mit libjpeg
Summary(pl): Pliki nag��wkowe do biblioteki jpeg
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description devel
This package is all you need to develop programs that manipulate jpeg
images, including documentation.

%description -l de devel
Dieses Paket bietet alles, was Sie brauchen, um Programme zur Manipulation
von jpeg-Grafiken, einschlie�lich Dokumentation, zu entwickeln.

%description -l fr devel
Ce package est tout ce dont vous avez besoin pour d�velopper des
programmes manipulant des images jpg, et comprend la documentation.

%description -l pl devel
Ten pakiet pozwoli Ci na programowanie z wykorzystniem formatu jpeg.
Zawiera tak�e dokumentacj�.

%description -l tr devel
Bu paket, jpeg resimlerini i�leyen programlar geli�tirmeniz i�in gereken
ba�l�k dosyalar�n�, kitapl�klar� ve ilgili yard�m belgelerini i�erir.

%package progs
Summary:     Simple clients for manipulating jpeg images
Summary(de): Einfachen Clients zur Manipulation von jpeg
Summary(fr): Clients simples pour manipuler de telles images
Summary(pl): Kilka prostych program�w do manipulowania na plikach jpeg
Group:       Development/Libraries
Requires:    %{name} = %{version}

%description progs
Simple clients for manipulating jpeg images.

%description progs -l de
Einfachen Clients zur Manipulation von jpeg.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych program�w do manipulowania na plikach jpeg.

%package static
Summary:     Static jpeg library
Summary(pl): Statyczna bibliteka jpeg
Group:       Development/Libraries
Requires:    %{name}-devel = %{version}

%description static
Static jpeg library

%description static -l pl
Statyczna bibliteka jpeg.

%prep
%setup -q -n jpeg-%{version}

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure \
	--prefix=$RPM_BUILD_ROOT/usr \
	--enable-shared --enable-static
make
LD_LIBRARY_PATH=$PWD make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{lib,include,bin,man/man1}
make install
make install-headers
make install-lib

strip $RPM_BUILD_ROOT/usr/{lib/lib*so.*.*,/bin/*}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%attr(755, root, root) /usr/lib/lib*.so.*.*

%files devel
%defattr(644, root, root, 755)
%doc libjpeg.doc structure.doc
/usr/lib/*.so
/usr/include/*.h

%files progs
%attr(755, root, root) /usr/bin/*
%attr(644, root,  man) /usr/man/man1/*

%files static
%attr(644, root, root) /usr/lib/*.a

%changelog
* Sat Aug  8 1998 Tomasz K�oczko <kloczek@rudy.mif.pg.gda.pl>
  [6b-8]
- modified pl translation,
- added -q %setup parameter and added using %%{version} in -n,
- Buildroot changed to /tmp/%%{name}-%%{version}-root,
- added static and progs subpackages,
- some modification in %files,
- removed *.la files from devel,
- added using %%{version} macro in Source,
- added striping shared libs and binaries,
- changed Requires to "Requires: %%{name}-%%{version}".

* Thu Jul 16 1998 Wojtek �lusarczyk <wojtek@shadow.eu.org>
  [6b-7]
- added polish desciptions,
- added %defattr support.

* Tue Jun 09 1998 Prospector System <bugs@redhat.com>
- translations modified for de

* Thu Jun 04 1998 Marc Ewing <marc@redhat.com>
- up to release 4
- remove patch that set (improper) soname - libjpeg now does it itself

* Thu May 07 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri May 01 1998 Cristian Gafton <gafton@redhat.com>
- fixed build on manhattan

* Wed Apr 08 1998 Cristian Gafton <gafton@redhat.com>
- upgraded to version 6b

* Wed Oct 08 1997 Donnie Barnes <djb@redhat.com>
- new package to remove jpeg stuff from libgr and put in it's own package
