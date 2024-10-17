%define major 0
%define libname %mklibname gmetadom_gdome_cpp_smart %{major}
%define devname %mklibname gmetadom_gdome_cpp_smart -d

%define _disable_ld_as_needed 1

Summary:	C++ Wrapper for GDOME
Name:		gmetadom
Version:	0.2.6
Release:	12
License:	LGPLv2.1+
Group:		System/Libraries
Url:		https://gmetadom.sourceforge.net/
Source0:	%{name}-%{version}.tar.bz2
Patch1:		gmetadom-0.2.6-fix-missing-header.patch
BuildRequires:	ocaml
BuildRequires:	ocaml-findlib
BuildRequires:	pkgconfig(gdome2)

%description
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

#----------------------------------------------------------------------------

%package -n %{libname}
Summary:	CPP Libraries for gdome2
Group:		System/Libraries

%description -n %{libname}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%files -n %{libname}
%{_libdir}/libgmetadom_gdome_cpp_smart.so.%{major}*

#----------------------------------------------------------------------------

%package -n %{devname}
Summary:	Libraries and include files for gdome2
Group:		Development/C++
Requires:	%{libname} = %{EVRD}
Provides:	%{name}-devel  = %{EVRD}

%description -n %{devname}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%files -n %{devname}
%doc AUTHORS COPYING ChangeLog HISTORY INSTALL LICENSE
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

#----------------------------------------------------------------------------

%package -n ocaml-%{name}
Summary:	Ocaml bindings for %{name}
Group:		Development/Other

%description -n ocaml-%{name}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

This are the Ocaml bindings of GMetaDOM.

%files -n ocaml-%{name}
%{_libdir}/ocaml/gdome2
%{_libdir}/ocaml/stublibs/*

#----------------------------------------------------------------------------

%prep
%setup -q
%autopatch -p1

%build
#gw we have to disable libtoolize, as the ocaml path doesn't build otherwise
%define __libtoolize true
%configure2_5x \
	--with-ocaml-lib-prefix=%{_libdir}/ocaml

%install
%makeinstall_std

# static lib needed for internal test
rm -f %{buildroot}%{_libdir}/*.a

