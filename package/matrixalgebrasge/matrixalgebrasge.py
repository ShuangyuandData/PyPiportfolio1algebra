import math
import numpy as np
import pandas as pd

class MatrixA():
    """ matrix for the algebra calculation
    
    Attributes:
        nrow (int) representing the number of rows in the matrix
        ncol (int) representing the number of columns in the matrix
        data_matrix  a matrix extracted from the data
        """
    
    def __init__(self, nrow=1, ncol=1):
        
        self.nrow=nrow
        self.ncol=ncol
        self.data_matrix=np.zeros([nrow,ncol])
        
    def get_nrow(self):
        """ calculate the row number of the data matrix
        
        Args:
            None
        
        Return:
            int: the row number"""
        
        self.nrow=self.data_matrix.shape[0]
        return self.nrow
    
    def get_ncol(self):
        """ calculate the column number of the data matrix
        
        Args:
            None
        
        Return:
            int: the column number"""      
        
        self.ncol=self.data_matrix.shape[1]
        return self.ncol
    
    def read_data_file(self, file_name):
        """Method to read in matrix from a text file. The text file should have
        a matrix with , seperated.
        
        Args: file_name (string): name of a file to read from
        
        Returns: 
        None
        
        """
        
        data_matrixtmp=np.loadtxt(file_name, delimiter=',')
        self.data_matrix=data_matrixtmp
        self.nrow=self.get_nrow()
        self.ncol=self.get_ncol()
        
    def print_matrix(self):
        """Method to print the current matrix
        
        Args:
            None
            
        Returns:
        None
        """
        
        print(self.data_matrix)
        
        
    def __add__(self, other):
        """Magic method to add together two matrix
        
        Args:
            other (MatrixA): Matrix instance
            
        Returns:
            MatrixA: Matrix 
        
        """
        
        result=MatrixA(self.nrow,self.ncol)
        
        
        for i in range(self.nrow):
            for j in range(self.ncol):
                result.data_matrix[i][j]=self.data_matrix[i][j]+other.data_matrix[i][j]
            
        return result