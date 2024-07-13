#!/usr/bin/python3
#Author : Sateesh
#Date   : 22/June/2024
#Purpose: Figure out how to implemene pipe and filter in python
#         https://patterns.eecs.berkeley.edu/?page_id=19
#TODO:
#         1. Create a PipeLineController class
#         2. Add  a private member for the data in question, it would be an RTSP video stream
#         3. Create an handle for this data, to achieve zero cp
#         4. Pass this handle to the filter class
#         5. Manipulate the data and return the handle
#         6. Pass the handle from one filter to next as an initial implementation
#         7. Concurrently execute all filters at one shot
# A concrete example is to take an image, create an R, G and B filters and concurrently apply the filters

class PipeLineController:
    def __init__(self, name,data):
    #private 
        self.__data = data
    #public
        self.name = name
        print("In ctor:", self.name)
        print("Data:",data)
    

    def get_pointer(self):
        pointer = self.__data
        return pointer

    def __del__(self):
        print("In dtor",self.name)


class AdditionFilter:
    def __init__(self, name, data):
    #private 
        self.__filter_data = data 
    #public
        self.name = name
        print("In ctor:", self.name)

    def __del__(self):
        print("In dtor",self.name)

if __name__ == "__main__":
# Create a pipeline object
    A = PipeLineController("X", [1, 2, 3])   

#Create a filter
    data = A.get_pointer()
    f = AdditionFilter("ff", data)     
