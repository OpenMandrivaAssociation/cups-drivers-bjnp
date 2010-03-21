%define origname cups-bjnp

Summary:	CUPS backend for the Canon BJNP network printers 
Name:		cups-drivers-bjnp
Version:	0.5.4
Release:	%mkrel 1
License:	GPLv2
Source:		http://downloads.sourceforge.net/%{origname}/%{origname}-%{version}.tar.gz
Group:		System/Printing
URL:		https://sourceforge.net/projects/cups-bjnp
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	cups-devel
Requires:	cups

%description
This package contains a backend for CUPS for Canon printers using the 
proprietary BJNP network protocol.

%prep
%setup -q -n %{origname}-%{version}

%build
%configure \
	--prefix=%{_prefix} \
	--with-cupsbackenddir=%{_prefix}/lib/cups/backend
%make

%install
rm -fr %{buildroot}
make DESTDIR=%{buildroot} INSTALL="install -p" install

%clean
rm -fr %{buildroot}
 
%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog TODO NEWS README
%{_prefix}/lib/cups/backend/bjnp

