def wrapper(f):
    def fun(l):
        formatted = []
        for number in l:
            num = number[-10:]  # take last 10 digits
            formatted.append(f"+91 {num[:5]} {num[5:]}")
        f(sorted(formatted))
    return fun



@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l) 
