#!/usr/bin/env python
# coding: utf-8

# In[29]:


graph={'A':['B','E','C'],
       'B':['E','D','A'],
       'E':['A','B','D'],
       'C':['A','F','G'],
       'F':[],
       'G':[]
}
print(graph)


# In[30]:


def DFS(graph,start,goal):
    stack=[]
    visited=[]
    stack.append(start) #pushing starting node into stack
    while stack:
        node=stack.pop(-1) #poping last node from stack
        if node not in visited:
            visited.append(node)
            child=graph[node]
            for i in child: #visiting adjacent nodes of vertex
                if i not in stack and i not in visited:
                    if i==goal:
                        visited.append(i)
                        return visited
                    stack.append(i) #if goal not found append and expand further until stack become empty


# In[31]:


def PATH(path):
    if path!=None:
        print("sequence of actions to reach goal")
        for i in range(0,len(path)):
            if(i<len(path)-1):
                print(path[i],end="->")
            else:
                print(path[i])
    else:
        print("path not found")


# In[32]:




path=DFS(graph,'A','F')
PATH(path)


# In[21]:





# In[ ]:




