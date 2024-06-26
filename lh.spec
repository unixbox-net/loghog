Name:           lh
Version:        1.0.0
Release:        1%{?dist}
Summary:        Lightweight log monitoring tool
License:        BSD-2
URL:            https://github.com/unixbox-net/lh
Source0:        %{name}-%{version}.tar.gz
BuildRequires:  gcc, json-c-devel, readline-devel
Requires:       json-c, readline

%description
lh (LogHOG) is a fast lightweight digital forensics tool designed for advanced log monitoring.

%prep
%setup -q

%build
gcc -o lh lh.c -Wall -lreadline -ljson-c -g

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/local/bin
mkdir -p %{buildroot}/usr/share/doc/%{name}-%{version}
install -m 755 lh %{buildroot}/usr/bin
install -m 755 lh %{buildroot}/usr/local/bin
install -m 644 LICENSE %{buildroot}/usr/share/doc/%{name}-%{version}
install -m 644 README.md %{buildroot}/usr/share/doc/%{name}-%{version}

%files
/usr/bin/lh
/usr/local/bin/lh
%doc /usr/share/doc/%{name}-%{version}/LICENSE
%doc /usr/share/doc/%{name}-%{version}/README.md

%changelog
* Sat May 11 2024 Anthony <info@unixbox.net> - 1.0.0-1
- Initial release
