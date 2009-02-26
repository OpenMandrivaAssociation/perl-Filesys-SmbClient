%define module   Filesys-SmbClient
%define version    3.1
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Provide Perl API for libsmbclient.so
Source:     http://www.cpan.org/modules/by-module/Filesys/%{module}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{module}
BuildRequires: perl-devel
BuildRequires: perl(Test::More)
BuildRequires: libsmbclient-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
Provide interface to access routine defined in libsmbclient.so provided
with Samba.

Since 3.0 release of this package, you need a least samba-3.0.2. For prior
release of Samba, use Filesys::SmbClient version 1.x.

For old and 2.x release, this library is available on Samba source, but is
not build by default. Do "make bin/libsmbclient.so" in sources directory of
Samba to build this libraries. Then copy source/include/libsmbclient.h to
/usr/local/samba/include and source/bin/libsmbclient.so to
/usr/local/samba/lib before install this module.

%prep
%setup -q -n %{module}-%{version} 
rm -f t/02tie.t

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor <<EOF
%{_includedir}
%{_libdir}
no
EOF
%make CFLAGS="%{optflags}"

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorarch/Filesys
%perl_vendorarch/auto/Filesys

