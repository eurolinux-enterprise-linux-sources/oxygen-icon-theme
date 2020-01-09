Name:    oxygen-icon-theme
Summary: Oxygen icon theme
Version: 4.10.5
Release: 2%{?dist}

# http://techbase.kde.org/Policies/Licensing_Policy
License: LGPLv3+ 
URL:     http://www.kde.org/
%global revision %(echo %{version} | cut -d. -f3)
%if %{revision} >= 50
%global stable unstable
%else
%global stable stable
%endif
Source0: http://download.kde.org/%{stable}/%{version}/src/oxygen-icons-%{version}.tar.xz
BuildArch: noarch

BuildRequires: cmake
BuildRequires: hardlink
BuildRequires: kde-filesystem

# upstream name
Provides: oxygen-icons = %{version}-%{release}
Provides: system-kde-icon-theme = %{version}-%{release}

%description
%{summary}.


%prep
%setup -q -n oxygen-icons-%{version}


%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ..
popd

make %{?_smp_mflags} -C %{_target_platform} 


%install
rm -rf %{buildroot}

make install/fast DESTDIR=%{buildroot} -C %{_target_platform}

# As of 4.7.3, hardlink reports 
#Directories 91
#Objects 6821
#IFREG 6730
#Comparisons 859
#Linked 859
#saved 7864320
/usr/sbin/hardlink -c -v %{buildroot}%{_kde4_iconsdir}/oxygen

# create/own all potential dirs
mkdir -p %{buildroot}%{_kde4_iconsdir}/oxygen/{16x16,22x22,24x24,32x32,36x36,48x48,64x64,96x96,128x128,512x512,scalable}/{actions,apps,devices,mimetypes,places}

# %%ghost icon.cache
touch  %{buildroot}%{_kde4_iconsdir}/oxygen/icon-theme.cache


%post 
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :

%posttrans 
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :

%postun 
if [ $1 -eq 0 ] ; then
touch --no-create %{_kde4_iconsdir}/oxygen &> /dev/null || :
gtk-update-icon-cache %{_kde4_iconsdir}/oxygen &> /dev/null || :
fi

%files 
%doc AUTHORS CONTRIBUTING COPYING
%dir %{_kde4_iconsdir}/oxygen/
%ghost %{_kde4_iconsdir}/oxygen/icon-theme.cache
%{_kde4_iconsdir}/oxygen/index.theme
%{_kde4_iconsdir}/oxygen/*x*/
%{_kde4_iconsdir}/oxygen/scalable/


%changelog
* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 4.10.5-2
- Mass rebuild 2013-12-27

* Sun Jun 30 2013 Than Ngo <than@redhat.com> - 4.10.5-1
- 4.10.5

* Sat Jun 01 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.4-1
- 4.10.4

* Mon May 06 2013 Than Ngo <than@redhat.com> - 4.10.3-1
- 4.10.3

* Sat Mar 30 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.2-1
- 4.10.2

* Sat Mar 02 2013 Rex Dieter <rdieter@fedoraproject.org> 4.10.1-1
- 4.10.1

* Thu Jan 31 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.10.0-1
- 4.10.0

* Sat Jan 19 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.98-1
- 4.9.98

* Thu Jan 03 2013 Rex Dieter <rdieter@fedoraproject.org> - 4.9.97-1
- 4.9.97

* Wed Dec 19 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.95-1
- 4.9.95

* Mon Dec 03 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.90-1
- 4.9.90 (4.10beta2)

* Fri Nov 02 2012 Rex Dieter <rdieter@fedoraproject.org> 4.9.3-1
- 4.9.3

* Fri Sep 28 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.2-1
- 4.9.2

* Mon Sep 03 2012 Than Ngo <than@redhat.com> - 4.9.1-1
- 4.9.1

* Sun Aug 12 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-2
- remove .spec cruft
- fancify Source0 handling

* Thu Jul 26 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.9.0-1
- 4.9.0

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.8.97-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Wed Jul 11 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.97-1
- 4.8.97

* Wed Jun 27 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.95-1
- 4.8.95

* Fri Jun 08 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.90-1
- 4.8.90

* Fri May 25 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.80-1
- 4.8.80

* Mon Apr 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.3-1
- 4.8.3

* Fri Mar 30 2012 Jaroslav Reznik <jreznik@redhat.com> - 4.8.2-1
- 4.8.2

* Mon Mar 05 2012 Radek Novacek <rnovacek@redhat.com> 4.8.1-1
- 4.8.1

* Sun Jan 22 2012 Rex Dieter <rdieter@fedoraproject.org> - 4.8.0-1
- 4.8.0

