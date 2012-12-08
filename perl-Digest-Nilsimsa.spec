%define	name	perl-Digest-Nilsimsa
%define	real_name Digest-Nilsimsa
%define	upstream_version	0.06
%define	release	%mkrel 6

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
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README 
%{_mandir}/*/*
%{perl_vendorarch}/auto/Digest/Nilsimsa
%{perl_vendorarch}/Digest/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-6mdv2012.0
+ Revision: 765188
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-5
+ Revision: 763704
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.60.0-4
+ Revision: 667121
- mass rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.60.0-3mdv2011.0
+ Revision: 564429
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 555245
- rebuild

* Mon Aug 03 2009 Götz Waschk <waschk@mandriva.org> 0.60.0-1mdv2010.1
+ Revision: 408206
- use perl version macro

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 0.06-12mdv2009.0
+ Revision: 223659
- rebuild

* Tue Jan 15 2008 Thierry Vignaud <tv@mandriva.org> 0.06-11mdv2008.1
+ Revision: 152066
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.06-10mdv2008.0
+ Revision: 67818
- rebuild

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.06-9mdv2008.0
+ Revision: 23414
- rebuild


* Sun Jan 01 2006 Mandriva Linux Team <http://www.mandrivaexpert.com/> 0.06-8mdk
- Rebuild

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-7mdk
- rebuild for new perl

* Thu Apr 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 0.06-6mdk
- rebuild for new perl

* Wed Aug 13 2003 Per �yvind Karlsen <peroyvind@linux-mandrake.com> 0.06-5mdk
- rebuild against new perl
- don't use PREFIX
- use %%makeinstall_std macro

* Tue May 27 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.06-4mdk
- rebuild for new auto{prov,req}

* Mon Sep 02 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.06-3mdk
- Recompiled with perl multithreaded (spotted by Ben Reser)

* Wed Jul 10 2002 Pixel <pixel@mandrakesoft.com> 0.06-2mdk
- rebuild for perl 5.8.0

* Fri Jun 14 2002 Frederic Crozat <fcrozat@mandrakesoft.com> 0.06-1mdk
- Initial Mdk package

