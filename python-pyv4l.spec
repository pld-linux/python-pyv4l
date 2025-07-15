%define 	module	pyv4l

Summary:	Python Video 4 Linux extension module developed in C
Summary(pl.UTF-8):	Moduł obsługi Video 4 Linux dla Pythona rozwijany w C
Name:		python-%{module}
Version:	0.5.0
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/download/%{module}-%{version}.tar.gz
# Source0-md5:	1bcf20c13e1ae36a0d40130158d96a67
Patch0:		%{name}-enable_channel_norm.patch
URL:		http://members.optushome.com.au/pythondeveloper/programming/python/pyv4l/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	python-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python Video 4 Linux extension module developed in C. Provides a
convenient Object Oriented interface to Video 4 Linux functions.

%description -l pl.UTF-8
Moduł obsługi Video 4 Linux dla Pythona rozwijany w C. Dostarcza
wygodny interfejs obiektowy do funkcji Video 4 Linux.

%prep
%setup -q -n %{module}-%{version}
%patch -P0 -p1

%build
CFLAGS="%{rpmcflags}" \
LDFLAGS="-L/usr/X11R6/%{_lib}" \
%py_build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{py_sitedir},%{_examplesdir}/%{name}-%{version}}

%py_install

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
