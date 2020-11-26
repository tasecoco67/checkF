from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time
import setting

driver = webdriver.Chrome()

def twfcheck():
    driver.get(setting.TWR)
    time.sleep(5)
    twf = driver.find_element_by_xpath(r'//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div/div[1]/div/div[5]/div[2]/a/span[1]/span').text
    return twf;
#twfcheck();

def infcheck():
    driver.get('https://www.instagram.com/kaiminasse/?hl=ja')
    time.sleep(5);
    inf=driver.find_element_by_xpath(r'//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a/span').text
    return inf;
#infcheck()

def ntfcheck():
    driver.get(setting.NUR)
    time.sleep(5)
    ntf=driver.find_element_by_xpath(r'//*[@id="__layout"]/div/main/header/div/div[2]/div/div[2]/div[2]/div/div/div[1]/a[2]/span[1]').text
    return ntf;

def ntvcheck():
    driver.get(setting.NUR2)
    driver.find_element_by_name('login').send_keys(setting.MAIL)
    driver.find_element_by_name('password').send_keys(setting.PSW)
    #ログインボタンをクリック
    driver.find_element_by_xpath(r'/html/body/main/login/div/section/div/div/form/button').click()
    time.sleep(4);
    driver.get(setting.NUR3)
    time.sleep(3);
    driver.find_element_by_xpath(r'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div/div[1]/div[1]/ul/li[3]/button').click()
    time.sleep(3)
    nv = driver.find_element_by_xpath(r'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div/div[2]/div[1]/div[2]').text
    ng = driver.find_element_by_xpath(r'//*[@id="__layout"]/div/div[2]/div[2]/div/div/div/div[2]/div[3]/div[2]').text
    return nv,ng

#print(ntvcheck()[0])

def writegs():
    import gspread
    import json
    #ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
    from oauth2client.service_account import ServiceAccountCredentials

    #2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
    scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']

    credential = {
  "type": "service_account",
  "project_id": "snsfollow",
  "private_key_id": setting.PKI,
  "private_key": "-----BEGIN PRIVATE KEY-----\n"+setting.PK+"\n-----END PRIVATE KEY-----\n",
  "client_email": setting.CEMAIL,
  "client_id": setting.CID,
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": setting.CCU
}


    credentials = ServiceAccountCredentials.from_json_keyfile_dict(credential, scope)

    gc = gspread.authorize(credentials)

    #共有設定したスプレッドシートのシート1を開く
    workbook = gc.open_by_key(setting.SPK)
    worksheet1 = workbook.worksheet('insta')
    worksheet2 = workbook.worksheet('note')
    worksheet3 = workbook.worksheet('twitter')
    worksheet1.update_acell("I2", infcheck())
    worksheet2.update_acell("G2", ntfcheck())
    m = ntvcheck()
    worksheet2.update_acell("F5", m[0])
    worksheet2.update_acell("G5", m[1])
    worksheet3.update_acell("G2", twfcheck())
writegs();
