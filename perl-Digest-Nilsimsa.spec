%define	name	perl-Digest-Nilsimsa
%define	real_name Digest-Nilsimsa
%define	version	0.06
%define	release	%mkrel 10

Summary:	Perl interface to the Nilsima Algorithm	
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/V/VI/VIPUL/%{real_name}-%{version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
Requires:	perl

%description
Digest-Nilsimsa module for perl.

%prep
%setup -q -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OPTIMIZE="$RPM_OPT_FLAGS"

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README 
%{_mandir}/*/*
%{perl_vendorarch}/auto/Digest/Nilsimsa
%{perl_vendorarch}/Digest/*
