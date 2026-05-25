# Jiaolong Panel

**专为 机械革命 蛟龙16 Pro (2023) 打造** 的 GTK4/Wayland 原生 CPU 功耗与温度控制面板。

| 项目 | 详情 |
|------|------|
| 适配机型 | 机械革命 蛟龙16 Pro (2023)，同方 Tongfang 模具 |
| CPU | AMD Ryzen 9 7945HX (16C/32T, Dragon Range, Zen4) |
| GPU | AMD Radeon 610M (iGPU) + NVIDIA RTX 4060 (dGPU) |
| 验证系统 | Arch Linux, linux-zen 7.0.8, Wayland (Niri) |
| EC 指示灯 | 0xE4 寄存器 (00=橙 01=红 02=蓝) |

## 功能

- 🌡 **实时监控** — Tctl / CCD1 / CCD2 / GPU 温度 + 核心频率 + governor + boost
- 🎛 **一键切换** — 省电 (35W/80°C) · 均衡 (55W/90°C) · 性能 (75W/95°C)
- 📐 **温度墙** — 70-100°C 滑块，松手 0.5s 应用
- 💡 **EC 灯同步** — 背面物理性能指示灯自动变色 (蓝/橙/红)
- 🔒 **pkexec 免终端** — 已配置 polkit 规则后零密码操作
- 🪟 **2s 刷新** — GTK4 每 2 秒拉取 sensors + sysfs 数据

## 截图

![screenshot](screenshot.png)

## 依赖

- `python` `python-gobject` `gtk4` — GUI
- `ryzenadj` (AUR) — SMU TDP/温度控制
- `lm_sensors` — 温度读取
- `polkit` — 提权
- `ec_sys` 内核模块 — EC 指示灯 (需 `write_support=1`)

## 安装

### Arch Linux (推荐)

```bash
paru -S jiaolong-panel
```

或本地打包：

```bash
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
makepkg -si
```

### Debian/Ubuntu

```bash
sudo apt install debhelper python3-gi gir1.2-gtk-4.0 ryzenadj lm-sensors
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
dpkg-buildpackage -us -uc -b
sudo dpkg -i ../jiaolong-panel_1.0.0-1_all.deb
```

### Fedora

```bash
git clone https://github.com/giantgkl/jiaolong-panel.git
cd jiaolong-panel
sudo dnf install python3-gobject gtk4 ryzenadj lm_sensors
rpmbuild -ba jiaolong-panel.spec
sudo dnf install ~/rpmbuild/RPMS/noarch/jiaolong-panel-*.rpm
```

### 通用手动安装

```bash
sudo cp jiaolong-panel /usr/bin/
sudo cp jiaolong-panel.desktop /usr/share/applications/
```

## 配置

### 免密码认证

```bash
sudo tee /etc/polkit-1/rules.d/50-jiaolong-panel.rules << 'EOF'
polkit.addRule(function(action, subject) {
    if (action.id == "org.freedesktop.policykit.exec" &&
        subject.user == "YOUR_USERNAME" &&
        (action.lookup("program") == "/usr/bin/ryzenadj" ||
         action.lookup("program") == "/usr/bin/bash")) {
        return polkit.Result.YES;
    }
});
EOF
sudo systemctl restart polkit
```

### EC 指示灯

仅限同方模具（机械革命、Tuxedo 等），需加载 `ec_sys`：

```bash
echo 'ec_sys write_support=1' | sudo tee /etc/modules-load.d/ec_sys.conf
sudo modprobe ec_sys write_support=1
```

非蛟龙/非同方机型：EC 灯控会静默失败，其他功能正常。

## 开发说明

本项目针对 **7945HX + 同方模具** 做了 EC 寄存器适配。若你的机型不同，EC 指示灯可能不工作——需要通过 `sudo xxd /sys/kernel/debug/ec/ec0/io` 找出对应寄存器地址后修改代码中 0xE4 偏移量。

## 许可证

MIT
