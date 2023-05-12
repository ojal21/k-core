#%%
from collections import defaultdict
import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
import random
import copy

def matrix_to_list(matrix,n):
        
    adjList=defaultdict(list)
    for i in range(n):
        for j in range(n):
           
            if matrix[i][j]!=0 :
                
                adjList[i].append(j)
    return adjList

def graph_nx(matrix):
    graph_nx = nx.Graph()
    for i in range(0,27):
        graph_nx.add_node(i)
    for i in range(0,27):
        for j in range(0,27):
            if i<=j and matrix[i][j]==1:
                graph_nx.add_edge(i,j)    
    return graph_nx

def edge_removal(graph_nx_org):
    edge_remove=random.choice(list(graph_nx_org.edges()))
    graph_nx_org.remove_edge(edge_remove[0],edge_remove[1])
    graph_nx_list = list(graph_nx_org.edges())
    
    new_edge_list=[[0 for _ in range(27)] for _ in range(27)]
    
    for edge in graph_nx_list:
        new_edge_list[edge[0]][edge[1]]=1
        new_edge_list[edge[1]][edge[0]]=1
    
    return new_edge_list

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        self.k_values = defaultdict()
        
    def add_edge(self,matrix):
        n=0
        for i in matrix:
            for idx,value in enumerate(i):
                if value==1:
                    self.graph[n].append(idx)
            n+=1           
        
    
    def k_core(self,ver,visited,degree,k):
        visited.add(ver)
        
        for node in self.graph[ver]:
            if degree[ver]<k:
                degree[node]-=1
                
            if node not in visited:
                self.k_core(node,visited,degree,k)

    
    def vertex_degree(self,k):
        visited=set()
        degree=defaultdict(lambda:0)
        
        
        for node in list(self.graph):
            degree[node]=len(self.graph[node])
        
        
        
        for node in list(self.graph):
            if node not in visited:
                self.k_core(node,visited,degree,k)

        return degree
        
    def print_output(self,k,degree):
        output=[]
        flag=0
        
        for node in list(self.graph):
            if degree[node]>=k:
                output.append(node)
        return output
    
    def multiple_k_values(self,flag):
        k=1
        output=[]
        degree=[]
        
        while k:
            degree=self.vertex_degree(k)
            output=self.print_output(k,degree)
            if len(output)==0:
                if flag==0:
                    print("k_value=",k-1,"nodes:",output2," number of nodes=",len(output2))                   
                    print("k_value=",k," no nodes")
                    break
                else:
                    print("k_value=",k," no nodes")
                    break
            
            for node in output:
                self.k_values[node]=k
                    
            if flag==0:
                output2=[]
                val=self.k_values.get(0)
                for node in self.k_values:
                    if self.k_values.get(node)==val:
                        output2=copy.deepcopy(output)
                        continue
                    else:
                        flag=1
            
                
            else:
                print("k_value=",k ,"nodes:",output," number of nodes=",len(output))
            k+=1  
            
                     
if __name__ == "__main__":
    
    #student_id=[1,2,3,4,5,1,2,3,4,5]
    student_id=[2,0,2,1,5,9,9,2,9,5]
    #[1]replace
    
    for i in range(len(student_id)):
        if student_id[i]%2==0:
            student_id[i]=0
        else:
            student_id[i]=1

    #[2] sequence
    sequence=student_id*73
    
    #[3] matrix
    sequence=np.array(sequence[:729])
    matrix=np.reshape(sequence,(27,27))
    
     #diagonal values to 0
    for i in range(27):
        matrix[i,i]=0
    
    
    #[5]symmetric 
    for i in range(27):
        for j in range(27):
            if i<j:
                matrix[i,j]=matrix[j,i]
    
    n=27
    #[4] eliminate isolated nodes
    adjList=matrix_to_list(matrix,n)
    degree=defaultdict(lambda:0)
    
    for node in list(adjList):
        degree[node]=len(adjList[node])

    for i in range(27):
        #setting first and last positions to 1
        if degree.get(i)==0:
            matrix[0,i]=matrix[i,0]=matrix[26,i]=matrix[i,26]=1
    
   
    g1=Graph()
    g1.add_edge(matrix)
    g1.multiple_k_values(0)
    
    #plot
    graph_nx_org=graph_nx(matrix)
    fig = plt.figure(figsize=(20,20))

    ax = fig.add_subplot(3,3,1)
    ax.set_title("original graph")
    nx.draw(graph_nx_org, with_labels = True, node_color=list(g1.k_values.values()), node_size=600)
    
    #removed edge 
    print("removing random edge")
    new_edge_matrix=edge_removal(graph_nx_org)
    g2=Graph()
    g2.add_edge(new_edge_matrix)
    g2.multiple_k_values(1)    
    
    graph_nx_new=graph_nx(new_edge_matrix)
    
    ax2 = fig.add_subplot(3,3,2)
    ax2.set_title("graph after removing an edge")
    nx.draw(graph_nx_new, with_labels = True, node_color=list(g2.k_values.values()), node_size=600)
    
    
    #removing second edge
    print("removing second random edge")
    new_edge_matrix2=edge_removal(graph_nx_new)
    g3=Graph()
    g3.add_edge(new_edge_matrix2)
    g3.multiple_k_values(1)    
    
    graph_nx_new2=graph_nx(new_edge_matrix2)
    
    ax3 = fig.add_subplot(3,3,3)
    ax3.set_title("graph after removing second edge")
    nx.draw(graph_nx_new2, with_labels = True, node_color=list(g3.k_values.values()), node_size=600)
# %%
