
import python

def test_average():
    result = python.average([5, 6, 7, 8, 9, 1], [7, 8, 6, 1, 4, 5])
    assert result == "Первый список имеет большее среднее значение"

def test_average2():
    result = python.average([5, 6, 7, 8, 9, 1], [7, 8, 6, 1, 4, 5000])
    assert result == "Второй список имеет большее среднее значение"

def test_average3():
    result = python.average([5, 6, 7, 8, 9, 1], [5, 6, 7, 8, 9, 1])
    assert result == "Средние значения равны"