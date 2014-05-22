'''
@author: nouralkhatib
*This script is used for gathering information about Pinterest users using Pinterest API
*The information to be gather in this script is User, Followers and Following.
*Please NOTE that this code will not work properly in case Pinterest changed their API 
'''
#Importing libararies
import urllib2
import csv
import simplejson
import time 
from httplib import HTTP
import httplib


#Get information about users followers for a certain user
#Takes user's name and returns a list of follower
def get_info(name):
    try:
        list_followers=[]
        count_items=0
        counter=1

        url_sub_1='https://api.pinterest.com/v2/users/'
        url_sub_2='/followers/?page='
        url_sub3='&limit=100'
        flag=True
        item=""

        #Wait for secends to prevent Pinterest from blocking your IP
        while flag :
            time.sleep(7)
            url_sub=url_sub_1+(name)+url_sub_2+(str(counter))+url_sub3
            print url_sub

        #Call the restful API 
            pintersete_api_call = urllib2.urlopen(url_sub)
            content = pintersete_api_call.read()
            json = simplejson.loads(content)
            print json
         #Extract items from the retrived JSON

            for item in json['people']:

                item=item['username']
                list_followers.append(item)
                print item
            if item=="":

                #Retrun list of followers
                return list_followers
            
                count_items=count_items+1
            counter=counter+1
            item=""
            print counter
            
    except httplib.BadStatusLine:
        return list_followers        
    except urllib2.HTTPError:
        return list_followers    
    except ValueError:
        return list_followers     





if __name__ == '__main__':
    pass
try:
    myfile_node = open("node_5.csv",'wr')
    wr_node = csv.writer(myfile_node)
    myfile_edge = open("edge_5.csv",'wr')
    wr_edge = csv.writer(myfile_edge)
    list_1=[]
    list_2=[]
    list_3=[]
    list_4=[]
    number_nodes=1
    total_list=['zara']
    list_to_write=[]
    list_0=['zara']
    #for item in list_users:
        #item_list=[]
        #item_list.append(item)
        #wr_node.writerow(item_list)
    list_1=get_info(list_0[0])#105
        
    for target in list_1:#write il 105 (level -1)

        total_list.append(target)
        string=list_0[0]+","+target
        list_string=[]
        list_string.append(string)
        wr_edge.writerow(list_string)
        list_2=get_info(target) 
        for item in list_2:#child il 105 (level -2)
            total_list.append(item)
            list_3=get_info(item)  
            string=item+","+item
            list_string=[]
            list_string.append(string)
            wr_edge.writerow(list_string)
            for user in list_3:
                #total_list.append(user)
                string=item+","+user
                list_string=[]
                list_string.append(string)
                wr_edge.writerow(list_string)
    print total_list
    print len(total_list)
                
            
        
    print number_nodes    

except ValueError:
        pass
    
