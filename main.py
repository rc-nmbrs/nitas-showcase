# Rafael Chavez

import pandas as pd

min_occurring_item = -1
max_occurring_item = 0
file_name = "puzzle3.txt"


def filter_puzzleList(content_list):
    filtered_list = list(filter(None, content_list))

    return filtered_list


def get_puzzle3Data(file_name):
    puzzle1_file = open(file_name, "r")
    puzzle1_content = puzzle1_file.read()
    content_list = puzzle1_content.split("\n")
    content_list = filter_puzzleList(content_list)

    return content_list


def split_binary(binary_data):
    binary_rows_list = []

    for binary in binary_data:
        binary_rows_list.append(list(binary))
    return binary_rows_list


def create_binary_df(split_binary):
    df = pd.DataFrame(split_binary)
    df.columns = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven']

    return df


def build_subDF01(df1):
    col = 0
    col_str = df1.columns.values

    while (len(df1.index) > 1) & (col <= len(df1.columns)):
        df1 = df1.loc[df1[col_str[col]] == '1']
        col += 1

    return df1


def max_occurance_rate(df, max_occuring_item):
    fin_binary_list = []

    # Adds most occuring option in column, in this case
    # the most common binary value in a dataframe column
    # gets added to list fin_binary_list
    for col in df.columns:
        # .value_counts() returns frequency of unique values in a df
        # column, in descending order. Meaning, highest occuring
        # item is at index 0
        fin_binary_list.append(df[col].value_counts().index[max_occuring_item])
    return fin_binary_list


def min_occurance_rate(df, min_occuring_item):
    fin_binary_list = []
    # Adds most occuring option in column, in this case
    # the most common binary value in a dataframe column
    # gets added to list fin_binary_list
    for col in df.columns:
        # .value_counts() returns frequency of unique values in a df
        # column, in descending order. Meaning, highest occuring
        # item is at index 0

        fin_binary_list.append(df[col].value_counts().index[min_occuring_item])
        # If .value_counts() == 1,
        # for row in column:
        #      if row_index = 1
        #            df[col:row_index].append()

    return fin_binary_list


def convert_string_list(fin_binary_list):
    content_listInt = [int(i) for i in fin_binary_list]

    return content_listInt


def binary_toDec(content_listInt):
    binaryInt = int(''.join(content_listInt), 2)

    return binaryInt


# Store file object in binary_data
binary_data = get_puzzle3Data(file_name)

# Create dataframe
bin_df = create_binary_df(split_binary(binary_data))

'''count = convert_string_list(occurance_rate(bin_df))'''
# Create binary representation of highest occuring values
# in any df column (max, min)
gamma_rate = (max_occurance_rate(bin_df, 0))
epsilon_rate = (min_occurance_rate(bin_df, -1))
g_rate_binaryDec = binary_toDec(gamma_rate)
e_rate_binaryDec = binary_toDec(epsilon_rate)

power_consumption = g_rate_binaryDec * e_rate_binaryDec

print("Gamma Rate: " + str(g_rate_binaryDec))
print("Epsilon Rate: " + str(e_rate_binaryDec))
print("Power Consumption: " + str(power_consumption))

final = build_subDF01(bin_df)
print(final)




