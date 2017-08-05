def s_pop(s, command):
    s.pop()
            
def s_remove(s, command):
    s.remove(int(command[1]))
        
def s_discard(s,command):
    s.discard(int(command[1]))

if __name__=='__main__':
    n = input()
    s = set(map(int, raw_input().split()))
    m = input()
    functions = {'pop':s_pop, 'remove': s_remove, 'discard': s_discard}
    for i in range(m):
        command = raw_input().split()
        functions[command[0]](s, command)
        print sum(s)
