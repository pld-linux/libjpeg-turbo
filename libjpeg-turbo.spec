# TODO
# - ftp://ftp.graphicsmagick.org/pub/GraphicsMagick/delegates/ljpeg-6b.tar.gz
#
# Conditional build:
%bcond_with	crop	# "apply" crop pseudo-patch
#
Summary:	Library for handling different jpeg files
Summary(de):	Library zum Verarbeiten verschiedener jpeg-Dateien
Summary(es):	Biblioteca para manipulaci�n de diferentes archivos jpegs
Summary(fr):	Biblioth�que pour g�rer diff�rents fichiers jpeg
Summary(pl):	Biblioteka do manipulacji plikami w formacie jpeg
Summary(pt_BR):	Biblioteca para manipula��o de diferentes arquivos jpegs
Summary(ru):	���������� ��� ��������� ��������� jpeg-������
Summary(tr):	jpeg resimlerini i�leme kitapl���
Summary(uk):	��̦����� ��� ������� Ҧ�����Φ���� jpeg-���̦�
Name:		libjpeg
Version:	6b
Release:	26
License:	distributable
Group:		Libraries
Source0:	ftp://ftp.uu.net/graphics/jpeg/jpegsrc.v%{version}.tar.gz
# Source0-md5:	dbd5f3b47ed13132f04c685d608a7547
Source1:	http://www.mif.pg.gda.pl/homepages/ankry/man-PLD/%{name}-non-english-man-pages.tar.bz2
# Source1-md5:	d6342c015a489de275ada637a77dc2b0
Source2:	http://sylvana.net/jpegcrop/croppatch.tar.gz
# Source2-md5:	45d76e4226232439308e2129b64c4ea1
URL:		http://www.ijg.org/
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-arm.patch
Patch2:		%{name}-include.patch
Patch3:		%{name}-c++.patch
Patch4:		%{name}-libtool.patch
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The libjpeg package contains a library of functions for manipulating
JPEG images.

%description -l de
Dieses Paket ist eine Library mit Funktionen zur Manipulation von
jpeg-Bildern, zusammen mit einfachen Clients zur Manipulation von
jpeg.

%description -l es
Este paquete contiene una biblioteca de funciones y programas
sencillos que manipulan im�genes jpeg.

%description -l fr
Biblioth�que de fonctions qui manipulent des images jpeg, et clients
simples pour manipuler de telles images.

%description -l pl
Ten pakiet zawiera bibliotek� funkcji do manipulacji plikami jpeg.

%description -l pt_BR
Este pacote cont�m uma biblioteca de fun��es e programas simples que
manipulam imagens jpeg.

%description -l ru
���������� ������� ��� ��������� jpeg-����������� � ������� �������
��� ����� ���������.

%description -l tr
Bu paket, jpeg �ekillerini i�lemek i�in kitapl�klar ve basit
istemciler i�erir.

%description -l uk
��̦����� ����æ� ��� ������� jpeg-��������� �� ����Ԧ �̦���� ���
���ϧ �������.

%package devel
Summary:	Headers for developing programs using libjpeg
Summary(de):	Header und statische Libraries zum Entwickeln von Programmen mit libjpeg
Summary(es):	Archivos de inclusi�n y bibliotecas para desarrollar programas usando libjpeg
Summary(fr):	Biblioth�ques statiques et en-t�tes pour d�velopper avec libjpeg
Summary(pl):	Pliki nag��wkowe libjpeg
Summary(pt_BR):	Arquivos de inclus�o e bibliotecas para desenvolver programas usando libjpeg
Summary(ru):	������ � ���������� ��� ���������� ��������, ������������ libjpeg
Summary(tr):	libjpeg i�in geli�tirme kitapl�klar� ve ba�l�k dosyalar�
Summary(uk):	������ �� ¦�̦����� ��� �������� �������, �� �������������� libjpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libjpeg-devel package includes the header files and static
libraries necessary for developing programs which will manipulate JPEG
files using the libjpeg library.

If you are going to develop programs which will manipulate JPEG
images, you should install libjpeg-devel. You'll also need to have the
libjpeg package installed.

%description devel -l de
Dieses Paket bietet alles, was Sie brauchen, um Programme zur
Manipulation von jpeg-Grafiken, einschlie�lich Dokumentation, zu
entwickeln.

