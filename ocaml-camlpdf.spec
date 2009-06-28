Name:           ocaml-camlpdf
Version:        0.4
Release:        %mkrel 2
Summary:        CamlPDF allows you to read, write, and manipulate PDF data with OCaml
Group:          Development/Other
License:        BSD
URL:            http://freshmeat.net/projects/camlpdf/
Source0:        http://www.coherentgraphics.co.uk/camlpdf-%{version}.tar.bz2
Source1:        camlpdf-META.in
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}
BuildRequires:  ocaml
BuildRequires:  zlib-devel
BuildRequires:  tetex-latex
BuildRequires:  gzip

%description
This is CamlPDF, an OCaml library for reading, writing and manipulating Adobe
portable document files. 
CamlPDF consists of a set of low level modules for representing, reading and
writing the basic structure of PDF, together with an initial attempt at a
higher level API.

Please advise of the following:
  o Files which cannot be read or written, or any other runtime error;
  o Instances of particularly slow or resource-hungry scenarios.

Please be aware that PDF is a highly complex format and that many files are
malformed. We will incorporate support for malformed files if Acrobat reads
them.


%package        devel
Summary:        Development files for %{name}
Group:          Development/Other
Requires:       %{name} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and signature files for
developing applications that use %{name}.


%prep
%setup -q -n camlpdf-%{version}
cp %{SOURCE1} META.in

%build
make
make htdoc
make psdoc
gzip --best doc/camlpdf/latex/doc.ps

sed -e 's/@VERSION@/%{version}/g' < META.in > META

mkdir -p examples
cp pdfhello.ml pdfdecomp.ml pdfmerge.ml pdfdraft.ml pdftest.ml  examples/
cp examplesmake  examples/Makefile
cp OCamlMakefile  examples/

%install
rm -rf %{buildroot}
%define destdir %{buildroot}/%{_libdir}/ocaml/camlpdf
%define destdll %{buildroot}/%{_libdir}/ocaml/stublibs

mkdir -p %{destdir}/
mkdir -p %{destdll}/

install -m 0644 *.cma *.cmxa *.a *.cmi *.mli %{destdir}/
install -m 0644 META %{destdir}/
install -m 0755 *.so %{destdll}/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc LICENCE
%dir %{_libdir}/ocaml/camlpdf
%{_libdir}/ocaml/camlpdf/META
%{_libdir}/ocaml/camlpdf/*.cma
%{_libdir}/ocaml/camlpdf/*.cmi
%{_libdir}/ocaml/stublibs/*.so

%files devel
%defattr(-,root,root,-)
%doc LICENCE README examples
%doc doc/camlpdf/html
%doc doc/camlpdf/latex/*.{dvi,ps.gz}
%{_libdir}/ocaml/camlpdf/*.a
%{_libdir}/ocaml/camlpdf/*.cmxa
%{_libdir}/ocaml/camlpdf/*.mli

