from selenium.webdriver import Chrome
from selenium.webdriver.support.select import Select
path="C:\\Users\\B\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")

#To maximize the browser we use this method
driver.maximize_window()

#Fetching title
#print(driver.title)
#fetch url of page
#print(driver.current_url)
#fetch complete html
#print(driver.page_source)

