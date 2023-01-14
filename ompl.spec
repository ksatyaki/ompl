%global soversion 17

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
BuildRequires:  doxygen
BuildRequires:  flann-devel
BuildRequires:  graphviz
Requires: eigen3-devel
Requires: boost-devel

%description
OMPL, the Open Motion Planning Library, consists of many state-of-the-art sampling-based motion planning algorithms. OMPL itself does not contain any code related to, e.g., collision checking or visualization.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       boost-devel

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%autosetup

%build
%cmake -DCMAKE_SKIP_RPATH:BOOL=ON
%cmake_build 

%install
%cmake_install

%files
%doc LICENSE
%{_libdir}/libompl.so
%{_libdir}/libompl.so.%{version}
%{_libdir}/libompl.so.%{soversion}
%{_mandir}/man1/*.1.*
 
%files devel
%license LICENSE
%doc doc
%{_includedir}/ompl-1.6/%{name}
%{_datadir}/%{name}
%{_libdir}/pkgconfig/*.pc
%{_datadir}/ament_index/resource_index/packages/ompl
/usr/lib/debug/usr/lib64/libompl.so.1.6.0-1.6.0-1.fc36.x86_64.debug


%changelog
* Sat Jan 14 2023 Chittaranjan S Srinivas <ksatyaki@gmail.com>
- 
