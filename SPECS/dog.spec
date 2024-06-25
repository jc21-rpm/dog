%global debug_package %{nil}

Name:           dog
Version:        0.1.0
Release:        1%{?dist}
Summary:        dog is a command-line DNS client.
Group:          Applications/System
License:        EUPL-1.2
URL:            https://github.com/ogham/%{name}
BuildRequires:  cmake, libgit2, openssl-devel
Source:         https://github.com/ogham/%{name}/archive/refs/tags/v%{version}.tar.gz

%{?el7:BuildRequires: cargo, rust}

%description
dog is a command-line DNS client, like dig. It has colourful output, understands
normal command-line argument syntax, supports the DNS-over-TLS and DNS-over-HTTPS
protocols, and can emit JSON.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/%{name} %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/%{name}

%changelog
* Thu Dec 8 2021 Jamie Curnow <jc@jc21.com> - 0.1.0-1
- Initial spec
