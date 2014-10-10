%define modname	Crypt-DES_EDE3
%define modver	0.01

Summary:	Triple-DES EDE encryption/decryption
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc MANIFEST README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/*

