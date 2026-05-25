# Maintainer: giantgkl
pkgname=jiaolong-panel
pkgver=1.0.0
pkgrel=1
pkgdesc="CPU power/temperature control panel for Mechrevo Jiaolong 16 Pro (2023)"
arch=('any')
url="https://github.com/giantgkl/jiaolong-panel"
license=('MIT')
depends=('python' 'python-gobject' 'gtk4' 'ryzenadj' 'lm_sensors' 'polkit')
makedepends=('git')
source=("git+$url.git")
sha256sums=('SKIP')

package() {
    cd "$srcdir/jiaolong-panel"
    install -Dm755 jiaolong-panel "$pkgdir/usr/bin/jiaolong-panel"
    install -Dm644 jiaolong-panel.desktop "$pkgdir/usr/share/applications/jiaolong-panel.desktop"
}
