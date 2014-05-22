pinterest-breakdown
===================
Overview
--------

A careful analysis of the features of the Pinterest social platform and community. 
This research code is sperate into three main topics:

* Message Complexity.
* Degree Distribution.
* Popularity.

Bellow is the description and the part of code associated with each part:

Message Complexity
==================

 This part is for studying the complexity of image captions (Pin caption). It calculates the following
matrices:

* Message length in characters unit.
* Message length in words unit.
* URL occurrence.
* Hashtag occurrence.
* Number of dictionary and non dictionary words.
* Number of abbreviations.

How to use this code?
---------------------
- Go to MsgComplexity.py
- Change INPUTFILE and OUTPUT file to the CSV files that you want.
- Run the code. 
- The resulted CSV file will have the following structure:
[message],[message_after_removing_punctuation],[URL],[Hahtags],[numberOfDictionaryWords],{ListOfDictionaryWords],[numberOfNonDictionaryWords],[ListOfNonDictionaryWords]


Degree Distribution
===================

 This part is for gathering data and measuring Degree Distribution in Pinterest. Due to the limitaion of their API,
 we prefered to use HTML scraping. the mechanism of collecting the data is randomized to overcome the problem of preferential attachment. 
 We pick an random PIn and then get the Pinner information.

ow to use this code?
---------------------
- Go to degree_without_api.py
- Change FILENAME to the CSV file you want to record the results.
- Run the code. 
- The resulted CSV file will have the following structure:
[username],[outdegree],[indegree],[totalDegree]

Popularity
===================

 This part is for studying the relationship between popular user accounts and their spcialty and gender.
 Note: This code is designed specially for analysing a test publish on AMT (amazon mechanical turk). Each test is done by
 three requesters. We only take a result in consideration if at least 2 requesters agreed on it.
 
 ow to use this code?
---------------------
- Go to popularity.py
- Run the code. 


 
 




