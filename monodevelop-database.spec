#
# spec file for package monodevelop-database
#
# Copyright (c) 2014 SUSE LINUX Products GmbH, Nuernberg, Germany.
# This file and all modifications and additions to the pristine
# package are under the same license as the package itself.
#
# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

%define db_packages mono-data-oracle mono-data-postgresql mono-data-sqlite

Name:           monodevelop-database
Version:        5.7.0.660
Release:        0
License:        MIT
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Url:            http://www.monodevelop.com
Source:         %{name}_%{version}.orig.tar.gz
BuildRequires:  %db_packages
BuildRequires:  gettext
BuildRequires:  pkgconfig(mono)
BuildRequires:  pkgconfig(mono-addins)
BuildRequires:  pkgconfig(monodevelop) >= 5.7
Requires:       %db_packages
Summary:        Monodevelop Database Addin
Group:          Development/Languages/Mono

%description
Addin for MonoDevelop for an integrated database explorer and editor.

%package devel
Summary:        Development files for MonoDevelop Database
Group:          Development/Languages/Mono
Requires:       monodevelop-database = %{version}

%description devel
The pkgconfig file for MonoDevelop Database.

%prep
%setup -q -n %{name}-5.7

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

