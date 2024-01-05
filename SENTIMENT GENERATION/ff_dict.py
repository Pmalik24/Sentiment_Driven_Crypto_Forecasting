from copy import copy
def create_dict_from_file(file_path):
    with open(file_path, 'r') as file:
        text = file.readlines()
        
        ff_dict = {}

        for line in text:
            short, full = line.strip().split('\t')
            ff_dict[short] = full
    
        ff_dict['ATH'] = 'All Time High'
        ff_dict['FUD'] = 'Fear, Uncertainity, and Doubt'
        return ff_dict

def ff_2_dict(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    crypto_dict = {}
    
    for line in lines:
        # Split the line into abbreviation and full form
        abbreviation, full_form = line.strip().split(' : ')
        crypto_dict[abbreviation] = full_form

    return crypto_dict

def merge():
    dict1 = create_dict_from_file('./fullforms.txt')
    dict2 = ff_2_dict('./ff2.txt')
    merged_dict = dict1  # Start with dict1's keys and values
    for key, value in dict2.items():  # Go over dict2's keys and values
        if key not in merged_dict:  # If key is not in dict1, add it to the merged_dict
            merged_dict[key] = value

    merged_dict = dict(sorted(merged_dict.items()))
    
    return merged_dict

if __name__ == '__main__':
    final_dict = merge()
    

    for x, y in final_dict.items():
        print(f'Key: {x}\nValue: {y}\n')




    

