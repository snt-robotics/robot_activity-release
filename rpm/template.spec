Name:           ros-lunar-robot-activity-tutorials
Version:        0.1.1
Release:        0%{?dist}
Summary:        ROS robot_activity_tutorials package

Group:          Development/Libraries
License:        BSD
URL:            http://www.ros.org/wiki/robot_activity_tutorials
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-lunar-robot-activity
Requires:       ros-lunar-roscpp
Requires:       ros-lunar-std-srvs
BuildRequires:  ros-lunar-catkin
BuildRequires:  ros-lunar-robot-activity
BuildRequires:  ros-lunar-roscpp
BuildRequires:  ros-lunar-roslint
BuildRequires:  ros-lunar-std-srvs

%description
The robot_activity_tutorials package

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_LIBDIR="lib" \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/lunar" \
        -DCMAKE_PREFIX_PATH="/opt/ros/lunar" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/lunar/setup.sh" ]; then . "/opt/ros/lunar/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/lunar

%changelog
* Wed Apr 18 2018 Maciej ZURAD <maciej.zurad@gmail.com> - 0.1.1-0
- Autogenerated by Bloom

