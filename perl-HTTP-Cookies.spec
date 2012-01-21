%define upstream_name    HTTP-Cookies
%define upstream_version 6.00

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Storage of cookies
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(HTTP::Date)
BuildRequires: perl(HTTP::Headers::Util)
BuildRequires: perl(Time::Local)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


