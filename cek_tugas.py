from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"
# import only system from os 
from os import system, name 
  
# import sleep to show output for some time period 
  

class tugasbot:
	# pelajaran = ["""driver.find_element_by_xpath("//a[contains(@href,'MTK')]").click()"""]
	def __init__(self, username , password):
		# self.options = Options()
		# self.options.page_load_strategy = 'eager'
		# self.driver = webdriver.Chrome(options=options)
		self.driver = webdriver.Chrome(PATH)
		# if username!="" or password != "":
		self.driver.get("http://elearning.smkmediainformatika.sch.id/#/user/login")
		# self.wait = WebDriverWait(driver, 10)
		self.driver.find_element_by_name("username").send_keys(username)
		self.driver.find_element_by_name("password").send_keys(password)
		# elem.send_keys(Keys.ARROW_DOWN)
		# button
		self.driver.find_element_by_xpath("//span[contains(@class,'label')]").click() 
		sleep(4)
		# self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/app-topnav/nav/div[1]/a[1]").click()
		# self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/app-sidebar/div/div[1]/perfect-scrollbar/div/div[1]/ul/li[3]/a").click()
		# sleep(2)

	def cek(self , a):
		if any("Open" or "open" in word for word in a):
			print("\n",bcolors.WARNING,"woi forum dah di buka absen !",bcolors.ENDC)

	def forum2(self, guru):
		sleep(1)
		# pelajaran = ['pjok', 'skd', 'pkn', 'kim', 'sri', 'sb']
		pelajaran = ['pjok', 'skd', 'pkn', 'kim', 'sri', 'sb' ,' fis', 'sk', 'eng', 'kjd', 'bind', 'pds', 'mtk', 'pai', 'ba ', 'ddg']

		self.guru = guru
		self.driver.get("http://elearning.smkmediainformatika.sch.id/#/app/ruang-kelas/forum")
		# self.driver.find_element_by_xpath("//i[contains(@ng-reflect-ng-class,'blackboard')]").click()#buat ke halaman forum
		# Mtk
		if(guru == pelajaran[12]):
			sleep(2)
			self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div/div/div[4]/span/a[2]").click() #buat halaman ke 2
			sleep(2)
			self.driver.find_element_by_xpath("//a[contains(@href,'MTK')]").click()
			sleep(1)
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			a = []
			
			for x in range (len(row)):
				a.append(row[x].text)
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)
			self.cek
		
		
		#PJOK	
		elif(guru == pelajaran[0]):
			sleep(2)
			print("jing :(")
			# percobaan1
			# self.driver.find_element_by_xpath("//a[contains(@href,"+pelajaran[0].upper+")]").click()
			self.driver.find_element_by_xpath("//a[contains(@href,'PJOK')]").click()
			# elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]")
			# print([elmd.text for elmd in elems])
			# print(pjok)
			sleep(1)
			# revisi 1
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			a = []
			for x in range (len(row)):
				a.append(row[x].text)
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)
			if any("Open" or "open" in word for word in a):
				print("\n",bcolors.WARNING,"woi forum dah di buka absen !",bcolors.ENDC)





		# SKD
		elif(guru == pelajaran[1]):
			sleep(2)
			self.driver.find_element_by_xpath("//a[contains(@href,'SKD')]").click()
			# wd = driver.find_elements(By.TAG_NAME, 'tbody')
			sleep(1)
			# col cuma percobaan
			# col = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			#col dan row cuma percobaan xpath josss
			# col2 = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody")
			# sleep(1)
			# revisi 2.0
			
			# row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			
			# print(row)
			# print(col)
			# print(col2)
			#gak bisa karena list tidak punya .text
			# print(row.text)
			# print(col.text)
			# print(col2.text)
			# col2.reversed()
			# revisi 2.0
			
			# for x in range (len(row)):
			# 	print("  =========||====================================|          |===||")
			# 	print(x,"|",row[x].text)
			# 	print("  =========||====================================|          |===||")
			
			
			# # for i in en:
				# print("="*40,col2[i])

			# print([elmd.text for elmd in row])
			# print([elmds.text for elmds in col])
			# print([elmdsd.text for elmdsd in col2])

			#gak bisa
			# print(self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_4']/tbody"))
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)

		# PKN
		elif(guru == pelajaran[2]):
			sleep(2)
			self.driver.find_element_by_xpath("//a[contains(@href,'PKN')]").click()
			sleep(1)
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)

		# ENG
		elif(guru == pelajaran[8]):
			sleep(2)
			# self.driver.find
			self.driver.find_element_by_xpath("//a[contains(@href,'ENG')]").click()
			sleep(1)
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)

		
		# KJD
		elif(guru == pelajaran[9]):
			sleep(2)
			self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div/div/table/tbody/tr[10]/td[1]/a").click()
			print("berhasil")
			sleep(10)
			sleep(1)
			pertama = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]")
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			
			
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(bcolors.FAIL,x,bcolors.ENDC,"|",bcolors.OKBLUE,row[x].text,bcolors.ENDC)
				print("  =========||====================================|          |===||")
			print("\n",bcolors.UNDERLINE,"forum pertama adalah :",bcolors.ENDC,"\n",bcolors.OKGREEN,pertama.text,bcolors.ENDC)

		elif(guru == 'b'):
			print("hello world")
		
	def forum(self):
		sleep(1)
		self.driver.find_element_by_xpath("//i[contains(@ng-reflect-ng-class,'blackboard')]").click()

	def tugas(self):
		sleep(1)
		# self.driver.find_element_by_xpath("//span[contains(text(), 'Tugas Siswa')]").click()
		self.driver.get("http://elearning.smkmediainformatika.sch.id/#/app/ruang-kelas/tugas-siswa")
		sleep(2)
		elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_1']/tbody")
		# elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_3']/tbody")
		# gilakkkkkk
		try:
			for elmd in range (len(elems)):
				print("="*30)
				print(bcolors.OKGREEN+"tugas anda adalah : \n"+ elems[elmd].text+bcolors.ENDC)
				print("="*30)
				self.forr()
			
		  # print([elmd.text for elmd in elems])
		except:
		  print("An exception occurred")
		  for ko in range(1,4):
			  print(".")
			  sleep(2)
			  self.driver.quit(0)
			# sleep(0.5)
			# self.driver.quit(0)
			# sys.exit(0)
	def update(self):
		print("\n",bcolors.HEADER,"Menu",bcolors.ENDC,bcolors.BOLD,"Menu",bcolors.ENDC)
		print("="*35)
		print("1.apakah anda mau",bcolors.FAIL,"|",bcolors.ENDC," keluar dari sini?")
		print("2.apakah anda mau",bcolors.FAIL,"|",bcolors.ENDC," ke forum pelajaran lain ?")
		print("3.apakah anda mau",bcolors.FAIL,"|",bcolors.ENDC,bcolors.WARNING,"chat room di room ?",bcolors.ENDC)
		print("4.apakah anda mau",bcolors.FAIL,"|",bcolors.ENDC," ke forum paling atas ?")
		print("="*35)
		scanner = input("pilih mana 1-4 ? ")
		# scanner2 =tanya2(scanner)
		# quitt(scanner)
		return self.jikapilihan(scanner)
		
			
	def tanya(self):
		return input("sudah selesai (Y/N) : ")

	def tanya2(self, param):

		if param == 'y' or param == 'Y':
			return True
		elif param == 't' or param == 'T':
				return False
	def quitt(self,param):
		if (param == True):
			try:
				self.driver.quit()
			finally:
				
				self.driver.quit()
				print("quitt")
				# sys.exit(0)

		elif (param == False):
			print("ok")
			tanya = self.update()
		
	
	def forr(self):
		ju = True
		while ju :
			tanya = self.tanya2(self.tanya())  
			if tanya == True:
				self.driver.quit()
				break
			elif tanya == False:
				update()
				continue
		# sys.exit(0)
	
	def jikapilihan(self, jawaban):


		# self.driver = webdriver.Chrome(PATH)
		if (jawaban == '1'):
			print("1")
			self.driver.quit()
			sys.exit()
		elif jawaban == '2':
			print("\n2")
			
			guru = input("mau cek forum pelajaran apa ? ")
			self.driver.execute_script("window.open('','_blank');")
			self.driver.switch_to_window(self.driver.window_handles[1])
			self.forum2(guru)
			self.forr()
			# quit(tanya1)
			# jikapilihan(tanya2)

		elif jawaban == '3':
			print("3")
			tanya1 = self.tanya2(self.tanya())
			if tanya1 == True:
				self.chat("selamat pagi, hadirr")
				self.forr()
			else:
				self.driver.quit()


		elif jawaban == '4':
			print("4")
			tanya1 = self.tanya2(self.tanya())
			if tanya1 == True:
				print("masuk ke forum pertama ")
				sleep(1)
				# tombol click pertama
				self.click = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr[1]/td[1]/a")
				self.click.click()
				self.forr()
			else:
				self.driver.quit()
				

	def chat(self,pesan):
		try:
			self.element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div/textarea")))	
			self.element.send_keys(pesan)
			self.element.send_keys(Keys.RETURN)
			self.driver.find_element_by_xpath("//*[@id='button-addon2']").click() #button kirim
		finally:
			driver.quit()

		
		# diskusi = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div/textarea")
		# diskusi.send_keys(pesan)
		# diskusi.send_keys(Keys.RETURN)
		sleep(1)
