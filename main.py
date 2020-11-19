import csv
import os

# from sklearn.preprocessing import StandardScaler
from preprocessor import preprocess
from extractor import extract

double_quote_feature_list = []      # Feature list for CSV feature columns
programmer_list = ['L']
#programmer_list = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K']   # dataset labels(classes)
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
csv_file = open('./CSVResult/L_added.csv', 'w', newline='', encoding='utf-8')
wr = csv.writer(csv_file, quotechar="'")    # quotechar = '' (If not, " becomes """)
wr.writerow(double_quote_feature_list)

for programmer in programmer_list:
    for (path, dir, files) in os.walk(f'{data_path}{programmer}'):
        for filename in files:
            preprocessed_line_list = []     # list for preprocessed codes (without strings, comments)
            features_data_dictinoary = {}   # dictionary for extracted features data
            features_data_list = []         # list for feature data values

            ext = os.path.splitext(filename)[-1]
            if ext == '.c':
                full_directory = path + '/' + filename
                full_directory = full_directory.replace('\\', '/')
                
                print(full_directory)
                
                preprocessed_line_list = preprocess(full_directory) # Preprocessing
                features_data_dictinoary = extract(features_list, preprocessed_line_list)   # Extraction

                for feature in features_data_dictinoary:
                    features_data_list.append(features_data_dictinoary[feature])
                features_data_list.append(f'{programmer}')
                wr.writerow(features_data_list) # Writing Data on CSV File

            else:
                continue
        
            print("done")
csv_file.close()