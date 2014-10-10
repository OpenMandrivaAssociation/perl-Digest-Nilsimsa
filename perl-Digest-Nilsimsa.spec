%define	modname	Digest-Nilsimsa
%define	modver	0.06

Summary:	Perl interface to the Nilsima Algorithm	
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	13
License:	GPLv2 or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/authors/id/V/VI/VIPUL/%{modname}-%{modver}.tar.bz2
BuildRequires:	perl-devel
Requires:	perl

%description
Digest-Nilsimsa module for perl.

%prep
%setup -qn %{modname}-%{modver}

%build
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

