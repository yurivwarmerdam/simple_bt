cd build/btcpp_sample
# cmake -DCMAKE_PREFIX_PATH=/home/yuri/btrees/src/BehaviorTree.CPP -DCMAKE_MODULE_PATH=../BehaviorTree.CPP -S ../../src/btcpp_sample -B .
cmake -DCMAKE_PREFIX_PATH="/home/yuri/btrees/src/BehaviorTree.CPP" -S ../../src/btcpp_sample -B .
# cmake --build . --parallel
cd ../../