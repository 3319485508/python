# _*_ coding: utf-8 _*_

'''
    将文件逐行读取，每6行组成新行
'''

lst = []

#读
f = open("links.txt", "r")
for line in f:
    lst.append(line.strip("\n"))
f.close()

#分组
lst2 = [lst[i: i+6] for i in range(0, len(lst), 6)]

cont = ""
for s in lst2:    
    cont += "		subs_filter '<div class=\"footer\">' '<div class=\"footer\">" + " | ".join(s) + " | </div>';\n"

#写
f2 = open("bbb.txt", "w")
f2.write(cont)
f2.close()

print "写入成功"