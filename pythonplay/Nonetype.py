def calc_prod(lst):
    def ff():
        print(map(lambda x:x*x,lst))
    return ff

f = calc_prod([1,2,3,4])
print(f())