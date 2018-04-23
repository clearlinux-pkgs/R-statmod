#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-statmod
Version  : 1.4.30
Release  : 23
URL      : https://cran.r-project.org/src/contrib/statmod_1.4.30.tar.gz
Source0  : https://cran.r-project.org/src/contrib/statmod_1.4.30.tar.gz
Summary  : Statistical Modeling
Group    : Development/Tools
License  : GPL-2.0 GPL-3.0
Requires: R-statmod-lib
BuildRequires : clr-R-helpers

%description
No detailed description available

%package lib
Summary: lib components for the R-statmod package.
Group: Libraries

%description lib
lib components for the R-statmod package.


%prep
%setup -q -c -n statmod

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1502421600

%install
rm -rf %{buildroot}
export SOURCE_DATE_EPOCH=1502421600
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statmod
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library statmod
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export _R_CHECK_FORCE_SUGGESTS_=false
R CMD check --no-manual --no-examples --no-codoc -l %{buildroot}/usr/lib64/R/library statmod
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :


%files
%defattr(-,root,root,-)
/usr/lib64/R/library/statmod/CITATION
/usr/lib64/R/library/statmod/DESCRIPTION
/usr/lib64/R/library/statmod/INDEX
/usr/lib64/R/library/statmod/Meta/Rd.rds
/usr/lib64/R/library/statmod/Meta/data.rds
/usr/lib64/R/library/statmod/Meta/features.rds
/usr/lib64/R/library/statmod/Meta/hsearch.rds
/usr/lib64/R/library/statmod/Meta/links.rds
/usr/lib64/R/library/statmod/Meta/nsInfo.rds
/usr/lib64/R/library/statmod/Meta/package.rds
/usr/lib64/R/library/statmod/NAMESPACE
/usr/lib64/R/library/statmod/NEWS
/usr/lib64/R/library/statmod/R/statmod
/usr/lib64/R/library/statmod/R/statmod.rdb
/usr/lib64/R/library/statmod/R/statmod.rdx
/usr/lib64/R/library/statmod/data/welding.rdata
/usr/lib64/R/library/statmod/help/AnIndex
/usr/lib64/R/library/statmod/help/aliases.rds
/usr/lib64/R/library/statmod/help/paths.rds
/usr/lib64/R/library/statmod/help/statmod.rdb
/usr/lib64/R/library/statmod/help/statmod.rdx
/usr/lib64/R/library/statmod/html/00Index.html
/usr/lib64/R/library/statmod/html/R.css
/usr/lib64/R/library/statmod/libs/symbols.rds

%files lib
%defattr(-,root,root,-)
/usr/lib64/R/library/statmod/libs/statmod.so
/usr/lib64/R/library/statmod/libs/statmod.so.avx2
