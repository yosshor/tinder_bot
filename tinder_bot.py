"""
Created on Mon Apr 20 17:58:26 2020
@author: yoss
"""
import time 
from selenium import webdriver
from secret_user_pass import username, password




class TinderBot():
    
    def __init__(self):

        # # Specifying incognito mode as you launch your browser[OPTIONAL]
        # self.option = webdriver.ChromeOptions()
        # self.option.add_argument("--incognito")
        # self.driver = webdriver.Chrome(chrome_options = self.option)        
        self.driver = webdriver.Chrome()
        
        
    def login(self):
        self.driver.get('https://tinder.com')
        # self.driver.maximize_window() 
        time.sleep(5)
        face_option = ['//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[2]/button', \
                       '//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/div[1]/div/span/div[2]/button', \
                       '//*[@id="modal-manager"]/div/div/div/div/div[3]/span/div[3]/button', \
                        '//*[@id="content"]/div/div[1]/div/div/main/div/div[2]/div[2]/div/div/span/div[2]/button/span[2]']
        facebook_button = self.driver.find_element_by_xpath(face_option[0] or face_option[1] or face_option[2] or face_option[3])
        time.sleep(3)
        facebook_button.click()
        first_window = self.driver.window_handles[0]
        self.driver.switch_to_window(self.driver.window_handles[1]) #switch to login facebook popup window 
        email_login = self.driver.find_element_by_xpath('//*[@id="email"]')
        email_login.send_keys(username)
        passw_login = self.driver.find_element_by_xpath('//*[@id="pass"]')
        passw_login.send_keys(password)
        self.driver.find_element_by_xpath('//*[@id="u_0_0"]').click()
        time.sleep(2)
        self.driver.switch_to_window(first_window)
        time.sleep(6)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]').click()
        time.sleep(2)
        self.driver.find_element_by_xpath('//*[@id="content"]/div/div[2]/div/div/div[1]/button').click()
        time.sleep(1)
        self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[1]/button' or '//*[@id="modal-manager"]/div/div/div[1]/button/span').click()
        print('Login Successful') 

    def like(self):
        like = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button' \
                                                  or '//*[@id="content"]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button' \
                                                  or  '/html/body/div[1]/div/div[1]/div/div/main/div/div[1]/div/div[2]/div[4]/button')
        like.click()

        
    def close_match(self, match):
        close = self.driver.find_element_by_xpath('//*[@id="modal-manager-canvas"]/div/div/div[1]/div/div[3]/a')
        close.click()
        match +=1
        return match
    
    def close_popup(self):
        close_pop = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[2]/button[2]')
        close_pop.click()
    
    def out_of_likes(self):
        try :
            close = self.driver.find_element_by_xpath('//*[@id="modal-manager"]/div/div/div[3]/button[2]/span'\
                                                      or '//*[@id="modal-manager"]/div/div/div[3]/button[2]')
            try :
                time_left = self.driver.find_element_by_css_selector('#modal-manager > div > div > div.Bg\(\$green-gradient-radial\).CenterAlign.D\(f\).Fld\(c\) > div.D\(f\).Fxg\(1\).Jc\(c\).Fld\(c\).Maw\(100\%\).Pos\(r\) > div.Mb\(20px\) > div > div:nth-child(1) > div > div > span > div > div > div:nth-child(1) > div')
                time_left = time_left.text
                
            except Exception :
                time_left = '12:00:00 Hours'
            
        except Exception as error :
            print(error)
       
        finally :
            print("You're Out Of Likes! ")  
            print(f"TIME LEFT: {time_left}")
            close.click()



    def main(self):
        # username = input("Enter username : ") 
        # password = input("Enter password : ") 

        self.login()
        time.sleep(1)
        like, match = 0, 0
        print("Start to make likes")
        while True:
            try :
                self.like()
                like += 1
                time.sleep(0.5)
            except Exception:
                try :
                    print("checks to close match popup ")
                    match = self.close_match(match)
                except Exception:
                    try :
                        print("checks to close popup ")
                        self.close_popup()
                    except Exception:
                        print("checks if you're out of likes ")
                        self.out_of_likes()
                        print(f"You have found {match} {'matches' if match > 1 else 'match'} in this round")
                        print(f"You have made {like} Likes") 
                        self.driver.close()
                        break
                    
if __name__ == '__main__':
    TinderBot().main()
    
