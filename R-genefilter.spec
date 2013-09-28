%global packname  genefilter
%global rlibdir  %{_libdir}/R/library

Name:             R-%{packname}
Version:          1.42.0
Release:          1
Summary:          genefilter: methods for filtering genes from microarray experiments
Group:            Sciences/Mathematics
License:          Artistic-2.0
URL:              http://bioconductor.org/packages/release/bioc/html/%{packname}.html
Source0:          http://bioconductor.org/packages/release/bioc/src/contrib/genefilter_1.42.0.tar.gz
Requires:         R-AnnotationDbi R-annotate R-Biobase R-graphics R-methods
Requires:         R-stats R-survival R-Biobase R-class R-hgu95av2.db
Requires:         R-tkWidgets R-ALL
BuildRequires:    R-devel Rmath-devel texlive-collection-latex
BuildRequires:    R-AnnotationDbi R-annotate R-Biobase R-graphics R-methods
BuildRequires:    R-stats R-survival R-Biobase R-class R-hgu95av2.db
BuildRequires:    R-tkWidgets R-ALL

%description
Some basic functions for filtering genes

%prep
%setup -q -c -n %{packname}

%build

%install
mkdir -p %{buildroot}%{rlibdir}
%{_bindir}/R CMD INSTALL -l %{buildroot}%{rlibdir} %{packname}
test -d %{packname}/src && (cd %{packname}/src; rm -f *.o *.so)
rm -f %{buildroot}%{rlibdir}/R.css

%check
%{_bindir}/R CMD check %{packname}

%files
%dir %{rlibdir}/%{packname}
%doc %{rlibdir}/%{packname}/doc
%doc %{rlibdir}/%{packname}/html
%doc %{rlibdir}/%{packname}/DESCRIPTION
%{rlibdir}/%{packname}/INDEX
%{rlibdir}/%{packname}/NAMESPACE
%{rlibdir}/%{packname}/Meta
%{rlibdir}/%{packname}/R
%{rlibdir}/%{packname}/data
%{rlibdir}/%{packname}/help
%{rlibdir}/%{packname}/libs
%{rlibdir}/%{packname}/wFun

