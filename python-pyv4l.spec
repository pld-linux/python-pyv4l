# TODO: Add examples package. Install docs.
%include	/usr/lib/rpm/macros.python
%define 	module pyv4l

Summary:	Python Video 4 Linux extension module developed in C
Summary(pl):	Modu³ obs³ugi Video 4 Linux dla Pythona rozwijany w C
Name:		python-%{module}
Version:	0.4.1
Release:	2
License:	GPL
Group:		Libraries/Python
Source0:	http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/download/%{module}-%{version}.tar.gz
# Source0-md5:	b3cbdb082bcd5879420a0195f0128ef4
URL:		http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/
Requires:	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Video 4 Linux extension module developed in C. Provides a
convenient Object Oriented interface to Video 4 Linux functions.

%description -l pl
Modu³ obs³ugi Video 4 Linux dla Pythona rozwijany w C. Dostarcza
wygodny interfejs obiektowy do funkcji Video 4 Linux.

%prep
%setup -q -n %{module}-%{version}

%build
CFLAGS="%{rpmcflags}"
export CLFAGS
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{py_sitedir}

python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%%doc CREDITS ChangeLog README doc
%{py_sitedir}/v4l.so
