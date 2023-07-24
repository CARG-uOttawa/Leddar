import open3d as o3d
import numpy as np
import pandas as pd
import time

data = pd.read_csv("Data\LeddarVu8-Data-1.0mins-5.0Hz.csv").fillna(0)

pcd = o3d.geometry.PointCloud()

rate = 5

def getSetPoints(data):
    ptsx = [data["X Coord 7"],data["X Coord 6"],data["X Coord 5"],data["X Coord 4"],data["X Coord 3"],data["X Coord 2"],data["X Coord 1"],data["X Coord 0"]] 
    ptsy = [data["Y Coord 7"],data["Y Coord 6"],data["Y Coord 5"],data["Y Coord 4"],data["Y Coord 3"],data["Y Coord 2"],data["Y Coord 1"],data["Y Coord 0"]]
    return (ptsx , ptsy, [0 for i in range(8)])


vis = o3d.visualization.Visualizer()
vis.create_window(height=480, width=640)
ctr = vis.get_view_control()
parameters = o3d.io.read_pinhole_camera_parameters("ScreenCamera.json")


increment = 0
while increment<data.shape[0]:
    previous = time.time()
    while not (time.time()-previous > 1/float((rate))):
        pass
    points = np.vstack(getSetPoints(data.iloc[increment])).transpose()
    origin = np.array([0,0,0])
    pcd.points = o3d.utility.Vector3dVector(np.vstack((points, origin)))
    vis.add_geometry(pcd)
    ctr.convert_from_pinhole_camera_parameters(parameters)
    vis.poll_events()
    vis.update_renderer()
    increment+=1

