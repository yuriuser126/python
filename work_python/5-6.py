file_names = ["file1.py","fijle2.txt","file3.pptx","file4.doc"]


for file_name in file_names:
    arr = file_name.split(".") #파일네임으로 받아서 스플릿트한걸 배열로 만든다 새로.
    print(arr)
    # print("%s => 파일명: %s,확장자:.%s" %(file_name,arr[0],arr[1]))
