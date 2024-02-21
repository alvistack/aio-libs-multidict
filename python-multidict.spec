# Copyright 2025 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

%global source_date_epoch_from_changelog 0

Name: python-multidict
Epoch: 100
Version: 6.1.0
Release: 1%{?dist}
Summary: MultiDict implementation
License: Apache-2.0
URL: https://github.com/aio-libs/multidict/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-Cython3
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
Multidicts are useful for working with HTTP headers, URL query args etc.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitearch} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitearch}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-multidict
Summary: MultiDict implementation
Requires: python3
Provides: python3-multidict = %{epoch}:%{version}-%{release}
Provides: python3dist(multidict) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-multidict = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(multidict) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-multidict = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(multidict) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-multidict
Multidicts are useful for working with HTTP headers, URL query args etc.

%files -n python%{python3_version_nodots}-multidict
%license LICENSE
%{python3_sitearch}/*
%endif

%if !(0%{?suse_version} > 1500)
%package -n python3-multidict
Summary: MultiDict implementation
Requires: python3
Provides: python3-multidict = %{epoch}:%{version}-%{release}
Provides: python3dist(multidict) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-multidict = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(multidict) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-multidict = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(multidict) = %{epoch}:%{version}-%{release}

%description -n python3-multidict
Multidicts are useful for working with HTTP headers, URL query args etc.

%files -n python3-multidict
%license LICENSE
%{python3_sitearch}/*
%endif

%changelog