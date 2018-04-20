# Script generated with Bloom
pkgdesc="ROS - Various actions which help in moving the arms of the PR2 or getting data from its tilting laser."
url='http://wiki.ros.org/pr2_common_actions'

pkgname='ros-kinetic-pr2-common-actions'
pkgver='0.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-catkin'
)

depends=('ros-kinetic-joint-trajectory-action-tools'
'ros-kinetic-joint-trajectory-generator'
'ros-kinetic-pr2-arm-move-ik'
'ros-kinetic-pr2-common-action-msgs'
'ros-kinetic-pr2-tilt-laser-interface'
'ros-kinetic-pr2-tuck-arms-action'
)

conflicts=()
replaces=()

_dir=pr2_common_actions
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_common_actions $srcdir/pr2_common_actions
}

build() {
  # Use ROS environment variables
  source /usr/share/ros-build-tools/clear-ros-env.sh
  [ -f /opt/ros/kinetic/setup.bash ] && source /opt/ros/kinetic/setup.bash

  # Create build directory
  [ -d ${srcdir}/build ] || mkdir ${srcdir}/build
  cd ${srcdir}/build

  # Fix Python2/Python3 conflicts
  /usr/share/ros-build-tools/fix-python-scripts.sh -v 2 ${srcdir}/${_dir}

  # Build project
  cmake ${srcdir}/${_dir} \
        -DCMAKE_BUILD_TYPE=Release \
        -DCATKIN_BUILD_BINARY_PACKAGE=ON \
        -DCMAKE_INSTALL_PREFIX=/opt/ros/kinetic \
        -DPYTHON_EXECUTABLE=/usr/bin/python2 \
        -DPYTHON_INCLUDE_DIR=/usr/include/python2.7 \
        -DPYTHON_LIBRARY=/usr/lib/libpython2.7.so \
        -DPYTHON_BASENAME=-python2.7 \
        -DSETUPTOOLS_DEB_LAYOUT=OFF
  make
}

package() {
  cd "${srcdir}/build"
  make DESTDIR="${pkgdir}/" install
}

