# http://github.com/matttproud/golang_protobuf_extensions

%global goipath         github.com/matttproud/golang_protobuf_extensions
%global commit          c12348ce28de40eed0136aa2b644d0ee0650e56c


%gometa -i

Name:           golang-github-matttproud-golang_protobuf_extensions
Version:        0
Release:        0.19%{?dist}
Summary:        Support for streaming Protocol Buffer messages for the Go language (golang)
License:        ASL 2.0
URL:            %{gourl}
Source0:        %{gosource}
Source1:        glide.yaml
Source2:        glide.yaml

%description
%{summary}

%package devel
Summary:       %{summary}
BuildArch:     noarch

BuildRequires: golang(github.com/golang/protobuf/proto)

%description devel
%{summary}

This package contains library source intended for
building other packages which use import path with
%{goipath} prefix.

%prep
%gosetup -q
cp %{SOURCE1} %{SOURCE2} .
%install
%goinstall glide.lock glide.yaml

%check
%gochecks

#define license tag if not already defined
%{!?_licensedir:%global license %doc}

%files devel -f devel.file-list
%license LICENSE
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - Forge-specific packaging variables
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Mon Jun 18 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.18.gitc12348c
- Upload glide files

* Thu Mar 01 2018 Jan Chaloupka <jchaloup@redhat.com> - 0-0.17.20160424gitc12348c
- Autogenerate some parts using the new macros

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.16.gitc12348c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Thu Nov 30 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.15.gitc12348c
- Polish the spec file
  related: #1214797

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.14.gitc12348c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.13.gitc12348c
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Mar 16 2017 Jan Chaloupka <jchaloup@redhat.com> - 0-0.12.gitc12348c
- Bump to upstream c12348ce28de40eed0136aa2b644d0ee0650e56c
  related: #1214797

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.11.gitd0c3fe8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Thu Jul 21 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.10.gitd0c3fe8
- https://fedoraproject.org/wiki/Changes/golang1.7

* Sun Mar 06 2016 jchaloup <jchaloup@redhat.com> - 0-0.9.gitd0c3fe8
- Bump to upstream d0c3fe89de86839aecf2e0579c40ba3bb336a453
  related: #1214797

* Mon Feb 22 2016 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.8.gitfc2b8d3
- https://fedoraproject.org/wiki/Changes/golang1.6

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.7.gitfc2b8d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Sat Sep 12 2015 jchaloup <jchaloup@redhat.com> - 0-0.6.gitfc2b8d3
- Update to spec-2.1
  resolves: #1214797

* Fri Aug 07 2015 Fridolin Pokorny <fpokorny@redhat.com> - 0-0.5.gitfc2b8d3
- Update spec file to spec-2.0
- Disable failing test
  resolves: #1214797

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0-0.4.gitfc2b8d3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Apr 23 2015 jchaloup <jchaloup@redhat.com> - 0-0.3.gitfc2b8d3
- Bump to upstream fc2b8d3a73c4867e51861bbdd5ae3c1f0869dd6a
  resolves: #1214797

* Thu Mar 05 2015 jchaloup <jchaloup@redhat.com> - 0-0.2.gitba7d65a
- Bump to upstream ba7d65ac66e9da93a714ca18f6d1bc7a0c09100c
  related: #1190438

* Sat Feb 07 2015 jchaloup <jchaloup@redhat.com> - 0-0.1.git7a864a0
- First package for Fedora
  resolves: #1190438

