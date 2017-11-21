from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

coord_x = 0
coord_y = 0

time_to_load = 2

#buildings
place = ""
barracks = ""
main=""



world = "pl122"

village_no = "12345"




def get_links():
	file=open("links.txt","r")
	
	#get link to world
	file.readline() #skip comment
	global world
	world=file.readline() #get link to world
	
	#get village number
	file.readline()
	file.readline()
	global village_no
	village_no = file.readline()
	
	#get coords
	file.readline()
	file.readline()
	coords = file.readline()
	global coord_x
	coord_x = coords[0:3]
	global coord_y
	coord_y = coords[4:7]

def get_user_name():
	file=open("credencials.txt","r")
	username = file.readline()
	file.close()
	return username
	
def get_password():
	file=open("credencials.txt","r")
	file.readline()
	password = file.readline()
	file.close()
	return password
	
def get_num(num_str):
	num_temp = ''
	for x in num_str:
		if(x.isdigit()):
			num_temp = num_temp + x
	return int(num_temp)
	
def login():
	username = get_user_name()
	password = get_password()
	el_user = driver.find_element_by_id("user")
	el_user.send_keys(username)
	el_pass = driver.find_element_by_id("password")
	el_pass.send_keys(password)
	el_pass.send_keys(Keys.RETURN)
	time.sleep(1)
	driver.get("https://www.plemiona.pl/page/play/pl122")
	
def attack(coords,units):
	#if before 23 daily mode else night mode
	el_time = driver.find_elements_by_id("serverTime")
	print(el_time[0].text)
	
	#enter to the place
	driver.get(place)
	
	#set units	
	el_spear_num = driver.find_elements_by_id("units_entry_all_spear")
	if(len(el_spear_num)>0):
		if(get_num(el_spear_num[0].text) >= units[0]):
			el_spear = driver.find_elements_by_id("unit_input_spear")
			if(len(el_spear)>0):
				el_spear[0].send_keys(units[0])
			else:
				print("el_spear does not exist")
				driver.get(village)
				return
		else:
			print("not enough army")
			driver.get(village)
			return
	else:
		print("el_spear_num does not exist")
		driver.get(village)
		return
		
	el_spear_num = driver.find_elements_by_id("units_entry_all_sword")
	if(len(el_spear_num)>0):
		if(get_num(el_spear_num[0].text) >= units[1]):
			el_spear = driver.find_elements_by_id("unit_input_sword")
			if(len(el_spear)>0):
				el_spear[0].send_keys(units[1])
			else:
				print("el_spear does not exist")
				driver.get(village)
				return
		else:
			print("not enough army")
			driver.get(village)
			return
	else:
		print("el_spear_num does not exist")
		driver.get(village)
		return
		
	el_spear_num = driver.find_elements_by_id("units_entry_all_axe")
	if(len(el_spear_num)>0):
		if(get_num(el_spear_num[0].text) >= units[2]):
			el_spear = driver.find_elements_by_id("unit_input_axe")
			if(len(el_spear)>0):
				el_spear[0].send_keys(units[2])
			else:
				print("el_spear does not exist")
				driver.get(village)
				return
		else:
			print("not enough army")
			driver.get(village)
			return
	else:
		print("el_spear_num does not exist")
		driver.get(village)
		return
	
	#type village coords to attack
	el_coords = driver.find_elements_by_xpath("//div[@id='place_target']//input[@type='text']")
	if(len(el_coords)):
		el_coords[0].send_keys(coords)
		el_target_attack = driver.find_elements_by_id("target_attack")
		if(len(el_target_attack)):
			el_target_attack[0].click()
		else:
			driver.get(village)
			return			
	else:
		driver.get(village)
		return
	
	time.sleep(time_to_load)
	el_send_attack = driver.find_elements_by_id("troop_confirm_go")
	if(len(el_send_attack)):
		el_send_attack[0].click()
	else:
		driver.get(village)
		return
		
	
	
	



driver = webdriver.Chrome()
driver.get("https://www.plemiona.pl/")

login()
get_links()

place = "https://%s.plemiona.pl/game.php?village=%s&screen=place" %( world.rstrip() ,village_no.rstrip())
barracks = "https://%s.plemiona.pl/game.php?village=%s&screen=barracks" %( world.rstrip() ,village_no.rstrip())
main = "https://%s.plemiona.pl/game.php?village=%s&screen=main" %( world.rstrip() ,village_no.rstrip())
village = "https://www.plemiona.pl/page/play/%s" %world.rstrip()

units = (1,10,3,0,0,0,0,0,0,0,0,0)
attack("289|323", units)

time.sleep(100)

driver.close()

