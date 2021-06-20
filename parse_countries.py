
#-*- coding: utf-8 -*-

'''
@Author: Sohel Mahmud
@Date: 04/02/2019
@Description: Parsing cities, countries from a string

'''


countries = ['Afghanistan', 'Albania', 'Algeria', 'America', 'Andorra', \
			 'Angola', 'Antigua and Barmuda', 'Argentina', 'Armenia', \
			 'Aruba', 'Australia', 'Austria', 'Azerbaijan', 'Bahamas', \
			 'Bahrain', 'Bangladesh', 'Barbados', 'Belarus', 'Belgium', \
			 'Belize', 'Benin', 'Bhutan', 'Bolivia', 'Bosnia and Herzegovina', \
			 'Bosnia Herzegovina', 'Botswana', 'Brazil', 'Brunei', 'Bulgaria', \
			 'Burkina', 'Burkina Faso', 'Burma', 'Burundi', 'Cape Verde', 'Cambodia', \
			 'Cameroon', 'Canada', 'Cape Verde', 'Central African Rep', 'Central African Republic', \
			 'Chad', 'Chile', 'China', 'Colombia', 'Comoros', 'Congo', 'Costa Rica', "Cote d'Ivoire", \
			 'Croatia', 'Cuba', 'Curacao', 'Cyprus', 'Czech Republic', 'Czechia', \
			 'Democratic Republic of the Congo', 'Denmark', 'Djibouti', 'Dominica',\
			 'Dominican Republic', 'East Timor', 'Ecuador', 'Egypt', 'El Salvador', \
			 'Equatorial Guinea', 'Eritrea', 'Estonia', 'Eswatini', 'Ethiopia', 'Fiji',\
			 'Finland', 'France', 'Gabon', 'Gambia', 'Gambia, The', 'Georgia', 'GER', 'Germany', \
			 'Ghana', 'Great Britain', 'Greece', 'Grenada', 'Guatemala', 'Guinea', 'Guinea-Bissau', \
			 'Guyana', 'Haiti', 'Holy See', 'Honduras', 'Hong Kong', 'Hungary', 'Iceland', 'India', \
			 'Indonesia', 'Iran', 'Iraq', 'Ireland', 'Israel', 'Italy', 'Ivory Coast', 'Jamaica', 'Japan', \
			 'Jordan', 'Kazakhstan', 'Kenya', 'Kiribati', 'North Korea', 'N. Korea', 'South Korea', 'S. Korea', \
			 'Kosovo', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Latvia', 'Lebanon', 'Lesotho', 'Liberia', 'Libya', \
			 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Macau', 'Macedonia', 'Madagascar', 'Malawi', \
			 'Malaysia', 'Maldives', 'Mali', 'Malta', 'Marshall Islands', 'Mauritania', 'Mauritius', \
			 'Mexico', 'Micronesia', 'Moldova', 'Monaco', 'Mongolia', 'Montenegro', 'Morocco', 'Mozambique', \
			 'Myanmar', 'Namibia', 'Nauru', 'Nepal', 'Netherlands', 'New Zealand', 'Nicaragua', 'Niger', 'Nigeria', \
			 'North Korea', 'Norway', 'Oman', 'Pakistan', 'Palau', 'Palestinian Territories', 'Panama', 'Papua New Guinea', \
			 'Paraguay', 'Peru', 'Philippines', 'Poland', 'Portugal', 'Qatar', 'Republic of the Congo', 'Romania', 'Russia', \
			 'Russian Federation', 'Rwanda', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent & the Grenadines', \
			 'Saint Vincent and the Grenadines', 'Samoa', 'San Marino', 'Sao Tome & Principe', 'Sao Tome and Principe', \
			 'Saudi Arabia', 'Senegal', 'Serbia', 'Seychelles', 'Sierra Leone', 'Singapore', 'Sint Maarten', 'Slovakia', \
			 'Slovenia', 'Solomon Islands', 'Somalia', 'South Africa', 'South Korea', 'South Sudan', 'Spain', 'Sri Lanka', \
			 'St Kitts & Nevis', 'St Lucia', 'Sudan', 'Suriname', 'Swaziland', 'Sweden', 'Switzerland', 'Syria', 'Taiwan', \
			 'Tajikistan', 'Tanzania', 'Thailand', 'The Bahamas', 'Timor-Leste', 'Togo', 'Tonga', 'Trinidad & Tobago', \
			 'Trinidad and Tobago', 'Tunisia', 'Turkey', 'Turkmenistan', 'Tuvalu', 'UAE', 'Uganda', 'UK', 'Ukraine', \
			 'United Arab Emirates', 'United Kingdom', 'United States', 'United States of America', 'Uruguay', 'USA', \
			 'Uzbekistan', 'Vanuatu', 'Vatican City', 'Venezuela', 'Vietnam', 'Yemen', 'Zambia', 'Zimbabwe', 'Zimbabwe']


def filter_country(string):
	global countries
	for country in countries:
		if country in string:
			if string[string.find(country) - 1] != ' ':
				string = string[:-len(country)] + ' ' + country
			else:
				return string

	return string


def parse_city_country(string):
	global countries

	for item in countries:
		if item in string:
			country = item
			city = string[:-len(item)]
		else:
			country = ''
			city = string

	return city, country