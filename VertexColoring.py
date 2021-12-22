#
#This function takes in a dictionary (i.e. the graph parameter) whhich includes the vertices of the graph as the keys, and the adjacent
#vertices of each vertex as the values. The second parameter (ordering) gives the order in which to color the vertices. The function returns nothing
#if either the graph or ordering parameters are empty. The first vertex as denoted by the ordering is numbered one, and from there the function
#continues to loop through the vertices and their adjacent vertices to determine what color each vertex can be.
#
def greedy(graph, ordering):
    if not graph or not ordering: #return if parameters are emtpy
        return
      
    output = {} #This is our dictionary we will return with the coloring of each vertex
    
    output[ordering[0]] = 1 #Set the first vertex as denoted by the ordering parameter to the color 1
    
    ordering.pop(0) #Remove the first odering element so we can ignore it during our for loop
    
    color = 1 #Default start value when trying to color any of the vertices
    
    curr_set = {} #Dictionary to keep track of what color the neighboring vertices of each vertex in the graph are
    
    for vertex in ordering: 
        output[vertex] = 1 #Set the color of the vertex to 1 to start
        for neighbor in graph[vertex]: #Loop through each neighbor as denoted in graph parameter
            if (neighbor in output): #If neighboring vertex already has a color, we want to add it to our set of values to check during the loop
                curr_set[neighbor] = output[neighbor]
                
                #If the value of the vertex we are trying to color is the same as the neighboring one we are comparing, then increase the values
                #of the color by one
            while ((neighbor in output) and output[neighbor] == output[vertex]):
                color += 1
                output[vertex] = color #Make sure value in the output table reflects this change
                
                #Now we want to continue increasing the value of the vertex by one while it is still equal to any of the values of its
                #adjacent vertices
                while (output[vertex] in curr_set.values()):
                    output[vertex] += 1
            color = 1 #Reset color value to one for next vertex to be changed
            
        curr_set = {} #Rest the dictionary which holds the values of a vertex's adjacent vertices
        
    return output
