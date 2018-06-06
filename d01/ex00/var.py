#!/usr/bin/env python3


def ft_var():
    # variable integer
    var_int = 42                # or int(42)
    # variable string
    var_str = "42"              # or str(42)
    var_str2 = "quarante-deux"  # or str("quanrante-deux")
    # variable float
    var_float = 42.0            # or float(42)
    # variable boolean
    var_bool = True             # or bool(True)
    # variable lists
    var_list = [42]             # or var_list = list()
    # variable dictionary, kind of union ?
    var_dict = {42: 42}
    # variable tupple, unmodifiable list
    var_tupple = (42,)
    # variable set
    var_set = set()

    print(var_int, "est de type", type(var_int))
    print(var_str, "est de type", type(var_str))
    print(var_str2, "est de type", type(var_str2))
    print(var_float, "est de type", type(var_float))
    print(var_bool, "est de type", type(var_bool))
    print(var_list, "est de type", type(var_list))
    print(var_dict, "est de type", type(var_dict))
    print(var_tupple, "est de type", type(var_tupple))
    print(var_set, "est de type", type(var_set))


if __name__ == '__main__':
    ft_var()
