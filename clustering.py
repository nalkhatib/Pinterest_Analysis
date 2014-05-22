'''
Created on Aug 4, 2012

@author: nouralkhatib
*This Script for ploting Clustering Information for a ceratin network.
*It reads a CSV file that has information about Nodes in a network and connecting Edges.
*Write clustering coeffecient values to a file.
'''
import csv
import networkx as nx

def get_clustering_coeffecient():

    #Read the file that has Nodes and Edges
    read=csv.reader(open('graph_3.csv','rb'))

    #File to write clustering_coeffecient 
    myfile = open("clustering.csv",'wr')
    wr = csv.writer(myfile)

    #Create graph
    g=nx.Graph()
    
    for row in read:
        g.add_node(row[0])
        g.add_node(row[1])
        g.add_edge(row[0],row[1])

        
    #calculate clustering_coeffecient   
    print(nx.average_clustering(g))
    clustering=nx.clustering(g)

    for key, value in clustering.items():
        list=[key,value]
        wr.writerow(list)
        
    #main Function
if __name__ == '__main__':
    get_clustering_coeffecient()
   
    
    pass
