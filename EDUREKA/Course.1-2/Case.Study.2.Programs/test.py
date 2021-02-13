items = ['sss', 'sss', 'asda', 'asdasd', 'sfsdf']
prefix = 's'

filteredlist = list(filter(lambda x: x.startswith(prefix), items))
print(filteredlist)
