Summary:	High performance collections for Java
Summary(pl.UTF-8):	Wysokowydajne kolekcje dla Javy
Name:		gnu.trove
Version:	1.0.2
Release:	0.1
License:	LGPL
Group:		Development/Languages/Java
Source0:	http://downloads.sourceforge.net/trove4j/trove-%{version}.tar.gz
# Source0-md5:	a246a09db112b7986b02c2a9f771bae0
Source1:	%{name}-build.xml
URL:		http://trove4j.sourceforge.net/
BuildRequires:	ant >= 0:1.6
BuildRequires:	ant-junit >= 0:1.6
BuildRequires:	jdk
BuildRequires:	jpackage-utils >= 0:1.5.32
BuildRequires:	junit
BuildRequires:	rpm-javaprov
BuildRequires:	rpmbuild(macros) >= 1.300
%if %(locale -a | grep -q '^en_US$'; echo $?)
BuildRequires:	glibc-localedb-all
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The GNU Trove library has two objectives:

Provide "free" (as in "free speech" and "free beer"), fast,
lightweight implementations of the java.util Collections API. These
implementations are designed to be pluggable replacements for their
JDK equivalents.

Whenever possible, provide the same collections support for primitive
types. This gap in the JDK is often addressed by using the "wrapper"
classes (java.lang.Integer, java.lang.Float, etc.) with Object-based
collections. For most applications, however, collections which store
primitives directly will require less space and yield significant
performance gains.

%description -l pl.UTF-8
Biblioteka GNU Trove ma dwa cele:

1. Udostępnienie wolnodostępnych, szybkich, lekkich implementacji API
java.util Collections. Implementacje te są projektowane jako
zamienniki ich odpowiedników z JDK.

2. Na ile to możliwe udostępnienie takiej samej obsługi kolekcji dla
typów prymitywnych. W JDK jest to zwykle osiągane poprzez użycie klas
obudowujących (java.lang.Integer, java.lang.Float itp.) wraz z
kolekcjami opartymi na obiektach. Dla większości aplikacji jednak
kolekcje przechowujące prymitywy zwykle wymagają mniej pamięci i
osiągają znaczącą poprawę wydajności.

%package javadoc
Summary:	Javadoc for %{name}
Summary(pl.UTF-8):	Dokumentacja Javadoc do pakietu %{name}
Group:		Documentation
Requires:	jpackage-utils

%description javadoc
Javadoc documentation for %{name}.

%description javadoc -l pl.UTF-8
Dokumentacja Javadoc do pakietu %{name}.

%prep
%setup -q -n trove-%{version}
cp %{SOURCE1} build.xml

%build
export OPT_JAR_LIST="ant/ant-junit junit"

export LC_ALL=en_US # source code not US-ASCII
%ant -Dbuild.sysclasspath=only dist

%install
rm -rf $RPM_BUILD_ROOT
# jars
install -d $RPM_BUILD_ROOT%{_javadir}
cp -a target/trove-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}-%{version}.jar
ln -s %{name}-%{version}.jar $RPM_BUILD_ROOT%{_javadir}/%{name}.jar

# javadoc
install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -pr dist/docs/api/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
ln -s %{name}-%{version} $RPM_BUILD_ROOT%{_javadocdir}/%{name} # ghost symlink

%clean
rm -rf $RPM_BUILD_ROOT

%post javadoc
ln -nfs %{name}-%{version} %{_javadocdir}/%{name}

%files
%defattr(644,root,root,755)
%{_javadir}/*.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
%ghost %{_javadocdir}/%{name}
