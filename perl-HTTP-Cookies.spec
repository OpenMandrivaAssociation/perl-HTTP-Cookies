%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32\\)'
%else
%define _requires_exceptions Win32
%endif

%define upstream_name    HTTP-Cookies
%define upstream_version 6.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
Summary:	Storage of cookies
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Headers::Util)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
This class is for objects that represent a "cookie jar" -- that is, a
database of all the HTTP cookies that a given LWP::UserAgent object knows
about.

Cookies are a general mechanism which server side connections can use to
both store and retrieve information on the client side of the connection.
For more information about cookies refer to
<URL:http://curl.haxx.se/rfc/cookie_spec.html> and
<URL:http://www.cookiecentral.com/>. This module also implements the new
style cookies described in _RFC 2965_. The two variants of cookies are
supposed to be able to coexist happily.

Instances of the class _HTTP::Cookies_ are able to store a collection of
Set-Cookie2: and Set-Cookie: headers and are able to use this information
to initialize Cookie-headers in _HTTP::Request_ objects. The state of a
_HTTP::Cookies_ object can be saved in and restored from files.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm lib/HTTP/Cookies/Microsoft.pm
sed -i -e '/Microsoft.pm/d' MANIFEST

%build
%__perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Fri Jul 20 2012 Bernhard Rosenkraenzer <bero@bero.eu> 6.10.0-1
+ Revision: 810460
- Adjust build dependencies
- Update to 6.01
- Fix requirement on perl(Win32)

* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-4
+ Revision: 765315
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-3
+ Revision: 763862
- rebuilt for perl-5.14.x

* Fri Jan 20 2012 Oden Eriksson <oeriksson@mandriva.com> 6.0.0-2
+ Revision: 763070
- rebuild

* Wed May 04 2011 Guillaume Rousse <guillomovitch@mandriva.org> 6.0.0-1
+ Revision: 665969
- import perl-HTTP-Cookies

