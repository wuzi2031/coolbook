from multiprocessing import Process, Queue


def f(q):
    q.put([42, None, 'hello'])
    q.put([41, None, 'hello'])



if __name__ == '__main__':
    q = Queue()
    p = Process(target=f, args=(q,))
    p.start()
    print(q.get())  # prints "[42, None, 'hello']"
    print(q.get())  # prints "[41, None, 'hello']"
    p.join()