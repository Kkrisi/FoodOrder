import time
import random
import pyautogui as py
import easygui 	# Ha nem jön össze, akkor Tkinter-t kell használnom
import webbrowser


class EgészségkonyhaBot:

	def start(self):
		url = "https://egeszsegkonyha.hu/index.php/etlapunk?week="		# Ha nem írjuk mögé a hét számát, elv mindig az aktuális hetet fogja betölteni
		chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s --incognito'
		webbrowser.get(chrome_path).open_new(url)

		# Oldal betöltése
		x = True
		while(x == True):
			try:
				x, y = py.locateCenterOnScreen('upperline.png', confidence=0.5)
				print("-----------------------")
				print("Oldal megtalálása siker")

				# Reklám kiiktatása
				py.moveTo(x-250,y+100)
				time.sleep(0.5)
				py.click()
			except TypeError:
				print("----------------------------")
				print("Oldal megtalálása sikertelen")
			time.sleep(1)

		'''
		# Nem kell akciós termék	
		x = True	
		while(x == True):
			try:
				x, y = py.locateCenterOnScreen('x.png', confidence=0.7)
				print("------------------------------")
				print("Pop up ablak megtalálása siker")
				py.moveTo(x,y)
				time.sleep(0.5)
				py.click()
			except TypeError:
				print("-----------------------------------")
				print("Pop up ablak megtalálása sikertelen")

				# B terv, ne jelenjen meg többé
				x = True
				while(x == True):
					try:
						x, y = py.locateCenterOnScreen('noreklam.png', confidence=0.5)
						print("-----------------------")
						print("Oldal megtalálása siker")
						py.moveTo(x,y)
						time.sleep(0.5)
						py.click()
					except TypeError:
						print("----------------------------")
						print("Oldal megtalálása sikertelen")
			time.sleep(1)
			'''

		# Bejelentkezés
		x = True	
		while(x == True):
			try:
				x, y = py.locateCenterOnScreen('username.png', confidence=0.5)
				print("-----------------------------------")
				print("Felhasználási név megtalálása siker")

				username = '1970zsolt'
				password = 'Lorka7krisi'

				# Felhasználási név beírása
				py.moveTo(x,y)
				time.sleep(0.5)
				py.click()
				time.sleep(0.5)
				py.write(username)
				time.sleep(1)

				# Jelszó beírása
				py.press("tab")
				time.sleep(0.5)
				py.write(password)
				time.sleep(0.5)
				py.press("enter")
				time.sleep(1)
			except TypeError:
				print("----------------------------------------")
				print("Felhasználási név megtalálása sikertelen")
			time.sleep(1)

		# Készenlét a vásárláshoz	
		x = True	
		while(x == True):
			try:
				x, y = py.locateCenterOnScreen('x.png', confidence=0.7)
				print("------------------")
				print("Kész a vásárláshoz")
			except TypeError:
				print("------------------------")
				print("Nincs kész a vásárláshoz")
			time.sleep(1)


	def buy():
		# Készenlét a vásárláshoz	
		x = True	
		while(x == True):
			try:
				x, y = py.locateCenterOnScreen('openall.png', confidence=0.7)
				print("---------------------")
				print("Siker, menük kinyitva")

				# Lefelé menetel a menüsorban
				for i in range(160):
					py.press("down")
					time.sleep(0.3)

					# Ismert ételek keresése
					x = True	
					while(x == True):
						try:
							x, y = py.locateCenterOnScreen('x.png', confidence=0.7)
							print("Megvan egy, az óhajtott ételek közül: ") #print("Megvan egy, az óhajtott ételek közül: ", csirkecomb)
							time.sleep(0.5)

							# Választott étel hozzáadása a listához	
							x = True	
							while(x == True):
								try:
									x, y = py.locateCenterOnScreen('sutotokrakas.png', confidence=0.7)
									print("------------------")
									print("Sütőtökrakás megtalálva")
								except TypeError:
									print("------------------------")
									print("Nincs sütőtökrakás találat")
								time.sleep(1)

						except TypeError:
							print("Nincs meg az óhajtott étel")
						time.sleep(1)

			except TypeError:
				print("-------------------------------")
				print("Nem sikerült kinyitni a menüket")
			time.sleep(1)





egesz = EgészségkonyhaBot()
egesz.start()








# stopper indítása
# minden locateonscreen rprobalkozasnal kiirja hogy hanyadjara nem talalta meg
# az egész kódot meglehessen szakíteni egy "q" betűvel