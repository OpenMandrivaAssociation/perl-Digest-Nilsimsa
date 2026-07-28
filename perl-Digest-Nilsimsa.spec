%define	modname	Digest-Nilsimsa
%define	modver	0.06

Summary:	Perl interface to the Nilsima Algorithm	
Name:		perl-%{modname}
Version:	%{modver}
Release:	22
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
export CFLAGS="${CFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
export CXXFLAGS="${CXXFLAGS:-%{optflags}} -Wno-error=implicit-function-declaration -Wno-implicit-function-declaration"
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
make test

%install
%makeinstall_std

%files
%doc README 
%{perl_vendorarch}/auto/Digest/Nilsimsa
%{perl_vendorarch}/Digest/*
%{_mandir}/man3/*

