import csv
import os

from preprocessor import preprocess

double_quote_feature_list = []      # Feature list for CSV feature columns
programmer_list = ['A', 'B', 'C']   # dataset labels(classes)
features_list = [
                    'inline_NO_brace', 'inline_YES_brace', 'nextline_brace', # Feature 1. Brace
                    'double_backslash_NO_Space', 'double_backslash_YES_Space', 'single_backslash_asterisk', # Feature 2. Comment
                    'NO_parenthesis', 'YES_parenthesis', # Feature 3. Parenthesis
                    'unary_NO_space', 'unary_YES_space', # Feature 4. Unary Operator
                    'NO_binary_NO', 'NO_binary_YES', 'YES_binary_NO', 'YES_binary_YES'  # Feature 5. Binary Opeartor
                ]

data_path = 'C:/Users/Nyx_24/Desktop/Dataset/'

# Making CSV's First Row (Feature Name Row)
for feature in features_list:
    double_quote_feature_list.append(feature.replace(f'{feature}', f'"{feature}"')) 
double_quote_feature_list.append(r'"Programmer"')
csv_file = open('./CSVResult/Code_Handwriting_data.csv', 'w', encoding='utf-8')
wr = csv.writer(csv_file, quotechar="'")    # quotechar = '' (If not, " becomes """)
wr.writerow(double_quote_feature_list)

for programmer in programmer_list:
    for (path, dir, files) in os.walk(f'{data_path}{programmer}'):
        for filename in files:
            preprocessed_line_list = []
            ext = os.path.splitext(filename)[-1]
            if ext == '.c':
                full_directory = path + '/' + filename
                full_directory = full_directory.replace('\\', '/')
                preprocessed_line_list = preprocess(full_directory)
            ### HERE! ###
            
            else:
                continue

csv_file.close()