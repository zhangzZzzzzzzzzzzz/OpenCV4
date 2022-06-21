import cv2
import numpy as np

if __name__ == '__main__':
    # 创建FileStorage对象file，用于写入数据 .yam .yaml
    file = cv2.FileStorage('MyXml.xml', cv2.FileStorage_WRITE)
    # 写入数据
    file.write('name', '张三')
    file.write('age', 16)
    file.write('date', '2022-3-16')
    scores = np.array([[1, 2], [96, 97], [95, 98]])
    file.write('scores', scores)
    # 释放对象
    file.release()

    # 创建FileStorage对象file1，用于读取数据   3种数据类型 real 、 string 、 mat
    file1 = cv2.FileStorage('MyXml.xml', cv2.FILE_STORAGE_READ)
    if file1.isOpened():
        # 读取数据
        name1 = file1.getNode('name').string()
        age1 = file1.getNode('age').real()
        date1 = file1.getNode('date').string()
        scores1 = file1.getNode('scores').mat()

        print('姓名：{}'.format(name1))
        print('年龄：{}'.format(age1))
        print('日期：{}'.format(date1))
        print('成绩单：{}'.format(scores1))
    else:
        print('无法打开MyXml文件')
    # 释放对象
    file1.release()