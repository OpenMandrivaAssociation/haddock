
Summary: Haddock documentation tool for annotated Haskell source code
Name: haddock
Version: 0.8
Release: %mkrel 1
License: BSD-like
Group: Development/Other
Source: http://www.haskell.org/haddock/haddock-%{version}-src.tar.bz2
URL: http://www.haskell.org/haddock/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires: ghc
BuildRequires: happy
BuildRequires: alex
BuildRequires: libxslt-proc docbook-style-xsl
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
%setup -q -n %{name}-%{version}

%build
runhaskell Setup.lhs configure --prefix=%{_prefix}
runhaskell Setup.lhs build
cd doc
test -f configure || autoreconf
./configure
make html


%install
rm -rf ${RPM_BUILD_ROOT}
runhaskell Setup.lhs copy --destdir=${RPM_BUILD_ROOT}

%clean
rm -rf ${RPM_BUILD_ROOT}

%files
%defattr(-,root,root)
%doc doc/haddock/*
%{_datadir}/*
%{_bindir}/haddock


