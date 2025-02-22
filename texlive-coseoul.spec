Name:		texlive-coseoul
Version:	23862
Release:	2
Summary:	Context sensitive outline elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coseoul
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
