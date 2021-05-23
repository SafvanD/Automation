from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import time
path="C:\\Users\\B\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/testings")
driver.maximize_window()

driver.find_element_by_name("fld_username").send_keys("sana")

act = ActionChains(driver)
act.key_down(Keys.CONTROL).send_keys('a').perform()
time.sleep(10)

#act.send_keys(Keys.TAB).perform()


