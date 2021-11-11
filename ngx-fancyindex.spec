#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : ngx-fancyindex
Version  : 0.5.2
Release  : 23
URL      : https://github.com/aperezdc/ngx-fancyindex/archive/v0.5.2/ngx-fancyindex-0.5.2.tar.gz
Source0  : https://github.com/aperezdc/ngx-fancyindex/archive/v0.5.2/ngx-fancyindex-0.5.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
Requires: ngx-fancyindex-lib = %{version}-%{release}
BuildRequires : buildreq-nginx
BuildRequires : openssl-dev

%description
========================
Nginx Fancy Index module
========================
.. image:: https://travis-ci.com/aperezdc/ngx-fancyindex.svg?branch=master
:target: https://travis-ci.com/aperezdc/ngx-fancyindex
:alt: Build Status

%package lib
Summary: lib components for the ngx-fancyindex package.
Group: Libraries

%description lib
lib components for the ngx-fancyindex package.


%prep
%setup -q -n ngx-fancyindex-0.5.2
cd %{_builddir}/ngx-fancyindex-0.5.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
nginx-module configure
nginx-module build

%install
nginx-module install %{buildroot}


%files
%defattr(-,root,root,-)

%files lib
%defattr(-,root,root,-)
/usr/lib64/nginx-mainline/ngx_http_fancyindex_module.so
