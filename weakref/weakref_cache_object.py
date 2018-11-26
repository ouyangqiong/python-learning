# coding =utf-8
from pprint import pprint
import gc
import weakref

class Person(object):
    
    def __init__(self, name):
        self.name=name

    def __repr__(self):
        return 'Person({})'.format(self.name)

    def __del__(self):
        print('deleting {}'.format(self))

def demo(cache_factory):
    all_refs = {}
    print("CACHE_TYPE：{}".format(cache_factory))
    cache = cache_factory()
    for name in ["qiaofeng", "duanyu", "xuzhu"]:
        person = Person(name)
        cache[name] = person
        all_refs[name]=person
        del person

    print("all_refs=", end=' ')
    pprint(all_refs)
    print("\nBefore cache contains:{}".format(list(cache.keys())))
    for name, value in cache.items():
        print('{}={}'.format(name, value))
        del value
    
    print("Cleanup:")
    del all_refs
    gc.collect()

    print("\nAfter cache contains:{}".format(list(cache.keys())))
    for name, value in cache.items():
        print('{}={}'.format(name, value))
    print("demo returning") 

if __name__ == "__main__":
    print("=====================================================")
    demo(dict)
    print("=====================================================")
    demo(weakref.WeakValueDictionary)

