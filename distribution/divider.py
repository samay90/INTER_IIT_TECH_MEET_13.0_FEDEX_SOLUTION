from distribution.logic import algo
from distribution.task1 import task1
from distribution.task2 import task2
def filter_filled(packages):
    # Filters the non-assigned packages
    remained = []
    for i in packages: 
        if (not i.uld_name):
            remained.append(i)
    return remained
def filter_priority(packages):
    # Filter the priority packages
    packages = []
    for i in range(len(packages)):
        if packages[i].is_priority:
            packages.append(i)
    return packages

def distibute(packages):
    # Distribute the packages priority and non priority
    non_priority_packages = []
    priority_packages = []
    for package in packages:
        if package.is_priority:
            priority_packages.append(package)
        else:
            non_priority_packages.append(package)
    return priority_packages+non_priority_packages

def filter_non_priority(packages):
    # Filter the non priority packages
    new_packages = []
    for i in range(len(packages)):
        if (not packages[i].is_priority) and (not packages[i].COM):
            new_packages.append(packages[i])
    return new_packages
ans = []
def divider(ulds,packages):
    # Converts the objects for task1
    ulds_list = []
    for uld in ulds:
        ulds_list.append([uld.name,uld.length,uld.width,uld.height,uld.max_weight])
        
    # Finds the best sutiable ULD for the priority packages
    priority_packages = []    
    for package in packages:
        if package.is_priority:
            priority_packages.append([package.name,package.length,package.width,package.height,package.weight])
    ulds_for_priority = task1(ulds_list,priority_packages)
    
    # Stacks the priority packages into the best ULD and 2nd priority to economy packages
    for i in range(len(ulds_for_priority)):
        ans.extend(algo(distibute(filter_filled(packages)),ulds[ulds_for_priority[i]]))
        
    # Filters the un-used ulds
    ulds_remained = []
    for i in range(len(ulds)):
        if i not in ulds_for_priority:
            ulds_remained.append(ulds[i])
    
    non_priority_packages = filter_non_priority(packages)
    non_priority_packages_task2 = []
    ulds_remained_task2 = []
    for i in ulds_remained:
        ulds_remained_task2.append([i.name,i.length,i.width,i.height,i.max_weight])
    for i in non_priority_packages:
        non_priority_packages_task2.append([i.name,i.length*i.width*i.height,i.weight,i.delay_cost])
    task2_output = []
    if (len(non_priority_packages_task2)>0 and len(ulds_remained_task2)>0):
        task2_output = task2(non_priority_packages_task2,ulds_remained_task2)
    prior_economy = []
    for i in range(len(task2_output)):
        prior_economy.append(non_priority_packages[non_priority_packages_task2.index(task2_output[i])])
    non_considered_priority_packages = []
    for i in non_priority_packages:
        if i not in prior_economy:
            non_considered_priority_packages.append(i)
    final_economy = prior_economy+non_considered_priority_packages
    # Stacks the remained packages
    for i in range(len(ulds_remained)):
        ans.extend(algo(filter_filled(filter_priority(packages)+final_economy),ulds_remained[i]))
        
    return ans
        
    