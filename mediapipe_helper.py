import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D
import json
import matplotlib.animation as animation
from IPython.display import clear_output
import ntpath
# https://github.com/google/mediapipe/blob/master/mediapipe/python/solutions/drawing_utils.py
mediapipe_names = [
    "nose", "left_eye_inner", "left_eye", "left_eye_outer", "right_eye_inner", "right_eye", "right_eye_outer", "left_ear", "right_ear", "mouth_left", "mouth_right", "left_shoulder", "right_shoulder", "left_elbow", "right_elbow", "left_wrist", "right_wrist", "left_pinky", "right_pinky", "left_index", "right_index", "left_thumb", "right_thumb", "left_hip", "right_hip", "left_knee", "right_knee", "left_ankle", "right_ankle", "left_heel", "right_heel", "left_foot_index", "right_foot_index"]


def set_axes(ax, azim=10, elev=10):
    ax.set_xlim(-1.0, 1.0)
    ax.set_xlabel("-Z")
    ax.set_ylim(-1.0, 1.0)
    ax.set_ylabel("X")
    ax.set_zlim(-1.0, 1.0)
    ax.set_zlabel("-Y")
    ax.set_title('Mediapipe')
    ax.view_init(elev=elev, azim=azim)


def get_mediapipe_json_keypoints_with_color_and_mark(json_object, fidx):
    dot1 = []
    size = len(json_object['frames'][fidx]['keypoints3D'])
    for idx in range(0, size):
        landmark = json_object['frames'][fidx]['keypoints3D'][idx]
        dot1.append(
            [-float(landmark['z']), float(landmark['x']), -float(landmark['y'])])
        if idx < 10:
            dot1[idx].append('r')
        elif idx == 24 or idx == 23 or idx == 11 or idx == 12:
            dot1[idx].append('b')
        else:
            dot1[idx].append('g')
        dot1[idx].append('o')
    return dot1


def draw_mediapipe(json_object, fidx, azim=10):
    dot1 = get_mediapipe_json_keypoints_with_color_and_mark(json_object, fidx)
    plt.figure()
    ax1 = plt.axes(projection='3d')
    set_axes(ax1)
    for x in dot1:
        ax1.scatter3D(x[0], x[1], x[2], c=x[3],
                      marker=x[4], linewidths=1)
    plt.show()


def draw_all_frame_mediapipe_in_ipython(json_object, azim=10):
    for fidx in range(0, len(json_object['frames'])):
        clear_output(wait=True)
        draw_mediapipe(json_object, fidx, azim)


def json_one_frame_to_360_gif(json_object, frame_idx, save_path):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    frame = get_mediapipe_json_keypoints_with_color_and_mark(
        json_object, frame_idx)
    size = len(json_object['frames'][frame_idx]['keypoints3D'])

    def update_round(i):
        set_axes(ax, i)
    ax.clear()
    for i in range(0, size):
        ax.scatter(frame[i][0], frame[i][1], frame[i][2],
                   c=frame[i][3], marker=frame[i][4])
    ani = animation.FuncAnimation(
        fig, update_round, frames=360, interval=json_object["ticksPerSecond"])
    if save_path[-1] == '/':
        save_path = save_path[0: -1]
    ani.save(save_path + '/' +
             ntpath.basename(json_object['fileName']) + '_json_round.gif', writer='pillow')


def json_to_gif(json_object, save_path, max_frame_num=100,  is_axes_move=False):
    fig = plt.figure()
    ax = plt.axes(projection='3d')
    frames = min(len(json_object["frames"]), max_frame_num)

    size = len(json_object['frames'][0]['keypoints3D'])

    def update(idx):
        ax.clear()
        dot1 = get_mediapipe_json_keypoints_with_color_and_mark(
            json_object, idx)
        for i in range(0, size):
            ax.scatter(dot1[i][0], dot1[i][1], dot1[i][2],
                       c=dot1[i][3], marker=dot1[i][4])
        if is_axes_move:
            set_axes(ax, idx)
        else:
            set_axes(ax, 0)

    ani = animation.FuncAnimation(
        fig, update, frames=frames, interval=json_object["ticksPerSecond"])
    if save_path[-1] == '/':
        save_path = save_path[0: -1]
    if is_axes_move:
        ani.save(save_path + '/' + ntpath.basename(
            json_object['fileName']) + '_json_mp_round_.gif', writer='pillow')
    else:
        ani.save(save_path + '/' +
                 ntpath.basename(json_object['fileName']) + '_json_mp_.gif', writer='pillow')


def get_name_idx_map():
    name_idx_map = {}
    for idx in range(0, len(mediapipe_names)):
        name_idx_map[mediapipe_names[idx]] = idx
    return name_idx_map
