Name:           ros-indigo-pr2-tilt-laser-interface
Version:        0.0.5
Release:        0%{?dist}
Summary:        ROS pr2_tilt_laser_interface package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/pr2_tilt_laser
Source0:        %{name}-%{version}.tar.gz

Requires:       eigen3-devel
Requires:       ros-indigo-actionlib
Requires:       ros-indigo-actionlib-msgs
Requires:       ros-indigo-laser-geometry
Requires:       ros-indigo-message-runtime
Requires:       ros-indigo-pcl-conversions
Requires:       ros-indigo-pcl-ros
Requires:       ros-indigo-pr2-msgs
Requires:       ros-indigo-roscpp
Requires:       ros-indigo-sensor-msgs
BuildRequires:  eigen3-devel
BuildRequires:  ros-indigo-actionlib
BuildRequires:  ros-indigo-actionlib-msgs
BuildRequires:  ros-indigo-catkin
BuildRequires:  ros-indigo-laser-geometry
BuildRequires:  ros-indigo-message-generation
BuildRequires:  ros-indigo-pcl-conversions
BuildRequires:  ros-indigo-pcl-ros
BuildRequires:  ros-indigo-pr2-msgs
BuildRequires:  ros-indigo-roscpp
BuildRequires:  ros-indigo-sensor-msgs

%description
Provides a set of tools/actions for manipulating the pr2's tilting laser.
Simplifies previously complex tasks, such as fetching a single sweep, given a
set of desired parameters for both the laser driver and tilting platform.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/indigo" \
        -DCMAKE_PREFIX_PATH="/opt/ros/indigo" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/indigo/setup.sh" ]; then . "/opt/ros/indigo/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/indigo

%changelog
* Fri Feb 06 2015 Austin Hendrix <ahendrix@willowgarage.com> - 0.0.5-0
- Autogenerated by Bloom

