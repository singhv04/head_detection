# head_detection

Dataset: https://github.com/HCIILAB/SCUT-HEAD-Dataset-Release

Trained yolo on custom for head detection.Concepts behind the yolo is mentioned in **yolo_basic_working.pdf**.

xml_2_txt.py converts the xml to reqiured label format i.e. for each image we need separate text file containg the details of each head on new line.The details contain the following information:

**1.** class_num

**2.** x co-ordinate of centre of the object with respect to entire image i.e.i.e.(xmin+(xmax-xmin))/image_width

**3.** y co-ordinate of centre of the object with respect to entire image i.e.(ymin+(ymax-ymin))/image_height

**4.** absolute width of the object i.e. absolute_width=(xmax-xmin)/image_width

**5.** absolute height of the object i.e. absolute_height=(ymax-ymin)/image_height
