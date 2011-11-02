Name:		texlive-ltxnew
Version:	1.3
Release:	1
Summary:	A simple means of creating commands
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ltxnew
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ltxnew.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package ltxnew provides \new, \renew and \provide prefixes
for checking definitions. It is designed to work with e-TeX
distributions of LaTeX and relies on the LaTeX internal macro
\@ifdefinable. Local allocation of counters, dimensions, skips,
muskips, boxes, tokens and marks are provided by the etex
package. \new and \renew as well as \provide may be used for
all kind of control sequences. Please refer to the section
"Using \new" of the PDF documentation.

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