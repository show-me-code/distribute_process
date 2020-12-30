# -*-coding:utf-8-*-
import torch.multiprocessing as mp



def start_client(manager, host, port, key):
    manager.register('get_list')
    manager.__init__(address=(host, port), authkey=key)
    manager.connect()
    return manager

def logic(manager):
    l = manager.get_list()
    for i in range(0, 10):
        l.append(i)
    print(l)

if __name__=='__main__':
    manager = mp.Manager()
    manager = start_client(manager, '127.0.0.1', 5000, b'abc')
    logic(manager)
