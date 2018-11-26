# coding=utf-8

import weakref

class Person(object):

    def __init__(self):
        self.name="乔峰"

    def kongfu(self):
        print("降龙十八掌")

def callback(reference):
    print("callback:{}".format(reference))




if __name__ == "__main__":
    person = Person()
    print("weakrefcount:{}".format(weakref.getweakrefcount(person)))
    print("WeakKeyDictionary:{}".format(weakref.WeakKeyDictionary({person: "aa"})))
    print("WeakValueDictionary:{}".format(weakref.WeakValueDictionary({"aa": person})))
    print("Weakset:{}".format(weakref.WeakSet([person])))
    print("ReferenceType:{}".format(weakref.ReferenceType))
    print("ProxyType:{}".format(weakref.ProxyType))

    person2 = weakref.ref(person, callback)
    print("weakrefcount:{}".format(weakref.getweakrefcount(person)))
    print("WeakKeyDictionary:{}".format(weakref.WeakKeyDictionary({person: "aa"})))
    print("WeakValueDictionary:{}".format(weakref.WeakValueDictionary({"aa": person})))
    print("Weakset:{}".format(weakref.WeakSet([person])))
    print("ReferenceType:{}".format(weakref.ReferenceType))
    print("ProxyType:{}".format(weakref.ProxyType))
    print("-------------------------")
    print("persion:{},\nperson2():{}\nperson2:{}".format(
        person, person2(),person2))
    print("-------------------------")

    print("========================")
    print("person2:{}".format(person2))
    print(">person3 ========================")
    person3 = weakref.proxy(person)
    print("weakrefcount:{}".format(weakref.getweakrefcount(person)))
    print("WeakKeyDictionary:{}".format(weakref.WeakKeyDictionary({person: "aa"})))
    print("WeakValueDictionary:{}".format(weakref.WeakValueDictionary({"aa": person})))
    print("Weakset:{}".format(weakref.WeakSet([person])))
    print("ReferenceType:{}".format(weakref.ReferenceType))
    print("ProxyType:{}".format(weakref.ProxyType))
    print("**************************************************")
    print("deleting person")
    del person
    print("person2():{}\nperson2:{}".format(
        person2(),person2))
    print("-------------------------")