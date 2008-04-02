#
# TODO: shared/static scheme
# (if something more than plplot driver uses it, little sense otherwise...)
Summary:	CGM Draw library and tools
Summary(pl.UTF-8):	Biblioteka i narzędzia CGM Draw
Name:		cd
Version:	1.3
Release:	3
License:	free (see cd.html)
Group:		Libraries
Source0:	http://www.pa.msu.edu/ftp/pub/unix/%{name}%{version}.tar.gz
# Source0-md5:	5484b3fe667170c221eb8871ea2bb332
URL:		http://www.pa.msu.edu/reference/cgmdraw_ref.html
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGM Draw is a freely available library for generating CGM files from a
C program. It has been tested on Solaris, Ultrix, Linux, IRIX, AIX,
OpenVMS, and DOS. CGM (Computer Graphics Metafile) is a vector
graphics format that can be read by many popular packages. With CGM
Draw your code can quickly draw images complete with lines, arcs,
rectangles, polygons, and text. CGM Draw is ideal for creating CGM
files on the fly when you have a rapidly changing data set (such as in
response to database queries.)

%description -l pl.UTF-8
CGM Draw to wolnodostępna biblioteka do generowania plików CGM z
poziomu programu w C. Była testowana pod Solarisem, Ultriksem,
Linuksem, IRIX-em, AIX-em, OpenVMS-em oraz DOS-em. CGM (Computer
Graphics Metafile) to wektorowy format graficzny czytany przez wiele
popularnych pakietów. Przy pomocy CGM Draw kod może szybko rysować
obrazki z linii, łuków, prostokątów, wielokątów oraz tekstu. CGM Draw
sprawdza się przy tworzeniu plików CGM w locie z szybko zmieniających
się zbiorów danych (takich jak odpowiedzi na zapytania do baz danych).

%package devel
Summary:	Header file and static CGM Draw library
Summary(pl.UTF-8):	Pliki nagłówkowe i statyczna biblioteka CGM Draw
Group:		Development/Libraries

%description devel
CGM Draw is a freely available library for generating CGM files from a
C program. It has been tested on Solaris, Ultrix, Linux, IRIX, AIX,
OpenVMS, and DOS. CGM (Computer Graphics Metafile) is a vector
graphics format that can be read by many popular packages. With CGM
Draw your code can quickly draw images complete with lines, arcs,
rectangles, polygons, and text. CGM Draw is ideal for creating CGM
files on the fly when you have a rapidly changing data set (such as in
response to database queries.)

This package contains the header file and static CGM Draw library.

%description devel -l pl.UTF-8
CGM Draw to wolnodostępna biblioteka do generowania plików CGM z
poziomu programu w C. Była testowana pod Solarisem, Ultriksem,
Linuksem, IRIX-em, AIX-em, OpenVMS-em oraz DOS-em. CGM (Computer
Graphics Metafile) to wektorowy format graficzny czytany przez wiele
popularnych pakietów. Przy pomocy CGM Draw kod może szybko rysować
obrazki z linii, łuków, prostokątów, wielokątów oraz tekstu. CGM Draw
sprawdza się przy tworzeniu plików CGM w locie z szybko zmieniających
się zbiorów danych (takich jak odpowiedzi na zapytania do baz danych).

Ten pakiet zawiera plik nagłówkowy i statyczną bibliotekę CGM Draw.

%prep
%setup -q -n %{name}%{version}

%build
# libcd is used in plplot shared module - needs PIC
%{__make} libcd.a \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -fPIC -Wall -pedantic"

%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -pedantic"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_includedir},%{_examplesdir}/%{name}-%{version}}

install libcd.a $RPM_BUILD_ROOT%{_libdir}
install cd.h $RPM_BUILD_ROOT%{_includedir}
install cdexpert.c cdmulti.c cdsimple.c cdtest.c cdtext.c color16.c \
	$RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files devel
%defattr(644,root,root,755)
%doc cd.announce cd.html readme
%{_libdir}/libcd.a
%{_includedir}/cd.h
%{_examplesdir}/%{name}-%{version}
