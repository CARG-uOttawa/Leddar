import open3d as o3d
import numpy as np
import pandas as pd

data = pd.read_csv("Data\LeddarVu8-Data-30mins-5Hz.csv")

pcd = o3d.geometry.PointCloud()

row = data.iloc[0]

def getSetPoints(data):
    ptsx = [data["X Coord 7"],data["X Coord 6"],data["X Coord 5"],data["X Coord 4"],data["X Coord 3"],data["X Coord 2"],data["X Coord 1"],data["X Coord 0"]]
    ptsy = [data["Y Coord 7"],data["Y Coord 6"],data["Y Coord 5"],data["Y Coord 4"],data["Y Coord 3"],data["Y Coord 2"],data["Y Coord 1"],data["Y Coord 0"]]
    return (ptsx, ptsy, [0 for i in range(8)])

points = np.vstack(getSetPoints(row)).transpose()
pcd.points = o3d.utility.Vector3dVector(points)
o3d.visualization.draw_geometries([pcd])