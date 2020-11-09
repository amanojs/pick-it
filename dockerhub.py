#!/usr/bin/env python
# coding: utf-8

# In[81]:


#get_ipython().system('pip install selenium')


# In[82]:


#get_ipython().system('pip install beautifulsoup4')


# In[ ]:





# In[97]:


from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
import os

os.system("cls")


# ## Dockerhubのログイン情報

# In[108]:


USER = "takashivue"
PASS = "keion1207"


# In[116]:

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-extensions')
browser = webdriver.Chrome(executable_path='C:\\Users\\takashi\\Desktop\\chromedriver_win32\\chromedriver.exe',options=options)
browser.implicitly_wait(3)
actions = ActionChains(browser)


# In[117]:


login_url = "https://id.docker.com/login/?next=%2Fid%2Foauth%2Fauthorize%2F%3Fclient_id%3D43f17c5f-9ba4-4f13-853d-9d0074e349a7%26nonce%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOjE2MDQ3Mzc4NTQsImlhdCI6MTYwNDczNzU1NCwicmZwIjoiOUtEamNCS2t1V1BpbHgtempYVzVVZz09IiwidGFyZ2V0X2xpbmtfdXJpIjoiaHR0cHM6Ly9odWIuZG9ja2VyLmNvbSJ9.qZqbojb31jRghcIM50CNDByCLj8TIAH3l5ZLQGPHtZI%26redirect_uri%3Dhttps%253A%252F%252Fhub.docker.com%252Fsso%252Fcallback%26response_type%3Dcode%26scope%3Dopenid%26state%3DeyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhdWQiOiI0M2YxN2M1Zi05YmE0LTRmMTMtODUzZC05ZDAwNzRlMzQ5YTciLCJleHAiOjE2MDQ3Mzc4NTQsImlhdCI6MTYwNDczNzU1NCwicmZwIjoiOUtEamNCS2t1V1BpbHgtempYVzVVZz09IiwidGFyZ2V0X2xpbmtfdXJpIjoiaHR0cHM6Ly9odWIuZG9ja2VyLmNvbSJ9.qZqbojb31jRghcIM50CNDByCLj8TIAH3l5ZLQGPHtZI"
browser.get(login_url)
time.sleep(0.5)
print("-> " + "\u001b[33mDockerHubのログインページにアクセス。\u001b[37m")


# In[118]:


element = browser.find_element_by_id("nw_username")
element.clear()
element.send_keys(USER)
time.sleep(1)
element = browser.find_element_by_id("nw_password")
element.clear()
element.send_keys(PASS)
print("-> " + "\u001b[33mログイン情報を入力。\u001b[37m")


# In[119]:


submit_btn = browser.find_element_by_id("nw_submit")
time.sleep(1)
submit_btn.click()
print("-> " + "\u001b[33mサブミットボタンをクリック。\u001b[37m")
time.sleep(2)
if browser.current_url != "https://hub.docker.com/":
    print("ログイン失敗")
    exit(-1)
else:
    print("-> " + "\u001b[33m認証成功 \u001b[37m")


# In[120]:


selector = "img[alt='Avatar']"
element = browser.find_element_by_css_selector(selector)
avatar_src = element.get_attribute("src")

options = webdriver.ChromeOptions()
options.add_argument("--window-size=400,400")
options.add_argument("--window-position=1000,100")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
img_browser = webdriver.Chrome(executable_path='C:\\Users\\takashi\\Desktop\\chromedriver_win32\\chromedriver.exe',options=options)
img_browser.implicitly_wait(1)
img_browser.get(avatar_src)
print("-> " + "\u001b[33mアバターアイコンを表示。\u001b[37m")


# In[121]:


element = browser.find_element_by_class_name("styles__username___oMG_s")
account = element.text
print("\n"  +"\u001b[32m" + "===========================================\n" + "|| ユーザ名: " + account + "\n===========================================\u001b[37m" + "\n")
time.sleep(1)

# In[122]:


list = browser.find_elements_by_css_selector("div[data-testid='repositoryList'] a")
print("\n" + account + "イメージ一覧")
print("\u001b[32m" + "===========================================\u001b[37m")
for item in list:
    href = item.get_attribute("href")
    print("|| ・" + "\u001b[32m" + href.replace("https://hub.docker.com/repository/docker/","") + "\u001b[37m")
    href = href.replace("https://hub.docker.com","")
    test = browser.find_element_by_css_selector("a[href='" + href + "']")
    actions.move_to_element(browser.find_element_by_css_selector("a[href='" + href + "']")).perform()
    actions.reset_actions()
    time.sleep(0.5)
print("\u001b[32m" + "===========================================\n\u001b[37m")


# In[ ]:
time.sleep(2)
#browser.close()
exit(0)


