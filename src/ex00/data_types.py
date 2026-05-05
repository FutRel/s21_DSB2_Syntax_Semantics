def data_types():
    first = 5
    second = "5"
    third = 5.0
    fourth = True
    fifth = []
    sixth = dict(a=1)
    seventh = (1, 2, 3)
    eighth = {"1", "2"}
    result = str([type(i).__name__ for i in (first, second, third, fourth, fifth, sixth, seventh, eighth)])
    print(result.replace("'", ""))


if __name__ == '__main__':
    data_types()
