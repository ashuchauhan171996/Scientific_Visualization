# Scientific_Visualization
The goal of this assignment is to give you practice in terms of creating some basic scientific data visualizations, and possibly some basic interaction.

# VTK:

Your goal in this assignment is to produce a visualization of a scientific data set using the Visualization ToolKit (VTK).  VTK is a library to support visualization of a variety of data types, but is most known for its use in visualizing scientific data.  Please see https://vtk.org/ for more information.  You may find it especially helpful to visit the Resources part of this page.  VTK can be used with C++, Java, Python, and other languages.  VTK is open-source, and can be downloaded from the website.  VTK is a very complete system, and support many more visualizations than we will make use of.

# Data:

You should use the following datasets:

3D volume dataset (foot): vtk-js-datasets/data/vti/foot.vti at master · Kitware/vtk-js-datasets (github.com)
3D volume dataset (head): vtk-js-datasets/data/vti/mri_ventricles.vti at master · Kitware/vtk-js-datasets (github.com)
3D vector dataset (Rocks): https://urldefense.com/v3/__https://www.digitalrocksportal.org/projects/175__;!!KwNVnqRv!ED16fk1nJcmkUhnly_V_lO9K_VvyauWhIb_wBx2yB-ZrXgZClsZ5vixrrEslKRsExSVjXcOAHziCR4nGfHw7ZhNWTkzD$
3D vector dataset (Pore-Aventura): https://github.com/Nico04/Pore-Aventura/releases/download/v1.0/Data.h5.7z
Note: you will only need to use one volume dataset and/or one vector dataset.

# Visualization:

You should create a 3D visualization of volume data or flow data.

For volume data, you are expected to have a visualization of a 3D volume of data, in which isosurfaces of some features in the data are highlighted.  There should be either the ability to interactively select isosurface values, or to use transfer functions with transparency so that multiple isosurfaces can be seen at the same time. 

For flow data, you are expected to have a visualization that shows flow through a 3D region.  This can be with glyphs or with streamlines.  The visualization should allow the viewer to understand the flow information even on the interior (not just on the outermost layer).

Producing a single basic visualization will earn a maximum 80% grade.  To achieve a higher grade, you will need to do one or more of the following (up to 100% maximum).

10% for each additional type of visualization.
10% for incorporating view interaction: being able to change the camera view of the data interactively.
10% for incorporating data interaction: being able to adjust how the data itself is displayed (not just the camera parameters). Examples would be an interactive transfer function, interactive changes to the glyph density or style, interactively removing or creating a slice through data, etc.
