Name:ompl
Version:1.6.0
Release:1%{?dist}
Summary:OMPL, the Open Motion Planning Library, consists of many state-of-the-art sampling-based motion planning algorithms. OMPL itself does not contain any code related to, e.g., collision checking or visualization.

License:BSD
URL:https://github.com/ompl/ompl
Source0:https://github.com/ompl/ompl/archive/refs/tags/1.6.0.tar.gz

BuildRequires: cmake
BuildRequires: gcc
BuildRequires: make
BuildRequires: g++
BuildRequires: boost-devel
BuildRequires: eigen3-devel
Requires: eigen3-devel
Requires: boost-devel

%description
OMPL, the Open Motion Planning Library, consists of many state-of-the-art sampling-based motion planning algorithms. OMPL itself does not contain any code related to, e.g., collision checking or visualization.

%prep
%autosetup


%build
cmake .
make -j8


%install
rm -rf $RPM_BUILD_ROOT
%make_install


%files
%license LICENSE
%doc doc



%changelog
* Sat Jan 14 2023 Chittaranjan S Srinivas <ksatyaki@gmail.com>
- 
