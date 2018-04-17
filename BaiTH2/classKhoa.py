class MangKhoa:
	def __init__(self, MaKhoa, TenKhoa):
		self.MaKhoa = MaKhoa
		self.TenKhoa = TenKhoa
	def getMaKhoa(self):
		return self.MaKhoa
	def setMaKhoa(self, MSSV):
		self.MaKhoa = MaKhoa
	def getTenKhoa(self):
		return self.TenKhoa
	def setTenKhoa(self, TenKhoa):
		self.TenKhoa = TenKhoa
	def toString(self):
		print self.MaKhoa+" ----",self.TenKhoa+" ---"
