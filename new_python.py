# import requests
# import re

# url = "https://linkedin-data5.p.rapidapi.com/"

# querystring = {"username":"satyanadella"}

# headers = {
# 	"x-rapidapi-key": "93e69d4612mshb9882c64196bebap186e1ajsn4e3c4ca3b804",
# 	"x-rapidapi-host": "linkedin-data5.p.rapidapi.com"
# }

# response = requests.get(url, headers=headers, params=querystring)
# # print(response.json())

# sample_text =str(response.json())

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?:\/\/(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[^\s]*)?'
phone_pattern = r'(\(\d{3}\)\s|\d{3}[-.])?\d{3}[-.]\d{4}'
credit_card_pattern = r'(\d{4}[-\s]?){3}\d{4}'
time_pattern = r'(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?'
currency_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
html_tag= r'\^<[a-zA-z\s{20,}\d>]'

# Extracting data
# emails = re.findall(email_pattern, sample_text)
# urls = re.findall(url_pattern, sample_text)
# phones = re.findall(phone_pattern, sample_text)
# credit_cards = re.findall(credit_card_pattern, sample_text)
# times = re.findall(time_pattern, sample_text)
# currencies = re.findall(currency_pattern, sample_text)

# print("Emails:", emails)
# print("URLs:", urls)
# print("Phone Numbers:", phones)
# print("Credit Cards:", credit_cards)
# print("Times:", times)
# # print("Currency:", currencies)