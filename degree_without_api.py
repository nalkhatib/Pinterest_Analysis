'''
Created on Jul 29, 2012
This script is for collecting dataset for degree distribution part.
This script is for collecting the number of followers and following from ransom users users in pinterest.
Please NOTE that this code might change a little in case Pinterest changed their HTML layout.
@author: nouralkhatib
'''
import csv
from BeautifulSoup import BeautifulSoup
import urllib2
from urllib2 import HTTPError
import time

#Methof for collecting indegree (followers) and out degree (following) in pinterest
def get_degree(name):
    
    follower=0
    following=0
    sub="http://pinterest.com/"
    url=sub+name
    #call the HTML page
    page=urllib2.urlopen(url)
    soup=BeautifulSoup(page)
    html_str=str(soup)
    length_str=len(html_str)
    #start of the number of following HTML part
    following_s=html_str.find('following" content="')
    #End of the number of following HTML part
    following_e=html_str.find('" />',following_s)
    #start of the number of followers HTML part
    follower_s=html_str.find('followers" content="')
    #end of the number of followers HTML part
    follower_e=html_str.find('" />',follower_s)
    #substring following number
    following=html_str[following_s+20:following_e]
    #substring followers number
    follower=html_str[follower_s+20:follower_e]
    print following
    print follower
    #Calculate degree=following+followers
    degree=float(following)+float(follower)
  

        except urllib2.HTTPError:
            time.sleep(50)
            continue
        except ValueError:
            continue

    return follower,following,degree
  

#Generate a Random Number to use it as random pin number
def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

def randomize_pin(pin_number):
   
    try:
        rand_pin=str(random_with_N_digits(18))     
        url_1="http://pinterest.com/pin/"
        url=url_1 + (str(rand_pin))
        call_page = urllib2.urlopen(url)
        soup=BeautifulSoup(call_page)
        pin_html_page=str(soup)
            
        #start of the person (user) name in HTML part
        person_s=html_str.find('pinner" content="http://pinterest.com/')
        #end of the person (user) name in HTML part
        person_e=html_str.find('" />',person_s)
        person=pin_html_page[person_s+(len(person_s)):person_e]
        return person    
                            
        except httplib.InvalidURL:
            continue
        except urllib2.HTTPError:
            continue
        except urllib2.URLError:
            continue

    

 
    #Change the name of FILENAME 
    #Use CSV file type

if __name__=='__main__':
    myfile = open(FILENAME,'wr')
    wr = csv.writer(myfile)
   
   per=[]
    
    #By Defult it collects 1000 users degree info..
    #Change 1000 to the number of users you want.
   while True and len(per)<=1000:
       per.append(randomize_pin())
       
   
   for person in per:
        follower,following,degree=get_degree(person)
        print person
        list=[person,following,follower,degree]
        wr.writerow(list)
 
                       
    
    

    

