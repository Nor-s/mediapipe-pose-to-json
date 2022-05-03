import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import json
from IPython.display import clear_output
# https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/drawing_utils.py
mediapipe_names = [
"nose"
,"left_eye_inner"
,"left_eye"
,"left_eye_outer"
,"right_eye_inner"
,"right_eye"
,"right_eye_outer"
,"left_ear"
,"right_ear"
,"mouth_left"
,"mouth_right"
,"left_shoulder"
,"right_shoulder"
,"left_elbow"
,"right_elbow"
,"left_wrist"
,"right_wrist"
,"left_pinky"
,"right_pinky"
,"left_index"
,"right_index"
,"left_thumb"
,"right_thumb"
,"left_hip"
,"right_hip"
,"left_knee"
,"right_knee"
,"left_ankle"
,"right_ankle"
,"left_heel"
,"right_heel"
,"left_foot_index"
,"right_foot_index"]

def get_mediapipe_json_keypoints_with_color_and_mark(json_object, fidx):
  dot1 = []
  size = len(json_object['frames'][fidx]['keypoints3D'])
  for idx in range(0,size):
    landmark = json_object['frames'][fidx]['keypoints3D'][idx]
    dot1.append([-float(landmark['z']), float(landmark['x']), -float(landmark['y'])])
    if idx < 10: 
      dot1[idx].append('r')
    elif idx == 24 or idx == 23 or idx == 11 or idx == 12:
      dot1[idx].append('b')
    else:
      dot1[idx].append('g')
    dot1[idx].append('o')
  return dot1

def draw_mediapipe(json_object, fidx, azim = 10):
  dot1 = get_mediapipe_json_keypoints_with_color_and_mark(json_object, fidx)
  plt.figure()
  ax1 = plt.axes(projection='3d')
  ax1.view_init(elev=10, azim=azim)
  ax1.set_xlim(-1.0, 1.0) 
  ax1.set_xlabel("z") 
  ax1.set_ylim(-1.0, 1.0)  
  ax1.set_ylabel("x") 
  ax1.set_zlim(-1.0, 1.0)  
  ax1.set_zlabel("y") 
  for x in dot1:
    ax1.scatter3D(x[0],x[1],x[2], c=x[3],
                marker= x[4], linewidths=1)  
  plt.show()

def draw_all_frame_mediapipe_in_ipython(json_object, azim = 10):
  for fidx in range(0, len(json_object['frames'])):
    clear_output(wait=True)
    draw_mediapipe(json_object, fidx, azim)