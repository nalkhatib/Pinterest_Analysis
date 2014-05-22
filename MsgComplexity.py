'''
Created on Jul 11, 2012
*This part of code is related to the study of Message Complexity.
*Process the datasets of both Twitter and Pinterest and filter them.
*Find Msg length in both chars unit and words unit.
*Detect URL and Hashtags in Msg.
*Detect abbv in Msg.
*Find the number of dictionary and non dictionary words in Msg.
*Find the frequency of each word mentioned in a dataset in another dataset
@author: nouralkhatib
'''
import csv
from topia.termextract import  tag
import string
import enchant
import urllib2
from BeautifulSoup import BeautifulSoup




#This function to process the dataset of message complexty part
def process_file(filename,outputfile):

    #Create file to write the result in

    myfile = open(outputfile,'wr')
    wr = csv.writer(myfile)

    
    term=tag.Tagger()
    term.initialize()

    #Open the file that has the messages (Ex, tweets or Pin caption) 
    reader = csv.reader(open(filename, "rb"))

    #read the messags one by one

    for row in reader:
     
        sentance= row[1].lower()#Convert to lower case

        if len(sentance)>0:
            #call remove_html_tags function to remove html tags like (&ampt)
            sentance=remove_html_tags(sentance)
            
            #Call detect_url method to detect the occurrence of URL in a message
            sentance_without_url,url_found=detect_url(sentance)

            #Call detect_hashtags method to detect the occurrence of Hashtags
            sentance_without_hash,hashtages=detect_hashtags(sentance_without_url)

            if len(sentance)>0:
                #Split the message into words
                token= term.tokenize(sentance)

                sentance_after_filter=""

                for word in token:
                    #Remove Punctuation from message
                    word= word.translate(string.maketrans("",""), string.punctuation)

                    if len(word)!=0:
                        sentance_after_filter=sentance_after_filter+word+" "

                #Filter the message from the words in list_to_remv
                list_to_remv=['http','href','target','blank','title','rel','search','pintag','nofollow','class','Pinterest']

                for i in list_to_remv:
                    if (sentance_after_filter.find (i)!=-1 and len(sentance_after_filter)>0):
                        sentance_after_filter.replace(i, '')
                 #Call get_char_length to get the length of the message in chars
                char_length= get_char_length(sentance_after_filter)
                

                 #Call get_words_length to get the length of the message in chars
                word_length= get_words_length(sentance_after_filter)

                url_detection= url_found

                if char_length>-1:

                    #Call spellcheck to get the dictionary, none dictionary words in the message
                    dict_words,list_dict_words,non_dict_words,list_non_dict_words=spellcheck(sentance_after_filter)

                    #Call detect_abbv to get the list of abbreveations in message
                    count_abbr, list_abbr=detect_abbv(sentance_after_filter)


                    #Write data into file
                    list_to_write=[sentance,sentance_after_filter,char_length,word_length,url_detection,hashtages,dict_words,list_dict_words,non_dict_words,list_non_dict_words]
                    wr.writerow(list_to_write)



 #function to remove the HTML tags                    
def remove_html_tags(sentance):

    amp=sentance.find('&amp;')!=-1
    if amp!=-1:
        end=sentance.find (' ',amp)
        sub=sentance[amp:end]
        sentance=sentance.replace(sub,' ')
    i=0
    
    while i<len(sentance):
        start=sentance.find(';&#',i)
        if start!=-1:
            end=sentance.find(';',start+1)
            sub=sentance[start:end]
            sentance=sentance.replace(sub,' ')
            i=end+1
        elif start==-1:
            start=sentance.find("&#",i)
            if start!=-1:
                end=sentance.find(';',start+1)
                sub=sentance[start:end]
                sentnace=sentance.replace(sub,' ')
                i=end+1
            else:
                i=len(sentance)
    #Return sentance after filtering            
    return sentance

 #function to detect URLs in messgae  