class bcolors:
	HEADER = '\033[95m'
	OKBLUE = '\033[94m'
	OKCYAN = '\033[96m'
	OKGREEN = '\033[92m'
	WARNING = '\033[93m'
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
# define our clear function 
def clear(): 
  
	# for windows 
	if name == 'nt': 
		_ = system('cls')


	

pelajaran = [' pjok', ' skd', ' pkn', ' kim', ' sri', ' sb ' ,' fis', ' sk ', ' eng', ' kjd', 'bind', 'pds', 'mtk', 'pai', 'ba ', 'ddg']
clear()
print("="*40)
print("mau kemana disi ada : ")
print(bcolors.OKCYAN+" 1.[Forum] <--buat absen dan diskusi")
print(" 2.[Tugas] <--buat lihat tugas yang belum di kerjakan"+bcolors.ENDC)
print("\n"+"PILIH 1 atau 2")
print("="*40)

# for index1, i in enumerate pelajaran:
# 	print("index ke :"+ index1 + "pelajaran : " +i)
man = input("mau kemana : " )
if(man == '1'):
	print("="*30)
	for i, mata in enumerate(pelajaran):
		print(bcolors.BOLD,"|",i ," : ", bcolors.OKGREEN,mata,"|",bcolors.ENDC)
	guru = input("nama pelajaran nya apa : ")
	if(guru != ''):
		print("posisi a")
		print(guru)
		# mybot = tugasbot()
		mybot = tugasbot("2021099", "2021099")
		mybot.forum2(guru)
	elif(guru == 'b'):
		print("Menuju ke forum saja")
		mybot = tugasbot("2021099", "2021099")
		mybot.forum()
	else:
		print("masukin perintah yang benar ?")
		sys.exit()
