# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from selenium import webdriver
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

from ChatBot import ChatBot

from selenium.webdriver.common.keys import Keys



class App:
    def __init__(self):

        # 配信ページにアクセス
        self.rippon_url = 'https://17.live/live/9965553'
        self.candy_url = 'https://17.live/live/7304533'
        self.mayumin_url = 'https://17.live/live/7565751'
        self.sei_url = 'https://17.live/live/8424517'

        self.chatbot = ChatBot()

        self.streamer_name = ''

        self.not_sending_list = []

        self.log = Log()

        self.stranger = False


    def run(self):

        # Use a breakpoint in the code line below to debug your script.
        profile = webdriver.FirefoxProfile('/Users/seisuke/Library/Application Support/Firefox/Profiles/z7hdzbh3.default-release')

        self.browser = webdriver.Firefox(profile)
        self.browser.implicitly_wait(3)

        url_login = self.mayumin_url
        self.browser.get(url_login)

        time.sleep(15)
        print('配信ページにアクセスしました')

        # 配信者名取得
        self.streamer_name = self.browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > div.Header__HeaderWrapper-jLblBB.iLqSfq > div > div > div.StreamerInfo__InfoWrapper-ccXIXy.ipGXYO > div > div.StreamerInfo__Info-KToUN.bZQsAG > div > a').text
        print(self.streamer_name)

        # 要素を取得
        self.comment_textbox = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/form/div[3]/div[2]/textarea')

        # send_button = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/form/div[3]/div[3]/span/svg/path')
        self.send_button = self.browser.find_element_by_css_selector(
            '#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > form > div.SubmitChat__FlexTextBox-cncOkz.bQvNGn > div.SubmitChat__SubmitButton-kXYuum.kSQpDq > span > svg')


        #input_text = self.input()
        #comment_text = self.get_comment(input_text)

        #self.comment_textbox.clear()
        #self.comment_textbox.send_keys(comment_text)
        #self.send_button.click()

        #self.send_greeting()
        #self.send_greeting()


        comment_list = []

        i = 1
        text_index = 3

        last_comment_time = datetime.datetime.now()



        while True:
            #comment = browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(i) + ']/span[4]/span/span/text()')

            current_second = datetime.datetime.now().second
            if current_second == 30 or current_second == 31:
                self.not_sending_list = []

            try:
                #name = browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > div.ChatList__ChatListWrapper-jeEuyN.dGxlpL > ul > li:nth-child(' + str(i) + ') > span.ChatUserName__NameWrapper-fuwNzK.bYkGbh')
                #text = browser.find_element_by_css_selector('#app > div > div > div.MainLayout__Body-bzjWnr.jlypKq > section > main > div > header > aside > div > div.AsideContent-eTOXSN.ChatRoom__ChatRoomWrapper-cgNZhR.eNBJLm > div.ChatList__ChatListWrapper-jeEuyN.dGxlpL > ul > li:nth-child(' + str(i) + ') > span.Chat__ContentWrapper-krutWa.BGiJf')

                name_element = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(i) + ']/span[2]')
                text_element = self.browser.find_element_by_xpath('/html/body/div[1]/div/div/div[3]/section/main/div/header/aside/div/div[1]/div[1]/ul/li[' + str(i) + ']/span[' + str(text_index) + ']')

                name = name_element.text
                text = text_element.text


                if len(name) <= 0:

                    name = self.streamer_name

                # 新しいコメントを見つけた
                if len(text) > 0:

                    last_comment_time = datetime.datetime.now()
                    self.log.add(name, text, datetime.datetime.now())

                    print(text)

                    i += 1
                    text_index = 3

                    comment_to_send = ''
                    #comment_to_send = self.chatbot.get_reply(text)


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
                                for count in range(8):
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

                        if not self.stranger:
                            coin_str = text.split('を送りました (')[1].split(')')[0]
                            coin = int(coin_str)

                            #if name not in self.not_sending_list:

                                #if coin >= 1000:
                                    #comment_to_send = 'ｷﾀ━━━━(ﾟ∀ﾟ)━━━━!!'
                                    #self.not_sending_list.append(name)
                                #elif coin >= 100:
                                    #comment_to_send = '👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻👏🏻'
                                    #self.not_sending_list.append(name)

                                #for count in range(8):
                                    #comment_to_send += emoji.emojize(':clap:', use_aliases=True)




                    elif 'ライバーにいいねしました' in text:

                        if not self.stranger:
                            if 'せい.ai' not in name:
                                pass
                                #comment_to_send = self.streamer_name + 'の配信へようこそ！ゆっくりしていってね(っ´∀`)っ' + emoji.emojize(':tea:', use_aliases=True)
                                #comment_to_send = '@' + name + ' ' + comment_to_send


                    elif 'ライバーをフォローし始めました' in text:
                        pass
                        #if not self.stranger:
                            #comment_to_send = 'ナイスフォロー' + emoji.emojize(':clap:', use_aliases=True) + emoji.emojize(':clap:', use_aliases=True)
                           #comment_to_send = 'ナイスフォロー👏🏻👏🏻'
                            #comment_to_send = '@' + name + ' ' + comment_to_send


                    if len(comment_to_send) > 0:
                        comment_to_send = comment_to_send.replace('\n', '')
                        self.send_comment(comment_to_send)

                else:
                    text_index += 1

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

            time.sleep(0.1)


        time.sleep(0.5)

    def send_comment(self, message):

        print(message)

        self.comment_textbox.clear()

        self.comment_textbox.send_keys(message)

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


    # Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app = App()
    app.run()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
