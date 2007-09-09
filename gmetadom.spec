%define name    gmetadom
%define version 0.2.5
%define release %mkrel 2

%define major 0
%define libname  %mklibname gmetadom_gdome_cpp_smart %major

Summary: C++ Wrapper for GDOME
Name: %name
Version: %version
Release: %release
Group:  System/Libraries
License:   LGPL
URL:  http://gmetadom.sourceforge.net/    
Source:   %{name}-%{version}.tar.bz2
Patch: gmetadom-0.2.3-gcc4.1.patch.bz2
BuildRequires: autoconf2.5 
BuildRequires: ocaml
BuildRequires: gdome2-devel
BuildRequires: libgdome-devel
BuildRoot: %_tmppath/%{name}-%{version}

%description
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%package -n %libname
Summary: CPP Libraries for gdome2
Group: System/Libraries 

%description -n %libname
 GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets.

%package -n %libname-devel
Summary: Libraries and include files for gdome2
Group:    Development/C++ 
Requires: %libname = %{version}
Requires: glib2-devel >= 2.4.4 libgdome-devel libxml2-devel >= 2.6.11  
Provides: %name-devel  = %version-%release
Provides: libgmetadom_gdome_cpp_smart-devel = %version-%release

%description -n %libname-devel
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets. 

%package -n ocaml-%{name}
Group: Development/Other
Summary: Ocaml bindings for %name
Obsoletes:  %{name}-ocaml

%description -n ocaml-%{name}
GMetaDOM is a collection of libraries, each library providing a
DOM implementation. Each DOM implementation is generated
automatically by means of XSLT stylesheets. 

This are the Ocaml bindings of GMetaDOM.

%prep
rm -rf %{buildroot}
%setup -qn %{name}-%{version}

%build
#gw we have to disable libtoolize, as the ocaml path doesn't build otherwise
%define __libtoolize true
%configure2_5x --with-ocaml-lib-prefix=%{ocaml_sitelib}

%install  
%makeinstall_std  
 
%clean
rm -rf %{buildroot} 
 
%post -n %libname -p /sbin/ldconfig

%postun -n %libname -p /sbin/ldconfig
 
%files -n %libname
%defattr(-, root, root) 
%_libdir/lib*.so.*
 
%files -n %libname-devel
%defattr(-,root,root)
%doc AUTHORS COPYING ChangeLog HISTORY INSTALL LICENSE      
%_includedir/*
%_libdir/pkgconfig/*.pc
%_libdir/lib*.so
%_libdir/*.a
%_libdir/*.la 

%files -n ocaml-%{name}
%defattr(-, root, root) 
%{ocaml_sitelib}/gdome2
%{ocaml_sitelib}/stublibs/*
