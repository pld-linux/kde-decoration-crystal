%define		_decoration	crystal
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.9.2
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/13969-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	9de4c855201f1175495b61f5f58de12b
URL:		http://www.kde-look.org/content/show.php?content=13969
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-devel >= 9:3.2.0
BuildRequires:	python
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRequires:	unsermake
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This decoration is very closely modelled on the fvwm2 crystal style,
it's main asset is transparency.
 
It has a sleek and simple design, but it has (pseudo) TRANSPARENT
titlebar, buttons and borders. The style can use the current colors
for the title bar and blends it with the background image of the
desktop, or just play around with the brightness and intensity of the
background image. You can define the amount of shadeness for the
active and inactive window (all between fully transparent and fully
opaque).

%description -l pl
Ta dekoracja jest modelowana bardzo blisko stylu crystal dla fvwm2,
skupiaj±c siê g³ównie na przezroczysto¶ci.

Ma g³adki i prosty wystrój, ale ma (pseudo) PRZEZROCZYST¡ belkê
tytu³ow±, przyciski i ramki. Styl mo¿e u¿ywaæ bie¿±cych kolorów dla
belki tytu³owej i mieszaæ je z obrazem t³a pulpitu, lub tylko bawiæ
siê jasno¶ci± i nasyceniem obrazu t³a. Mo¿na definiowaæ ilo¶æ
cieniowania dla aktywnego i nieaktywnego okna (wszystko miêdzy
pe³n± przezroczysto¶ci± i pe³n± nieprzezroczysto¶ci±).

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f /usr/share/automake/config.sub admin
export UNSERMAKE=/usr/share/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/kwin*.la
%attr(755,root,root) %{_libdir}/kde3/kwin*.so
%{_datadir}/apps/kwin/*.desktop
