import os
from PIL import Image


# ## 修改图片格式，png2jpg
# dirname_read="E:/cal2city/set01/"  # 注意后面的斜杠
# dirname_write="E:/cal2city/set01new/"
# names=os.listdir(dirname_read)
# count=0
# for name in names:
#     img=Image.open(dirname_read+name)
#     name=name.split(".")
#     if name[-1] == "png":
#         name[-1] = "jpg"
#         name = str.join(".", name)
#         #r,g,b,a=img.split()
#         #img=Image.merge("RGB",(r,g,b))
#         to_save_path = dirname_write + name
#         img = img.convert('RGB')#RGBA意思是红色，绿色，蓝色，Alpha的色彩空间，Alpha指透明度。而JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件
#         img.save(to_save_path)
#         count1=0
#         count1+=1
#         print(to_save_path, "------conut：",count1)
#     else:
#         continue


#####################################################################
#####################################################################
# ##批量修改resize
# from PIL import Image
# import os.path
# import glob
# def convertjpg(jpgfile,outdir,width=640,height=480):
#     img=Image.open(jpgfile)
#     try:
#         new_img=img.resize((width,height),Image.BILINEAR)
#         new_img.save(os.path.join(outdir,os.path.basename(jpgfile)))
#     except Exception as e:
#         print(e)
# for jpgfile in glob.glob("E:\\cal2city\\set05\\*.jpg"):
#     convertjpg(jpgfile,"E:\\cal2city\\set05new")


# #####################################################################
# #####################################################################
# ## 修改命名，加0
# path_1 = "E:/cal2city/set05/V000_1/"  #/home/dlut/网络/make_database/数据集处理/JpGImages_img
# filelist = os.listdir(path_1)
# filelist.sort()
# count=1
# for file in filelist:
#     print(file)
# for file in filelist:
#     Olddir=os.path.join(path_1,file)
#     if os.path.isdir(Olddir):
#         continue
#     filename=os.path.splitext(file)[0]
#     filetype=os.path.splitext(file)[1]
#     Newdir=os.path.join(path_1,"set05_V000_I"+str(count-1).zfill(5)+filetype)  # set要改，V要改，count要改
#     os.rename(Olddir,Newdir)
#     count+=1
#
# path_2 = "E:/cal2city/set05/V000_2/"  #/home/dlut/网络/make_database/数据集处理/JpGImages_img
# filelist = os.listdir(path_2)
# filelist.sort()
# count=1
# for file in filelist:
#     print(file)
# for file in filelist:
#     Olddir=os.path.join(path_2,file)
#     if os.path.isdir(Olddir):
#         continue
#     filename=os.path.splitext(file)[0]
#     filetype=os.path.splitext(file)[1]
#     Newdir=os.path.join(path_2,"set05_V000_I"+str(count+9).zfill(5)+filetype)  # set要改，V要改，count要改
#     os.rename(Olddir,Newdir)
#     count+=1
#
# path_3 = "E:/cal2city/set05/V000_3/"  #/home/dlut/网络/make_database/数据集处理/JpGImages_img
# filelist = os.listdir(path_3)
# filelist.sort()
# count=1
# for file in filelist:
#     print(file)
# for file in filelist:
#     Olddir=os.path.join(path_3,file)
#     if os.path.isdir(Olddir):
#         continue
#     filename=os.path.splitext(file)[0]
#     filetype=os.path.splitext(file)[1]
#     Newdir=os.path.join(path_3,"set05_V000_I"+str(count+99).zfill(5)+filetype)  # set要改，V要改，count要改
#     os.rename(Olddir,Newdir)
#     count+=1
#
# path_4 = "E:/cal2city/set05/V000_4/"  #/home/dlut/网络/make_database/数据集处理/JpGImages_img
# filelist = os.listdir(path_4)
# filelist.sort()
# count=1
# for file in filelist:
#     print(file)
# for file in filelist:
#     Olddir=os.path.join(path_4,file)
#     if os.path.isdir(Olddir):
#         continue
#     filename=os.path.splitext(file)[0]
#     filetype=os.path.splitext(file)[1]
#     Newdir=os.path.join(path_4,"set05_V000_I"+str(count+999).zfill(5)+filetype)  # set要改，V要改，count要改
#     os.rename(Olddir,Newdir)
#     count+=1

#####################################################################
#####################################################################
## 间隔三张取一张，从2开始，取2 5 8 11...
dirname_read ="E:/cal2city/set05/V000old/"  # 注意后面的斜杠
dirname_write="E:/cal2city/set05/V000/"
names=os.listdir(dirname_read)
count=0
for name in names:
    img=Image.open(dirname_read+name)
    name=name.split(".")
    if count==2:
        name[-1] = "jpg"
        name = str.join(".", name)
        #r,g,b,a=img.split()
        #img=Image.merge("RGB",(r,g,b))
        to_save_path = dirname_write + name
        img = img.convert('RGB')#RGBA意思是红色，绿色，蓝色，Alpha的色彩空间，Alpha指透明度。而JPG不支持透明度，所以要么丢弃Alpha,要么保存为.png文件
        img.save(to_save_path)
        count=0
        print(to_save_path, "------conut：",count)
    else:
        count+=1
        continue

