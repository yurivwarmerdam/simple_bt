import ctypes

a_lib=ctypes.CDLL("build/BehaviorTree.CPP/libbehaviortree_cpp.so")
my_thing=ctypes.CDLL("/c/dev/c/btrees/simple_bt/build/libsimple_lib.so")

# my_thing=ctypes.CDLL("/c/dev/c/btrees/src/simple_bt/build/libsimple_tree.so")

print(dir(my_thing))
print("-------")
print(my_thing.__dict__)
print("-------")
print(vars(my_thing))
my_thing.simple_run()

# my_thing.main()