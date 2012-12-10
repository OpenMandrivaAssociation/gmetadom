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



%changelog
* Mon Mar 26 2012 Matthew Dawkins <mattydaw@mandriva.org> 0.2.6-10
+ Revision: 787031
- rebuild
- cleaned up spec

* Wed Oct 06 2010 Funda Wang <fwang@mandriva.org> 0.2.6-9mdv2011.0
+ Revision: 583369
- rebuild

* Wed Feb 03 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.6-8mdv2010.1
+ Revision: 500158
- rebuild for latest ocaml

* Fri Jul 31 2009 Funda Wang <fwang@mandriva.org> 0.2.6-7mdv2010.0
+ Revision: 405045
- rebuild for new ocaml

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.6-6mdv2009.1
+ Revision: 355052
- fix missing header
- disable -Wl,as-needed (lazy fix)
- ocaml site-lib hierarchy doesn't exist anymore

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Mon Mar 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.6-2mdv2008.1
+ Revision: 189766
- rebuild for latest ocaml

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Oct 29 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.2.6-1mdv2008.1
+ Revision: 102991
- New release 0.2.6

* Mon Oct 29 2007 JÃ©rÃ´me Soyer <saispo@mandriva.org> 0.2.5-6mdv2008.1
+ Revision: 102978
- New release

* Sun Sep 09 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.5-1mdv2008.1
+ Revision: 83938
- make ocaml bindings compliant with ocaml policy

  + JÃ©rÃ´me Soyer <saispo@mandriva.org>
    - Fix BR
    - Add gdome2
    - New release 0.2.5
    - Import gmetadom



* Tue Aug 08 2006 Jerome Soyer <saispo@mandriva.org> 0.2.4-1mdv2007.0
- New release 0.2.4
- Remove patch1

* Wed Jun 21 2006 Götz Waschk <waschk@mandriva.org> 0.2.3-4mdv2007.0
- fix build

* Mon Apr 24 2006 Pixel <pixel@mandriva.com> 0.2.3-3mdk
- rebuild for new ocaml

* Mon Mar 27 2006 GÃ¶tz Waschk <waschk@mandriva.org> 0.2.3-2mdk
- rebuild for new ocaml
- use mkrel

* Thu Jul 21 2005 Götz Waschk <waschk@mandriva.org> 0.2.3-1mdk
- New release 0.2.3

* Tue Apr 26 2005 Götz Waschk <waschk@mandriva.org> 0.2.2-1mdk
- New release 0.2.2

* Wed Nov 10 2004 Jerome Soyer <saispo@mandrake.org> 0.2.1-1mdk
- 0.2.1

* Fri Jun 11 2004 Götz Waschk <waschk@linux-mandrake.com> 0.1.8-5mdk
- disable libtoolize
- fix deps
- new g++

* Wed Jul  9 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.8-3mdk
- rebuild for new rpm

* Tue Jun 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.8-2mdk
- add the version and release number to the devel provides

* Tue Jun 10 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.8-1mdk
- fix release tag
- source URL
- from Charles A Edwards <eslrahc@bellsouth.net>
  - release 0.1.8	
  - patch for gcc-33
  - update file list
 
* Fri May  2 2003 Götz Waschk <waschk@linux-mandrake.com> 0.1.6-1mdk
- add ocaml subpackage
- dir ownership
- from  Charles A Edwards <eslrahc@bellsouth.net>:
  - initial mdk release
