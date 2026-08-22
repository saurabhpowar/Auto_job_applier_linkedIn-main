import undetected_chromedriver as uc  
from selenium.webdriver.chrome.options import Options  
import os  

options = uc.ChromeOptions()  
profile_dir = os.path.join(os.environ['LOCALAPPDATA'], 'Temp', 'uc_test_profile')  
os.makedirs(profile_dir, exist_ok=True)  
options.add_argument(f'--user-data-dir={profile_dir}')  

driver = uc.Chrome(options=options)  
driver.get("https://www.google.com")  
print(driver.title)  
driver.quit()  
