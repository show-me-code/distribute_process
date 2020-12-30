# -*-coding:utf-8-*-
import torch.multiprocessing as mp
import torch.multiprocessing as mp

def start_client(manager, host, port, key):
    manager.register('get_list')
    manager.__init__(address=(host, port), authkey=key)
    manager.connect()
    return manager

def print_object(obj):
    print('\n'.join(['%s:%s' % item for item in obj.__dict__.items()]))

def logic(manager):
    l = manager.get_list()
    #print(l[0])
    for i in range(0, 10):
        print(l[i])

if __name__=='__main__':
    manager = mp.Manager()
    manager.register('get_list')
    manager.__init__(address=('127.0.0.1', 5000), authkey=b'abc')
    manager.connect()
    logic(manager)
