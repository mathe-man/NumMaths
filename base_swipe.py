import interface


def base_swipe(in_base_size: int, out_base_size, inputs):
    # Check if there is no base under 2 (minimum supported)
    if in_base_size < 2 or out_base_size < 2:
        raise ValueError("Base size cannot be under 2")

    # Check if there is no value greater than his base
    for i in inputs:
        if i >= in_base_size:
            raise ValueError(str(i) + " is greater than his base size (" + str(in_base_size) + ")")


    total = 0
    print("Value in base 10 to divide after:")
    for i in range(len(inputs)):
        total += inputs[-(i+1)] * in_base_size**i
        print(" " + str(inputs[i]) + " * " + str(in_base_size) + "^" + str(i))

    print("total = " + str(total))

    #== This could be done but will skip the formating made at the end
    # Directly return if it's the requested base
    # if out_base_size == 10:
    #     return total

    outputs = []
    while total != 0:
        rest = total % out_base_size
        quot = total // out_base_size

        print(str(total) + " / " + str(out_base_size) + " = " + str(quot) + " | Rest = " + str(rest))
        outputs.insert(0, rest)
        total = quot

    interface.space()

    print("The list of the rests need to be reversed to get the value: ")
    # Show the input
    print("( ", end='')
    for i in inputs:
        print(str(i) + " ", end='')
    print(")" + str(in_base_size), end='') #Input base
    # Equality
    print(" = ", end='')

    # Show the result
    print("( ", end='')
    for i in outputs:
        print(str(i) + " ", end='')
    print(")" + str(out_base_size)) # Output base

    return outputs

base_swipe(16, 2, [14, 15])