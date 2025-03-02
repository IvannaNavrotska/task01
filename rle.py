import sys
import os


def RLE_encoder(data: bytes) -> bytes:

    restriction = 5 #обмеження для стискання послідовності різних символів
    
    i = 0
    n = len(data)
    output = bytearray()
    
    while i < n:  #накопичення однакових символів (>= 2)
        run_len = 1
        run_byte = data[i]
        
        j = i + 1
        while j < n and data[j] == run_byte and run_len < 129:
            run_len += 1
            j += 1
        
        if run_len >= 2:
            L = 128 + (run_len - 2)  #послідовність з однакових символів
            output.append(L)
            output.append(run_byte)
            i += run_len
            
        else:  
            unique = [run_byte] #послідовність з неповторюваних символів
            i += 1          
            while i < n and len(unique) < restriction:
                if i + 1 < n and data[i] == data[i+1]: 
                    unique.append(data[i])
                    i += 1
                    break
                else:
                    unique.append(data[i])
                    i += 1
            
            L = len(unique) - 1 
            output.append(L)
            output.extend(unique)
    
    return bytes(output)



def RLE_decoder(encoded: bytes) -> bytes:
    
    i = 0
    n = len(encoded)
    output = bytearray()
    
    while i < n:
        if i >= n:
            break  
        L = encoded[i]
        i += 1
        
        if L < 128:
            length = L + 1  #для різних символів
            if i + length > n:
                raise ValueError('неповнивний блок для різних байтів')
            block = encoded[i : i + length]
            output.extend(block)
            i += length
        else:
            length = (L - 128) + 2  #кількість однакових символів
            if i >= n:
                raise ValueError('неповнивний блок для різних байтів')
            repeated_byte = encoded[i]
            i += 1
            output.extend([repeated_byte]*length)
    
    return bytes(output)



def encode_file(in_filename: str, out_filename: str = None) -> None:
    
    if not out_filename:
        out_filename = in_filename + '.rle'
    
    with open(in_filename, 'rb') as f_in:
        data = f_in.read()
    
    encoded = RLE_encoder(data)
    
    with open(out_filename, 'wb') as f_out:
        f_out.write(encoded)
    
    print(f"файл '{in_filename}' закодовано у '{out_filename}'.")



def decode_file(in_filename: str, out_filename: str = None) -> None:
   
    if not out_filename:
        if in_filename.endswith('.rle'):
            out_filename = in_filename[:-4]
        else:
            out_filename = in_filename + '.decoded'
    
    with open(in_filename, 'rb') as f_in:
        encoded_data = f_in.read()
    
    with open(out_filename, 'wb') as f_out:
        f_out.write(decoded)
    
    print(f"Файл '{in_filename}' декодовано у '{out_filename}'.")






def main():
   
    if len(sys.argv) < 3:
        print('Використання:')
        print('rle.py encode <in_file> [out_file]')
        print('rle.py decode <in_file> [out_file]')
        sys.exit(1)
    
    mode = sys.argv[1]
    in_file = sys.argv[2]
    out_file = sys.argv[3] if len(sys.argv) > 3 else None
    
    if mode == 'encode':
        encode_file(in_file, out_file)
    elif mode == 'decode':
        decode_file(in_file, out_file)
    else:
        print('Неправильна команда')


if __name__ == "__main__":

    if len(sys.argv) == 1:
        original_data = b'acdefghgrtwaaaBBBcDDDDDDDDDDDeeeeeeeeeeffffffgggggggh'  
        print('оригінальні дані:', original_data)
        
        encoded = RLE_encoder(original_data)
        print('закодовано (hex):', encoded.hex())
        
        decoded = RLE_decoder(encoded)
        
        print('розкодовано:', decoded)
        print("Співпадають?", decoded == original_data)
        
