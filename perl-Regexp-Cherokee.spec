#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Regexp
%define		pnam	Cherokee
Summary:	Regexp::Cherokee - regular expressions support for Cherokee Script
Summary(pl):	Regexp::Cherokee - obs³uga wyra¿eñ regularnych dla pisma Cherokee
Name:		perl-Regexp-Cherokee
Version:	0.03
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ae8d5220635ff420e5b3a711d792478e
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Regexp::Cherokee module provides POSIX style character class
definitions for working with the Cherokee syllabary. The character
classes provided by the Regexp::Cherokee package correspond to inate
properties of the script and are language independent.

%description -l pl
Modu³ Regexp::Cherokee dostarcza definicje klas znaków w stylu POSIX
dzia³aj±ce z pismem sylabicznym Cherokee. Klasy znaków dostarczone
przez pakiet Regexp::Cherokee odpowiadaj± w³asno¶ciom pisma i s±
niezale¿ne od jêzyka.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
install examples/*.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Regexp/Cherokee.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
