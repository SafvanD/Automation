from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\B\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

#To maximize the browser we use this method
driver.maximize_window()

#Enter data into textbox

driver.find_element_by_name("fld_username").send_keys("sana")
driver.find_element_by_xpath("//input[@name='fld_email']").send_keys("san@gmail.com")
driver.find_element_by_name("fld_password").send_keys("s123@123")
driver.find_element_by_name("fld_cpassword").send_keys("s123@123")

#working on radio button

driver.find_element_by_xpath("//input[@value='home']").click()

#work on drop down

obj = Select(driver.find_element_by_name("sex"))
obj.select_by_visible_text("Male")

#obj.select_by_index(1)

#working on check button

driver.find_element_by_name("terms").click()

#close browser

#driver.close()
