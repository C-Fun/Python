# -*- coding: cp936 -*-
from PIL import Image
import numpy as np

SaveImageName = "D:/��������Ա�����/Computer Language File/Python Language File/Python���ݷ������ʾ/33.png"
ImageName = "D:/33.png"

a = np.asarray(Image.open(ImageName).convert('L')).astype('float')
 
depth = 10.                      # (0-100)
grad = np.gradient(a)             #ȡͼ��Ҷȵ��ݶ�ֵ
grad_x, grad_y = grad               #�ֱ�ȡ����ͼ���ݶ�ֵ
grad_x = grad_x*depth/100.
grad_y = grad_y*depth/100.
A = np.sqrt(grad_x**2 + grad_y**2 + 1.)
uni_x = grad_x/A
uni_y = grad_y/A
uni_z = 1./A
 
vec_el = np.pi/2.2                   # ��Դ�ĸ��ӽǶȣ�����ֵ
vec_az = np.pi/4.                    # ��Դ�ķ�λ�Ƕȣ�����ֵ
dx = np.cos(vec_el)*np.cos(vec_az)   #��Դ��x ���Ӱ��
dy = np.cos(vec_el)*np.sin(vec_az)   #��Դ��y ���Ӱ��
dz = np.sin(vec_el)              #��Դ��z ���Ӱ��
 
b = 255*(dx*uni_x + dy*uni_y + dz*uni_z)     #��Դ��һ��
b = b.clip(0,255)
 
im = Image.fromarray(b.astype('uint8'))  #�ع�ͼ��
im.save(SaveImageName)
