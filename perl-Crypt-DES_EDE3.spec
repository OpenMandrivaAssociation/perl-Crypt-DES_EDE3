Name:		 perl-Crypt-DES_EDE3
Summary:	 Crypt-DES_EDE3 Perl module
Version:	 0.01
Release:	 %mkrel 6
License:	 Artistic
Group:		 Development/Perl
Source:		 http://search.cpan.org/%{name}-%{version}.tar.bz2
BuildRoot:	 %_tmppath/%name-%version-root
Buildrequires:	 perl-devel
URL:		 http://search.cpan.org/
Buildarch:	noarch

%description
This is Crypt::DES_EDE3, a module implementing Triple-DES EDE
(encrypt-decrypt-encrypt) encryption and decryption.

%prep

%setup

%build
[ -n "%{buildroot}" -a "%{buildroot}" != / ] && rm -rf %{buildroot}

CFLAGS="$RPM_OPT_FLAGS" %{__perl} Makefile.PL INSTALLDIRS=vendor
make

%install

make PREFIX=$RPM_BUILD_ROOT%{_prefix} DESTDIR=$RPM_BUILD_ROOT install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
%doc MANIFEST README
%{perl_vendorlib}/Crypt/*.pm
%{_mandir}/*/*




