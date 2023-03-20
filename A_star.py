#!/usr/bin/env python
# coding: utf-8

# In[45]:


#dict for stroing each  node with adjacent child  
maze = {
    'A':['F'],
    'F':['H'],
    'H':['I','M'],
    'I':['J','H','N'],
    'M':['R','H','N'],
    'J':['G','I'],
    'N':['S','I','M'],
    'R':['S','N'],
    'G':['J','B'],
    'B':['G','C'],
    'S':['T','R','N'],
    'C':['B','D'],
    'T':['W','S','U'],
    'D':['C','E'],
    'E':['D'],
    'W':['T'],
    'U':['O','T'],
    'O':['P','U'],
    'P':['O','Q'],
    'Q':['V','L'],
    'V':['Y','Q'],
    'Y':['X','V'],
    'X':['Y'],
    'L':['K','Q'],
    'K':['L','P']
}


# In[46]:


#storing coordinates of each child 
coordinates={
    'A':[0,0],
    'F':[0,1],
    'H':[0,2],
    'M':[0,3],
    'R':[0,4],
    'S':[1,4],
    'N':[1,3],
    'I':[1,2],
    'W':[2,5],
    'T':[2,4],
    'J':[2,2],
    'G':[2,1],
    'B':[2,0],
    'U':[3,4],
    'O':[3,3],
    'C':[3,0],
    'X':[4,5],
    'P':[4,3],
    'K':[4,2],
    'D':[4,0],
    'Y':[5,5],
    'V':[5,4],
    'Q':[5,3],
    'L':[5,2],
    'E':[5,0]
}


# In[47]:


#importing math 
import math


# In[48]:


#calculating the distance between adjacent nodes
def Gn(node1,node2):
    n=coordinates[node1] #storing coordinates of parent
    x,y=n[0],n[1] #x,y coordinate of parent
    g=coordinates[node2] #storing coordinates of child
    X,Y=g[0],g[1]  #X,Y coordinate of child
    euc_dist= (math.sqrt((X-x)**2+(Y-y)**2)) #calculating euclidean distance between nodes
    return round(euc_dist,2)
    
    


# In[49]:


def priority_queue(PQ):
    #F(n) value stored at end so sorting in ascending order.
    return sorted(PQ,key=lambda x:x[::-1])
    


# In[50]:


def fn(g,h):
    return round(g+h,2) #returning F(N)


# In[51]:


def PATH(path): #FUNCTION TO RETURN THE PATH 
    if path!=None:
        print("sequence of actions to reach goal")
        for i in range(0,len(path)):
            if(i<len(path)-1):
                print(path[i],end=" -> ")
            else:
                print(path[i])
    


# In[52]:


def A_star(maze,start,goal):
    L=[start,0,0,0] #L=[start,g(n),h(n),f(n)] 
    PQ=[L] #PQ to store the sequences of action
    visited=[] #to store nodes that are visited
    while PQ: 
        l=PQ.pop(0) #poping first element of priority queue and storing it in l
        node=l[len(l)-4] #accessing the node using indexing-> in my list fourth last element is node to be expand
        if node==goal:
            return l #sequences of action will be returnes if goal test becomes true
        if node not in visited: 
            child=maze[node] #storing child nodes of list for expansion
            visited.append(node)
            for i in range(0,len(child)): 
                temp=[] # temp list will contain the previous nodes of sequences along with g(n),hn,fn
                temp=l[:]
                temp.insert(len(temp)-3,child[i]) #inserting node at fourth last position
                LENGTH=len(temp) #finding length of temp after insertion of nodes
                g=float(temp[LENGTH-3]) + Gn(node,child[i]) #summing the value if g(n) 
                h=dict[node] #accesing the H(N) of node from N-goal node
                f=fn(g,h) # f stores f(n)
                g,h=round(g,2),round(h,2)
                temp[LENGTH-3]=g #storing g in third last element of g
                temp[LENGTH-2]=h #storing h in second last elemnet 
                temp[LENGTH-1]=f #storing f in last element
                PQ.append(temp) #appending in PQ
                
            
        PQ=priority_queue(PQ)
       
                    


# In[53]:


start =input("enter start node :")
goal=input("enter goal node: ")
#storing the heuristic values in dict
dict={}
for i in coordinates:
    n=coordinates[i]
    x,y=n[0],n[1]
    g=coordinates[goal]
    X,Y=g[0],g[1]
    euc_dist= (math.sqrt((X-x)**2+(Y-y)**2))
    dict[i]=round(euc_dist,2)
path=A_star(maze,start,goal)
PATH(path[:len(path)-3]) #printing path


# In[ ]:




