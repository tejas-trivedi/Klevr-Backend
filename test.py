import datetime

def with_opencv(filename):
    import cv2
    video = cv2.VideoCapture(filename)

    duration = video.get(cv2.CAP_PROP_POS_MSEC)
    #data = cv2.VideoCapture(filename)
    frame_count = video.get(cv2.CAP_PROP_FRAME_COUNT)
    #fps = int(data.get(cv2.CAP_PROP_FPS))

    #seconds = int(frame_count / fps)
    #video_time = str(datetime.timedelta(seconds=seconds))
    duration = str(datetime.timedelta(seconds=duration))

    return duration

print(with_opencv('https://firebasestorage.googleapis.com/v0/b/tech-75e07.appspot.com/o/KLEVR%2Ffile_example_AVI_1280_1_5MG.avi?alt=media&token=be86cc00-9154-4d85-9752-15edae0981e0'))