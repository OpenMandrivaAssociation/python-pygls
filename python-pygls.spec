Name:		python-pygls
Version:	1.3.1
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/p/pygls/pygls-%{version}.tar.gz
Summary:	A pythonic generic language server (pronounced like pie glass)
URL:		https://pypi.org/project/pygls/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python
BuildRequires:  python-poetry
BuildSystem:	python
BuildArch:	noarch

%description
A pythonic generic language server (pronounced like 'pie glass')

%files
%{py_sitedir}/pygls
%{py_sitedir}/pygls-*.*-info
