def text_creator(name,msg):
    pathe = 'E://ITfile/'
    fullpath = pathe + name + '.txt'
    file =open(fullpath,'w')
    file.write(msg)
    file.close()
    print('ok')
for i in range(1,11):
    text_creator(str(i),'hello')
    print(i)
