%define origname cups-bjnp

Summary:	CUPS backend for the Canon BJNP network printers 
Name:		cups-drivers-bjnp
Version:	2.0.3
Release:	2
License:	GPLv2
Source0:	http://sourceforge.net/projects/cups-bjnp/files/cups-bjnp/1.2.2/cups-bjnp-%{version}.tar.gz
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
%global optflags %{optflags} -Qunused-arguments

%configure \
	--with-cupsbackenddir=%{_prefix}/lib/cups/backend \
	--disable-Werror

%make_build

%install
%makeinstall_std

%files
%doc COPYING ChangeLog TODO NEWS README
%{_prefix}/lib/cups/backend/bjnp

