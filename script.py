from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import sys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
PATH = "C:\Program Files (x86)\chromedriver.exe"



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
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
		
		
		#PJOK	
		elif(guru == pelajaran[0]):
			sleep(2)
			print("jing :(")
			
			# self.driver.find_element_by_xpath("//a[contains(@href,"+pelajaran[0].upper+")]").click()
			self.driver.find_element_by_xpath("//a[contains(@href,'PJOK')]").click()
			# elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_0']/tbody/tr[1]")
			# print([elmd.text for elmd in elems])
			# print(pjok)
			sleep(1)
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
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
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			# print(row)
			# print(col)
			# print(col2)
			#gak bisa karena list tidak punya .text
			# print(row.text)
			# print(col.text)
			# print(col2.text)
			# col2.reversed()
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
			# for i in en:
				# print("="*40,col2[i])

			# print([elmd.text for elmd in row])
			# print([elmds.text for elmds in col])
			# print([elmdsd.text for elmdsd in col2])

			#gak bisa
			# print(self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_4']/tbody"))
		# PKN
		elif(guru == pelajaran[2]):
			sleep(2)
			self.driver.find_element_by_xpath("//a[contains(@href,'PKN')]").click()
			sleep(1)
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
		# ENG
		elif(guru == pelajaran[8]):
			sleep(2)
			# self.driver.find
			self.driver.find_element_by_xpath("//a[contains(@href,'ENG')]").click()
			sleep(1)
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
		
		# KJD
		elif(guru == pelajaran[9]):
			sleep(2)
			self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div/div/table/tbody/tr[10]/td[1]/a").click()
			print("berhasil")
			sleep(10)
			sleep(1)
			row = self.driver.find_elements_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div/div/div/table/tbody/tr")
			for x in range (len(row)):
				print("  =========||====================================|          |===||")
				print(x,"|",row[x].text)
				print("  =========||====================================|          |===||")
		elif(guru == 'b'):
			print("hello world")
		
	def forum(self):
		sleep(1)
		self.driver.find_element_by_xpath("//i[contains(@ng-reflect-ng-class,'blackboard')]").click()

	def tugas(self):
		sleep(1)
		self.driver.find_element_by_xpath("//span[contains(text(), 'Tugas Siswa')]").click()
		sleep(2)
		elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_1']/tbody")
		# elems = self.driver.find_elements_by_xpath("//*[@id='DataTables_Table_3']/tbody")
		# gilakkkkkk
		try:
			for elmd in range (len(elems)):
				print("="*30)
				print("tugas anda adalah : \n"+ elems[elmd].text)
				print("="*30)
			
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
		print("="*35)
		print("1.apakah anda mau keluar dari forum?")
		print("2.apakah anda mau pindah cek?")
		print("3.apakah anda mau pindah room ?")
		print("4.apakah anda mau chat di room ?")
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
				# self.driver.quit(0)
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
			# sys.exit(0)
		elif jawaban == '2':
			print("\n2")
			
			guru = input("mau cek forum pelajaran apa ? ")
			self.driver.execute_script("window.open('','_blank');")
			self.driver.switch_to_window(self.driver.window_handles[1])
			self.forum2(guru)
			self.forr()
			# tanya1 = tanya2(tanya())
			# quit(tanya1)
			# jikapilihan(tanya2)

		elif jawaban == '3':
			print("3")


		elif jawaban == '4':
			print("4")

	def chat(self,pesan):
		try:
			
   			self.element = WebDriverWait(driver, 10).until(
			EC.presence_of_element_located((By.XPATH, "/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div/textarea")))	
			element.send_keys(pesan)
			element.send_keys(Keys.RETURN)
			self.driver.find_element_by_xpath("//*[@id='button-addon2']").click() #button kirim
		finally:
			driver.quit()

		
		# diskusi = self.driver.find_element_by_xpath("/html/body/app-root/div/app-app/div/main/div/app-ruang-kelas/app-forum/div[2]/div/div/div/div[2]/div/div[2]/div/div/div[2]/form/div[2]/div/textarea")
		# diskusi.send_keys(pesan)
		# diskusi.send_keys(Keys.RETURN)
		sleep(1)


	

pelajaran = ['pjok', 'skd', 'pkn', 'kim', 'sri', ' sb' ,' fis', '  sk', ' eng', ' kjd', 'bind', 'pds', 'mtk', 'pai', 'ba ', 'ddg']
print("="*40)
print("mau kemana disi ada : ")
print(" 1.[Forum] <--buat absen dan diskusi")
print(" 2.[Tugas] <--buat lihat tugas yang belum di kerjakan")
print("\n"+"PILIH 1 atau 2")
print("="*40)

# for index1, i in enumerate pelajaran:
# 	print("index ke :"+ index1 + "pelajaran : " +i)
man = input("mau kemana : " )
if(man == '1'):
	print("="*30)
	for i, mata in enumerate(pelajaran):
		print("|",i ," : ", mata,"|")
	guru = input("nama pelajaran nya apa : ")
	if(guru != ''):
		print("posisi a")
		print(guru)
		# mybot = tugasbot()
		mybot = tugasbot("2021099", "2021099")
		mybot.forum2(guru)
	else:
		mybot = tugasbot("2021099", "2021099")
		mybot.forum()
elif(man == '2'):
	mybot = tugasbot("2021099", "2021099")
	mybot.tugas()
else:
	print("salah bro")

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
