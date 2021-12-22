""""
This is the Floyd Warshall algorithm which finds the shortest
weighted directed path between each pair of vertices. The bulk of the work is done within an adjacency matrix, which in this function is being represented by a list of lists. adj_matrix is the user-inputted adjacency matrix (list of lists) which should give the graph vertices and their directly connected weighted edges
@Brandon Thomas
@MTH 325 02 Professor Short
@V1.0.0
"""
def Floyd_Warshall(adj_matrix):
  short_mat = [[]] #This is the adjacency matrix which will hold the output (shortest weighted path) for each vertex in adj_matrix
  vertices = len(adj_matrix) #The amount of vertices given in adj_matrix
  
  #Here we are looping through (until the size of adj_matrix) and creating lists initialized as -1 to represent empty values
  for num in range(vertices): 
    short_mat.append([])
    for i in range(vertices):
      short_mat[num].append(-1)

  del short_mat[-1] #This is just a shortcoming of my understanding of adj. matrices, so I needed to remove the empty list at the bottom I was creating
  
  #Now, in order to further intialize the output adj_matrix, we are going to input the weighted directed edges as given by adj_matrix for each vertex,
  #and then if a vertex does not have a direct edge to another vertex in the graph, the value is set to float('inf') (or infinity).
  for vertex in range(vertices):
    for edge in range(vertices):
      if (adj_matrix[vertex][edge] != 0):
        short_mat[vertex][edge] = adj_matrix[vertex][edge] #Setting weight to that of the value in adj_matrix (user input)
      else:
        short_mat[vertex][edge] = float('inf') #Setting value to infinity if no direct path exists

  #This is really the main part of the Floyd_Warshall algorithm. k is an intermediary point between vertex i and vertex j. As we loop through these
  #nested loops, we want to see if these intermediary paths (which get longer and longer) have less of a weight / are shorter than the current edge/
  #connection between vertex i and j.  
  for k in range(vertices):
    for i in range(vertices):
      for j in range(vertices):
        if (short_mat[i][j] > short_mat[i][k] + short_mat[k][j]):
          short_mat[i][j] = short_mat[i][k] + short_mat[k][j]

  return short_mat
