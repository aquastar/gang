import instagram_explore as ie

# Search tag name
res = ie.tag('ms13')
print(res.data)  # All
print(res.data['media']['nodes'])  # Media list

# Next page
ins_cnt = 2
while ins_cnt >0 :
    ins_cnt -=1
    res = ie.tag('ms13', res.cursor)
    print(res.data)  # All
    print(res.data['media']['nodes'])  # Media list
