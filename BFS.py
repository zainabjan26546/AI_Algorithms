#!/usr/bin/env python
# coding: utf-8

# In[2]:


map={
    'Arad':['Zerind','Timisoara'],
    'Zerind':['Arad','Oradea'],
    'Timisoara':['Arad','Lugoj'],
    'Oradea':['Zerind','Sibiu'],
    'Lugoj':['Timisoara','Mehadia'],
    'Sibiu':['Arad','Oradea','Fagaras','Rimnicu Vilcea'],
    'Mehadia':['Lugoj','Drobeta'],
    'Fagaras':['Sibiu','Bucharest'],
    'Rimnicu Vilcea':['Sibiu','Pitesti','Craiova'],
    'Drobeta':['Mehadia','Craiova'],
    'Bucharest':['Giurgiu','Uzriceni','Fagaras','Pitesti'],
    'Pitesti':['Rimnicu Vilcea','Bucharest','Craiova'],
    'Craiova':['Rimnicu Vilcea','Drobeta','Pitesti'],
    'Giurgiu':['Bucharest'],
    'Uzriceni':['Vaslui','Hirsova'],
    'Vaslui':['Lasi','Uzriceni'],
    'Hirsova':['Eforie','Uzriceni'],
    'Eforie':[],
    'Lasi':['Neamt','Vaslui'],
    'Neamt':[]
}


# In[3]:


def BFS(graph,start,goal):
    queue=[]
    visited=[]
    queue.append(start) #pushing starting node into stack
    while queue:
        vertex=queue.pop(-1) #poping last node from stack
        if vertex not in visited:
            visited.append(vertex)
            child=graph[vertex]
            for i in child: #visiting adjacent nodes of vertex
                if i not in queue and i not in visited:
                    if i==goal:
                        visited.append(i)
                        return visited
                    queue.append(i) #if goal not found append and expand further until stack become empt


# In[4]:


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


# In[5]:


path=BFS(map,'Arad','Bucharest')
PATH(path)


# In[ ]:




