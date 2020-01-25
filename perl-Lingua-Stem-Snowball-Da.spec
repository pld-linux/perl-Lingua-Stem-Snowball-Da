#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	Lingua
%define		pnam	Stem-Snowball-Da
Summary:	Lingua::Stem::Snowball::Da - Porter's stemming algorithm for Danish
Summary(pl.UTF-8):	Lingua::Stem::Snowball::Da - algorytm Portera określający rdzenie słów dla języka duńskiego
Name:		perl-Lingua-Stem-Snowball-Da
Version:	1.01
Release:	4
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8d9a8285bce0c9e4bedc138cd6a1501
URL:		http://search.cpan.org/dist/Lingua-Stem-Snowball-Da/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Danish stemming algorithm, which can be
found at the Snowball website: http://snowball.tartarus.org/.

%description -l pl.UTF-8
Funkcja określająca rdzenie słów pobiera skalarny parametr i korzysta
z algorytmu dla języka duńskiego autorstwa Martina Portera. Algorytm
ten można znaleźć na stronie Snowballa: http://snowball.tartarus.org/.

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
cp -p stemmer.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/Stem/Snowball/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
