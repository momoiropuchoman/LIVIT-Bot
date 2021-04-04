import requests
import pya3rt
import json
import random
from enum import Enum, auto

class ChatBot:

	def __init__(self):

		APIKEY = '602943fc9e819'
		self.chaplus_url = f'https://www.chaplus.jp/v1/chat?apikey={APIKEY}'

		# 特別に返信するメッセージリストを準備
		self.special_responses = []
		self.special_responses.append(SpecialResponse('konnichiwa.txt'))
		self.special_responses.append(SpecialResponse('konbanwa.txt'))

	def get_reply(self, input_message):

		# 特別に返信するものがあるかここで探す
		for special_response in self.special_responses:
			result, output = special_response.get_output(input_message)
			if result:
				return output

		# リクエストに必要なパラメーター
		headers = {'content-type': 'text/json'}
		payload = {'utterance': input_message}

		# APIを叩く
		response = requests.post(url=self.chaplus_url, headers=headers, data=json.dumps(payload))

		# 最適と思われるレスポンスを抽出
		try:
			reply = response.json()['bestResponse']['utterance']
		except:
			reply = '日本語をもっと勉強なさってください'

		return reply


class SpecialResponseType(Enum):

	INCLUDE = auto()
	PERFECT_MATCH = auto()


class SpecialResponse:

	def __init__(self, file_name):

		self.first_string = ''
		self.final_string = ''
		self.type = SpecialResponseType.INCLUDE
		self.input_messages = []
		self.output_messages = []

		self.set_from_file(file_name)


	def set_from_file(self, file_name):

		file = open(file_name, 'r')
		whole_str = file.read()
		file.close()

		special_response = whole_str.split('\n\n')

		if len(special_response) >= 4:

			if special_response[0] == 'INCLUDE':
				self.type = SpecialResponseType.INCLUDE
			elif special_response[0] == 'PERFECT_MATCH':
				self.type = SpecialResponseType.PERFECT_MATCH

			self.input_messages = special_response[1].split('\n')
			self.output_messages = special_response[2].split('\n')

			options = special_response[3].split('\n')

			if len(options) >= 2:

				if options[0] != 'None':
					self.first_string = options[0]
				if options[1] != 'None':
					self.final_string = options[1]

			else:
				print('Incorrect Options')

		else:
			print('Incorrect Data Format')

		print(self.input_messages)
		print(self.output_messages)
		print(str(len(self.input_messages)))

	def set_from_args(self, input_messages, output_messages):

		self.input_messages = input_messages
		self.output_messages = output_messages

	def get_output(self, input_message):

		output = ''

		if self.type == SpecialResponseType.INCLUDE:
			has_found = self.including_candidate_exists(input_message)
		elif self.type == SpecialResponseType.PERFECT_MATCH:
			has_found = self.perfect_matching_candidate_exists(input_message)

		if has_found:
			output = self.get_output_randomly()

		return has_found, self.first_string + output + self.final_string

	def including_candidate_exists(self, input_message):

		for i in range(len(self.input_messages)-1):

			if self.input_messages[i] in input_message:
				return True

		return False

	def perfect_matching_candidate_exists(self, input_message):

		for candidate in self.input_messages:
			if input_message == candidate:
				return True

		return False

	def get_output_randomly(self):

		if len(self.output_messages) > 0:

			index = random.randint(0, len(self.output_messages))
			return self.output_messages[index]

		else:

			return '生きていると色々ありますよね'
