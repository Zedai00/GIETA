import getpass

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

options = Options()
options.page_load_strategy = "eager"
options.add_argument("--headless")
driver = webdriver.Firefox(options)
driver.get("https://gietcampus.com/gier/Default.aspx")
print("GIET Attendance Report")
user = driver.find_element(By.NAME, "txtId2")
user.clear()
user.send_keys(input("Enter Pin No: "))
password = driver.find_element(By.NAME, "txtPwd2")
password.clear()
password.send_keys(getpass.getpass())
loginBtn = driver.find_element(By.NAME, "imgBtn2")
loginBtn.click()
name = driver.find_element(By.ID, "lblUser")
print(name.text)

driver.get("https://gietcampus.com/gier/Academics/studentacadamicregister.aspx")
# for i in elm:
#     print(i.get_attribute("title"))
sum = 0.0
print("Subject: Score")
td = 1
while True:
    elm = driver.find_element(
        By.XPATH,
        f'//*[@id="tblReport"]/center/table/tbody/tr[5]/td/table/tbody/tr[1]/td[{td}]',
    )
    if "%" in elm.text:
        break
    td += 1


subCount = (
    len(
        driver.find_elements(
            By.XPATH,
            '//*[@id="tblReport"]/center/table/tbody/tr[5]/td/table/tbody/*',
        )
    )
    - 1
)
print(subCount)
for i in range(2, subCount + 2):
    elm = driver.find_element(
        By.XPATH,
        f'//*[@id="tblReport"]/center/table/tbody/tr[5]/td/table/tbody/tr[{i}]/td[{td}]',
    )
    sub = driver.find_element(
        By.XPATH,
        f'//*[@id="tblReport"]/center/table/tbody/tr[5]/td/table/tbody/tr[{i}]/td[2]',
    )
    sum += float(elm.text)
    print(f"{sub.text}: {elm.text}%")
print(f"Result: {format((sum / subCount),'.2f')}%")
driver.quit()
