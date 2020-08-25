def consumer():
    r = ''
    j = 0
    while True:
        n = yield r  # 3
        print("n=", n)
        j = j + 1
        print('********j=%d' % j)
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'


def produce(c):
    c.send(None)  # 1
    print('------------')
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)  # 2
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


if __name__ == "__main__":
    c = consumer()
    produce(c)
