# revision 23374
# category Package
# catalog-ctan /macros/latex/contrib/decimal
# catalog-date 2011-06-06 11:09:01 +0200
# catalog-license lppl1
# catalog-version undef
Name:		texlive-decimal
Version:	20110606
Release:	1
Summary:	LaTeX package for the English raised decimal point
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/decimal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
This LaTeX package should be used by people who need the
traditional English raised decimal point, instead of the
American-style period.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/decimal/decimal.sty
%doc %{_texmfdistdir}/doc/latex/decimal/decimal.pdf
#- source
%doc %{_texmfdistdir}/source/latex/decimal/decimal.dtx
%doc %{_texmfdistdir}/source/latex/decimal/decimal.ins
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
