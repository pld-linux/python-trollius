#
# Conditional build:
%bcond_without	doc	# don't build doc
# tests make builder hung
%bcond_with	tests	# do not perform "make test"
%bcond_without	python2 # CPython 2.x module
%bcond_with	python3 # CPython 3.x module (asyncio is part of Python 3.4 standard library(

%define		module		trollius
%define		egg_name	trollius
%define		pypi_name	trollius
Summary:	A port of the Tulip asyncio module to Python 2
Name:		python-trollius
Version:	2.1
Release:	1
License:	Apache v2.0
Group:		Libraries/Python
Source0:	https://files.pythonhosted.org/packages/source/t/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# Source0-md5:	0b36ff1057cb5a93befe7d8ef0edcbf8
URL:		https://github.com/haypo/trollius
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-futures
BuildRequires:	python-mock
BuildRequires:	python-modules
%endif
%endif
%if %{with python3}
BuildRequires:	python3-devel
BuildRequires:	python3-setuptools
%endif
Requires:	python-futures
BuildArch:	noarch

%description
Trollius provides infrastructure for writing single-threaded
concurrent code using coroutines, multiplexing I/O access over sockets
and other resources, running network clients and servers, and other
related primitives.

Trollius is a portage of the asyncio project (PEP 3156) on Python 2.
Trollius works on Python 2.6-3.5. It has been tested on Windows,
Linux, Mac OS X, FreeBSD and OpenIndiana.

%package -n python3-trollius
Summary:	A port of the Tulip asyncio module
Group:		Libraries/Python

%description -n python3-trollius
Trollius provides infrastructure for writing single-threaded
concurrent code using coroutines, multiplexing I/O access over sockets
and other resources, running network clients and servers, and other
related primitives.

Trollius is a portage of the asyncio project (PEP 3156) on Python 2.
Trollius works on Python 2.6-3.5. It has been tested on Windows,
Linux, Mac OS X, FreeBSD and OpenIndiana.

%prep
%setup -q -n %{pypi_name}-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
%{__python} runtests.py -v1 -x test_subprocess_kill
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
%{__python3} runtests.py -v1 -x test_subprocess_kill
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-trollius
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
