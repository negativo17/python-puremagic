%global real_name puremagic

Name:           python-%{real_name}
Version:        1.12
Release:        1%{?dist}
Summary:        Pure python implementation of magic file detection
License:        LGPLv3
BuildArch:      noarch

URL:            https://github.com/cdgriffith/%{real_name}/
Source0:        https://github.com/cdgriffith/%{real_name}/archive/%{version}.tar.gz#/%{real_name}-%{version}.tar.gz

BuildRequires:  python3-devel

%global _description %{expand:
puremagic is a pure python module that will identify a file based off it's magic
numbers. It is designed to be minimalistic and inherently cross platform
compatible.}

%description %_description

%package -n     python3-%{real_name}
Summary:        %{summary}

%description -n python3-%{real_name} %_description

%prep
%autosetup -n %{real_name}-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{real_name}

%check
%py3_check_import %{real_name}

%files -n python3-%{real_name} -f %{pyproject_files}
%license LICENSE
%doc AUTHORS.rst CHANGELOG.md README.rst

%changelog
* Sun Apr 17 2022 Simone Caronni <negativo17@gmail.com> - 1.12-1
- Update to 1.12.

* Thu Dec 16 2021 Simone Caronni <negativo17@gmail.com> - 1.11-1
- First build.

