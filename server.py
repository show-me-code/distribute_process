# -*-coding:utf-8-*-
import random, time, queue
from multiprocessing.managers import ListProxy
import torch.multiprocessing as mp

#from multiprocessing import Manager as mp


def start_server(manager, host, port, key):
    l = manager.list(range(10))
    manager.register('get_list', callable=lambda :l, proxytype=ListProxy) #need to define proxytype!
    manager.__init__(address=('127.0.0.1', 5000), authkey=b'abc')
    print('Connect to server %s' % host)
    #manager.start()
    s = manager.get_server()
    s.serve_forever()
    #return manager

if __name__ == "__main__":
    mp.set_start_method('spawn') #can't create manager or list out of main or function
    manager = mp.Manager()
    manager = start_server(manager, '', 5000, b'abc')
    #logic(manager)