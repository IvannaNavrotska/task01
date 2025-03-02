example = 'abbbbaaccccc'

def rle_coder(file):

    count = 0
    example_list = []
    
    for bite in file:
        example_list.append(bite)
    return example_list

print(rle_coder(example))