def detect_url(sentance):
    
    start=sentance.find('<a href="http:')
    if start!=-1:
        end=sentance.find("</a>")
        sub=sentance[start:end]
        sentance=sentance.replace(sub,' ')
        return sentance, True
            
    else:
        start=sentance.find("http")
        if start!=-1:
            end=sentance.find(" ",start)
            if end!=-1:
                sub=sentance[start:end]
            else: 
                sub=sentance[start:]
            return sentance.replace(sub,' '),True
        else:return sentance,False

  #function to calculate mesage length in chars                      
def get_char_length(sentance):
    return len(sentance)-1

  #function to calculate mesage length in words                      

def get_words_length(sentance):
    term=tag.Tagger()
    term.initialize()
    token= term.tokenize(sentance)
    return len(token)

 #function to detect Hashtags in messgae  

def detect_hashtags(sentance):
    hashtags=0
    i=0
    while i<len(sentance):
        start=sentance.find('<a href="/search?q',i)
        if start!=-1:
            end=sentance.find('</a>',start)
            sub=sentance[start:end+3]
            sentance=sentance.replace(sub,' ')
            hashtags=hashtags+1
            i=end+1
        elif start==-1:
            start=sentance.find('href="/search?q')
            if start!=-1:
                end=sentance.find("</a>",start)
                sub=sentance[start:end+3] 
                sentance=sentance.replace(sub,'')
                hashtags=hashtags+1
                i=end+1
            else:i=len(sentance)
    return sentance,hashtags
        
 #function to return dictionary and non dictionary words in messgae                 
def spellcheck(sentance):
    list_dict_words=[]
    list_non_dict_words=[]
    dict_words=0
    non_dict_words=0
    d = enchant.Dict("en_US")
    for word in sentance.split():
        if( d.check(word)==True):
            list_dict_words.append(word)
            dict_words=dict_words+1
        else:
            list_non_dict_words.append(word)
            non_dict_words=non_dict_words+1
       
    return dict_words,list_dict_words,non_dict_words,list_non_dict_words
    
#Get the number of hashtages in tweet
def get_hash_twitter(sentance):
    return sentance.count("#")

#Detect the occurrence of URL in tweet
def get_url_twitter(sentance):
    list=sentance.split()
    for word in sentance:
        if len(word)>9 and (word.find('.') !=-1 or word.find('/')!=-1):
            try:
                urllib2.urlopen(word)
                return True
            except IOError:
                continue
#Process tweets and find message complexty measures ..similar to process_file function           
def tweets_text_processing():
    myfile = open("twitter_analysis_txt_length.csv",'wr')
    wn = csv.writer(myfile)
    term=tag.Tagger()
    term.initialize()
    #add twitter dataset
    file = open("tweets5.txt")
    i=0
    while 1:
        i=i+1
        print i
        line = file.readline()
        if(line.count("\u")>0):
            continue
        print line
        text_start=line.find("text")
        text_end=line.find("in_reply_to")
        tweet=line[text_start+7:text_end-3].lower()
        hash_start=line.find('hashtags":')
        hash_end=line.find('"user_')
        hash=line[hash_start+10:hash_end-1]
        if len(hash)==2:
            hash_val=False
        else:hash_val=True
        url_start=line.find('"urls":')
        url_end=line.find('}',url_start)
        url=line[url_start+7:url_end]
        if len(url)==2:
            url_val=False
        else:url_val=True
        words=get_words_length(tweet)
        chars=get_char_length(tweet)
        if len(tweet)>0:
                token= term.tokenize(tweet)
                tweet_after_filter=""
                for word in token:
                    word= word.translate(string.maketrans("",""), string.punctuation)
                    if len(word)!=0:
                        tweet_after_filter=tweet_after_filter+word+" "
                print tweet_after_filter
                char_length= get_char_length(tweet_after_filter)
                word_length= get_words_length(tweet_after_filter)
                if char_length>-1:
                    dict_words,list_dict_words,non_dict_words,list_non_dict_words=spellcheck(tweet_after_filter)
                    #count_abbr, list_abbr=detect_abbv(tweet_after_filter)
                    list_to_write=[tweet,tweet_after_filter,char_length,word_length,url_val,hash_val,dict_words,list_dict_words,non_dict_words,list_non_dict_words]
                    wn.writerow(list_to_write)
        
        
        if not line:
            break
