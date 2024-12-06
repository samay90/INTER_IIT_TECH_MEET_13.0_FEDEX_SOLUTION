from ObjectPlotter import plotULD
def algo(packages,uld):
    packages_list = [i for i in range(len(packages))]
    to_fill_uld = uld
    filled = []
    layer = []
    y = 0
    k = 0
    weight = 0
    while True:
        i = packages[packages_list[k]]
        if (y>to_fill_uld.width):
            y=0;k=0;continue
        if ((y+i.width)>to_fill_uld.width):
            if (k+1>=len(packages_list)):
                y+=50;k=0;continue
            else:
                k+=1;continue
        y_com = y+(i.width/2)
        x_com = None
        z_com = None
        # // For x_com
        start_i_y = y
        end_i_y = y+i.width
        package_behind = None
        for j in layer:
            old_pkg = packages[j]
            
            start_j_y = old_pkg.COM[1]-(old_pkg.width/2)
            end_j_y = old_pkg.COM[1]+(old_pkg.width/2)
            if (((start_i_y>start_j_y and start_i_y<end_j_y) or (end_i_y>start_j_y and end_i_y<end_j_y) or (start_i_y<=start_j_y and end_i_y>=end_j_y)) ):
                if (package_behind):
                    if ((package_behind.COM[0]+(package_behind.length/2))<(old_pkg.COM[0]+(old_pkg.length/2))):
                        package_behind = old_pkg
                else:
                    package_behind = old_pkg
        if (package_behind):
            x_com = package_behind.COM[0]+(package_behind.length/2)+(i.length)/2
        else:
            x_com = (i.length)/2
        # //
        
        # // For z_com
        package_bottom = None
        corners = [(x_com-(i.length/2),y_com-(i.width/2)),(x_com+(i.length/2),y_com-(i.width/2)),(x_com+(i.length/2),y_com+(i.width/2)),(x_com-(i.length/2),y_com+(i.width/2))]
        for j in filled:
            old_pkg = packages[j]
            for corner in corners:
                if ((old_pkg.COM[0]+(old_pkg.length/2))>corner[0]>(old_pkg.COM[0]-(old_pkg.length/2)) and (old_pkg.COM[1]+(old_pkg.width/2))>corner[1]>(old_pkg.COM[1]-(old_pkg.width/2))):
                    if (package_bottom):
                        if ((package_bottom.COM[2]+(package_bottom.height/2))<(old_pkg.COM[2]+(old_pkg.height/2))):
                            package_bottom = old_pkg;break
                    else:
                        package_bottom = old_pkg;break
            if (corners[0][0]<old_pkg.COM[0]<corners[1][0] and corners[0][1]<old_pkg.COM[1]<corners[3][1]):
                if (package_bottom):
                    if ((package_bottom.COM[2]+(package_bottom.height/2))<(old_pkg.COM[2]+(old_pkg.height/2))):
                        package_bottom = old_pkg
                else:
                    package_bottom = old_pkg
        if (package_bottom):
            z_com = package_bottom.COM[2]+(package_bottom.height/2)+(i.height/2)
        else:
            z_com = (i.height)/2
        # //
        
        if (x_com+(i.length/2)>to_fill_uld.length):
            k+=1
            if (k+1>=len(packages_list)):
                y=0;
                k=0;
                layer=[]
            continue
        elif (z_com+(i.height/2)>to_fill_uld.height):
            k+=1
            if (not (k+1>=len(packages_list))):
                continue
            else:
                break
        else:
            weight+=i.weight
            if (weight>to_fill_uld.max_weight):
                break
            i.COM = (x_com,y_com,z_com)
            i.uld_name = to_fill_uld.name
            layer.append(packages_list[k])
            filled.append(packages_list[k])
            packages_list = packages_list[:k]+packages_list[k+1:]
            y = y+i.width
            k=0
            if (len(packages_list)==0):
                break
    total_vol = 0
    total_weight = 0
    data = []
    plotter_data = []
    for i in filled:
        pack = packages[i]
        total_vol+=pack.volume
        total_weight+=pack.weight
        data.append({"name":pack.name,"uld_name":pack.uld_name,"COM":pack.COM,"left_cord":(pack.COM[0]-pack.length/2,pack.COM[1]-pack.width/2,pack.COM[2]-pack.height/2),"right_cord":(pack.COM[0]+pack.length/2,pack.COM[1]+pack.width/2,pack.COM[2]+pack.height/2)})
        plotter_data.append([pack.name,[pack.COM[0],pack.COM[1],pack.COM[2]],[pack.length,pack.width,pack.height]])
    print(to_fill_uld.name,(total_vol/to_fill_uld.available_volume)*100,len(filled),total_weight)
    return data
    