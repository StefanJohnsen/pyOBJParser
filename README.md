# pyOBJParser

Empower your project with self-contained OBJ and MTL parser.

### Dependencies
- os
- numpy

### Parsed examples
*pyOBJParser have been integrated into the [pyOBJExplorer](https://github.com/StefanJohnsen/pyOBJExplorer), showcasing the parsing capabilities.*

![OBJExplorer](https://github.com/StefanJohnsen/pyOBJExplorer/blob/main/objFiles/explorer.png)

## Usage

Copy `WavefrontOBJ.py` and `WavefrontMTL.py` to your python project directory and import parsers 

```
from WavefrontOBJ import *
from WavefrontMTL import *
```

## Example
We've developed a console application for a practical demonstration of its usage. This sample application is found in the [pyOBJExplorer](https://github.com/StefanJohnsen/pyOBJExplorer) repository. It serves as a guide on integrating and utilising `WavefrontOBJ.py` and `WavefrontMTL.py`.

## WavefrontOBJ Parsing Capabilities

The WavefrontOBJ parser is processing a wide range of data encapsulated within Wavefront OBJ files. It reads vertices, texture coordinates, normals and geometrical elements like points, lines, faces. Notably, it is capable of interpreting all types of faces, including triangles, quads, and more complex polygons (with both positive and negative indices).

After parsing the obj file, users gain access to geometry by utilizing the following lists.
	
| Component | Description                                    |
|-----------|------------------------------------------------|
| vertex    | Defines points in 3D space, shaping the model. |
| texture   | Manages texture details for enhanced visuals.  |
| normal    | Specifies surface orientation for lighting.    |
| face      | Contains indices for creating flat surfaces.   |
| line      | Stores indices, useful for wireframe models.   |
| point     | Manages indices for individual 3D points.      |

Here are some sample formats of faces that OBJ parser can interpret:

```
# Triangle
f 1 2 3 
f 1//1 2//2 3//3 # triangle with vertex and normal
f 1/1/1 2/2/2 3/3/3 # triangle with vertex, texture and normal

# Quad
f 1 2 3 4
f 1//1 2//2 3//3 4//4 # quad with vertex and normal
f 1/1/1 2/2/2 3/3/3 4/4/4 # quad with vertex, texture and normal

# Polygon
f 1 2 3 4 5 6 ....
f 1//1 2//2 3//3 4//4 5//5 6//6 ... # polygon with vertex and normal
f 1/1/1 2/2/2 3/3/3 4/4/4 5/5/5 6/6/6 ... # polygon with vertex, texture and normal

# Also negative indices is supported
```

## WavefrontMTL Parsing Capabilities

The WavefrontMTL parser is designed to handle the most common material data found in Wavefront MTL files, providing essential functionality for 3D model materials. For those who require additional data types, the parser's code is straightforward and user-friendly, making it easy to understand and extend as needed.

After parsing the material file, you will be presented with a comprehensive list of all the materials discovered in the file. Each material is encapsulated within a structure and contains the following member variables.

| Member        | Type          | Description                  | Extension                              |
|---------------|---------------|------------------------------|----------------------------------------|
| name          | string        | Material name                |                                        |
| Kd            | Color         | Color                        |                                        |
| Ka            | Color         | Color Ambient                |                                        |
| Ks            | Color         | Color Specular               |                                        |
| Ke            | Color         | Color Emissive               | Physically Rendering/Clara.io          |
| Ns            | double        | Shininess factor [0..1000]   |                                        |
| Ns            | double        | Shininess factor [0..1000]   |                                        |
| Ni            | double        | Optical density              |                                        |
| d             | Opacity       | Dissolve factor              |                                        |
| illum         | int           | Illumination [0..10]         |                                        |
| map_Kd        | Texture       | Texture Diffuse              |                                        |
| map_Ka        | Texture       | Texture Ambient              |                                        |
| map_Ks        | Texture       | Texture Specular             |                                        |
| map_Ns        | Texture       | Texture Glossiness           |                                        |
| map_d         | Texture       | Opacity Texture (alpha)      |                                        |

Example of typical material data:

```
newmtl Material
Kd 0.5 0.5 0.5
Ka 0.0 0.0 0.0
Ks 0.5 0.5 0.5
Ke 0.0 0.0 0.0
Ns 168.89702
Ni 1.0
d 1.0
illum 2
map_Kd pic1.jpg
map_Ka pic2.jpg
map_Ks pic3.jpg
map_Ns pic4.jpg
map_d pic5.jpg
```

## Example.py
Clone this repository and study the provided example `Example.y`

```
python Example.py rubikcube.obj
```
```
Content of c:\temp\rubikcube.mtl:
material: mat_1, color: rgb(0.6, 0.6, 0.6)
material: mat_2, color: rgb(0.1, 0.1, 0.1)
material: mat_3, color: rgb(1.0, 0.0, 0.0)
material: mat_4, color: rgb(1.0, 1.0, 1.0)
material: mat_5, color: rgb(0.9, 0.5, 0.0)
material: mat_6, color: rgb(0.9, 0.7, 0.1)
material: mat_7, color: rgb(0.3, 0.6, 0.3)
material: mat_8, color: rgb(0.2, 0.2, 0.6)
Content of c:\temp\rubikcube.obj:
geometry: mat_1, color: rgb(0.6, 0.6, 0.6), faces : 1872
geometry: mat_2, color: rgb(0.1, 0.1, 0.1), faces : 13292
geometry: mat_3, color: rgb(1.0, 0.0, 0.0), faces : 18
geometry: mat_4, color: rgb(1.0, 1.0, 1.0), faces : 18
geometry: mat_5, color: rgb(0.9, 0.5, 0.0), faces : 18
geometry: mat_6, color: rgb(0.9, 0.7, 0.1), faces : 18
geometry: mat_7, color: rgb(0.3, 0.6, 0.3), faces : 18
geometry: mat_8, color: rgb(0.2, 0.2, 0.6), faces : 18

```

## References
The following sources have been utilized in the development of this Wavefront MTL parser.

[Paul Bourke: MTL material format (Lightwave, OBJ)](http://paulbourke.net/dataformats/mtl/)

[Wikipedia: Wavefront .obj file](https://en.wikipedia.org/wiki/Wavefront_.obj_file)

[FileFormat.info: WaveFront Material (.mtl) File Format](https://www.fileformat.info/format/material/)

## License
This software is released under the MIT License terms.
