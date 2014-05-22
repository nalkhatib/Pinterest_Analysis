'''
*This script is related to studying user popularity and user specialty in both Twitter and Pinterest
*This script is related to studying user popularity and user gender in both Twitter and Pinterest
@author: nouralkhatib
'''


import csv

#Find the Distribution of Gender in Popular accounts
def get_gender():
   #Create a file to write gender info for pinterest
   gender_pinterest = open('geneder_pinterest.csv','wr')
    gdp = csv.writer(gender_pinterest)
    #Create a file to write gender info for twitter
    gender_twitter = open('geneder_twitter.csv','wr')
    gdt = csv.writer(gender_twitter)
    
    read=csv.reader(open('popularity_twitter_pinterest.csv','rb'))
    counter=0
    #three list , one for each requester answers
    list_tester1=[]
    list_tester2=[]
    list_tester3=[]
    
    counter_testers=1
   
   #Read gender infor from the dataset of AMT test
    for row in read:
        counter=counter+1
        print counter
        #Read answers of each HIT
        gender1=row[94]
        gender2=row[95]
        gender3=row[96]
        gender4=row[97]
        gender5=row[98]
        gender6=row[99]
        gender7=row[100]
        gender8=row[90]
        gender9=row[91]
        gender10=row[92]
        
        if counter_testers==1:
            list_tester1=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10] 
            counter_testers=counter_testers+1     
            continue   

        if counter_testers==2:
            list_tester2=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10]
            counter_testers=counter_testers+1     
            continue  
        
        if counter_testers==3:
            counter_testers=1
            list_tester3=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10] 
            print list_tester1
            print list_tester2
            print list_tester3
            i=0
            
            #Comapre the answers of the three requesters. 
            #For more accuracy, we consider onlu answers that at least two requesters agreed on.
            while i<10:
                compare1=False
                compare2=False
                compare3=False
                if (list_tester1[i]==list_tester2[i]):
                    compare1=True
                if (list_tester1==list_tester3[i]):
                    compare2=True
                if (list_tester2[i]==list_tester3[i]):
                    compare3=True
                    
                if counter<129: #Pinterest dataset is before row 129
                    if (compare1):
                        gdp.writerow(list_tester1[i])
                    elif (compare2):
                        gdp.writerow(list_tester1[i])
                    elif(compare3):
                        gdp.writerow(list_tester3[i])
                    else:
                        print "None"
                if counter>=129: #Twitter dataset is after row 129
                    if (compare1):
                        gdt.writerow(list_tester1[i])
                    elif (compare2):
                        gdt.writerow(list_tester1[i])
                    elif(compare3):
                        gdt.writerow(list_tester3[i])
                    else:
                        print "None2"
                i=i+1

#Calculate the distribution of gender in Twitter and Pinterest datasets
def cal_gender():
    read_twitter=csv.reader(open('geneder_twitter.csv','rb'))
    read_pinterest=csv.reader(open('geneder_pinterest.csv','rb'))
    list_pinterest=[]
    list_twitter=[]
    counter=1
    
    for row in read_pinterest:
        print row[0]
        list_pinterest.append(row[0])
        
    for row in read_twitter:
        if counter<=len(read_pinterest):
            list_twitter.append(row[0])
            counter=counter+1
    
    print("Pinterest")
    #Persentage of Male in popular users in pinterest dataset
    print(list_pinterest.count("1")/len(list_pinterest)) 
    #Persentage of Female in popular users in pinterest dataset
    print(list_pinterest.count("2")/len(list_pinterest))
    #Persentage of Unknown in popular users in pinterest dataset
    print(list_pinterest.count("3")/len(list_pinterest))
    
    print("Twitter")   
    #Persentage of Male in popular users in twitter dataset
    print(list_twitter.count("1")/len(list_twitter))
    #Persentage of Female in popular users in twitter dataset
    print(list_twitter.count("2")/len(list_twitter))
    #Persentage of Unknown in popular users in twitter dataset
    print(list_twitter.count("3")/len(list_twitter))

#Find the Distribution of Specialty in Popular accounts
def get_specialty():
    spec_pinterest = open('specialty_pinterest.csv','wr')
    spp = csv.writer(spec_pinterest)
    spec_twitter = open('specialty_twitter.csv','wr')
    spt = csv.writer(spec_twitter)
    read=csv.reader(open('popularity_twitter_pinterest.csv','rb'))
    counter=0
    
    list_tester1=[]
    list_tester2=[]
    list_tester3=[]
    counter_testers=1
   
    for row in read:
        counter=counter+1
        print counter
        #Read answers of each HIT
        gender1=row[83]
        gender2=row[84]
        gender3=row[85]
        gender4=row[86]
        gender5=row[87]
        gender6=row[88]
        gender7=row[89]
        gender8=row[79]
        gender9=row[80]
        gender10=row[81]
        
        if counter_testers==1:
            list_tester1=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10] 
            counter_testers=counter_testers+1     
            continue   

        if counter_testers==2:
            list_tester2=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10]
            counter_testers=counter_testers+1     
            continue  
        
        if counter_testers==3:
            counter_testers=1
            list_tester3=[gender1,gender2,gender3,gender4,gender5,gender6,gender7,gender8,gender9,gender10] 
            #three list , one for each requester answers
            print list_tester1
            print list_tester2
            print list_tester3
            i=0
            while i<10:
                compare1=False
                compare2=False
                compare3=False
                if (list_tester1[i]==list_tester2[i]):
                    compare1=True
                if (list_tester1==list_tester3[i]):
                    compare2=True
                if (list_tester2[i]==list_tester3[i]):
                    compare3=True
                    
                if counter<129:#Pinterest dataset is before row 129
                    if (compare1):
                        list=[list_tester1[i]]
                        spp.writerow(list)
                    elif (compare2):
                        list=[list_tester1[i]]                        
                        spp.writerow(list)
                    elif(compare3):
                        list=[list_tester3[i]]                        
                        spp.writerow(list)
                    else:
                        print "None"
                if counter>=129:#Twitter dataset is before row 129
                    if (compare1):
                        list=[list_tester1[i]]                        
                        spt.writerow(list)
                    elif (compare2):
                        list=[list_tester1[i]]                        
                        spt.writerow(list)
                    elif(compare3):
                        list=[list_tester3[i]]                    
                        spt.writerow(list)
                    else:
                        print "None2"
                i=i+1    

