# Jiaolong Panel
GTK4/Wayland 原生 CPU 功耗与温度控制面板，专为 机械革命 蛟龙16 Pro (2023) 设计

![screenshot](screenshot.png)

## 功能

- 🌡 **实时监控** — Tctl/CCD/GPU 温度，频率，governor，boost 状态，每 2 秒刷新
- 🎛 **一键切换** — 省电（35W/80°C 蓝灯）· 均衡（55W/90°C 橙灯）· 性能（75W/95°C 红灯）
- 📐 **温度墙滑块** — 70-100°C 可调，松手生效
- 💡 **EC 指示灯同步** — 机械革命/同方模具物理性能灯自动变色
- 🔒 **pkexec 提权** — 无需终端，图形化认证

## 依赖

- `python-gobject` `gtk4` (GUI)
- `ryzenadj` (SMU 控制)
- `lm_sensors` (温度读取)
- `polkit` (提权)
- `ec_sys write_support=1` (EC 指示灯，需加载内核模块)

## 安装

### Arch Linux (AUR)

```bash
paru -S jiaolong-panel
```

或手动打包：

```bash
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
makepkg -si
```

### Debian/Ubuntu

```bash
sudo apt install debhelper
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
dpkg-buildpackage -us -uc -b
sudo dpkg -i ../jiaolong-panel_1.0.0-1_all.deb
```

### Fedora/RHEL

```bash
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
rpmbuild -ba jiaolong-panel.spec
sudo dnf install ~/rpmbuild/RPMS/noarch/jiaolong-panel-1.0.0-1.fc*.noarch.rpm
```

### 手动安装

```bash
sudo cp jiaolong-panel /usr/bin/jiaolong-panel
sudo cp jiaolong-panel.desktop /usr/share/applications/
```

## 免密码认证

创建 polkit 规则使面板操作无需密码：

```bash
sudo tee /etc/polkit-1/rules.d/50-jiaolong-panel.rules << 'EOF'
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.policykit.exec" &&
        subject.user == "YOUR_USER" &&
        (action.lookup("program") == "/usr/bin/ryzenadj" ||
         action.lookup("program") == "/usr/bin/bash")) {
        return polkit.Result.YES;
    }
});
EOF
sudo systemctl restart polkit
```

## EC 指示灯（机械革命/同方模具）

```bash
echo 'ec_sys write_support=1' | sudo tee /etc/modules-load.d/ec_sys.conf
sudo modprobe ec_sys write_support=1
```

## 许可证

MIT
