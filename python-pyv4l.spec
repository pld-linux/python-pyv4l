%include	/usr/lib/rpm/macros.python
%define 	module pyv4l

Summary:	Python Video 4 Linux extension module developed in C
Summary(pl):	Modu³ obs³ugi Video 4 Linux dla Pythona rozwijany w C
Name:		python-%{module}
Version:	0.5.0
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/download/%{module}-%{version}.tar.gz
# Source0-md5:	1bcf20c13e1ae36a0d40130158d96a67
Patch0:         %{name}-enable_channel_norm.patch
URL:		http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/
BuildRequires:	python-devel
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
%patch0 -p1

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="-L/usr/X11R6/%{_lib}" \
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

python setup.py install \
        --root=$RPM_BUILD_ROOT \
	--optimize=2

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
install examples/*.py $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py -exec rm {} \;

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/v4l.html
%attr(755,root,root) %{py_sitedir}/v4l.so
%{_examplesdir}/%{name}-%{version}
