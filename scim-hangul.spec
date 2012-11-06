Summary:	Hangul Input Method Engine for SCIM
Summary(pl.UTF-8):	Silnik metody wprowadzania znaków Hangul dla SCIM-a
Name:		scim-hangul
Version:	0.4.0
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	adc4b79508d0cbc639f1146ae124df58
Patch0:		%{name}-gcc4.patch
URL:		http://www.scim-im.org/
BuildRequires:	gettext-devel >= 0.18.1
BuildRequires:	scim-devel >= 1.2.0
BuildRequires:	libhangul-devel >= 0.0.12
BuildRequires:	libstdc++-devel
Requires:	libhangul >= 0.0.12
Requires:	scim >= 1.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input
support.

%description -l pl.UTF-8
Scim-hangul to moduł silnika IM SCIM do obsługi wprowadzania
znaków koreańskich (Hangul).

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%lang(ko) %doc README.ko
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/hangul.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%{_datadir}/scim/icons/scim-hangul*.png
%{_datadir}/scim/hangul
