#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Lingua
%define	pnam	Stem-Snowball-Da
Summary:	Lingua::Stem::Snowball::Da - Porter's stemming algorithm for Danish
Summary(pl):	Lingua::Stem::Snowball::Da - algorytm Portera okre¶laj±cy rdzenie s³ów dla jêzyka duñskiego
Name:		perl-Lingua-Stem-Snowball-Da
Version:	1.01
Release:	3
License:	GPL v2
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e8d9a8285bce0c9e4bedc138cd6a1501
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The stem function takes a scalar as a parameter and stems the word
according to Martin Porter's Danish stemming algorithm, which can be
found at the Snowball website: http://snowball.tartarus.org/.

%description -l pl
Funkcja okre¶laj±ca rdzenie s³ów pobiera skalarny parametr i korzysta
z algorytmu dla jêzyka duñskiego autorstwa Martina Portera. Algorytm
ten mo¿na znale¼æ na stronie Snowballa: http://snowball.tartarus.org/.

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
install stemmer.pl $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/Stem/Snowball/*.pm
%dir %{_examplesdir}/%{name}-%{version}
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}/*.pl
%{_mandir}/man3/*
