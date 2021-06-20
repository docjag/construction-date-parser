# -*- coding: utf-8 -*-

'''
@Author: Sohel Mahmud
@Date: 
@Description: Parsing Date and address from a json file
'''

import re
import json
import locale
import datetime
from dateutil.parser import parse
from parse_countries import filter_country

###############################################################################################
###############################################################################################
###############################################################################################

months_short = 'Jan|J\u00e4n|Feb|Mar|M\u00e4|Apr|May|Mai|Jun|Jul|Aug|Sept|Oct|Okt|Nov|Dec|Dez'
months_long = 'January|J\u00e4nner|Januar|February|Februar|March|M\u00e4rch|April|May|Mai|June| \
               Juni|July|Juli|August|Sepember|October|Oktober|November|December|Dezember'
months = '(' + months_short + '|' + months_long + ')'
seps = '[\s\./\|-]'

days = '(0[1-9]|[12][0-9]|3[01])'
months_num = '(0[1-9]|1[012])'
years = '[12][7890]\d{2}'
# years_short = '\d{2}'
time_zone = '(T\d{2}:\d{2}:\d{2}Z)'

quart_num = '(Q[1-4])'
regex_quart_num = quart_num + '\s' + years

quart_roman = '(I|I[IV]|I{3})\.\sQuartal'
regex_quart_roman = quart_roman + '\s' + years

regx_full_month = days + seps + months + seps + years
regx_us = months_num + seps + days + seps + years

regx_month_year_long = months_num + seps + years

regx_day_month = days + seps + months
regx_month_name_year = months + '\.?' + seps + years

regx_iso_short = years + seps + months_num + seps + days
regx_iso_full = years + seps + months_num + seps + days + time_zone

regx_list = [regx_full_month,
             regx_iso_full,
             regx_iso_short,
             regx_us,
             regx_month_name_year,
             regx_month_year_long,
             regx_day_month,
             years
             ]

###############################################################################################
###############################################################################################
###############################################################################################

def last_day_month(any_day):

    # any_day = datetime.date(dts_dt.year, dts_dt.month, dts_dt.day)
    next_month = any_day.replace(day=28) +  datetime.timedelta(days=4)
    last_day = next_month - datetime.timedelta(days=next_month.day)

    return last_day.strftime('%Y-%m-%d')

###############################################################################################
###############################################################################################

def convert_date(dts):
    try:
        date_iso = parse(dts).strftime('%Y-%m-%d')

    except:
        locale.setlocale(locale.LC_TIME,'de_DE.utf-8')
        
        # Changing the Austrian 'J\u00e4nner' to German 'Januar'
        if 'J\u00e4nner' in dts:
            dts = dts.replace('J\u00e4nner', 'Januar')
        elif 'J\u00e4n' in dts:
            dts = dts.replace('J\u00e4n', 'Jan')

        try:
            date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')
        except:
            try:
                date_iso = datetime.datetime.strptime(dts, '%B %Y').strftime('%Y-%m-%d')
            except:
            	try:
            		date_iso = datetime.datetime.strptime(dts, '%d %B').strftime('%Y-%m-%d')
            	except:
            		date_iso = ''

    return date_iso


###############################################################################################
###############################################################################################

def convert_season_dates(item):

    season_dict = {'Fr\u00fchjahr': '20 March','Sommer': '21 April', 'Sp\u00e4tsommer':'August', \
                'Mitte':' 1 June', 'Herbst':'23 September','Ende': '31 December'}


    reg_year = re.search(r'[12][7890]\d{2}', item)

    date_iso = ''
    dt_year = ''

    if reg_year:
        dt_year = reg_year.group()
        for key, value in season_dict.items():
	        if key in item:
	            dts = value + ' ' + dt_year
	            date_iso = parse(dts).strftime('%Y-%m-%d')
	            break

    return dt_year, date_iso

###############################################################################################
###############################################################################################

