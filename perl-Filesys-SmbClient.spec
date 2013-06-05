%define module   Filesys-SmbClient

Name:		perl-%{module}
Version:	%perl_convert_version 3.2
Release:	1
License:	GPL or Artistic
Group:		Development/Perl
Summary:	Provide Perl API for libsmbclient.so
Source:		http://www.cpan.org/modules/by-module/Filesys/Filesys-SmbClient-3.2.tar.gz
Url:		http://search.cpan.org/dist/%{module}

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	pkgconfig(smbclient)

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
perl Makefile.PL INSTALLDIRS=vendor <<EOF
%{_includedir}
%{_libdir}
no
EOF
%make CFLAGS="%{optflags}"

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorarch}/Filesys
%{perl_vendorarch}/auto/Filesys

%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 3.1-3mdv2012.0
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Mon Sep 14 2009 Thierry Vignaud <tv@mandriva.org> 3.1-2mdv2010.0
+ Revision: 440567
- rebuild

* Thu Feb 26 2009 Guillaume Rousse <guillomovitch@mandriva.org> 3.1-1mdv2009.1
+ Revision: 345099
- import perl-Filesys-SmbClient


* Thu Feb 26 2009 cpan2dist 3.1-1mdv
- initial mdv release, generated with cpan2dist


