# revision 21586
# category Package
# catalog-ctan /macros/latex/contrib/ltxnew
# catalog-date 2011-03-02 16:08:00 +0100
# catalog-license lppl1.3
# catalog-version 1.3
Name:		texlive-ltxnew
Version:	1.3
Release:	4
Summary:	A simple means of creating commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxnew
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package ltxnew provides \new, \renew and \provide prefixes
for checking definitions. It is designed to work with e-TeX
distributions of LaTeX and relies on the LaTeX internal macro
\@ifdefinable. Local allocation of counters, dimensions, skips,
muskips, boxes, tokens and marks are provided by the etex
package. \new and \renew as well as \provide may be used for
all kind of control sequences. Please refer to the section
"Using \new" of the PDF documentation.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/ltxnew/ltxnew.sty
%doc %{_texmfdistdir}/doc/latex/ltxnew/README
%doc %{_texmfdistdir}/doc/latex/ltxnew/ltxnew.pdf
#- source
%doc %{_texmfdistdir}/source/latex/ltxnew/ltxnew.dtx
%doc %{_texmfdistdir}/source/latex/ltxnew/ltxnew.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.3-2
+ Revision: 753577
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.3-1
+ Revision: 718916
- texlive-ltxnew
- texlive-ltxnew
- texlive-ltxnew
- texlive-ltxnew

