import json
import os
import math
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns; sns.set()  # for plot styling


def convert_yolo2gt(label, width=512, height=512):
    # temp_label = []
    # dx,dy,dw,dh = label
    dw,dh = label
    w = dw*width
    h = dh*height
    # x = (dx*width) - (w/2)
    # y = (dy*height) - (h/2)
    return [w,h]

# os.chdir("/media/deniz/02B89600B895F301/BBD100K")
train_path = os.getcwd()+"/train.txt"

w,h = [], []
file1 = open(train_path,"r")
for line1 in file1:
    label_file  = line1.strip().split(".")[0]+".txt"
    file2 = open(label_file,'r')
    for line2 in file2:
        _,dx,dy,dw,dh = line2.split(" ")
        # dx=int(dx)
        # dy=int(dy)
        dw=float(dw)
        dh=float(dh)
        width,height = convert_yolo2gt([dw,dh])
        w.append(width)
        h.append(height)
    file2.close()

file1.close()

w=np.asarray(w)
h=np.asarray(h)

print(w.shape)
print(h.shape)

print(w[0])
print(h[0])
# w,h = [] , []
# for ind1 in range(len(trlabel)):
#     for ind2 in range(len(trlabel[ind1]["labels"])):
#         try:
#             a=trlabel[ind1]["labels"][ind2]["box2d"]   #traffic sign
#             x1,y1,x2,y2 = list(a.values())
#             width = abs(x1-x2)
#             height = abs(y1-y2)
#             w.append(width)
#             h.append(height)
#         except:
#             pass
# w=np.asarray(w)
# h=np.asarray(h)
     
x=[w,h]
x=np.asarray(x)
x=x.transpose()
##########################################   K- Means
##########################################

from sklearn.cluster import KMeans
kmeans3 = KMeans(n_clusters=9)
kmeans3.fit(x)
y_kmeans3 = kmeans3.predict(x)

##########################################
centers3 = kmeans3.cluster_centers_

yolo_anchor_average=[]
for ind in range (9):
    yolo_anchor_average.append(np.mean(x[y_kmeans3==ind],axis=0))

yolo_anchor_average=np.array(yolo_anchor_average)

plt.scatter(x[:, 0], x[:, 1], c=y_kmeans3, s=2, cmap='viridis')
plt.scatter(yolo_anchor_average[:, 0], yolo_anchor_average[:, 1], c='red', s=50);
yoloV3anchors = yolo_anchor_average
yoloV3anchors[:, 0] =yolo_anchor_average[:, 0] /512 *512
yoloV3anchors[:, 1] =yolo_anchor_average[:, 1] /512 *512
yoloV3anchors = np.rint(yoloV3anchors)
fig, ax = plt.subplots()
for ind in range(9):
    rectangle= plt.Rectangle((304-yoloV3anchors[ind,0]/2,304-yoloV3anchors[ind,1]/2), yoloV3anchors[ind,0],yoloV3anchors[ind,1] , fc='b',edgecolor='b',fill = None)
    ax.add_patch(rectangle)
ax.set_aspect(1.0)
plt.axis([0,512,0,512])
plt.show()
yoloV3anchors.sort(axis=0)
print("Your custom anchor boxes are {}".format(yoloV3anchors))

F = open("custom_yolov3_anchors.txt", "w")
F.write("{}".format(yoloV3anchors))
F.close()