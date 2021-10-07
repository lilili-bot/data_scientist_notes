import cv2 as cv
import numpy as np
# https://www.jianshu.com/p/6bde79df3f9d
img = cv.imread("img/01.jpg")
img_h, img_w, _ = img.shape
blurimg = cv.GaussianBlur(img, (5, 5), 0)
'''
函数很简单，参数有三个
第一个参数：hsv指的是原图
第二个参数：lower_red指的是图像中低于这个lower_red的值，图像值变为0
第三个参数：upper_red指的是图像中高于这个upper_red的值，图像值变为0
而在lower_red～upper_red之间的值变成255
'''
hsv = cv.cvtColor(blurimg, cv.COLOR_RGB2HSV)
lower = (10, 0, 0)
upper = (120, 255, 255)
# 去除背景
mask = cv.inRange(hsv, lower, upper)
'''
膨胀与腐蚀能实现多种多样的功能，主要如下：
1）消除噪声
2）分割(isolate)出独立的图像元素，在图像中连接(join)相邻的元素。
3）寻找图像中的明显的极大值区域或极小值区域
4）求出图像的梯度

首先需要注意，腐蚀和膨胀是对白色部分（高亮部分）而言的，不是黑色部分。膨胀就是图像中的高亮部分进行膨胀，“领域扩张”，效果图拥有比原图更大的高亮区域。腐蚀就是原图中的高亮部分被腐蚀，“领域被蚕食”，效果图拥有比原图更小的高亮区域。
膨胀就是求局部最大值的操作。
'''
mask = cv.erode(mask, None, iterations=2)
'''
该函数的参数含义：
img – 目标图片
kernel – 进行操作的内核，默认为3×3的矩阵
iterations – 腐蚀次数，默认为1
'''
mask = cv.dilate(mask, None, iterations=2)
"""
# findContours 是寻找白色像素的轮廓，即白色是前景，黑色是背景
# processed_img 获取轮廓过程中被修改过的原图像
# contours 获得的所有轮廓的数组，每个轮廓是该轮廓上所有像素点组成的数组
# hierarchy 各个轮廓之间的继承关系
# retrieval_mode: 常用：
#     cv2.RETR_TREE 保留轮廓的层级结构
#     cv2.RETR_EXTERNAL 只提取最外层的轮廓
# contour_approximation_method: 
#     cv2.CHAIN_APPROX_NONE 表示保存所有的边缘像素坐标
#     cv2.CHAIN_APPROX_SIMPLE 直线的轮廓只保留直线的两个端点像素坐标
"""
'''
cv2.drawContours(img, contours, contour_index, color, thickness)
# 在img上用color颜色thickness厚度画出第contour_index个contour
# contour_index为-1表示画出所有contour
'''
contours, _hierarchy = cv.findContours(
    mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
# 寻找contour下最大的面积。
max_i = 0
for i, cnt in enumerate(contours):
    if cv.contourArea(cnt) > cv.contourArea(contours[max_i]):
        max_i = i
'''
这会把轮廓形状近似成别的边数少的形状，边数由我们指定的精确度决定。这是Douglas-Peucker算法的实现。
要理解这个，假设你试图找一个图像里的方块，但是由于图像里的一些问题，你得不到一个完美的方块，只能得到一个“坏方块”。现在你可以使用这个函数来近似，第二个参数叫epsilon，是从轮廓到近似轮廓的最大距离。是一个准确率参数，好的epsilon的选择可以得到正确的输出。
可以用cv2.arcLength()函数得到。第二个参数指定形状是否是闭合的轮廓（如果传True）。或者只是一个曲线。
perimeter=cv2.arcLength(cnt,True)
在下面第二个图像里，绿线显示了epsilon = 10% of arc length 的近似曲线。第三个图像显示了epsilon = 1% of the arc length。第三个参数指定曲线是否闭合。
'''
peri = cv.arcLength(contours[max_i], True)
'''
epsilon = 0.1*cv2.arcLength(cnt,True)
approx = cv2.approxPolyDP(cnt,epsilon,True)
'''
approx = cv.approxPolyDP(contours[max_i], 0.02 * peri, True)

'''
图像的透射
透视变换(Perspective Transformation)是将成像投影到一个新的视平面(Viewing Plane)，也称作投影映射(Projective Mapping)。如图1，通过透视变换ABC变换到A'B'C'。
'''
pts_o = np.float32([approx[0][0], approx[1][0],  approx[2][0], approx[3][0]])
pts_d = np.float32([[img_w, 0], [0, 0], [0, img_h], [img_w, img_h]])
M = cv.getPerspectiveTransform(pts_o, pts_d)
'''
	 cv::warpPerspective(
		cv::InputArray src, // 输入图像
		cv::OutputArray dst, // 输出图像
		cv::InputArray M, // 3x3 变换矩阵
		cv::Size dsize, // 目标图像大小
		int flags = cv::INTER_LINEAR, // 插值方法
		int borderMode = cv::BORDER_CONSTANT, // 外推方法
		const cv::Scalar& borderValue = cv::Scalar() //常量边界时使用
'''

dst = cv.warpPerspective(img, M, (img_w, img_h))


# cv.imwrite("1_mask.jpg", dst)


print(approx[0][0])


cv.imshow("mask", mask)
#cv.imshow("original img", img)
cv.imshow("blurimg", blurimg)
cv.imshow("dst", dst)
cv.waitKey(0)
