#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-user-bundles
Version  : 1
Release  : 1
URL      : http://localhost/cgit/projects/clr-user-bundles/snapshot/clr-user-bundles-1.tar.gz
Source0  : http://localhost/cgit/projects/clr-user-bundles/snapshot/clr-user-bundles-1.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: clr-user-bundles-bin = %{version}-%{release}
Requires: clr-user-bundles-license = %{version}-%{release}
BuildRequires : buildreq-golang

%description
[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/pflag)](https://goreportcard.com/report/github.com/spf13/pflag)
[![GoDoc](https://godoc.org/github.com/spf13/pflag?status.svg)](https://godoc.org/github.com/spf13/pflag)

%package bin
Summary: bin components for the clr-user-bundles package.
Group: Binaries
Requires: clr-user-bundles-license = %{version}-%{release}

%description bin
bin components for the clr-user-bundles package.


%package license
Summary: license components for the clr-user-bundles package.
Group: Default

%description license
license components for the clr-user-bundles package.


%prep
%setup -q -n clr-user-bundles-1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1548540020
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1548540020
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-user-bundles
cp COPYING %{buildroot}/usr/share/package-licenses/clr-user-bundles/COPYING
cp vendor/github.com/BurntSushi/toml/COPYING %{buildroot}/usr/share/package-licenses/clr-user-bundles/vendor_github.com_BurntSushi_toml_COPYING
cp vendor/github.com/inconshreveable/mousetrap/LICENSE %{buildroot}/usr/share/package-licenses/clr-user-bundles/vendor_github.com_inconshreveable_mousetrap_LICENSE
cp vendor/github.com/spf13/cobra/LICENSE.txt %{buildroot}/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_cobra_LICENSE.txt
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_pflag_LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/3rd-party-post
/usr/bin/mixer-user-bundler
/usr/bin/swupd-3rd-party

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-user-bundles/COPYING
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_pflag_LICENSE
