[Leia esta página em português](https://github.com/marco-teixeira/package_compiler/blob/master/README-pt.md)


Description
=================================

This package is intended to copy a ROS package to a user-defined destination. The package's python codes are compiled into the "pyc" format. The goal is to hide the package code when desired by the developer.

Configuration of the system used
--------------------------------

* Ubuntu 18.04.4 (http://releases.ubuntu.com/18.04.4/)
* ROS Melodic (http://wiki.ros.org/melodic/Installation/Ubuntu)



Parameters:
----------------------------------
1. **pkg_name**
   - Type: String
   - Default value: "package_compiler"
   - Description: Name of the package in your src, to be compiled and moved.

2. **dir_dest**
   - Type: String
   - Default value: ""
   - Description: Destination location to be installed the compiled package. The full path must be informed! If no path is provided, it will be placed in a folder named "compiled" within the package, in src.



Install:
--------------------------------

```
$ cd ~/catkin_ws/src/
$ git https://github.com/marco-teixeira/package_compiler.git
$ cd ~/catkin_ws
$ catkin_make
```

Run:
-------------------------------

```
rosrun package_compiler compile.py _pkg_name:="" _dir_dest:=""
roslaunch package_compiler compile_python_pkg.launch
```





