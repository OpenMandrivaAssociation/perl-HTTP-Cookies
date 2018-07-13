%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Win32\\)'
%else
%define _requires_exceptions Win32
%endif

%define modname	HTTP-Cookies
%define modver	6.04

Summary:	Storage of cookies
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test)
BuildRequires:	perl(HTTP::Date)
BuildRequires:	perl(HTTP::Headers::Util)
BuildRequires:	perl(Time::Local)
BuildRequires:	perl-devel

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
Set-Cookie2:	and Set-Cookie:	headers and are able to use this information
to initialize Cookie-headers in _HTTP::Request_ objects. The state of a
_HTTP::Cookies_ object can be saved in and restored from files.

%prep
%setup -qn %{modname}-%{modver}
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
%doc Changes META.yml
%{perl_vendorlib}/*
%{_mandir}/man3/*
