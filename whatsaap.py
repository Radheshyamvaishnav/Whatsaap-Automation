from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\chromedriver_win32\\chromedriver.exe")    # Give here your path to chromedriver

driver.get("https://web.whatsapp.com/")       
driver.maximize_window()         

name = input("Enter name of group or Individual")
msg = input("Enter the msg")

user = driver.find_element_by_xpath("//span[@title='{}']".format(name))
user.click()
msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")

msg_box.send_keys(msg)

driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()

print("Success")

