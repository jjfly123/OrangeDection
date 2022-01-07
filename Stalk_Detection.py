# 果柄检测
# 检测果柄位置是否朝上正放，设定果柄框中心位于橘子框顶部往下1/6处，左框往右1/2处
from PIL import Image
import cv2
import os
import time

class StalkDetect:

    def __init__(self, tup1, tup2, image):
        self.top1 = tup1[0]
        self.left1 = tup1[1]
        self.bottom1 = tup1[2]
        self.right1 = tup1[3]

        self.top2 = tup2[0]
        self.left2 = tup2[1]
        self.bottom2 = tup2[2]
        self.right2 = tup2[3]

        self.image = image

    def __call__(self, *args, **kwargs):
        return self.detect()

    def detect(self):
        ox = self.top1  # 橘子顶框中心横坐标
        oy = (self.left1 + self.right1)/2  # 橘子顶框中心纵坐标
        sx = (self.top2 + self.bottom2)/2  # 橘柄中心横坐标
        sy = (self.left2 + self.right2)/2  # 橘柄中心纵坐标
        oh = self.bottom1 - ox    # 橘子顶框到底框距离(框高)
        ow = self.right1 - self.left1    # 橘子左框到右框距离(框宽)
        xp = (sx - ox)/oh
        yp = (sy - self.left1)/ow
        # if (1/6 - 0.05) < xp < (1/6 + 0.05) & (1/2 - 0.01) < yp < (1/2 + 0.01):

        if (1 / 7 - 0.05) < xp < (1 / 7 + 0.05) and (1 / 2 - 0.05) < yp < (1 / 2 + 0.05):
            print("位姿调整结束  位姿调整结束  位姿调整结束  位姿调整结束  位姿调整结束  位姿调整结束")
            self.image.save(os.path.join("img_success/", "{}.jpg".format(time.time())))




