%define	modname	Digest-Nilsimsa
%define	modver	0.06

Summary:	Perl interface to the Nilsima Algorithm	
Name:		perl-%{modname}
Version:	%{modver}
Release:	23
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Digest-Nilsimsa
Source0:	https://cpan.metacpan.org/authors/id/V/VI/VIPUL/Digest-Nilsimsa-%{modver}.tar.gz
BuildRequires:	make
BuildRequires:	perl-devel
Requires:	perl

%description
Digest-Nilsimsa module for perl.

%prep
%setup -qn %{modname}-%{modver}

%build
# old XS: clang defaults to -Werror=implicit-function-declaration
%{__perl} Makefile.PL INSTALLDIRS=vendor \
  OPTIMIZE="%{optflags} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
find . -name Makefile -print0 | xargs -0 sed -i \
  -e 's/^\(CCFLAGS *=.*\)/\1 -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration/' \
  -e 's/^\(OPTIMIZE *=.*\)/\1 -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration/' \
  -e 's/^\(CCCDLFLAGS *=.*\)/\1 -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration/'
%make

%check
make test

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorarch}/auto/Digest/Nilsimsa
%{perl_vendorarch}/Digest/*
%{_mandir}/man3/*

