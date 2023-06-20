# Add-ons_for_Spatial
Add-ons to help the integration of Blender to the metaverse of Spatial

Documentation:
1- Hotspot Add-on:
The purpose of this Add-on is to facilitate the creation of Hotspot, the seatable objects in Spatial.

To use this Add-on you need to go to Edit>Preferences>Add-on and then install the Add-on into Blender. After the installation you should press the “N” key to show the sidebar with the panels. After you click on the Hotspot button in the sidebar it will open a panel in the 3D Viewport. The panel shows the button to create the Hotspot, and the options to set the location of the Hotspot. If you click on the button without changing the location, it will appear in the original location that matches the cube top when you create it on Blender. If you change the location of the Hotspot, it will move to the location you setted.

Is important to note that a seatable spot will be where the sphere origin is located.

One of the Add-on limitations is that you can’t make two or more Hotspot in the same scene. That happens because you can’t have two objects with the same name, and the name and hierarchy of the objects are needed so that the element Hotspot is created.

Once you’ve placed the Hotspot where you want, you can export the object, for example, using the Export Add-on also in this project. Is necessary to say that the Hotspot object only works with the .glb/gltf extension. .fbx and .obj doesn’t show the green mark on the object that allows the avatar to sit.

 2- Export Add-on:
This Add-on was created so that the user could export in a more easy and convenient way with the extensions that can be imported into Spatial metaverse. Is important to note that Spatial only supports files with the maximum size of 100mb. To help the user to realize that, in the Add-ons panel, is the 100mb reference so that the user will remember to be aware of this information.

The usage is pretty simple, when you install this Add-on, by going into Edit>Preferences>Add-on, and after the installation, you will have to press the “N” key to show the sidebar that shows the panels. Once you have done it, the Export Add-on on this sidebar will be shown. By clicking on the button, a panel will appear in the 3D Viewport, with three options of buttons, which are the three extensions that Spatial supports to import into its metaverse: .fbx, .glb/.gltf and .obj. When pressing the button a window will be open and the user has the possibility to name the object and then save it wherever he likes in his machine.

The next step is inside Spatial. When you create a new Spatial metaverse, you can upload an Environment, that can be a .fbx or .glb extension file, and then, you can import objects into the scene, by clicking on the plus button in the bottom of the Spatial window, or by dragging and dropping the file in the Spatial scene window.

Once you export in Blender and import in Spatial, the usage of the Add-on has been completed, just remember to don’t surpass the 100mb limit of size of the files.

3- Animation Add-on:

This Add-on was created so that the user could import objects into Spatial with rotation animation. One detail is that the object stops the rotation and then does the rotation again. This is because the Blender animation is based on the timeline, when the timeline ends, the object stops the rotation.

To use this Add-on you need to install the Add-on into Blender Edit>Preferences>Add-ons and after the installation, you need to press the “N” key to show the sidebar, with this you can click on the Animation button on the sidebar, and will open the Panel. In this panel, by clicking on which of the checkboxes that represents the x, y and z axis, and selecting the x, for example, the object will rotate in this axis direction. You can only choose one direction of rotation. That’s another limitation of this Add-on.

Another functionality of this Add-on is to choose the speed of the animation. The speed is a number that indicates the Keyframe of the animation. If you choose a low number, the animation will rotate faster. If you choose a big number, the animation will move slower.

After doing this configuration, choosing one axis and setting the speed of the rotation, you can export the object, for example, using the Export Add-on also created in this project. After exporting the object, it is important to note that the .obj extension doesn't support the animation. So the only extensions that work with animation are .fbx and .glb/gltf.

After exporting to the supported extension files, you can import it in Spatial. With this, the usage of this Add-on is completed.

