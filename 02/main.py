import re

def get_ints(s):
    return list(map(int, re.findall("\d+", s)))

def wrapping_paper_area(l,w,h):
    #orient box so lxw is the smallest side
    l,w,h = sorted((l,w,h))
    return 2*l*w + 2*w*h + 2*h*l + l*w

def ribbon_length(l,w,h):
    l,w,h = sorted((l,w,h))
    return 2*(l+w) + l*w*h

total_area = 0
total_length = 0
with open("input") as file:
    for line in file:
        dimensions = get_ints(line)
        total_area += wrapping_paper_area(*dimensions)
        total_length += ribbon_length(*dimensions)

print(total_area)
print(total_length)