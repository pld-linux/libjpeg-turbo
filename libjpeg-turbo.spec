#
# Conditional build
%bcond_without	tests	# don't perform "make test"
%bcond_without	java	# Java binding
#
%define		libjpeg_ver	8c
%define		libjpeg_ver_lt	9-1
Summary:	A MMX/SSE2 accelerated library for manipulating JPEG image files
Summary(pl.UTF-8):	Biblioteka do obróbki plików obrazów JPEG z akceleracją MMX/SSE2
Name:		libjpeg-turbo
Version:	1.2.1
Release:	2
License:	wxWidgets
Group:		Libraries
Source0:	http://downloads.sourceforge.net/libjpeg-turbo/%{name}-%{version}.tar.gz
# Source0-md5:	f61e60ff01381ece4d2fe65eeb52669e
Patch0:		%{name}-turbojpeg.patch
URL:		http://libjpeg-turbo.virtualgl.org/
BuildRequires:	autoconf >= 2.56
BuildRequires:	automake
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libstdc++-devel
BuildRequires:	libtool
# x86* SIMD code uses NASM; arm uses gas, no SIMD code for other archs
%ifarch %{ix86} %{x8664}
BuildRequires:	nasm
%endif
Provides:	libjpeg = %{libjpeg_ver}
Obsoletes:	libjpeg < %{libjpeg_ver_lt}
Obsoletes:	libjpegsimd
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libjpeg-turbo is a version of libjpeg which uses MMX, SSE, and SSE2
SIMD instructions to accelerate baseline JPEG
compression/decompression by about 2-4x on x86 and x86-64 platforms.
It is based on libjpeg/SIMD but has numerous enhancements.

%description -l pl.UTF-8
libjpeg-turbo to wersja biblioteki libjpeg wykorzystująca instrukcje
SIMD MMX, SSE i SSE2 w celu przyspieszenia kompresji/dekompresji JPEG
o około 2-4 razy na platformach x86 i x86-64. Jest oparta na
libjpeg/SIMD, ale ma wiele rozszerzeń.

%package devel
Summary:	Headers for developing programs using libjpeg-turbo
Summary(pl.UTF-8):	Pliki nagłówkowe do tworzenia programów przy użyciu libjpeg-turbo
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Provides:	libjpeg-devel = %{libjpeg_ver}
Obsoletes:	libjpeg-devel < %{libjpeg_ver_lt}
Obsoletes:	libjpegsimd-devel
Conflicts:	libjpeg6-devel

%description devel
The libjpeg-turbo-devel package includes the header files necessary
for developing programs which will manipulate JPEG files using the
libjpeg-turbo library.

%description devel -l de.UTF-8
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von JPEG-Grafiken, zu entwickeln.

%description devel -l es.UTF-8
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen imágenes JPEG.

%description devel -l fr.UTF-8
Ce package est tout ce dont vous avez besoin pour développer des
programmes manipulant des images JPEG.

%description devel -l pl.UTF-8
Ten pakiet zawiera pliki potrzebne do programowania z wykorzystaniem
biblioteki libjpeg-turbo.

%description devel -l pt_BR.UTF-8
Este pacote é tudo que você precisa para desenvolver programas que
manipulam imagens JPEG.

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
Obsoletes:	libjpeg-static < %{libjpeg_ver_lt}
Obsoletes:	libjpegsimd-static
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
Obsoletes:	libjpeg-progs < %{libjpeg_ver_lt}
Obsoletes:	libjpegsimd-progs
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

%package -n java-turbojpeg
Summary:	Java wrapper for the TurboJPEG/OSS library
Summary(pl.UTF-8):	Interfejs Javy do biblioteki TurboJPEG/OSS
Group:		Development/Languages/Java
Requires:	%{name} = %{version}-%{release}
Requires:	jpackage-utils

%description -n java-turbojpeg
Java wrapper for the TurboJPEG/OSS library.

%description -n java-turbojpeg -l pl.UTF-8
Interfejs Javy do biblioteki TurboJPEG/OSS.

%prep
%setup -q
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}

%configure \
	%{?with_java:JNI_CFLAGS="-I%{_jvmdir}/java/include -I%{_jvmdir}/java/include/linux"} \
	--enable-shared \
	--enable-static \
	%{?with_java:--with-java} \
	--with-jpeg8

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%{__mv} $RPM_BUILD_ROOT%{_prefix}/classes/turbojpeg.jar $RPM_BUILD_ROOT%{_javadir}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README change.log
%attr(755,root,root) %{_libdir}/libjpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libjpeg.so.8
%attr(755,root,root) %{_libdir}/libturbojpeg.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libturbojpeg.so.0

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libjpeg.so
%attr(755,root,root) %{_libdir}/libturbojpeg.so
%{_libdir}/libjpeg.la
%{_libdir}/libturbojpeg.la
%{_includedir}/jconfig.h
%{_includedir}/jerror.h
%{_includedir}/jmorecfg.h
%{_includedir}/jpeglib.h
%{_includedir}/turbojpeg.h

%files static
%defattr(644,root,root,755)
%{_libdir}/libjpeg.a
%{_libdir}/libturbojpeg.a

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/cjpeg
%attr(755,root,root) %{_bindir}/djpeg
%attr(755,root,root) %{_bindir}/jpegtran
%attr(755,root,root) %{_bindir}/rdjpgcom
%attr(755,root,root) %{_bindir}/tjbench
%attr(755,root,root) %{_bindir}/wrjpgcom
%{_mandir}/man1/cjpeg.1*
%{_mandir}/man1/djpeg.1*
%{_mandir}/man1/jpegtran.1*
%{_mandir}/man1/rdjpgcom.1*
%{_mandir}/man1/wrjpgcom.1*

%if %{with java}
%files -n java-turbojpeg
%defattr(644,root,root,755)
%doc java/doc/*
%{_javadir}/turbojpeg.jar
%endif
