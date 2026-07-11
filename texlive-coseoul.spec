%global tl_name coseoul
%global tl_revision 23862

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1
Release:	%{tl_revision}.1
Summary:	Context sensitive outline elements
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/coseoul
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/coseoul.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package provides "relative" commands that may be used in place of
\chapter, \section, etc. The documentation shows a number of document-
management scenarios in which such commands are valuable.

