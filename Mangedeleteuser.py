from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.support.ui import Select

# ระบุพาธของ ChromeDriver 
chrome_driver_path = "D:\ProjectAll\webdriver\chromedriver.exe"

# เริ่มต้น WebDriver
driver = webdriver.Chrome()
# ขยายหน้าต่างเบราว์เซอร์ให้เต็มหน้าจอ
driver.maximize_window()

# เปิดเว็บไซต์ของคุณ
driver.get("https://online-web-mauve.vercel.app/")

# คลิกปุ่ม "เข้าสู่ระบบ"
open_modal_button = driver.find_element(By.XPATH, "//span[text()='เข้าสู่ระบบ']")
open_modal_button.click()

# ระบุ element ของรหัสประจำตัวประชาชนและรหัสผ่านใน Modal
id_input = driver.find_element(By.XPATH, "//label[text()='รหัสประจำตัวประชาชน']/following-sibling::input")
password_input = driver.find_element(By.XPATH, "//label[text()='รหัสผ่าน']/following-sibling::input")

# กรอกข้อมูลใน input field
id_input.send_keys("8888888888888")
password_input.send_keys("123456")

time.sleep(2)

# คลิกปุ่ม "เข้าสู่ระบบ" ด้วย XPath
login_button = driver.find_element(By.XPATH, "//button[text()='เข้าสู่ระบบ']")
login_button.click()
time.sleep(5)

# ค้นหา <div> โดยใช้ XPath
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "จัดการ")]')

# คลิกที่ <div>
div_element.click()
time.sleep(5)

# ค้นหา <div> โดยใช้ข้อความ "รายชื่อผู้ใช้" ในหน้าเว็บ
div_element = driver.find_element(By.XPATH, '//div[contains(text(), "รายชื่อผู้ใช้")]')
div_element.click()
time.sleep(5)

search_input = driver.find_element(By.ID, "SearchUser")
search_input.send_keys("1342564534672")
time.sleep(2)


# ระบุปุ่ม "ลบ" ด้วย XPath
delete_button = driver.find_element(By.XPATH, "//button[@id='DeleteUser']")
delete_button.click()
time.sleep(5)

   # ระบุ element ของปุ่ม "ตกลง" ด้วย XPath
confirm_button = driver.find_element(By.XPATH, "//button[@class='swal2-confirm swal2-styled' and text()='ตกลง']")

        # คลิกปุ่ม "ตกลง"
confirm_button.click()
time.sleep(5)