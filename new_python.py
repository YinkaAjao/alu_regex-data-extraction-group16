import requests
import re

# Fetching data from LinkedIn api - 
url = "https://linkedin-data5.p.rapidapi.com/"

querystring = {"username":"satyanadella"}

headers = {
	"x-rapidapi-key": "93e69d4612mshb9882c64196bebap186e1ajsn4e3c4ca3b804",
	"x-rapidapi-host": "linkedin-data5.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)
# print(response.json())

# Adding mock data to the sample_text
mock_data = """
    Emails: ['test1@example.com', 'contact@company.com', 'info@domain.org']
    URLs: ['https://www.example.com', 'http://subdomain.example.org/page', 'https://sample.org']
    Phone Numbers: ['(123) 456-7890', '123-456-7890', '123.456.7890']
    Credit Cards: ['1234 5678 9012 3456', '1234-5678-9012-3456', '1234 5678 1234 9876']
    Times: ['14:30', '2:30 PM', '23:59']
    Currency: ['$19.99', '$1,234.56', '$500']
"""

# Combining LinkedIn response and mock data - this is because the linkedin data doesn't contain all the variables to check as the assignment request
sample_text = str(response.json()) + mock_data

# Regex patterns
email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
url_pattern = r'https?:\/\/(www\.)?[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}(\/[^\s]*)?'
phone_pattern = r'(\(\d{3}\)\s|\d{3}[-.])?\d{3}[-.]\d{4}'
credit_card_pattern = r'(\d{4}[-\s]?){3}\d{4}'
time_pattern = r'(?:[01]?\d|2[0-3]):[0-5]\d(?:\s?[APap][Mm])?'
currency_pattern = r'\$\d{1,3}(,\d{3})*(\.\d{2})?'
html_tag= r'\^<[a-zA-z\s{20,}\d>]'

# Extracting data
#emails = re.findall(email_pattern, sample_text)
#urls = re.findall(url_pattern, sample_text)
#phones = re.findall(phone_pattern, sample_text)
#credit_cards = re.findall(credit_card_pattern, sample_text)
#times = re.findall(time_pattern, sample_text)
#currencies = re.findall(currency_pattern, sample_text)

#Printing data
print("Emails:", emails)
print("URLs:", urls)
print("Phone Numbers:", phones)
print("Credit Cards:", credit_cards)
print("Times:", times)
print("Currency:", currencies)
