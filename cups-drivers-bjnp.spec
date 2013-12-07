%define origname cups-bjnp

Summary:	CUPS backend for the Canon BJNP network printers 
Name:		cups-drivers-bjnp
Version:	1.2.1
Release:	3
License:	GPLv2
Source0:	http://downloads.sourceforge.net/%{origname}/%{origname}-%{version}.tar.gz
Group:		System/Printing
URL:		https://sourceforge.net/projects/cups-bjnp
BuildRequires:	cups-devel
Requires:	cups

%description
This package contains a backend for CUPS for Canon printers using the 
proprietary BJNP network protocol.

%prep
%setup -q -n %{origname}-%{version}

%build
%configure2_5x \
	--with-cupsbackenddir=%{_prefix}/lib/cups/backend
%make

%install
%makeinstall_std

%files
%doc COPYING ChangeLog TODO NEWS README
%{_prefix}/lib/cups/backend/bjnp
