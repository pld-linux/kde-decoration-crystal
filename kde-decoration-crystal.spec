%define		_decoration	crystal
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	0.7.5
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/13969-%{_decoration}-%{version}.tar.bz2
# Source0-md5:	c952b13ae54bd4b460d5245577f0f884
URL:		http://www.kde-look.org/content/show.php?content=13969
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This decoration is very closely modelled on the fvwm2 crystal style, it's main asset is transparency.
 
It has a sleek and simple design, but it has (pseudo) TRANSPARENT titlebar, buttons and borders. 
The style can use the current colors for the title bar and blends it with the background image of the desktop, or just play around with the brightness and intensity of the background image. You can define the amount of shadeness for the active and inactive window (all between fully transparent and fully opaque).

#description -l pl


%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
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
