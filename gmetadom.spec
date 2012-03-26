%define major 0
%define libname  %mklibname gmetadom_gdome_cpp_smart %{major}
%define develname  %mklibname gmetadom_gdome_cpp_smart -d

%define _disable_ld_as_needed 1

Summary:	C++ Wrapper for GDOME
Name:		gmetadom
Version:	0.2.6
Release:	10
Group:		System/Libraries
License:	LGPL
URL:		http://gmetadom.sourceforge.net/
Source0:   %{name}-%{version}.tar.bz2
Patch1:	gmetadom-0.2.6-fix-missing-header.patch

BuildRequires: ocaml
BuildRequires: ocaml-findlib
BuildRequires: gdome2-devel
BuildRequires: libgdome-devel

%description
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%package -n %{libname}
Summary:	CPP Libraries for gdome2
Group:		System/Libraries

%description -n %{libname}
 GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%package -n %{develname}
Summary:	Libraries and include files for gdome2
Group:		Development/C++
Requires:	%{libname} = %{version}
Provides:	%{name}-devel  = %{version}-%{release}
Obsoletes:	%{_lib}gmetadom_gdome_cpp_smart0-devel

%description -n %{develname}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%package -n ocaml-%{name}
Group:		Development/Other
Summary:	Ocaml bindings for %{name}
Obsoletes:  %{name}-ocaml

%description -n ocaml-%{name}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

This are the Ocaml bindings of GMetaDOM.

%prep
%setup -q
%apply_patches

%build
#gw we have to disable libtoolize, as the ocaml path doesn't build otherwise
%define __libtoolize true
%configure2_5x \
	--with-ocaml-lib-prefix=%{_libdir}/ocaml

%install
%makeinstall_std

# static lib needed for internal test
rm -f %{buildroot}%{_libdir}/*.a

%files -n %{libname}
%{_libdir}/libgmetadom_gdome_cpp_smart.so.%{major}*

%files -n %{develname}
%doc AUTHORS COPYING ChangeLog HISTORY INSTALL LICENSE
%{_includedir}/*
%{_libdir}/pkgconfig/*.pc
%{_libdir}/lib*.so

%files -n ocaml-%{name}
%{_libdir}/ocaml/gdome2
%{_libdir}/ocaml/stublibs/*

