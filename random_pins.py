'''
Created on Jul 31, 2012
@author: nouralkhatib
---------------------------
This script to gather pins from Pinterest social network with their captions.
The output of this script is a csv file that contains random pins. 
The output file contains the following for each found pin:
*Pin Number.
*Flag (True/False) that indicates existing of a comments.
*Pin's image caption
'''
import csv
import urllib2
from random import randint
from BeautifulSoup import BeautifulSoup
import httplib

#Generate a Random Number to use it as random pin number
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)
    
#Try the random pin and check whethear this pin exist or not
#Geting information about the Pin is done by scraping the HTML
#If the Pin is exist ==> get the image caption
#Please note that the code might change a little in case Pinterest changer their website
def randomize_pin(filename,pin_number):
    myfile= open(filename,'wr')
    wr = csv.writer(myfile)
    
    list_pins=[]
    flag=True
    
    while flag:
        try:
            rand_pin=str(random_with_N_digits(18))
            
            url_1="http://pinterest.com/pin/"
            url=url_1 + (str(rand_pin))
            call_page = urllib2.urlopen(url)
            soup=BeautifulSoup(call_page)
            pin_html_page=str(soup)
            
            start_of_title=pin_html_page.find('<title>')
            start_comment=pin_html_page.find('/',start_of_title)
            end_comment=pin_html_page.find('</title>',start_comment)
            comment=pin_html_page[start_comment+1:end_comment]
            
            if len(comment)>2:
                comment_exist=True
            else :comment_exist=False
            
            pin=str(rand_pin)
            if list_pins.count(pin)==0:
                list_pins.append(pin)
                list_to_write=[pin,comment_exist,comment]
                wr.writerow(list_to_write)
           
            if len(list_pins)>=pin_number:
                flag=False
                
        except httplib.InvalidURL:
            continue
        except urllib2.HTTPError:
            continue
        except urllib2.URLError:
            continue

if __name__ == '__main__':


    #Replace FILENAME with the name of the csv file that you want to store pins in.
    #Replace PIN_NUMBER with integer number of the required pins to collect.  
    
    randomize_pin('FILENAME.csv', PIN_NUMBER)
    
    pass
