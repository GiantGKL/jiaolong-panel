# Jiaolong Panel

GTK4/Wayland 原生 CPU 功耗与温度控制面板，专为**机械革命 蛟龙16 Pro (2023)** 适配。

| 项目 | 详情 |
|------|------|
| 适配机型 | 机械革命 蛟龙16 Pro (2023)，同方 Tongfang 模具 |
| CPU | AMD Ryzen 9 7945HX (16C/32T, Dragon Range, Zen4) |
| GPU | AMD Radeon 610M (iGPU) + NVIDIA RTX 4060 (dGPU) |
| 验证系统 | Arch Linux, linux-zen 7.0.8, Wayland (Niri) |
| EC 指示灯 | 0xE4 寄存器 (00=橙 01=红 02=蓝) |

## 功能

- 实时 CPU 温度/频率/governor/boost 监控 (2s 刷新)
- 三种模式一键切换：省电 (35W/80°C) / 均衡 (55W/90°C) / 性能 (75W/95°C)
- 可拖拽温度墙滑块 (70-100°C，松手 0.5s 生效)
- EC 物理性能指示灯同步变色 (蓝/橙/红，仅同方模具)
- pkexec 提权，配置 polkit 规则后零密码操作

## 依赖

- `python` `python-gobject` `gtk4`
- `ryzenadj` — SMU TDP/温度控制
- `lm_sensors` — 温度读取
- `polkit` — 提权
- `ec_sys` 内核模块 — EC 指示灯 (需 `write_support=1`)

## 安装

### 下载预编译包

从 [GitHub Releases](https://github.com/GiantGKL/jiaolong-panel/releases) 下载对应发行版的包：

| 平台 | 包名 |
|------|------|
| Arch Linux | `jiaolong-panel-1.0.0-1-any.pkg.tar.zst` |
| Debian/Ubuntu | `jiaolong-panel_1.0.0-1_all.deb` |
| Fedora/RHEL | `jiaolong-panel-1.0.0-1.noarch.rpm` |

```bash
# Arch
sudo pacman -U jiaolong-panel-1.0.0-1-any.pkg.tar.zst

# Debian/Ubuntu
sudo dpkg -i jiaolong-panel_1.0.0-1_all.deb

# Fedora
sudo rpm -i jiaolong-panel-1.0.0-1.noarch.rpm
```

### 源码安装

```bash
git clone https://github.com/GiantGKL/jiaolong-panel.git
cd jiaolong-panel

# Arch
makepkg -si

# Debian/Ubuntu
dpkg-buildpackage -us -uc -b
sudo dpkg -i ../jiaolong-panel_*.deb

# Fedora
rpmbuild -ba jiaolong-panel.spec
sudo dnf install ~/rpmbuild/RPMS/noarch/jiaolong-panel-*.rpm
```

### 手动安装

```bash
sudo cp jiaolong-panel /usr/bin/
sudo cp jiaolong-panel.desktop /usr/share/applications/
```

## 配置

### 免密码认证

```bash
sudo tee /etc/polkit-1/rules.d/50-jiaolong-panel.rules << 'POLKIT'
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.policykit.exec" &&
        subject.user == "YOUR_USERNAME" &&
        (action.lookup("program") == "/usr/bin/ryzenadj" ||
         action.lookup("program") == "/usr/bin/bash")) {
        return polkit.Result.YES;
    }
});
POLKIT
sudo systemctl restart polkit
```

### EC 指示灯 (仅同方模具)

```bash
echo 'ec_sys write_support=1' | sudo tee /etc/modules-load.d/ec_sys.conf
sudo modprobe ec_sys write_support=1
```

非同方模具机型不会显示指示灯颜色变化，其他功能是否正常未经测试。

## 许可证

MIT
