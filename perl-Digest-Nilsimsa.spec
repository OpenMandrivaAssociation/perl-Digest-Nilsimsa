%define	name	perl-Digest-Nilsimsa
%define	real_name Digest-Nilsimsa
%define	upstream_version	0.06
%define	release	%mkrel 1

Summary:	Perl interface to the Nilsima Algorithm	
Name:		%{name}
Version:	%perl_convert_version %{upstream_version}
Release:	%{release}
License:	GPL or Artistic
Group:		Development/Perl
Source:		http://www.cpan.org/authors/id/V/VI/VIPUL/%{real_name}-%{upstream_version}.tar.bz2
URL:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-buildroot
Requires:	perl

%description
Digest-Nilsimsa module for perl.

%prep
%setup -q -n %{real_name}-%{upstream_version}

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
