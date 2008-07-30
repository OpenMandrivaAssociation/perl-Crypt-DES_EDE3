%define module  Crypt-DES_EDE3

Name:		 perl-%{module}
Summary:	 Triple-DES EDE encryption/decryption
Version:	 0.01
Release:	 %mkrel 9
License:	 Artistic
Group:		 Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Crypt/%{module}-%{version}.tar.gz
Buildarch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make CFLAGS="%{optflags}"

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root)
%doc MANIFEST README
%{perl_vendorlib}/Crypt
%{_mandir}/*/*
