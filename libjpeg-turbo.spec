%bcond_without	tests
#
%define	libjpeg_ver	6b
Summary:	A MMX/SSE2 accelerated library for manipulating JPEG image files
Name:		libjpeg-turbo
Version:	1.0.90
Release:	1
License:	wxWidgets
Group:		Libraries
Source0:	http://downloads.sourceforge.net/project/libjpeg-turbo/%{version}%20(1.1beta1)/%{name}-%{version}.tar.gz
# Source0-md5:	9dafc998ef7662b6cf78337afde4a8bf
URL:		http://libjpeg-turbo.virtualgl.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
BuildRequires:	libtool
BuildRequires:	nasm
Provides:	libjpeg = %{libjpeg_ver}
Obsoletes:	libjpeg
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libjpeg-turbo is a version of libjpeg which uses MMX, SSE, and SSE2
SIMD instructions to accelerate baseline JPEG
compression/decompression by about 2-4x on x86 and x86-64 platforms.
It is based on libjpeg/SIMD but has numerous enhancements.

%package devel
Summary:	Headers for developing programs using libjpeg-turbo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libjpeg-devel = %{libjpeg_ver}
Obsoletes:	libjpeg-devel
Conflicts:	libjpeg6-devel

%description devel
The libjpeg-turbo-devel package includes the header files necessary
for developing programs which will manipulate JPEG files using the
libjpeg-turbo library.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von JPEG-Grafiken, einschließlich Dokumentation, zu
entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes JPEG, incluso documentación.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images JPEG, et comprend la documentation.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libjpeg-turbo. Zawiera także dokumentację.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens JPEG, incluindo documentação.

%description devel -l ru.UTF-8
В этом пакете содержится все необходимое для разработки программ,
которые работают с JPEG-изображениями включая документацию.

%description devel -l tr.UTF-8
Bu paket, JPEG resimlerini işleyen programlar geliştirmeniz için
gereken başlık dosyalarını, kitaplıkları ve ilgili yardım belgelerini
içerir.

%description devel -l uk.UTF-8
Цей пакет містить все необхідне для розробки програм, котрі працюють з
JPEG-зображеннями, включаючи документацію.

%package static
Summary:	Static library for developing programs using libjpeg-turbo
Summary(pl.UTF-8):	Biblioteka statyczna libjpeg-turbo
Summary(pt_BR.UTF-8):	Bibliotecas estáticas para desenvolvimento com libjpeg-turbo
Summary(ru.UTF-8):	Статическая библиотека для программирования с libjpeg-turbo
Summary(uk.UTF-8):	Статична бібліотека для програмування з libjpeg-turbo
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Provides:	libjpeg-static = %{libjpeg_ver}
Obsoletes:	libjpeg-static
Conflicts:	libjpeg-turbo6-static

%description static
Static library for developing programs using libjpeg-turbo.

%description static -l pl.UTF-8
Statyczna biblioteka libjpeg-turbo.

%description static -l pt_BR.UTF-8
Bibliotecas estáticas para desenvolvimento com libjpeg-turbo.

%description static -l ru.UTF-8
Этот пакет содержит статические библиотеки, необходимые для написания
программ, использующих libjpeg-turbo.

%description static -l uk.UTF-8
Цей пакет містить статичні бібліотеки, необхідні для написання
програм, що використовують libjpeg-turbo.

%package progs
Summary:	Simple clients for manipulating JPEG images
Summary(de.UTF-8):	Einfachen Clients zur Manipulation von JPEG
Summary(fr.UTF-8):	Clients simples pour manipuler des images JPEG
Summary(pl.UTF-8):	Kilka prostych programów do manipulowania na plikach JPEG
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libjpeg-progs = %{libjpeg_ver}
Obsoletes:	libjpeg-progs
Conflicts:	libjpeg-turbo6-progs

%description progs
Simple clients for manipulating JPEG images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de.UTF-8
Einfachen Clients zur Manipulation von JPEG.

%description progs -l fr.UTF-8
Clients simples pour manipuler des images JPEG.

%description progs -l pl.UTF-8
Kilka prostych programów do obróbki plików JPEG, w tym: cjpeg, djpeg,
jpegtran, rdjpgcom i wrjpgcom. djpeg dekompresuje plik JPEG do
zwykłego pliku obrazu, jpegtran potrafi wykonywać różne
przekształcenia na plikach JPEG. rdjpgcom wyświetla komentarze
tekstowe dołączone do pliku JPEG, a wrjpgcom wstawia takie komentarze.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	--enable-shared \
	--enable-static \
	--with-jpeg8

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm $RPM_BUILD_ROOT%{_includedir}/turbojpeg.h
rm $RPM_BUILD_ROOT%{_libdir}/libturbojpeg.*

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.8

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg.so
%{_libdir}/libjpeg.la
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*
