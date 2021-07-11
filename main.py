# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import selenium
import time
import pandas
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import emoji
import random
import datetime
from Log import Log
from GUI import GUI

from ChatBot import ChatBot

from selenium.webdriver.common.keys import Keys



class App:
    def __init__(self, root):

        self.root = root

        gui = GUI(root, self)
        #gui.setup()

        # 配信ページにアクセス
        self.rippon_url = 'https://17.live/live/9965553'
        self.candy_url = 'https://17.live/live/7304533'
        self.mayumin_url = 'https://17.live/live/7565751'

        self.chatbot = ChatBot()
        self.streamer_name = ''
        self.not_sending_list = []
        self.already_welcomed_list = []
        self.log = Log()
        self.stranger = False

        self.i = 1
        self.text_index = 3


        #self.load();


    def load(self):

        # ログイン状態を継続するため、Firefoxのプロファイルを取得
        profile = webdriver.FirefoxProfile('/Users/seisuke/Library/Application Support/Firefox/Profiles/z7hdzbh3.default-release')

        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(3)

        # アクセスするライバーを指定
        url_login = self.mayumin_url

        self.browser.get(url_login)
        time.sleep(15)
        print('配信ページにアクセスしました')

        # ライバー名取得
        #self.streamer_name = self.browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > div.Header__HeaderWrapper-jLblBB.iLqSfq > div > div > div.StreamerInfo__InfoWrapper-ccXIXy.ipGXYO > div > div.StreamerInfo__Info-KToUN.bZQsAG > div > a').text
        self.streamer_name = "まゆみofficial"
        print(self.streamer_name)

        # 要素を取得
        #self.comment_textbox = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/form/div[3]/div[2]/textarea')
        self.comment_textbox = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/form/div[2]/div[2]/textarea')

        self.send_button = self.browser.find_element_by_css_selector(
            #'#app > div > div > div.Main__Body-eXRIOp.gkNETg > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > form > div.SubmitChat__FlexTextBox-cncOkz.bQvNGn > div.SubmitChat__SubmitButton-kXYuum.kSQpDq > span > svg'
            #'#app > div > div > div.Main__Body-eXRIOp.gkNETg > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > form > div.SubmitChat__FlexTextBox-cncOkz.bQvNGn > div.SubmitChat__SubmitButtonWrapper-jQNcMx.mqTGJ > span > svg > path'
            '#app > div > div > div.Main__Body-eXRIOp.gkNETg > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > form > div.SubmitChat__FlexTextBox-cncOkz.bQvNGn > div.SubmitChat__SubmitButtonWrapper-jQNcMx.mqTGJ > span > svg'
        )

    def loop(self):

        #input_text = self.input()
        #comment_text = self.get_comment(input_text)

        #self.comment_textbox.clear()
        #self.comment_textbox.send_keys(comment_text)
        #self.send_button.click()

        #self.send_greeting()
        #self.send_greeting()


        comment_list = []



        last_comment_time = datetime.datetime.now()



        #comment = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(i) + ']/span[4]/span/span/text()')

        current_second = datetime.datetime.now().second
        if current_second == 30 or current_second == 31:
            self.not_sending_list = []

        try:
            #name = browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > div.ChatList__ChatListWrapper-jeEuyN.dGxlpL > ul > li:nth-child(' + str(i) + ') > span.ChatUserName__NameWrapper-fuwNzK.bYkGbh')
            #text = browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > div.ChatList__ChatListWrapper-jeEuyN.dGxlpL > ul > li:nth-child(' + str(i) + ') > span.Chat__ContentWrapper-krutWa.BGiJf')

            name_element = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(self.i) + ']/span[2]')
            text_element = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(self.i) + ']/span[' + str(self.text_index) + ']')

            name = name_element.text
            text = text_element.text

            if len(name) <= 0:

                name = self.streamer_name

            # 新しいコメントを見つけた
            if len(text) > 0:

                last_comment_time = datetime.datetime.now()
                self.log.add(name, text, datetime.datetime.now())

                print(text)


                self.i += 1
                self.text_index = 3

                comment_to_send = ''
                #comment_to_send = self.chatbot.get_reply(text)

                #if 'せいofficial' not in name and name != self.streamer_name and name not in self.already_welcomed_list:
                    #comment_to_send = self.streamer_name + 'の配信へようこそ！ゆっくりしていってね(っ´∀`)っ' + emoji.emojize(':tea:',
                                                                                                        #use_aliases=True)
                    #comment_to_send = '@' + name + ' ' + comment_to_send

                    #self.already_welcomed_list.append(name)

                    #time.sleep(3)



                if '@せい.ai' in text and 'Pokeしました' not in text and len(name) > 0:

                    try:
                        comment_to_send = self.chatbot.get_reply(text)
                        comment_to_send = '@' + name + ' ' + comment_to_send

                    except Exception as e:
                        print(e)

                elif 'ライバーにプレゼントします' in text:
                    if not self.stranger:
                        coin_str = text.split('ライバーにプレゼントします (')[1].split(')')[0]
                        coin = int(coin_str)

                        if coin > 100 and name not in self.not_sending_list:
                            comment_to_send = 'ナイスギフト'
                            for count in range(5):
                                comment_to_send += emoji.emojize(':clap:', use_aliases=True)

                            self.not_sending_list.append(name)

                elif '春うららロシアン' in text:

                    if 'チューリップ' in text:
                        two_chara_str = 'チュー'
                    elif 'くしゃみ' in text:
                        two_chara_str = 'くしゃ'
                    else:
                        two_chara_str = text.split('を開けました， ')[1][:2]
                    comment_to_send = 'ナイ' + two_chara_str + '👏🏻👏🏻👏🏻👏🏻👏🏻'

                elif 'を送りました (' in text:

                    if not self.stranger and name not in 'せい':
                        coin_str = text.split('を送りました (')[1].split(')')[0]
                        coin = int(coin_str)


                        if name not in self.not_sending_list:

                            if coin >= 100:
                                comment_to_send = 'ナイスギフト👏🏻👏🏻👏🏻👏🏻👏🏻'
                                self.not_sending_list.append(name)

                            #for count in range(8):
                                #comment_to_send += emoji.emojize(':clap:', use_aliases=True)




                #elif 'ライバーにいいねしました' in text:

                    #if not self.stranger:
                        #if 'せいofficial' not in name and name not in self.already_welcomed_list:

                            #comment_to_send = self.streamer_name + 'の配信へようこそ！ゆっくりしていってね(っ´∀`)っ' + emoji.emojize(':tea:', use_aliases=True)
                            #comment_to_send = '@' + name + ' ' + comment_to_send

                            #self.already_welcomed_list.append(name)


                elif 'ライバーをフォローし始めました' in text:
                    pass
                    if not self.stranger:
                        #comment_to_send = 'ナイスフォロー' + emoji.emojize(':clap:', use_aliases=True) + emoji.emojize(':clap:', use_aliases=True)
                       comment_to_send = 'ナイスフォロー👏🏻👏🏻'
                        #comment_to_send = '@' + name + ' ' + comment_to_send


                if len(comment_to_send) > 0:
                    comment_to_send = comment_to_send.replace('\n', '')
                    self.send_comment(comment_to_send)

            else:
                self.text_index += 1

        except selenium.common.exceptions.NoSuchElementException:
            if (datetime.datetime.now() - last_comment_time).seconds > 35:
                input_comment = self.log.get_latest_comment()
                #comment_to_send = self.chatbot.get_reply(input_comment)
                #comment_to_send = comment_to_send.replace('\n', '')
                #print(repr(comment_to_send))
                #self.send_comment(comment_to_send)
                #last_comment_time = datetime.datetime.now()


        except Exception as e:
            print(e)

        self.root.after(10, self.loop)


    def send_period(self):
        str = '✨👶🏻🌟💓✨👶🏻🌟💓✨👶🏻🌟💓✨\n　　 無料ギフト2021人から貰うまで\n　　 終われまてんチャレンジ中です🙋🏻‍♀️‍\n　　　　️💐無料ギフトおひとつ💐\n　　　　よろしくお願いします🦭♡\n👶🏻🌟💓✨👶🏻🌟💓✨👶🏻🌟💓✨'

        self.send_comment_multi(str)
        self.root.after(60000, self.send_period)

    def send_comment(self, message):

        print(message)

        self.comment_textbox.clear()

        self.comment_textbox.send_keys(message)

        self.send_button.click()

    def send_comment_multi(self, message):

        self.comment_textbox.clear()

        for part in message.split('\n'):
            self.comment_textbox.send_keys(part)
            ActionChains(self.browser).key_down(Keys.SHIFT).key_down(Keys.ENTER).key_up(Keys.SHIFT).key_up(Keys.ENTER).perform()

        self.send_button.click()


    def send_by_count(self, message, count):
        for i in range(count):
            time.sleep(0.5)
            self.send_comment(message)

    def send_by_one_chara(self, message):
        for i in range(len(message)):
            time.sleep(0.5)
            self.send_comment(message[i])

    def send_greeting(self):
        tsuntsun = 'つんつん' + emoji.emojize(':point_right:', use_aliases=True)
        mokyumokyu = 'もきゅもきゅ' + emoji.emojize(':two_hearts:', use_aliases=True)
        list = ['こんばんは！', '初見です！', tsuntsun, '好きピ(๑ơ ₃ ơ)♥', mokyumokyu]
        for message in list:
            time.sleep(0.5)
            self.send_comment(message)

    def test(self):
        print('ボタンを押したよ')


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':

    root = tk.Tk()
    root.geometry('400x800')
    root.resizable(width=False, height=False)
    root.title('17 Live')

    app = App(root)
    #app.loop()
    #app.send_period()

    root.mainloop()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
