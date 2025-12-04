"""
Day 2 for the 2025 Advent of Code challenge. I must write a script that finds numbers with repeating
patterns (e.g. 11, 99, 1010, 1188511885, etc.) within a set of ranges, then return the sum of all the
repeating numbers in all of the ranges.
"""

input = '61-71,12004923-12218173,907895-1086340,61083-74975,7676687127-7676868552,3328-4003,48-59,3826934-3859467,178-235,75491066-75643554,92-115,1487-1860,483139-586979,553489051-553589200,645895-722188,47720238-47818286,152157-192571,9797877401-9798014942,9326-11828,879837-904029,4347588-4499393,17-30,1-16,109218-145341,45794-60133,491-643,2155-2882,7576546102-7576769724,4104-5014,34-46,67594702-67751934,8541532888-8541668837,72-87,346340-480731,3358258808-3358456067,78265-98021,7969-9161,19293-27371,5143721-5316417,5641-7190,28793-36935,3232255123-3232366239,706-847,204915-242531,851-1135,790317-858666'

def find_paired_ranges(ids: str)->list:
    """
    Given a string of ID ranges denoted by hyphens and separated by commas, returns a list of
    tuples, each with a pair of strings denoting the lower and upper bounds of the range.
    """
    id_ranges = ids.split(',') # ranges as strings with hyphens

    paired_ranges = []
    for id in id_ranges:
        paired_ranges.append(id.split('-')) # ranges as pairs of numerical strings

    return paired_ranges

def elaborate_ranges(pairs: list)->list:
    """
    Given a list of paired numerical strings representing the lower and upper bounds of a range,
    returns a list of numerical strings representing all integers within the ranges.
    """
    # convert ID bounds to ints so we can extract all IDs within the bounds
    all_id_ints = []
    for i in range(len(pairs)):
        all_id_ints.append(list(range(int(pairs[i][0]), int(pairs[i][1])+1)))
    
    # convert all IDs back to strings for ease of finding similarity
    all_id_strings = []
    for sublist in all_id_ints:
        for num in sublist:
            all_id_strings.append(str(num))

    return all_id_strings

def identify_invalid_ids_v1(strings: list)->list:
    """
    An ID is considered invalid if it is made only of two repeating patterns. Given a list of strings, returns a list
    of strings made of only two repeating patterns.
    """
    # only keep even-length strings since odd-length strings cannot have tandem similarity
    even_strings = []
    for string in strings:
        if len(string) % 2 == 0:
            even_strings.append(string)
    
    # if the first half of a string matches the second half, append it to the invalid list
    invalid_id = []
    for string in even_strings:
        if string[0:(len(string)//2)] == string[(len(string)//2):]:
            invalid_id.append(string)
    
    return invalid_id

def identify_invalid_ids_v2(strings: list)->list:
    """
    An ID is considered invalid if it is made only of repeating patterns of any length or number. Given a list of strings, returns a list
    of strings made of only repeating patterns.
    """
    
    # if the first half of a string matches the second half, append it to the invalid list
    invalid_id = []
    for string in strings:
        if string[0:(len(string)//2)] == string[(len(string)//2):]:
            invalid_id.append(string)
            continue
        elif string[0:(len(string)//2-1)] == string[]
    
    return invalid_id

def invalid_id_sum(invalid_ids: list)->int:
    """
    Given a list of numerical strings, converts the strings to integers and returns the sum.
    """

    # convert invalid ID strings to int
    invalid_id_ints = []
    for id in invalid_ids:
        invalid_id_ints.append(int(id))
    
    return sum(invalid_id_ints) # sum for the final answer form


# test
test = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

pairs = find_paired_ranges(test)

strings = elaborate_ranges(pairs)

invalid_ids = identify_invalid_ids(strings)

assert(invalid_id_sum(invalid_ids) == 1227775554)

# solution
print(invalid_id_sum(identify_invalid_ids(elaborate_ranges(find_paired_ranges(input)))))