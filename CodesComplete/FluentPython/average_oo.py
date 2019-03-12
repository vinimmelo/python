def make_averager():
    ## Scope average implementation, with nonlocal to best performance.
    
    count = 0
    total = 0

    def averager(new_value):
        nonlocal count, total
        count += 1
        total += new_value
        return total / count
    return averager
