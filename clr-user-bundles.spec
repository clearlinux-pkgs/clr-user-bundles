#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-user-bundles
Version  : 11
Release  : 10
URL      : https://github.com/clearlinux/clr-user-bundles/releases/download/v11/clr-user-bundles-v11.tar.xz
Source0  : https://github.com/clearlinux/clr-user-bundles/releases/download/v11/clr-user-bundles-v11.tar.xz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause MIT
Requires: clr-user-bundles-bin = %{version}-%{release}
Requires: clr-user-bundles-license = %{version}-%{release}
Requires: clr-user-bundles-man = %{version}-%{release}
Requires: clr-user-bundles-services = %{version}-%{release}
BuildRequires : buildreq-golang

%description
## TOML parser and encoder for Go with reflection
TOML stands for Tom's Obvious, Minimal Language. This Go package provides a
reflection interface similar to Go's standard library `json` and `xml`
packages. This package also supports the `encoding.TextUnmarshaler` and
`encoding.TextMarshaler` interfaces so that you can define custom data
representations. (There is an example of this below.)

%package bin
Summary: bin components for the clr-user-bundles package.
Group: Binaries
Requires: clr-user-bundles-license = %{version}-%{release}
Requires: clr-user-bundles-services = %{version}-%{release}

%description bin
bin components for the clr-user-bundles package.


%package extras
Summary: extras components for the clr-user-bundles package.
Group: Default

%description extras
extras components for the clr-user-bundles package.


%package license
Summary: license components for the clr-user-bundles package.
Group: Default

%description license
license components for the clr-user-bundles package.


%package man
Summary: man components for the clr-user-bundles package.
Group: Default

%description man
man components for the clr-user-bundles package.


%package services
Summary: services components for the clr-user-bundles package.
Group: Systemd services

%description services
services components for the clr-user-bundles package.


%prep
%setup -q -n clr-user-bundles-v11

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1553118575
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1553118575
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
%exclude /usr/bin/mixer-user-bundler
/usr/bin/3rd-party-post
/usr/bin/swupd-3rd-party

%files extras
%defattr(-,root,root,-)
/usr/bin/mixer-user-bundler
/usr/share/man/man1/mixer-user-bundler.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-user-bundles/COPYING
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_BurntSushi_toml_COPYING
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_inconshreveable_mousetrap_LICENSE
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_cobra_LICENSE.txt
/usr/share/package-licenses/clr-user-bundles/vendor_github.com_spf13_pflag_LICENSE

%files man
%defattr(0644,root,root,0755)
%exclude /usr/share/man/man1/mixer-user-bundler.1
/usr/share/man/man1/3rd-party-post.1
/usr/share/man/man1/swupd-3rd-party.1

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/3rd-party-update.service
/usr/lib/systemd/system/3rd-party-update.timer
