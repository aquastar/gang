import instagram_explore as ie

# Search tag name
res = ie.tag('ms13')
print(res.data)                   # All
print(res.data['media']['nodes']) # Media list

# Next page
data, cursor = ie.tag('cat', res.cursor)

# Image only
images = ie.tag_images('cat').data