# pyOBJParser

## OBJ Data Parsing Capabilities

The pyOBJExplorer's OBJ parser is processing a wide range of data encapsulated within Wavefront OBJ files. It reads vertices, texture coordinates, normals and geometrical elements like points, lines, faces. Notably, it is capable of interpreting all types of faces, including triangles, quads, and more complex polygons (with both positive and negative indices).

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

## MTL Data Parsing Capabilities

The pyOBJExplorer's MTL parser is designed to handle the most common material data found in Wavefront MTL files, providing essential functionality for 3D model materials. For those who require additional data types, the parser's code is straightforward and user-friendly, making it easy to understand and extend as needed.

Following material data is supported:

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
