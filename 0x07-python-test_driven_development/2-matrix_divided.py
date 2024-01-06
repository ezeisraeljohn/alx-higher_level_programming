#!/usr/bin/python3

""" This module contains function that multiplies element of a matrix"""

def matrix_divided(matrix, div):
    """Function That divides each element of a matrix by a number
        args:
            matrix(list of list): This is the list of the matrix
            div(int): Number to divide elements of matrix with
        
        Description: This function adds divides each element of the matrix,
                     and then the result will be in two decimal places
        
        Return: A new matrix containing the division
    """
    if not matrix:
        return matrix

    if div == 0:
        raise TypeError("division by zero")
    
    if not isinstance(div, (int, float)):
        raise TypeError("div must be an integer or float")

    new_matrix = [row[:] for row in matrix]
    length_matrix = len(new_matrix[0])

    # Check if the length of each row in the matrix is same
    for i in range(len(new_matrix)):
        if len(matrix[i]) != length_matrix:
            raise TypeError("Each row of the matrix must have the same size")

    # divide each integer of the array by 2 if all are of same type
    for row in range(len(new_matrix)):
        for column in range(length_matrix):
            if not isinstance(new_matrix[row][column], (int, float)):
                raise TypeError("matrix must be a matrix (list of lists)"
                                " of integers/floats")
            else:
                new_matrix[row][column] = round(new_matrix[row][column] / div,
                                                2)

    return new_matrix
