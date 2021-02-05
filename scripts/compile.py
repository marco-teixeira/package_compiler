#!/usr/bin/env python2
import compileall
import rospy
import rospkg
import shutil
import os 
from os import listdir



##Get param
def getParam():
        global package_name, dest
        package_name = rospy.get_param("~pkg_name","package_compiler")
        dest = rospy.get_param("~dir_dest","")
        print package_name


def getPathROS():
        global src, package_name
        rospack = rospkg.RosPack()
        rospack.list() 
        try:
                src = rospack.get_path(package_name)
        except:
                print("There is no package \""+str(package_name)+"\" in your workspace")
                exit()

def compile_dir():
        compileall.compile_dir(dest, force=True)


def copy_files():
        global dest
        if dest == "":
                dest = src+str("/compiled")
        else:
                dest = dest+str("/")+package_name
        try:
                shutil.copytree(src, dest) 
        except: 
                shutil.rmtree(dest)
                copy_files()

def remove_py():
        for parent, dirnames, filenames in os.walk(dest):
                for fn in filenames:
                        if fn.lower().endswith('.py'):
                                os.remove(os.path.join(parent, fn))
        


if __name__ == '__main__':
	rospy.init_node("package_compiler")
        #global
        global package_name, src, dest
	getParam()
        getPathROS()
        copy_files()
        compile_dir()
        remove_py()
