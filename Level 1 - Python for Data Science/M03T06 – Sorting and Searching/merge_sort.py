'''
A set of two functions to search through strings and return a sorted list by length of each string from longest to shortest
'''

def merge_sort(items): 
    items_length = len(items) 
    temporary_storage = [None] * items_length 
    size_of_subsections = 1 

    while size_of_subsections < items_length: 
        for i in range(0, items_length, size_of_subsections * 2): 
            first_section_start = i
            first_section_end = min(i + size_of_subsections, items_length)
            second_section_start = first_section_end
            second_section_end = min(first_section_end + size_of_subsections, items_length)
            sections = (first_section_start, first_section_end), (second_section_start, second_section_end)
            merge(items, sections, temporary_storage)
        size_of_subsections *= 2 

    return items

def merge(items, sections, temporary_storage): 
    (first_section_start, first_section_end), (second_section_start, second_section_end) = sections 
    left_index = first_section_start 
    right_index = second_section_start 
    temp_index = 0 

    while left_index < first_section_end or right_index < second_section_end: 
        if left_index < first_section_end and right_index < second_section_end: 
            # Compare by length instead of number value
            if len(items[left_index]) > len(items[right_index]): 
                temporary_storage[temp_index] = items[left_index] 
                left_index += 1 
            else: 
                temporary_storage[temp_index] = items[right_index] 
                right_index += 1 
            temp_index += 1 
        elif left_index < first_section_end: 
            for i in range(left_index, first_section_end): 
                temporary_storage[temp_index] = items[left_index] 
                left_index += 1 
                temp_index += 1 
        else: 
            for i in range(right_index, second_section_end): 
                temporary_storage[temp_index] = items[right_index]
                right_index += 1 
                temp_index += 1

    for i in range(temp_index): 
        items[first_section_start + i] = temporary_storage[i]

# Example usages:

flowers_list = ['Rose', 'Tulip', 'Lily', 'Daffodil', 'Sunflower', 'Orchid', 'Peony', 'Daisy', 'Chrysanthemum', 'Lavender', 'Geranium', 'Protea', 'Bluebells']
sorted_flowers_list = merge_sort(flowers_list)
print(sorted_flowers_list)  

dinosaurs_list = ['Dilong', 'Pegomastax', 'Linhenykus', 'Epidendrosaurus', 'Longisquama', 'Minmi', 'Graciliceratops', 'Masiakasaurus', 'Microraptor', 'Amargasaurus', 'Yutyrannus', 'Psittacosaurus']
sorted_dinos_list = merge_sort(dinosaurs_list)
print(sorted_dinos_list)  

team_list = ['Hardy', 'Ryan', 'Kevin', 'John', 'Mark', 'Gus', 'Daniel', 'James', 'Stephen', 'Greg']
sorted_team_list = merge_sort(team_list)
print(sorted_team_list)  