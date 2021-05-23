from selenium.webdriver import Chrome
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path="C:\\Users\\B\\Downloads\\chromedriver_win32\\chromedriver.exe"

driver=Chrome(executable_path=path)
driver.get("http://www.theTestingWorld.com/")
act=ActionChains(driver)

#click operation
#act.click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

#context click(Right click)
#act.context_click(driver.find_element_by_xpath("//a[text()='Login']")).perform()

act.move_to_element(driver.find_element_by_xpath("//span[contains(text(),'TUTORIAL')]")).perform()
