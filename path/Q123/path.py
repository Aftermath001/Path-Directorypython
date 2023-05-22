# # Create a new file named "output.txt" and write the 
# sentence "Hello, world!" to it using Python.

#Writing to a file
with open('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q123/output.txt', 'w') as bacon_file:
     bacon_file.write('Hello world!\n')
with open('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q123/output.txt') as bacon_file:
     content = bacon_file.read()
print(content)



# Write a Python code snippet to open a file named "data.txt" in read mode and print its contents.
	
# Content of the data.txt 
# Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
# Aliquam mollis dui at lectus iaculis, sed volutpat ipsum luctus. Vestibulum eget velit vel erat consectetur venenatis 
# finibus sed magna. Suspendisse eget libero iaculis, ornare sapien nec, porttitor nisl. Quisque sit amet commodo enim. 
# Vivamus ultricies rhoncus enim, ut facilisis est. 
# Praesent nec eros metus. Morbi in mattis tortor, sed pellentesque nunc. 
# Aenean mattis luctus velit eu facilisis.
with open('/home/alvin/Development/code/phase3/Path-Directorypython/path/Q123/data.txt') as hello_file:
    data_content = hello_file.readlines()
print(data_content)

