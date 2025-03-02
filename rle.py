example = 'abbbbaaccccc'


def rle_coder(example):

    rle_file = ''
    
    count = 1

    for i in range(1, len(example)):
        if example[i] == example[i-1]:
            count +=1
        else:
            rle_file += f'{int(count)}{example[i-1]}'

            count = 1
            
    rle_file += f'{int(count)}{example[-1]}'

    return rle_file

print(rle_coder(example))


def rle_decoder(example):

    file = ''
    i = 0

    while i < len(example):
        count = ''
        while i < len(example) and example[i].isdigit():
            count += example[i]
            i += 1

        if i < len(example):
            file += example[i] * int(count) 
            i += 1

    return file
    

print(rle_decoder(rle_coder(example)))
    



