# Script generated with Bloom
pkgdesc="ROS - The pr2_tuck_arms_action package"
url='http://wiki.ros.org/pr2_tuck_arms_action'

pkgname='ros-kinetic-pr2-tuck-arms-action'
pkgver='0.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-catkin'
'ros-kinetic-pr2-common-action-msgs'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-rospy'
'ros-kinetic-trajectory-msgs'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-actionlib-msgs'
'ros-kinetic-pr2-common-action-msgs'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-rospy'
'ros-kinetic-trajectory-msgs'
)

conflicts=()
replaces=()

_dir=pr2_tuck_arms_action
source=()
md5sums=()

prepare() {
    cp -R $startdir/pr2_tuck_arms_action $srcdir/pr2_tuck_arms_action
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

