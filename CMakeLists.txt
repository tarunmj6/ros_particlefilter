cmake_minimum_required(VERSION 2.8.3)
project(uml_hmm)

#option(BUILD_TEST "Test CXX helper functions" ON)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
)

catkin_package()

include_directories(${catkin_INCLUDE_DIRS})

#if(BUILD_TEST)
    add_executable(query_cxx nodes/sensing_model_and_map.hpp 
                             nodes/sensing_model_and_map.cpp
                             nodes/query_cxx.cpp)
    target_link_libraries(query_cxx ${catkin_LIBRARIES})
#endif(BUILD_TEST)
