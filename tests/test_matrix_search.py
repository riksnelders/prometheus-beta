import pytest
from src.matrix_search import search_matrix

def test_matrix_search_basic():
    """Test basic matrix search scenario"""
    matrix = [
        [1, 3, 5],
        [7, 9, 11],
        [13, 15, 17]
    ]
    assert search_matrix(matrix, 9) == True
    assert search_matrix(matrix, 12) == False

def test_matrix_search_empty():
    """Test empty matrix scenarios"""
    assert search_matrix([], 5) == False
    assert search_matrix(None, 5) == False

def test_matrix_search_single_row():
    """Test matrix with a single row"""
    matrix = [[1, 2, 3, 4, 5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_single_column():
    """Test matrix with a single column"""
    matrix = [[1], [2], [3], [4], [5]]
    assert search_matrix(matrix, 3) == True
    assert search_matrix(matrix, 6) == False

def test_matrix_search_invalid_input():
    """Test error handling for invalid inputs"""
    with pytest.raises(TypeError):
        search_matrix([[1, 2], [3, 4]], "5")
    
    with pytest.raises(ValueError):
        search_matrix([[1, 2], 3], 5)

def test_matrix_search_edge_cases():
    """Test various edge cases"""
    matrix = [[]]
    assert search_matrix(matrix, 5) == False
    
    matrix = [[1]]
    assert search_matrix(matrix, 1) == True
    assert search_matrix(matrix, 2) == False