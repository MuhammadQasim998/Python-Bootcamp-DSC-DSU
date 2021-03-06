from selenium import webdriver
from getpass import getpass
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://m.facebook.com")
    
email = input("Enter your email:")
password = getpass("Enter your password:")

#login Information
email = driver.find_element_by_id("m_login_email")
password = driver.find_element_by_css_selector("input[name='pass']")
log_button = driver.find_element_by_name("login")

email.send_keys(email)
password.send_keys(password)
log_button.click()

url = 'https://m.facebook.com/DeveloperStudentClubDHASuffaUniversity/photos/a.1451042185216529/2839108256409908/'

#loading fb post
driver.get(url)
    
#Post_Like
like_button = driver.find_element_by_css_selector("div[data-sigil='ufi-inline-actions'] div a")
like_button.click()

#Comment
comm_Text = "Great instructors and great experience. Thankyou DSC-DSU for giving us this great opportunity to learn some new skills. Bootcamp was well managed."
comment = comm_Text.split(".")
for i in comment:
     comment_Area = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.mentions textarea#composerInput")))
        comment_Area.send_keys(i)

        post_Button = WebDriverWait(driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, 'button[data-sigil="touchable composer-submit"]')))
        post_Button.click()

#sharing_Post
share_button = driver.find_element_by_css_selector("div[data-sigil='ufi-inline-actions'] div a[data-sigil='share-popup']")
write_button = driver.find_element_by_id("share-with-message-button")

share_button.click()

write_button.click()

#Adding_caption
caption = ('''Created a bot that will do like and share on a fb posts, learning from python_bootcamp_2020. #DSCDSU #DeveloperStudentClubs #DSCPakistan #Python #Bot''')
share_box = ('<textarea class="sharerTextAreaArea mentions-input" name="comment" rows="3" id="share_msg_input" data-sigil="sharer-textarea m-textarea-input"></textarea>')
while True:
    capt_text = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR ,'div[data-sigil="marea"] div textarea')))
        
    if capt_text.get_attribute("outerHTML") != share_box:
        break

capt_text.send_keys(caption)

#post_clicking
post_button = driver.find_element_by_id("share_submit")
post_button.click()

