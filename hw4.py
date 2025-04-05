def rep_char(c, n):
    return c * n

def draw_line_string(msg):
    print(rep_char('-', len(msg)))
    print(msg)
    print(rep_char('-', len(msg)))

def welcome_message():
    name = input('Input his/her name: ')

    msg1 = f'Hello {name}'
    msg2 = 'Welcome to Seoul.'

    nstr = len(msg1) if len(msg1) > len(msg2) else len(msg2)

    print(rep_char('-', nstr))
    print(msg1)
    print(msg2)
    print(rep_char('-', nstr))

welcome_message()