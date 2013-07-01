%define _cabal_setup Setup.lhs
%define _no_haddock 1

Summary:	Documentation tool for annotated Haskell source code
Name:		haddock
Version:	2.13.1
Release:	7
License:	BSD
Group:		Development/Other
Source0:	http://hackage.haskell.org/packages/archive/%{name}/${version}/%{name}-%{version}.tar.gz
URL:		http://www.haskell.org/haddock/
BuildRequires:	ghc-devel
BuildRequires:	happy
BuildRequires:	alex
BuildRequires:	libxslt-proc
BuildRequires:	docbook-style-xsl
BuildRequires:  ghc-paths
buildrequires:	haskell-macros
buildrequires:	ghc-xhtml
buildrequires:	pkgconfig(libffi)
requires:				haskell(ghc-paths)
requires:				haskell(xhtml)
requires:		ghc
requires(post):		ghc
requires(preun):	ghc

%description
Haddock is a tool for automatically generating documentation from
annotated Haskell source code. It is primary intended for documenting
libraries, but it should be useful for any kind of Haskell code.

Haddock lets you write documentation annotations next to the
definitions of functions and types in the source code, in a syntax
that is easy on the eye when writing the source code (no heavyweight
mark-up). The documentation generated by Haddock is fully hyperlinked
-- click on a type name in a type signature to go straight to the
definition, and documentation, for that type.

Haddock can generate documentation in multiple formats; currently HTML
is implemented, and there is partial support for generating DocBook.
The generated HTML uses stylesheets, so you need a fairly up-to-date
browser to view it properly (Mozilla, Konqueror, Opera, and IE 6
should all be ok).

%prep
%setup -q 

%build
%_cabal_build

cd doc
test -f configure || autoreconf
./configure
make html

%install
%_cabal_install
%_cabal_rpm_gen_deps
%_cabal_scriptlets


%files
%defattr(-,root,root)
%doc %{_docdir}/%{name}-%{version}
%doc doc/haddock/*
%{_datadir}/%{name}-%{version}/html
%{_datadir}/%{name}-%{version}/latex
%{_libdir}/%{name}-%{version}/*
%{_bindir}/haddock
%_cabal_rpm_deps_dir
#% _cabal_haddoc_files




%changelog
* Wed Feb 10 2010 Funda Wang <fwang@mandriva.org> 2.5.0-2mdv2010.1
+ Revision: 503554
- rebuild for new gmp

* Sun Nov 08 2009 Olivier Thauvin <nanardon@mandriva.org> 2.5.0-1mdv2010.1
+ Revision: 463096
- 2.5.0

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Mon Dec 08 2008 Olivier Thauvin <nanardon@mandriva.org> 2.4.1-1mdv2009.1
+ Revision: 311949
- 2.4.1

* Thu Aug 07 2008 Adam Williamson <awilliamson@mandriva.org> 0.9-1mdv2009.0
+ Revision: 267126
- new release 0.9
- clean spec

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot


* Mon Dec 11 2006 Michael Scherer <misc@mandriva.org> 0.8-1mdv2007.0
+ Revision: 94821
- also add stylesheet
- Add libxslt-proc, as haddock fail with "make: stringparam: Command not found"
- add missing source
- upgrade to 0.8
- Import haddock

