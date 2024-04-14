"""Function to perform matrix factorization using Singular Value decomposition"""
import numpy as np

def generate_matrix(choice, rows, columns):
    if choice == 1:
        matrix = np.random.rand(rows,columns)
    else:
        matrix = np.random.randint(1,100,size=(rows,columns))
        
    matrix_factorization(matrix)
    
def matrix_factorization(matrix):
    u, s, v = np.linalg.svd(matrix)
    print(f"u: {u}\n\ns: {s}\n\nv: {v}\n")
    reconstruct_matrix(u,s,v)

def reconstruct_matrix(u,s,v):
    sigma = np.zeros((u.shape[0], v.shape[0]))
    sigma[:s.shape[0], :s.shape[0]] = np.diag(s)
    
    reconstructed_matrix = np.dot(u, np.dot(sigma, v))
    print(f'Reconstructed Matrix: \n{reconstructed_matrix}')
      
    
choice = input("Do you want to generate matrix of\n1. Float datatype\n2. Integer datatype")    

if choice == 'Float datatype':
    choice = 1
else:
    choice = 0
    
rows= int(input('No. of rows: '))
columns = int(input('No. of columns: '))
generate_matrix(choice,rows,columns)