def convert_quartal_dates(item):

    global regex_quart_num, regex_quart_roman

    q_dict = {'Q1':'01 Januar', 'Q2':'01 April','Q3':'01 Juli', 'Q4':'01 Oktober',\
              'I.':'01 Januar', 'II.':'01 April','III.':'01 Juli', 'IV.':'01 Oktober'}

    locale.setlocale(locale.LC_TIME,'de_DE.utf-8')

    q_num = re.search(regex_quart_num, item)
    q_roman = re.search(regex_quart_roman, item)
    reg_year = re.search(years, item)

    date_iso = ''
    dt_year = ''

    if reg_year:
        dt_year = reg_year.group()

    if q_num:
        q, dt_year = q_num.group().split()
        dts = q_dict[q] + ' ' + dt_year
        date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')

    elif q_roman:
        roman = q_roman.group().replace(' Quartal', '')
        q, dt_year = roman.split()
        dts = q_dict[q] + ' ' + dt_year
        date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')

    return dt_year, date_iso

###############################################################################################
###############################################################################################

def convert_ende_dates(item):
    global regx_month_name_year, years

    tmp = re.search(regx_month_name_year, item)

    locale.setlocale(locale.LC_TIME,'de_DE.utf-8')

    dts = ''
    
    if tmp:
        dts = tmp.group(0)
        dts = '31 ' + dts
        dts_dt = datetime.datetime.strptime(dts, '%d %B %Y')
        date_iso = last_day_month(dts_dt)

    else:
        dts = re.search(years, item).group(0)
        dts = '31 Dezember ' + dts
        date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')
    
    return dts, date_iso

###############################################################################################
###############################################################################################

def convert_anfang_dates(item):
    global regx_month_name_year, years

    tmp = re.search(regx_month_name_year, item)
    
    locale.setlocale(locale.LC_TIME,'de_DE.utf-8')

    dts = ''

    if tmp:
        dts = tmp.group(0)
        dts = '01 ' + dts
        date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')

    else:
        dts = re.search(years, item).group(0)
        dts = '01 Januar ' + dts
        date_iso = datetime.datetime.strptime(dts, '%d %B %Y').strftime('%Y-%m-%d')

    return dts, date_iso


###############################################################################################
###############################################################################################
###############################################################################################

def regx_date(item):

    date_iso = ''
    dts = ''

    for i in range(len(regx_list)):
        tmp = re.search(regx_list[i], item)
        if tmp:
            dts = tmp.group(0)                      
            date_iso = convert_date(dts)
            break

    return dts, date_iso

###############################################################################################
###############################################################################################

def rank_maker(addr, date_iso):

    if addr and date_iso: rank = 1
    
    else:
        if not addr and not date_iso: rank = 4
        elif not addr: rank = 2
        elif not date_iso: rank = 3

    return rank

###############################################################################################
###############################################################################################

def write_json(data):
	with open('parsing_challenge_cleaned.json', 'a') as fh:
		result = json.dumps(data, ensure_ascii=False)
		fh.write(result + '\n')


###############################################################################################
###############################################################################################
###############################################################################################

def main():
    with open('parsing_challenge.json','r') as fh_read:
        file_json = json.load(fh_read)
        
        count = 1
        dts = ''
        data = {}

        for item in file_json:
            item = item.strip()

            dts, quart = convert_quartal_dates(item)
            dts, season = convert_season_dates(item)

            if quart:
                date_iso = quart

            elif season:
                date_iso = season 

            elif 'Ende ' in item:
                dts, date_iso = convert_ende_dates(item)

            elif 'Anfang ' in item:
                dts, date_iso = convert_anfang_dates(item)

            else:
                dts, date_iso = regx_date(item)

            if dts:
                loc = item.find(dts)
                if loc > 0:
                    addr = item[:(loc-1)].strip().strip(',')
                elif loc == 0:
                    addr = ''
            else: 
                addr = item.strip()

            addr = filter_country(addr)

            data['addr'] = addr
            data['date_iso'] = date_iso
            data['rank'] = rank_maker(addr, date_iso)

            write_json(data)    
            print(data)
            
            count += 1


###############################################################################################
###############################################################################################
###############################################################################################

if __name__ == '__main__':
    main()