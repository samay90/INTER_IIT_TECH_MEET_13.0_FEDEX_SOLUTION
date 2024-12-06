def task1(uld, priority_packages):
    volume_uld_sorted_decreasing_order=[]
    for i in range(len(uld)):
        vol=uld[i][1]*uld[i][2]*uld[i][3]
        ans=(vol,i+1)
        volume_uld_sorted_decreasing_order.append(ans)
    volume_uld_sorted_decreasing_order.sort()
    volume_uld_sorted_decreasing_order.reverse()

    weight_limit_uld_sorted_decreasing_order=[]
    for m in range(len(uld)):
        ans=(uld[m][4],m+1)
        weight_limit_uld_sorted_decreasing_order.append(ans)
    weight_limit_uld_sorted_decreasing_order.sort()
    weight_limit_uld_sorted_decreasing_order.reverse()
    total_volume_priority_packages=0
    for i in range(len(priority_packages)):
        volume=priority_packages[i][1]*priority_packages[i][2]*priority_packages[i][3]
        total_volume_priority_packages+=volume

    total_weight_priority_packages=0
    for j in range(len(priority_packages)):
        weight=priority_packages[j][4]
        total_weight_priority_packages+=weight
    min_uld_volume=0
    min_uld_weight=0
    i=0
    j=0
    while(min_uld_volume <= total_volume_priority_packages):
        min_uld_volume+= volume_uld_sorted_decreasing_order[i][0]
        i+=1
    while(min_uld_weight <= total_weight_priority_packages):
        min_uld_weight+=weight_limit_uld_sorted_decreasing_order[j][0]
        j+=1

    minimum_ulds_for_priority_packages= max(i,j)
    v_duplicate=list(volume_uld_sorted_decreasing_order)
    w_duplicate=list(weight_limit_uld_sorted_decreasing_order)
    v=0
    while(v<=total_volume_priority_packages):
        v=0
        for i in range(len(v_duplicate)-1,len(v_duplicate)-minimum_ulds_for_priority_packages-1,-1):
            v=v+v_duplicate[i][0]
        x=v_duplicate.pop()
    v_duplicate.append(x)
    w=0
    while(w<=total_weight_priority_packages):
        w=0
        for i in range(len(w_duplicate)-1,len(w_duplicate)-minimum_ulds_for_priority_packages-1,-1):
            w=w+w_duplicate[i][0]
        y=w_duplicate.pop()
    w_duplicate.append(y)
    v_uld=[]
    w_uld=[]
    for i in range(len(v_duplicate)):
        v_uld.append(v_duplicate[i][1])
    for j in range(len(w_duplicate)):
        w_uld.append(w_duplicate[j][1])
    ulds_assigned_for_priority_packages=[]
    l=[]
    while (len(v_uld)!=0 and len(w_uld)!=0 and len(ulds_assigned_for_priority_packages)!=minimum_ulds_for_priority_packages):
        x=v_uld.pop()
        if x in l:
            ulds_assigned_for_priority_packages.append(x)
        else:
            l.append(x)
        y=w_uld.pop()
        if y in l:
            ulds_assigned_for_priority_packages.append(y)
        else:
            l.append(y)
    return ulds_assigned_for_priority_packages
