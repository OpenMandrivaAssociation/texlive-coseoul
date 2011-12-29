# revision 23862
# category Package
# catalog-ctan /macros/latex/contrib/coseoul
# catalog-date 2011-09-06 16:13:05 +0200
# catalog-license lppl1.3
# catalog-version 1.1
Name:		texlive-coseoul
Version:	1.1
Release:	1
Summary:	Context sensitive outline elements
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/coseoul
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package provides "relative" commands that may be used in
place of \chapter, \section, etc. The documentation shows a
number of document-management scenarios in which such commands
are valuable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/coseoul/coseoul.sty
%doc %{_texmfdistdir}/doc/latex/coseoul/README
%doc %{_texmfdistdir}/doc/latex/coseoul/coseoul.pdf
%doc %{_texmfdistdir}/doc/latex/coseoul/coseoul.tex
%doc %{_texmfdistdir}/doc/latex/coseoul/cosexamp.pdf
%doc %{_texmfdistdir}/doc/latex/coseoul/cosexamp.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
