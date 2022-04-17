%global real_name puremagic

Name:           python-%{real_name}
Version:        1.12
Release:        1%{?dist}
Summary:        Pure python implementation of magic file detection
License:        LGPLv3
BuildArch:      noarch

URL:            https://github.com/cdgriffith/%{real_name}/
Source0:        https://github.com/cdgriffith/%{real_name}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz
Patch0:         %{real_name}-py36.patch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

%global _description %{expand:
puremagic is a pure python module that will identify a file based off it's magic
numbers. It is designed to be minimalistic and inherently cross platform
compatible.}

%description %_description

%package -n     python3-%{real_name}
Summary:        %{summary}

%description -n python3-%{real_name} %_description

%prep
%autosetup -p1 -n %{real_name}-%{version}

%build
%py3_build

%install
%py3_install

%files -n python3-%{real_name}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.md README.rst
%{python3_sitelib}/%{real_name}/
%{python3_sitelib}/%{real_name}-%{version}-py*.egg-info/

%changelog
* Sun Apr 17 2022 Simone Caronni <negativo17@gmail.com> - 1.12-1
- Update to 1.12.

* Thu Dec 16 2021 Simone Caronni <negativo17@gmail.com> - 1.11-1
- First build.

