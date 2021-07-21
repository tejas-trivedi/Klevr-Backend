import cv2
import datetime

# create video capture object
data = cv2.VideoCapture('https://firebasestorage.googleapis.com/v0/b/tech-75e07.appspot.com/o/KLEVR%2Ffile_example_AVI_1280_1_5MG.avi?alt=media&token=be86cc00-9154-4d85-9752-15edae0981e0')

# count the number of frames
frames = data.get(cv2.CAP_PROP_FRAME_COUNT)
fps = int(data.get(cv2.CAP_PROP_FPS))

# calculate dusration of the video
seconds = int(frames / fps)
video_time = str(datetime.timedelta(seconds=seconds))
print("duration in seconds:", seconds)
print("video time:", video_time)