d =   [["P-6", 91, 56, 84, 47],
    ["P-9", 73, 71, 88, 50],
    ["P-10", 88, 70, 85, 81],
    ["P-20", 88, 106, 56, 71],
    ["P-46", 71, 62, 94, 39],
    ["P-50", 73, 104, 64, 75],
    ["P-68", 92, 46, 81, 62],
    ["P-94", 67, 98, 66, 95],
    ["P-106", 90, 54, 92, 100],
    ["P-124", 54, 104, 72, 96],
    ["P-129", 110, 59, 85, 64],
    ["P-133", 63, 109, 91, 174],
    ["P-183", 105, 72, 57, 37],
    ["P-252", 48, 110, 95, 139],
    ["P-277", 54, 108, 105, 93],
    ["P-284", 70, 110, 52, 86],
    ["P-285", 81, 108, 54, 78],
    ["P-295", 49, 109, 69, 32],
    ["P-319", 48, 102, 101, 144],
    ["P-350", 85, 60, 69, 52],['P-10', 88, 70, 85, 81], ['P-36', 86, 80, 78, 146], ['P-68', 92, 46, 81, 62], ['P-94', 67, 98, 66, 95], ['P-125', 68, 85, 91, 139], ['P-134', 80, 88, 97, 150],  ['P-142', 92, 74, 83, 169], ['P-145', 75, 106, 79, 66], ['P-168', 68, 87, 88, 109], ['P-183', 105, 72, 57, 37], ['P-211', 96, 95, 81, 142], ['P-215', 87, 89, 80, 126], ['P-217', 78, 74, 72, 97], ['P-219', 94, 61, 76, 57], ['P-273', 85, 79, 71, 127], ['P-274', 75, 88, 110, 114], ['P-282', 107, 92, 54, 147], ['P-283', 100, 97, 66, 79],  ['P-297', 103, 101, 68, 149], ['P-300', 97, 69, 101, 57], ['P-333', 100, 85, 72, 59], ['P-376', 101,101,89,73]]

da = []
for i in d:
    da.append({"name":i[0],"length":i[1],"width":i[2],"height":i[3],"weight":i[4],'isPriority':True,'delayCost':0,"priority "})
print(da)