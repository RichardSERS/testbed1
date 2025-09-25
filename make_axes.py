import trimesh
import numpy as np

def make_arrow(direction, color, length=1.0, radius=0.02):
    # cylinder for shaft
    shaft = trimesh.creation.cylinder(radius=radius, height=length*0.8, sections=16)
    shaft.apply_translation([0, 0, length*0.4])

    # cone for head
    head = trimesh.creation.cone(radius=radius*2, height=length*0.2, sections=16)
    head.apply_translation([0, 0, length*0.9])

    arrow = trimesh.util.concatenate([shaft, head])

    # orient to direction
    direction = np.array(direction, dtype=float)
    direction /= np.linalg.norm(direction)
    z_axis = np.array([0,0,1])
    rot, _ = trimesh.geometry.align_vectors(z_axis, direction, return_angle=True)
    arrow.apply_transform(rot)

    # color (RGBA)
    arrow.visual.face_colors = np.tile(np.array(color+[255]), (arrow.faces.shape[0], 1))
    return arrow

# Red X, Green Y, Blue Z
x_arrow = make_arrow([1,0,0], [255,0,0])
y_arrow = make_arrow([0,1,0], [0,255,0])
z_arrow = make_arrow([0,0,1], [0,0,255])

scene = trimesh.Scene([x_arrow, y_arrow, z_arrow])
scene.export("axes.glb")
print("✅ axes.glb created")
