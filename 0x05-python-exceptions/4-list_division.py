#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    result = [0] * list_length
    for i in range(list_length):
        val = 0
        try:
            val = my_list_1[i] / my_list_2[i]
        except (TypeError, ValueError):
            print("Wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("Out of range")
        finally:
            result[i] = val
    return result