elif(man == '2'):
	mybot = tugasbot("2021099", "2021099")
	mybot.tugas()
else:
	clear()
	print(bcolors.WARNING+"ups")
	print(bcolors.FAIL+"salah bro"+bcolors.ENDC)
	sys.exit()

good = mybot.update()


	
mybot.quitt(mybot.tanya2(mybot.tanya())) 
# if(mon == 'y' or mon =='Y'):
# 	print("ok  ____ ")
# 	print("ok (>  <)")
# 	print("ok ( O  ) ")
# 	for ko in range(1,4):
# 		print(".")
# 		sleep(0.5)
# 	try:
# 		sys.exit(0)
# 	except SystemExit:
# 		print("exited")
# else:           
# 	print("ok  ____ ")
# 	print("ok (>  <)")
# 	print("ok ( O  ) ")
# 	for ko in range(1,4):
# 		print(".")
# 		sleep(0.5)
# 	sys.exit(0)





# click button
# ilim.send_keys(Keys.RETURN)
# driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/app-topnav/nav/div[1]/a[1]/svg[1]").click()

		# driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/app-sidebar/div/div[2]/perfect-scrollbar/div/div[1]/ul[3]/li[3]/a/span").click()

# driver.back()

# page2 = driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div/div/div[4]/span/a[2]").click()

# page2 = driver.find_element_by_xpath("//a[contains(@data-dt-idx,'2')]")


# sleep(3)

# try:
#     main = WebDriverWait(driver, 10).until(
#         EC.presence_of_element_located((By.ID, "myDynamicElement"))
#     )
# except:
#    



# time.sleep(10)
# driver.quit()

# class mahasiswa()
# 	def __init__(self, input):
# 		self.name= input
# 		pass
# ari = mahasiswa("ari putra frederick Leluly")
