
def base_swipe(in_base_size: int, out_base_size, inputs):
    # TODO add security checks (no inputs greater than his base, ...)

    total = 0
    for i in range(len(inputs)):
        total += inputs[i] * in_base_size**i

    if out_base_size == 10:
        return total

    outputs = []
    while total != 0:
        outputs.insert(0, (total % out_base_size))
        total = total // out_base_size

    return outputs
