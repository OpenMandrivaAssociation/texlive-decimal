%global tl_name decimal
%global tl_revision 23374

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	LaTeX package for the English raised decimal point
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/decimal
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This LaTeX package should be used by people who need the traditional
English raised decimal point, instead of the American-style period.

