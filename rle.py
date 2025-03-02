example = 'abbbbaaccccc'


def rle_coder(example):

    rle_file = ''
    
    count = 1

    for i in range(1, len(example)):
        if example[i] == example[i-1]:
            count +=1
        else:
            rle_file += f'{example[i-1]}{count}'

            count = 1
            
    rle_file += f'{example[-1]}{count}'

    return rle_file

print(rle_coder(example))

