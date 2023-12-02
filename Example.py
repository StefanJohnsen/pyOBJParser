# Example.py
# Python script for loading wavfront obj(+mtl) files
#
# Copyright (c) 2023 by FalconCoding
# Author: Stefan Johnsen
# Email: stefan.johnsen@outlook.com
#
# This software is released under the MIT License.

#-------------------------------------------------------------------------------------    

from WavefrontOBJ import *
from WavefrontMTL import *

import os
import sys
import argparse
    
#-------------------------------------------------------------------------------------

loadThisObjFileInDebug = 'c:\\temp\\rubikcube.obj'

#-------------------------------------------------------------------------------------

def rgb(rgb):
    return f"rgb({rgb[0]:.1f}, {rgb[1]:.1f}, {rgb[2]:.1f})"

def load_Wavefront(file):
    
    obj = WavefrontOBJ()
    obj.load(file)
        
    mtl = WavefrontMTL()
    mtl.load(obj.mtllib)
    
    mtllib = mtlFile(file)
    
    if mtllib: 
        if len(mtl.materials) == 0:
            print(f"Content of {mtllib} is empty")
        else:
            print(f"Content of {mtllib}:")
            for material in mtl.materials:
                name = material.name
                color = rgb(material.color())
                print(f"material: {name}, color: {color}")

    geometries = obj.geometries()
    
    if len(geometries) == 0:
        print(f"Content of {file} is empty")
    else:
        print(f"Content of {file}:")
        for name, geometry in geometries.items():
            material = mtl.material(name)
            color = rgb(material.color())
            faces = len(geometry.face)
            print(f"geometry: {name}, color: {color}, faces : {faces}")

#-------------------------------------------------------------------------------------

description = 'Load Wavefront .obj (+mtl) file'

def main():
    
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('filename', help='The name of the file to check')

    if 'pydevd' in sys.modules:
        args = parser.parse_args([loadThisObjFileInDebug])
    else:
        args = parser.parse_args()

    if not os.path.isfile(args.filename):
        print(f"Error: The file {args.filename} does not exist.")
        return

    _, ext = os.path.splitext(args.filename)
    if ext.lower() != '.obj':
        print("Error: The file is not a wavefront .obj file.")
        return

    load_Wavefront(args.filename)

if __name__ == "__main__":
     main()
    
    
    