#Compare the occurrence of words in twitter dataset into pinterest dataset and the opposite
def word_freq_comparasion():
    myfile1 = open("twitter_pinterest_limited.csv",'wr')
    wr1 = csv.writer(myfile1)
    myfile2 = open("pinterest_twitter_limited.csv",'wr')
    wr2= csv.writer(myfile2)
    myfile3 = open("words_found_in_both.csv",'wr')
    wr3 = csv.writer(myfile3)
    twitter_reader=csv.reader(open('twitter_analysis_txt_length.csv','rb'))
    pintrest_reader=csv.reader(open('pinterest_analysis_txt_length.csv','rb'))
    list_twitter=[]
    list_pinterest=[]
    count_t=0
    count_p=0
   
    for row in twitter_reader :
        temp=[]
        len=0
        temp=row[1].split()
        
        for word in temp:
            if count_t<65783:
                list_twitter.append(word.lower())
                count_t=count_t+1
        
                
    for row in pintrest_reader:
    
        temp=[]
        len=0
        temp=row[1].split()
        for word in temp:
            if count_p<65783:
                list_pinterest.append(word.lower())
                count_p=count_p+1
            
   
  
    list_com_twitter_to_pin=[]
    list_com_pin_to_twitter=[]

    for word in list_twitter:
        num_word_twitter=0
        num_word_pinterest=0
        final_num=0
        num_word_twitter=list_twitter.count(word)
        num_word_pinterest=(list_pinterest.count(word))
        if num_word_pinterest>0:
            list=[word]
            wr3.writerow(list)
        final_num=num_word_twitter-num_word_pinterest
        list_com_twitter_to_pin=[word,final_num]
        wr1.writerow(list_com_twitter_to_pin)
        
    for word in list_pinterest:
        num_word_twitter=0
        num_word_pinterest=0
        final_num=0
        num_word_twitter=list_twitter.count(word)
        num_word_pinterest=(list_pinterest.count(word))
        if num_word_twitter>0:
            list=[word]
            wr3.writerow(list)
        final_num=num_word_twitter-num_word_pinterest
        list_com_pin_to_twitter=[word,final_num]
        wr2.writerow(list_com_pin_to_twitter)
    print count_p
    print  count_t
       
#Function to detect abbreviations using API            
def detect_abbv(sentance):
    count=0
    list_abbr=[]
    for word in sentance.split():
        url_1="http://www.stands4.com/services/v2/abbr.php?uid=2249&tokenid=Kiq1M2B0gop1qJz&categoryid=CHAT&term="
        url=url_1+word
        call=urllib2.urlopen(url)
        data_abbr=BeautifulSoup(call)
        abbr=str(data_abbr)
        if len(abbr)!=59:
            flag=True
        else:
            url_1="http://www.stands4.com/services/v2/abbr.php?uid=2249&tokenid=Kiq1M2B0gop1qJz&categoryid=twitter&term="
            url=url_1+word
            call=urllib2.urlopen(url)
            data_abbr=BeautifulSoup(call)
            abbr=str(data_abbr)
            if len(abbr)==59:
                flag=False
        if flag:
            count=count+1
            list_abbr.append(word)
    return count,list_abbr            

     
     
#CHANGE THE NAME OF INPUTFILE and OUTPUTFILE        
               
def main():
    
    process_file(INPUTFILE, OUTPUTFILE)
    #tweets_text_processing()
    word_freq_comparasion()
  
if __name__ == '__main__':
    main()
