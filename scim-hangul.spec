Summary:	Hangul Input Method Engine for SCIM
Name:		scim-hangul
Version:	0.3.2
Release:	0.1
License:	GPL v3
Group:		Libraries
Source0:	http://downloads.sourceforge.net/scim/%{name}-%{version}.tar.gz
# Source0-md5:	882460f47dd3211f94c80ed894ad05cb
Patch0:		%{name}-gcc43.patch
URL:		http://www.scim-im.org/
BuildRequires:	scim-devel >= 1.2.0
BuildRequires:	libhangul-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Scim-hangul is a SCIM IMEngine module for Korean (Hangul) input
support.

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
%doc AUTHORS README ChangeLog
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/hangul.so
%attr(755,root,root) %{_libdir}/scim-1.0/*/SetupUI/hangul-imengine-setup.so
%{_datadir}/scim/icons/scim-hangul.png
%{_datadir}/scim/hangul
