from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import names
import random
import string
import strgen
import time
import os



def full_mail():
    R = int(input("Enter You Want 📦 : "))
    email_format = "@outlook.com"
    ZX = ":"
    full = []
    MailF = []
    for i in range(
        0,
        R,
    ):
        letters_list = [string.digits, string.ascii_lowercase, string.ascii_uppercase]
        letters_list_to_str = "".join(letters_list)
        email_generated = (
            "".join(random.choices(letters_list_to_str, k=20)) + email_format + ZX
        )
        MailF.append(email_generated)
        # print(MailF)

        random_pw = strgen.StringGenerator("[\d]{2}&[\w]{4}&[\p]{2}").render()
        full.append(email_generated + random_pw)
        # print(full)

    Item = ["{}\n".format(i) for i in full]
    with open(r"mail.txt", "w") as fp:
        fp.writelines(Item)
        print("Gen🔥", i + 1, "📦 Email ⚡")


def reggmail():
    os.system('cls')
    R = int(input("Enter You Want 📦 : "))
    
    email_format = "@outlook.com"
    ZX = ":"
    full = []
    MailF = []
    FullData = []
    for i in range(
        0,
        R,
    ):
        email_generated = ''.join([random.choice(string.ascii_uppercase + string.ascii_lowercase) for n in range(10)])
                        
        # email_generated = "".join(random.choices(letters_list_to_str, k=10)) + email_format

        random_pw = strgen.StringGenerator("[\w]{4}&[\d]{2}&[\p]{2}").render()

        f_name = names.get_first_name()
        l_name = names.get_last_name()

        # with open("proxy.txt",'r') as data:
        #   speech = data.read().splitlines()
        #   print(speech)

        chrome_op1 = webdriver.ChromeOptions()
        chrome_op1.add_argument('--incognito')

        browser = webdriver.Chrome(executable_path="RX_DRIVER/chromedriver", options=chrome_op1)
        browser.set_window_size(20, 500)
        browser.get("https://signup.live.com")
        os.system('cls')
        print(" Waiting ⛱️ ", i + 1,'/', R)
        
        password_selector = "#PasswordInput"
        WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, password_selector))
        )

        browser.find_element(By.CSS_SELECTOR, '#MemberName').send_keys(email_generated,email_format)
        browser.find_element(By.ID, "iSignupAction").click()
        time.sleep(3)
        browser.find_element(By.ID, "PasswordInput").send_keys(random_pw)
        browser.find_element(By.ID, "iSignupAction").click()
        os.system('cls')
        print(" Waiting ⛱️ ", i + 1,'/', R)
        
        time.sleep(1)
        browser.find_element(By.ID, "FirstName").send_keys(f_name)
        browser.find_element(By.ID, "LastName").send_keys(l_name)
        browser.find_element(By.ID, "iSignupAction").click()
        
        time.sleep(1)
        browser.find_element_by_xpath("//*[@id='BirthDay']/option[text()='16']").click()
        browser.find_element_by_xpath("//*[@id='BirthMonth']/option[text()='กันยายน']").click()
        browser.find_element(By.CSS_SELECTOR, '#BirthYear').send_keys("2000")
        browser.find_element(By.ID, "iSignupAction").click()
        
        os.system('cls')
        
        join_data = email_generated + email_format + ":" + random_pw + " " + f_name + " " + l_name
        FullData.append(join_data)
        Item = ["{}\n".format(i) for i in FullData]
        with open(r"mail.txt", "w") as fp:
         fp.writelines(Item)
        
        
        print(
            "",
            email_generated + email_format,
            "\n",
            random_pw,
            "\n",
            f_name,
            "",
            l_name,
        )
        print(" Working 📈", i + 1,'/', R , "Email ♻️")
        
        
    time.sleep(40)
    print(" Success 🍕", i + 1, "Email 📧")

full_mail()