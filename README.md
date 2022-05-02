# mediapipe_pose_to_json

구글에서 제공하는 AI 프레임워크인 mediapipe를 사용하여

영상에서 사람의 관절을 측정(pose estimation)하고 키값들을 얻고자함.

## json sample

-   results.pose_world_landmarks의 데이터를 추출하여 json 파일에 저장.
    -   `x, y, z`: Real-world 3D coordinates in meters with the origin at the center between hips.
    -   `score`: A value in [0.0, 1.0] indicating the likelihood of the landmark being visible (present and not occluded) in the image.

```json
{
  "fileName": "sample/mixamo_dance.gif",
  "frames": [
    {
      "frameNum": 0,
      "keypoints3D": [
        {
          "x": 0.15194424986839294,
          "y": -0.5785813331604004,
          "z": -0.10521744191646576,
          "score": 0.9901335835456848,
          "name": "nose"
        },
    ...
```

## TODO

-   키값 전처리

## references

-   https://google.github.io/mediapipe/
-   https://bleedai.com/introduction-to-pose-detection-and-basic-pose-classification/
