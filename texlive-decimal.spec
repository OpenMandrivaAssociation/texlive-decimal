Name:		texlive-decimal
Version:	23374
Release:	1
Summary:	LaTeX package for the English raised decimal point
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/decimal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This LaTeX package should be used by people who need the
traditional English raised decimal point, instead of the
American-style period.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/decimal/decimal.sty
%doc %{_texmfdistdir}/doc/latex/decimal/decimal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/decimal/decimal.dtx
%doc %{_texmfdistdir}/source/latex/decimal/decimal.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
