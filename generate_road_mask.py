import json
import cv2
import os
import numpy as np

# 根据coco标签值生成黑白图片
if __name__ == "__main__":
    path = "/data/data/road_label/"
    read_path = "/data/data/road/"
    write_path_root = "/data/data/road_mask/"
    for file in os.listdir(path):
        abs_path = os.path.join(path, file)
        with open(abs_path, "r") as r:
            points = None
            load_dict = json.load(r)
            img_path = load_dict["imagePath"]
            write_path = os.path.join(write_path_root, img_path)
            objs = load_dict["shapes"]
            # TODO suport multi reigon
            assert len(objs) == 1
            for obj in objs:
                points = obj["points"]
                for point in points:
                    point[0] = int(point[0])
                    point[1] = int(point[1])
            cnt = np.expand_dims(np.array(points), axis=1)
            cont3 = np.array([[[0, 0]], [[10, 0]], [[10, 10]], [[10, 10]], [[0, 10]]])
            img = cv2.imread(os.path.join(read_path, img_path))
            shape = img.shape
            for i in range(shape[0]):
                for j in range(shape[1]):
                    ret = cv2.pointPolygonTest(cnt, (j, i), False)
                    if ret < 0:
                        img[i,j,:] = 255
                    else:
                        img[i,j,:] = 0
            cv2.imwrite(write_path, img)
            print("write image: ", write_path)
            # for obj in load_dict["shapes"]:
