#!/usr/bin/python3
""" Module that houses function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """ The function that multiplies two matrices

        args:
            m_a([[]]): The first matrix
            m_a([[]]): The second matrix
    """
    length_row_m_a = len(m_a[0])
    length_row_m_b = len(m_b[0])
    length_m_a = len(m_a)
    length_m_b = len(m_b)

    """ Edge Cases for m_a(first matrix) """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list of lists")

    for row1 in m_a:
        if not isinstance(row1, list):
            raise TypeError("m_a must be a list of lists")

    if not m_a:
        raise ValueError("m_a can't be empty")

    count = 0
    for i in range(length_m_a):
        if len(m_a[i]) == 0:
            count += 1

    if count == length_m_a:
        raise ValueError("m_a can't be empty")

    for index in range(length_m_a):
        for m in range(len(m_a[index])):
            if not isinstance(m_a[index][m], (int, float)):
                raise TypeError("m_a should contain only integers or floats")

    for length in range(length_m_a):
        if len(m_a[length]) != length_row_m_a:
            raise TypeError("each row of m_a must be of the same size")

    """ Edge Cases for m_b(second matrix) """

    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list of lists")

    for row2 in m_b:
        if not isinstance(row2, list):
            raise TypeError("m_b must be a list of lists")

    if not m_b:
        raise ValueError("m_b can't be empty")

    count2 = 0
    for j in range(length_m_b):
        if len(m_b[j]) == 0:
            count2 += 1

    if count2 == length_m_b:
        raise ValueError("m_b can't be empty")

    for index2 in range(length_m_a):
        for m2 in range(len(m_b[index2])):
            if not isinstance(m_b[index][m2], (int, float)):
                raise TypeError("m_b should contain only integers or floats")

    for length2 in range(length_m_b):
        if len(m_b[length2]) != length_row_m_b:
            raise TypeError("each row of m_b must be of the same size")

    if length_row_m_a != length_m_b:
        raise ValueError("m_a and m_b can't be multiplied")
