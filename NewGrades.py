'''
Created on 9 lis 2018

@author: ewelina
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

# from PrivateData import privateData as pv
from SendMail import sendEmail
from Tests import TestCase
from ListDiff import listDiff

class HasGotNewGrades(TestCase):
    url = "https://uonetplus.vulcan.net.pl/rybnik"
    mainLogButtonCss = "//*[@id='MainPage_InfoPage']/div/div[1]/div[2]/div/a[1]"
    gradesCss = "[class='panel oceny klient szary isotope-item'] [class='subDiv pCont']"
                
    subject = "Check new grades!"
    message = "There are new grades: "
    
    def test_hasGotNewGrades(self):
        self.driver.get(self.url)
                
        try:
            mainLogButton = self.driver.find_element_by_xpath(self.mainLogButtonCss)
        except Exception:
            self.fail("Main log button not found.")
        mainLogButton.click()
        
        HasGotNewGrades.logInToVulcan(self)

        wait = WebDriverWait(self.driver, 10)
        try:
            wait.until(EC.presence_of_element_located((By.XPATH, "//*[@id='content']/div[6]")))
        except Exception:
            self.fail("Grades panel not found.")

        grades = self.driver.find_element_by_css_selector(self.gradesCss)
        newGrades = grades.text
        listOfNewGrades = newGrades.splitlines()
        print("\nNew grades: \n" + newGrades)
        
        fileName = "grades.txt"
        file = open(fileName, 'a+')
        file.seek(0)
        fileText = file.read() 
        listOfGradesInFile = fileText.splitlines()
        print("\nGrades in a file: \n" + fileText)

        changes = listDiff(listOfNewGrades, listOfGradesInFile)
        partOfMessage = str(changes)
        print (partOfMessage)
         
        if (fileText == 0 or (fileText != newGrades)):
            file.truncate(0)
            file.writelines(grades.text)
            file.close()
            print("Send an email.")
            sendEmail(pv.emailsToNotify, self.subject, self.message + partOfMessage, fileName)
        else:
            file.close()
            print("There is no changes. Email wasn't send.")
            
             
    def logInToVulcan(self):
        loginFieldCss = loginName
        passwordFieldCss = password
        logButtonXpath = "//*[@id='MainDiv']/form/div[2]/div[4]/input"
         
        try:
            logButton = self.driver.find_element_by_xpath(logButtonXpath)
        except Exception:
            self.fail("Log button not found.")
    
        loginField = self.driver.find_element_by_id(loginFieldCss)
        loginField.send_keys(vulcanLogin)
        passwordField = self.driver.find_element_by_id(passwordFieldCss)
        passwordField.send_keys(vulcanPassword)
        logButton.click()
