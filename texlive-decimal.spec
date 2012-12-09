# revision 23374
# category Package
# catalog-ctan /macros/latex/contrib/decimal
# catalog-date 2011-06-06 11:09:01 +0200
# catalog-license lppl1
# catalog-version undef
Name:		texlive-decimal
Version:	20110606
Release:	2
Summary:	LaTeX package for the English raised decimal point
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/decimal
License:	LPPL1
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/decimal.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20110606-2
+ Revision: 750880
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20110606-1
+ Revision: 718209
- texlive-decimal
- texlive-decimal
- texlive-decimal
- texlive-decimal

