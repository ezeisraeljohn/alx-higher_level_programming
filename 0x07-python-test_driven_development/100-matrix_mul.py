#!/usr/bin/python3
""" Module that houses function that multiplies two matrices"""


def matrix_mul(m_a, m_b):
    """ The function that multiplies two matrices

        args:
            m_a([[]]): The first matrix
            m_a([[]]): The second matrix
    """

    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list of lists")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list of lists")

    for row1 in m_a:
        if not isinstance(row1, list):
            raise TypeError("m_a must be a list of lists")

    for row2 in m_b:
        if not isinstance(row2, list):
            raise TypeError("m_b must be a list of lists")

    if not m_a:
        raise ValueError("m_a can't be empty")

    if not m_b:
        raise ValueError("m_b can't be empty")

    count = 0
    for i in range(len(m_a)):
        if len(m_a[i]) == 0:
            count += 1

    if count == len(m_a):
        raise ValueError("m_a can't be empty")

    count2 = 0
    for j in range(len(m_b)):
        if len(m_b[j]) == 0:
            count2 += 1

    if count2 == len(m_b):
        raise ValueError("m_b can't be empty")
