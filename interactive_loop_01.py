while True:
    reply = input('Enter text:')
    if reply == 'stop' :
        break
    try:
        num = int(reply)
    except:   
        print('write a number')
    else:
        print(int(reply) ** 2)
print('bye')    