* Wed Jan 11 2012 Rex Dieter <rdieter@fedoraproject.org> 4.7.97-2
- icon theme cache not removed on uninstall (#771487)
- try harder to own all related dirs

* Wed Jan 04 2012 Radek Novacek <rnovacek@redhat.com> - 4.7.97-1
- 4.7.97

* Fri Dec 23 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.95-2
- Provides: oxygen-icons

* Wed Dec 21 2011 Radek Novacek <rnovacek@redhat.com> - 4.7.95-1
- 4.7.95

* Sat Dec 03 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.90-1
- 4.7.90

* Fri Nov 18 2011 Jaroslav Reznik <jreznik@redhat.com> 4.7.80-1
- 4.7.80 (beta 1)

* Fri Oct 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.3-1
- 4.7.3

* Tue Oct 04 2011 Rex Dieter <rdieter@fedoraproject.org> 4.7.2-1
- 4.7.2

* Wed Sep 14 2011 Radek Novacek <rnovacek@redhat.com> 4.7.1-1
- 4.7.1

* Tue Jul 26 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.7.0-1
- 4.7.0

* Fri Jul 08 2011 Jaroslav Reznik <jreznik@redhat.com> - 4.6.95-1
- 4.6.95 (rc2)

* Tue Jun 28 2011 Than Ngo <than@redhat.com> - 4.6.90-1
- 4.6.90 (rc1)

* Fri May 27 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.80-1
- 4.6.80 (beta1)

* Thu Apr 28 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.3-1
- 4.6.3

* Wed Apr 06 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.2-1
- 4.6.2

* Sat Feb 26 2011 Rex Dieter <rdieter@fedoraproject.org> 4.6.1-1
- 4.6.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.6.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jan 21 2011 Jaroslav Reznik <jreznik@redhat.com> 4.6.0-1
- 4.6.0

* Wed Jan 05 2011 Jaroslav Reznik <jreznik@redhat.com> 4.5.95-1
- 4.5.95 (4.6rc2)

* Wed Dec 22 2010 Rex Dieter <rdieter@fedoraproject.org> 4.5.90-1 
- 4.5.90 (4.6rc1)

* Fri Dec 03 2010 Thomas Janssen <thomasj@fedoraproject.org> 4.5.85-1
- 4.5.85 (4.6beta2)

* Sat Nov 20 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.80-1
- 4.5.80 (4.6beta1)

* Sun Oct 31 2010 Than Ngo <than@redhat.com> - 4.5.3-1
- 4.5.3

* Fri Oct 01 2010 Rex Dieter <rdieter@fedoraproject.org> -  4.5.2-1
- 4.5.2

* Tue Sep 28 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-2
- Obsoletes: fedora-kde-icon-theme (f13+)
- Provides:  system-kde-icon-theme (f13+)

* Fri Aug 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.5.1-1
- 4.5.1

* Thu Aug 05 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.5.0-1
- 4.5.0

* Sat Jul 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.95-1
- 4.5 RC3 (4.4.95)

* Wed Jul 07 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.92-1
- 4.5 RC2 (4.4.92)

* Fri Jun 25 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.90-1
- 4.5 RC 1 (4.4.90)

* Mon Jun 07 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.85-1
- 4.5 Beta 2 (4.4.85)

* Fri May 21 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.80-1
- 4.5 Beta 1 (4.4.80)

* Fri Apr 30 2010 Jaroslav Reznik <jreznik@redhat.com> - 4.4.3-1
- 4.4.3

* Mon Mar 29 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.4.2-1
- 4.4.2

* Sat Feb 27 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.1-1
- 4.4.1

* Tue Feb 09 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.4.0-2
- hardlink dup'd icons

* Fri Feb 05 2010 Than Ngo <than@redhat.com> - 4.4.0-1
- 4.4.0

* Sun Jan 31 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.98-1
- KDE 4.3.98 (4.4rc3)

* Thu Jan 21 2010 Lukas Tinkl <ltinkl@redhat.com> - 4.3.95-1
- KDE 4.3.95 (4.4rc2)

* Wed Jan  6 2010 Rex Dieter <rdieter@fedoraproject.org> - 4.3.90-1
- 4.3.90 (4.4 rc1)

* Fri Dec 18 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.85-1
- 4.3.85 (4.4 beta2)

* Tue Dec  1 2009 Lukáš Tinkl <ltinkl@redhat.com> - 4.3.80-1
- KDE 4.4 beta1 (4.3.80)

* Sat Nov 21 2009 Ben Boeckel <MathStuf@gmail.com> - 4.3.75-0.1.svn1048496
- Update to 4.3.75 snapshot

* Sat Oct 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.3.3-1
- 4.3.3

* Mon Oct 05 2009 Than Ngo <than@redhat.com> - 4.3.2-1
- 4.3.2

* Fri Aug 28 2009 Than Ngo <than@redhat.com> - 4.3.1-1
- 4.3.1

* Thu Jul 30 2009 Than Ngo <than@redhat.com> - 4.3.0-1
- 4.3.0

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.2.98-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Jul 22 2009 Than Ngo <than@redhat.com> - 4.2.98-1
- 4.3rc3

* Mon Jul 13 2009 Than Ngo <than@redhat.com> - 4.2.96-1
- 4.3rc2

* Fri Jun 26 2009 Than Ngo <than@redhat.com> - 4.2.95-1
- 4.3rc1

* Wed Jun 03 2009 Rex Dieter <rdieter@fedoraproject.org> 4.2.90-1
- KDE-4.3 beta2 (4.2.90)

* Fri May 08 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.85-1
- oxygen-icons-4.2.85

* Tue Mar 31 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.2-1
- kde-4.2.2

* Mon Mar 30 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-11
- License: LGPLv3+
- %%doc: AUTHORS CONTRIBUTING COPYING TODO*

* Fri Mar 27 2009 Rex Dieter <rdieter@fedoraproject.org> - 4.2.1-10
- standalone (noarch) oxygen-icon-theme

