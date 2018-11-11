'''
Created on 9 lis 2018

@author: ewelina
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from PrivateData import privateData as pv
from SendMail import sendEmail
from Tests import TestCase


class HasGotNewGrades(TestCase):
    url = "https://uonetplus.vulcan.net.pl/rybnik"
    mainLogButtonCss = '//*[@id="MainPage_InfoPage"]/div/div[1]/div[2]/div/a[1]'
    loginFieldCss = "LoginName"
    passwordFieldCss = "Password"
    logButtonCss = '//*[@id="MainDiv"]/form/div[2]/div[4]/input'
    gradesCss = '[class="panel oceny klient szary isotope-item"] [class="subDiv pCont"]'
    cookieCss = 'cookiePanel-exit'            
    subject = "Check new grades!"
    message = "There are new grades! Check an attached file: "
    
    def test_hasGotNewGrades(self):
        self.driver.get(self.url)
        
        cookies = self.driver.find_element_by_id(self.cookieCss)
#         if cookies.:
        cookies.click()
            
        try:
            mainLogButton = self.driver.find_element_by_xpath(self.mainLogButtonCss)
        except Exception:
            self.fail("Main log button not found.")
        mainLogButton.click()
        
        try:
            logButton = self.driver.find_element_by_xpath(self.logButtonCss)
        except Exception:
            self.fail("Log button not found.")
    
        loginField = self.driver.find_element_by_id(self.loginFieldCss)
        loginField.send_keys(pv.vulcanLogin)
        passwordField = self.driver.find_element_by_id(self.passwordFieldCss)
        passwordField.send_keys(pv.vulcanPassword)
        logButton.click()

        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="content"]/div[6]')))
        except Exception:
            self.fail("Grades panel not found.")

        grades = self.driver.find_element_by_css_selector(self.gradesCss)
        newGrades = grades.text
        print("\nNew grades: \n" + newGrades)
        
        fileName = "grades.txt"
        file = open(fileName, 'a+')
        file.seek(0)
        fileText = file.read() 
        print("\nGrades in a file: \n" + fileText)
        
        if (fileText == 0 or (fileText != newGrades)):
            file.truncate(0)
            file.writelines(grades.text)
            file.close()
            print("Send an email.")
            sendEmail(pv.smtpLogin, pv.emailsToNotify, self.subject, self.message, fileName)
        else:
            file.close()
            print("There is no changes. Email wasn't send.")
             
