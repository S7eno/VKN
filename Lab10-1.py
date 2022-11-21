
with open('data/text.txt') as file:
    
    listt = file.read().split(',')
    listt = list(listt)
    spisoc = []
    spisoc.append(listt[4])
    spisoc.append(listt[6])
    
    print(spisoc)
    listt = set(listt)
    listt = sorted(listt)
    print(listt)

    com = str(open('data/text.txt').read().count(','))
    print("Кількість ком у файлі:",com)
    spisoc = str (spisoc)
    listt = str(listt)
    com = str(com)

    file.close() 
    
    double_file = open("lb10-1\\Double_el.txt", "x")
    double_file_writer = double_file.write(spisoc)  
    double_file.close()


    unique_file = open("lb10-1\\Unique_el.txt", "x")
    unique_file_writer = unique_file.write(listt)  
    unique_file.close()


    count_of_koma_file = open("lb10-1\\Count_of_koma.txt", "x")
    count_of_koma_file_writer = count_of_koma_file.write(com)  
    count_of_koma_file.close()