def cal_specialty():
    read_twitter=csv.reader(open('specialty_twitter.csv','rb'))
    read_pinterest=csv.reader(open('specialty_pinterest.csv','rb'))
    list_pinterest=[]
    list_twitter=[]
    counter=1
    for row in read_pinterest:
        list_pinterest.append(row[0])
        
    for row in read_twitter:
        if counter<=len(list_pinterest):
            list_twitter.append(row[0])
            counter=counter+1
            
    print("Pinterest Specialty")
    #Persentage of Technologists in popular users in pinterest dataset
    print(float(list_pinterest.count("1"))/len(list_pinterest))
    #Persentage of Politicians in popular users in pinterest dataset   
    print(float(list_pinterest.count("2"))/len(list_pinterest))
    #Persentage of Performers in popular users in pinterest dataset   
    print(float(list_pinterest.count("3"))/len(list_pinterest))
    #Persentage of Painter/DYI in popular users in pinterest dataset   
    print(float(list_pinterest.count("4"))/len(list_pinterest))
    #Persentage of Photographers in popular users in pinterest dataset   
    print(float(list_pinterest.count("5"))/len(list_pinterest))
    #Persentage of Designers in popular users in pinterest dataset   
    print(float(list_pinterest.count("6"))/len(list_pinterest))
    #Persentage of Healthcare Experts in popular users in pinterest dataset   
    print(float(list_pinterest.count("7"))/len(list_pinterest))
    #Persentage of Fashion Experts in popular users in pinterest dataset   
    print(float(list_pinterest.count("8"))/len(list_pinterest))
    #Persentage of Food Chefs in popular users in pinterest dataset   
    print(float(list_pinterest.count("9"))/len(list_pinterest))
    #Persentage of Journalist/Bloggers in popular users in pinterest dataset   
    print(float(list_pinterest.count("10"))/len(list_pinterest))
    #Persentage of Business Companies in popular users in pinterest dataset   
    print(float(list_pinterest.count("11"))/len(list_pinterest))
    #Persentage of Organization - news feed in popular users in pinterest dataset   
    print(float(list_pinterest.count("12"))/len(list_pinterest))
    #Persentage of Other in popular users in pinterest dataset   
    print(float(list_pinterest.count("13"))/len(list_pinterest))
    #Persentage of Unkown in popular users in pinterest dataset   
    print(float(list_pinterest.count("14"))/len(list_pinterest))


    
    print("Twitter Specialty")     
    #Persentage of Technologists in popular users in twitter dataset
    print(float(list_twitter.count("1"))/len(list_twitter))
    #Persentage of Politicians in popular users in twitter dataset   
    print(float(list_twitter.count("2"))/len(list_twitter))
    #Persentage of Performers in popular users in twitter dataset   
    print(float(list_twitter.count("3"))/len(list_twitter))
    #Persentage of Painter/DYI in popular users in twitter dataset   
    print(float(list_twitter.count("4"))/len(list_twitter))
    #Persentage of Photographers in popular users in twitter dataset   
    print(float(list_twitter.count("5"))/len(list_twitter))
    #Persentage of Designers in popular users in twitter dataset   
    print(float(list_twitter.count("6"))/len(list_twitter))
    #Persentage of Healthcare Experts in popular users in twitter dataset   
    print(float(list_twitter.count("7"))/len(list_twitter))
    #Persentage of Fashion Experts in popular users in twitter dataset   
    print(float(list_twitter.count("8"))/len(list_twitter))
    #Persentage of Food Chefs in popular users in twitter dataset   
    print(float(list_twitter.count("9"))/len(list_twitter))
    #Persentage of Journalist/Bloggers in popular users in twitter dataset   
    print(float(list_twitter.count("10"))/len(list_twitter))
    #Persentage of Business Companies in popular users in twitter dataset   
    print(float(list_twitter.count("11"))/len(list_twitter))
    #Persentage of Organization - news feed in popular users in twitter dataset   
    print(float(list_twitter.count("12"))/len(list_twitter))
    #Persentage of Other in popular users in twitter dataset   
    print(float(list_twitter.count("13"))/len(list_twitter))
    #Persentage of Unkown in popular users in twitter dataset   
    print(float(list_twitter.count("14"))/len(list_twitter))
             

            
              
        
if __name__ == '__main__':
    get_gender()
    cal_gender()
    get_specialty()
    cal_specialty()
    
    pass