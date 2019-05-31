import os

z=os.listdir()

z.remove('c_files')
#for k in range(0,2000):
for k in range(0,2405):
    file = open(z[k],'r')
    print(file)
    s=""
    for line in file:
        s=s+line.strip()
    file.close()
    size=s[s.index('<size>'):s.rindex('</size>')]
    image_width=size[size.index('<width>')+7:size.rindex('</width>')]
    image_height=size[size.index('<height>')+8:size.rindex('</height>')]
    try:
        object_l1=s[s.index('<object>'):]
        
        temp_f=''
        objects=object_l1.split('</object>')
        for i in range(0,len(objects)-1):
            temp=objects[i]
            locations = [temp[temp.index('<xmin>')+6:temp.rindex('</xmin>')],temp[temp.index('<ymin>')+6:temp.rindex('</ymin>')],temp[temp.index('<xmax>')+6:temp.rindex('</xmax>')],temp[temp.index('<ymax>')+6:temp.rindex('</ymax>')]]
            class_num='0'
            x=(int(locations[0])+((int(locations[2])-int(locations[0]))/2))/int(image_width)
            y=(int(locations[1])+((int(locations[3])-int(locations[1]))/2))/int(image_height)
            absolute_height=(int(locations[3])-int(locations[1]))
            absolute_width=(int(locations[2])-int(locations[0]))
            ah=absolute_height/int(image_height)
            aw=absolute_width/int(image_width)
            temp_f=temp_f+class_num+' '+str(x)+' '+str(y)+' '+str(aw)+' '+str(ah)+'\n'
    except:
        temp_f=''
    print(os.listdir()[k][:-3]+'txt')
    file1=open('c_files/'+z[k][:-3]+'txt','w')
    file1.write(temp_f)
    file1.close()
    s=""
    temp_f=""    
    print(k)
    
    
