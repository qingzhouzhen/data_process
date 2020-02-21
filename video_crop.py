import cv2
import os

#
if __name__ == "__main__":
    root_path = "/data/huanghanqing_fly/"
    for root,dir,files in os.walk(root_path):
        for file in files:
            if not file.endswith(".MP4"):
                continue
            video_path = os.path.join(root, file)
            vid = cv2.VideoCapture(video_path)
            fps = int(vid.get(5))
            while(True):
                ret, frame = vid.read()
                if not ret:
                    break
                frame_index = int(vid.get(1))
                if frame_index % (10*fps) == 0:
                    img_path = os.path.join(video_path.replace(".MP4", "_" + str(int(frame_index/fps))+".jpg"))
                    cv2.imwrite(img_path, frame)
                    print("write: ", img_path)
                    
