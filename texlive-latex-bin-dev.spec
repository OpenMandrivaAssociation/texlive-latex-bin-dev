Name:		texlive-latex-bin-dev
Version:	62387
Release:	2
Summary:	LaTeX pre-release executables and formats
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/latex-bin-dev
License:	
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin-dev.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/latex-bin-dev.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
See the latex-base-dev package for information.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_datadir}
cp -a texmf-dist %{buildroot}%{_datadir}

%files
%{_texmfdistdir}/texmf-dist
%{_texmfdistdir}/texmf-dist/doc
%doc %{_texmfdistdir}/texmf-dist/doc/man
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xelatex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/xelatex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/uplatex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/uplatex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/platex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/platex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdflatex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/pdflatex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/lualatex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/lualatex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/latex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/latex-dev.1
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvilualatex-dev.man1.pdf
%doc %{_texmfdistdir}/texmf-dist/doc/man/man1/dvilualatex-dev.1

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
