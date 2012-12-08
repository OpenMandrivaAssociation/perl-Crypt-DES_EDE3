%define upstream_name    Crypt-DES_EDE3
%define upstream_version 0.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	Triple-DES EDE encryption/decryption
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc MANIFEST README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-5mdv2012.0
+ Revision: 765125
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-4
+ Revision: 763628
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-3
+ Revision: 676623
- rebuild

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 0.10.0-2
+ Revision: 676567
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.10.0-1mdv2011.0
+ Revision: 403031
- rebuild using %%perl_convert_version

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 0.01-9mdv2009.0
+ Revision: 256254
- rebuild

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-7mdv2008.1
+ Revision: 137161
- use CPAN sources
  spec cleanup

* Sat Dec 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.01-6mdv2008.1
+ Revision: 136929
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Oct 28 2006 Nicolas Lécureuil <neoclust@mandriva.org> 0.01-5mdv2007.0
+ Revision: 73460
- Fix Build
- import perl-Crypt-DES_EDE3-0.01-4mdk

* Wed Aug 25 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.01-4mdk
- rebuild

