Name:           jiaolong-panel
Version:        1.0.0
Release:        1%{?dist}
Summary:        CPU power/temperature control panel for Mechrevo Jiaolong 16 Pro (2023)
License:        MIT
URL:            https://github.com/giantgkl/jiaolong-panel
Source0:        %{url}/archive/v%{version}.tar.gz

Requires:       python3, python3-gobject, gtk4, ryzenadj, lm_sensors, polkit
BuildArch:      noarch

%description
A Wayland-native control panel for AMD Ryzen CPUs providing real-time
temperature and frequency monitoring, one-click power profile switching,
TDP limit and temperature wall control via ryzenadj, and EC performance
LED synchronization for Tongfang-chassis laptops.

%prep
%setup -q

%install
install -Dm755 jiaolong-panel %{buildroot}/usr/bin/jiaolong-panel
install -Dm644 jiaolong-panel.desktop %{buildroot}/usr/share/applications/jiaolong-panel.desktop

%files
/usr/bin/jiaolong-panel
/usr/share/applications/jiaolong-panel.desktop

%changelog
* Sun May 25 2025 giantgkl - 1.0.0-1
- Initial release
