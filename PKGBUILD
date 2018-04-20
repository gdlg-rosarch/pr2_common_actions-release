# Script generated with Bloom
pkgdesc="ROS - joint_trajectory_generator action takes in a trajectory specified by a number of joint positions, and it generates a new smooth trajectory through these joint positions."
url='http://ros.org/wiki/joint_trajectory_generator'

pkgname='ros-kinetic-joint-trajectory-generator'
pkgver='0.0.10_1'
pkgrel=1
arch=('any')
license=('BSD'
)

makedepends=('ros-kinetic-actionlib'
'ros-kinetic-angles'
'ros-kinetic-catkin'
'ros-kinetic-joint-trajectory-action'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-urdf'
)

depends=('ros-kinetic-actionlib'
'ros-kinetic-angles'
'ros-kinetic-joint-trajectory-action'
'ros-kinetic-orocos-kdl'
'ros-kinetic-pr2-controllers-msgs'
'ros-kinetic-roscpp'
'ros-kinetic-urdf'
)

conflicts=()
replaces=()

_dir=joint_trajectory_generator
source=()
md5sums=()

prepare() {
    cp -R $startdir/joint_trajectory_generator $srcdir/joint_trajectory_generator
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

