from classMang import MangSV
from classKhoa import MangKhoa

sv = []
sv.append(MangSV("001","Tran Van A","k57"))
sv.append(MangSV("002","Nguyen Van B","k57"))
sv.append(MangSV("003","Nguyen Van C","k58"))
print "MSSV---Ten---Khoa"
for i in sv:
	print i.toString()
M = []
M.append(MangKhoa("k57","Khoa K57"))
M.append(MangKhoa("k58","Khoa K58"))
M.append(MangKhoa("k59","Khoa K59"))
print "Ma Khoa --- Ten Khoa"
for i in M:
	print i.toString()

