import os

folder_list = os.listdir("C:\\Program Files\\")
folder_list = str(folder_list) 

print(folder_list )

folder_file = open("lb10-2\\Folder_file.txt", 'x'  )
folder_file_writer = folder_file.write(folder_list)
folder_file.close()