%description devel -l es
Este paquete es todo lo que necesitas para desarrollar programas que
manipulen im�genes jpeg, incluso documentaci�n.

%description devel -l fr
Ce package est tout ce dont vous avez besoin pour d�velopper des
programmes manipulant des images jpg, et comprend la documentation.

%description devel -l pl
Ten pakiet pozwoli Ci na programowanie z wykorzystaniem formatu jpeg.
Zawiera tak�e dokumentacj�.

%description devel -l pt_BR
Este pacote � tudo que voc� precisa para desenvolver programas que
manipulam imagens jpeg, incluindo documenta��o.

%description devel -l ru
� ���� ������ ���������� ��� ����������� ��� ���������� ��������,
������� �������� � jpeg-������������� ������� ������������.

%description devel -l tr
Bu paket, jpeg resimlerini i�leyen programlar geli�tirmeniz i�in
gereken ba�l�k dosyalar�n�, kitapl�klar� ve ilgili yard�m belgelerini
i�erir.

%description devel -l uk
��� ����� ͦ����� ��� ����Ȧ��� ��� �������� �������, ���Ҧ �������� �
jpeg-������������, ��������� ���������æ�.

%package progs
Summary:	Simple clients for manipulating jpeg images
Summary(de):	Einfachen Clients zur Manipulation von jpeg
Summary(fr):	Clients simples pour manipuler de telles images
Summary(pl):	Kilka prostych program�w do manipulowania na plikach jpeg
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description progs
Simple clients for manipulating jpeg images. Libjpeg client programs
include cjpeg, djpeg, jpegtran, rdjpgcom and wrjpgcom. Djpeg
decompresses a JPEG file into a regular image file. Jpegtran can
perform various useful transformations on JPEG files. Rdjpgcom
displays any text comments included in a JPEG file. Wrjpgcom inserts
text comments into a JPEG file.

%description progs -l de
Einfachen Clients zur Manipulation von jpeg.

%description progs -l fr
Clients simples pour manipuler de telles images.

%description progs -l pl
Kilka prostych program�w do manipulowania na plikach jpeg.

%package static
Summary:	Static libraries for developing programs using libjpeg
Summary(pl):	Biblioteki statyczne libjpeg
Summary(pt_BR):	Bibliotecas est�ticas para desenvolvimento com libjpeg
Summary(ru):	����������� ���������� ��� ���������������� � libjpeg
Summary(uk):	�������� ¦�̦����� ��� ������������� � libjpeg
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libraries for developing programs using libjpeg.

%description static -l pl
Statyczna biblioteka libjpeg.

%description static -l pt_BR
Bibliotecas est�ticas para desenvolvimento com libjpeg.

%description static -l ru
���� ����� �������� ����������� ����������, ����������� ��� ���������
��������, ������������ libjpeg.

%description static -l uk
��� ����� ͦ����� ������Φ ¦�̦�����, ����Ȧ�Φ ��� ���������
�������, �� �������������� libjpeg.

%prep
%setup  -q -n jpeg-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1
%patch4 -p1

%if %{with crop}
gzip -dc %{SOURCE2} | tar xf -
%endif

cp -f %{_datadir}/libtool/config.sub .

%build
%configure \
	--enable-shared \
	--enable-static

%{__make} \
	libdir=%{_libdir}

LD_PRELOAD=$PWD/.libs/%{name}.so make test

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_bindir},%{_mandir}/man1}


%{__make} install install-headers install-lib \
	libdir=%{_libdir} \
	DESTDIR=$RPM_BUILD_ROOT

install jversion.h $RPM_BUILD_ROOT%{_includedir}

# remove HAVE_STD{DEF,LIB}_H
# (not necessary but may generate warnings confusing autoconf)
(cd $RPM_BUILD_ROOT%{_includedir}
grep -v 'HAVE_STD..._H' jconfig.h > jconfig.h.new
mv -f jconfig.h.new jconfig.h
)

bzip2 -dc %{SOURCE1} | tar xf - -C $RPM_BUILD_ROOT%{_mandir}

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc {libjpeg,structure}.doc

%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*.h

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
%lang(fi) %{_mandir}/fi/man1/*
%lang(pl) %{_mandir}/pl/man1/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
