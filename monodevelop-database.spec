#
# spec file for package monodevelop-database
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define db_packages mono(System.Data.OracleClient) mono(Mono.Data.Sqlite)
%define db_packages_source %db_packages pkgconfig(npgsql)
%define db_packages_binary %db_packages mono(Npgsql)

Name:           monodevelop-database
Version:        5.10.0.871
Release:        0.xamarin.3
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://www.monodevelop.com
Source:         %{name}_%{version}.orig.tar.bz2
BuildRequires:  %db_packages_source
BuildRequires:  gettext
BuildRequires:  pkgconfig(mono) >= 4.2
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(monodevelop) >= 5.10
Requires:       %db_packages_binary
Requires:	monodevelop > 5.10
Requires:	monodevelop < 5.11
Summary:        Monodevelop Database Addin
Group:          Development/Languages/Mono
AutoReqProv:	no
Patch0:		fix_dependencies.patch
Patch1:		use_distro_npgsql.patch

%description
Addin for MonoDevelop for an integrated database explorer and editor.

%package devel
Summary:        Development files for MonoDevelop Database
Group:          Development/Languages/Mono
Requires:       monodevelop-database = %{version}

%description devel
The pkgconfig file for MonoDevelop Database.

%prep
%setup -q -n %{name}-5.10
%patch0 -p1
%patch1 -p1

%build
%{?env_options}
./configure --prefix=%{_prefix}
make

%install
%{?env_options}
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{_datadir}/pkgconfig
mv %{buildroot}%{_prefix}/lib/pkgconfig/*.pc %{buildroot}%{_datadir}/pkgconfig
%{find_lang} %{name}

%files -f %{name}.lang
%defattr(-, root, root)
%{_prefix}/lib/monodevelop/AddIns/MonoDevelop.Database

%files devel
%defattr(-,root,root)
%{_datadir}/pkgconfig/monodevelop-database.pc

%changelog

