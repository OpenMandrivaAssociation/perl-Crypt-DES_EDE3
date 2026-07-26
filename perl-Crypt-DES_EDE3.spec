%define modname	Crypt-DES_EDE3
Summary:	Triple-DES EDE encryption/decryption
Name:		perl-%{modname}
Version:	0.01
Release:	19
License:	Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Crypt/%{modname}-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep
%setup -qn %{modname}-%{version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
%makeinstall_std

%files
%doc MANIFEST README
%{perl_vendorlib}/Crypt
%{_mandir}/man3/*

