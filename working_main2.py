import vtk
# Loading the 3D foot dataset
reader = vtk.vtkXMLImageDataReader()
# reader.SetFileName('mri_ventricles.vti')
reader.SetFileName('foot.vti')
reader.Update()
# print(reader)

# Create a volume mapper and volume property
mapper = vtk.vtkSmartVolumeMapper()
property = vtk.vtkVolumeProperty()
property.ShadeOff()
mapper.SetInputConnection(reader.GetOutputPort())
property.SetInterpolationTypeToLinear()

# Define a color and opacity transfer function and adding differnet color/opacity points to plot
colorTF = vtk.vtkColorTransferFunction()
opacityTF = vtk.vtkPiecewiseFunction()
colorTF.AddRGBPoint(0, 0, 0, 1)
opacityTF.AddPoint(0, 0)
colorTF.AddRGBPoint(20, 0, 1, 1)
opacityTF.AddPoint(20, 0.02)
colorTF.AddRGBPoint(40, 1, 0, 0)
opacityTF.AddPoint(40, 0.02)
colorTF.AddRGBPoint(60, 1, 1, 1)
opacityTF.AddPoint(60, 0.1)
colorTF.AddRGBPoint(80, 0, 1, 1)
opacityTF.AddPoint(80, 0.2)
colorTF.AddRGBPoint(100, 1, 1, 1)
opacityTF.AddPoint(100, 1)
property.SetColor(colorTF)
property.SetScalarOpacity(opacityTF)

# Creating a volume and renderer and adding volume to the renderer
volume = vtk.vtkVolume()
volume.SetMapper(mapper)
volume.SetProperty(property)
renderer = vtk.vtkRenderer()
renderer.AddVolume(volume)
# print(volume)


# Creating an actor to add heading of plot
heading = vtk.vtkOpenGLTextActor()
heading.SetTextScaleModeToNone()
heading.GetPositionCoordinate().SetCoordinateSystemToNormalizedDisplay()
heading.SetPosition(0.5, 0.95)  
heading.GetTextProperty().SetFontSize(45)  
heading.GetTextProperty().SetBold(1)
heading.GetTextProperty().SetShadow(1)  
heading.GetTextProperty().SetColor(1.0, 1.0, 1.0)  
heading.GetTextProperty().SetJustificationToCentered()
heading.GetTextProperty().SetVerticalJustificationToTop()
heading.SetInput("3D Volume Visualization of Foot") 
renderer.AddActor(heading)
print(renderer)
# Creating a render window and adding interaction to it
renderWindow = vtk.vtkRenderWindow()
renderWindow.SetWindowName("3D Volume Visualization of Foot")
renderWindow.SetSize(1200, 900)
renderWindow.AddRenderer(renderer)
renderWindowInterface = vtk.vtkRenderWindowInteractor()
renderWindowInterface.SetRenderWindow(renderWindow)
interactor_style = vtk.vtkInteractorStyleTrackballCamera()
interactor_style.SetMouseWheelMotionFactor(1.0) 
renderWindowInterface.SetInteractorStyle(interactor_style)


# Adding a slider widget in plot to control iso-surfaces
slider = vtk.vtkSliderRepresentation2D()
slider.SetMinimumValue(0)
slider.SetMaximumValue(100)
slider.SetValue(45) 
slider.GetPoint1Coordinate().SetCoordinateSystemToNormalizedDisplay()
slider.GetPoint1Coordinate().SetValue(0.1, 0.1)
slider.GetPoint2Coordinate().SetCoordinateSystemToNormalizedDisplay()
slider.GetPoint2Coordinate().SetValue(0.9, 0.1)
slider.SetTitleText("Slider to control Iso-surfaces")
slider.SetTitleHeight(0.02)
slider_widget = vtk.vtkSliderWidget()
slider_widget.SetInteractor(renderWindowInterface)
slider_widget.SetRepresentation(slider)
slider_widget.SetAnimationModeToAnimate()
slider_widget.EnabledOn()

# Function to update opacity transfer function based on slider value
def opacity_control_via_slider(widget, event):
    value = widget.GetRepresentation().GetValue()
    opacityTF.RemoveAllPoints()
    opacityTF.AddPoint(0, 0)
    opacityTF.AddPoint(value, 0.02)
    opacityTF.AddPoint(100, 1)
    property.SetScalarOpacity(opacityTF)
    renderWindow.Render()
    
# Connecting the slider widget to the opacity transfer function
slider_widget.AddObserver("InteractionEvent", opacity_control_via_slider)

# Initializing and starting the render window interface
renderWindowInterface.Initialize()
renderWindow.Render()
renderWindowInterface.Start()
