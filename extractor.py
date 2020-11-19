'''
    [ Sourcecode Handwriting Characteristics Extractor ]
        From Source Code(C Based) -> CSV
        Made by Chu7zpah
      
      <Features>
        Feature 1. Brace('{') Habits
            case 1: 'FUNCTION(){'       (inline brace with NO Space)
            case 2: 'FUNCTION() {'      (inline brace with Space)
            case 3: 'FUNCTION()         (next line brace)
                     {'          

        Feature 2. Comment('//' or '/* */') Habits
            case 1: '//COMMENT'         ('//' with NO Space)
            case 2: '// COMMENT'        ('//' with Space)
            case 3: '/* COMMENT */'     (using '/* */')

        Feature 3. Parenthesis('(') Habits
            case 1: '{if/switch/while/for}('    (Reserved words with No Space)
            case 2: '{if/switch/while/for} ('   (Reserved words with Space)

        Feature 4. Unary Operator(Type Casting) Habits
            case 1: '(TYPE)VARIABLE'        (Type Casting with NO Space)
            case 2: '(TYPE) VARIABLE'       (Type Casting with Space)
        
        Feature 5. Binary Operator(Arithmetic, Assignments, etc.) Habits
            ex) '+' Operator
            case 1: 'VARIABLE+VARIABLE'     (NO Space && Binary Operator && NO Space)
            case 2: 'VARIABLE+ VARIABLE'    (NO Space && Binary Operator && Space)
            case 3: 'VARIABLE +VARIABLE'    (Space && Binary Operator && NO Space)
            case 4: 'VARIABLE + VARIABLE'   (Space && Binary operator && Space)
'''

import re

def extract(features_list, line_list):
    # <Extracted Feature Data Dictionary>
    features_data_dictionary = {}
    for feature in features_list:       # Initialize counting variables
        features_data_dictionary[f'{feature}_count'] = 0

    # <Feature RE Expressions>
    inline_NO_brace = re.compile(r'[\)|\S]\{')       # 'Function(){' (RE: '\)\{')  OR  'struct{' (RE: \S\{)
    inline_YES_brace = re.compile(r'[\)|\S]\s+\{')   # 'Function() {' (RE: '\)\s+\{')  OR  'struct {' (RE: \S\s+\{)
    nextline_brace = re.compile(r'\s*\{')            # 'ENTER' + '{' (RE: '\s*\{')

    double_backslash_NO_Space = re.compile(r'//\S')      # '//Comment'
    double_backslash_YES_Space = re.compile(r'//\s+\S')  # '// Comment'
    single_backslash_asterisk = re.compile(r'/\*')       # '/* Comment */'

    NO_parenthesis = re.compile(r'if\(|switch\(|for\(|while\(')                  # '{if/switch/while/for}('
    YES_parenthesis = re.compile(r'if\s+\(|switch\s+\(|for\s+\(|while\s+\(')     # '{if/switch/while/for} ('

    # Type list for Unary Operator(Type Casting)
    type_list = ['char', 'short', 'int', 'long', 'long long', 
                'unsigned char', 'unsigned short', 'unsigned int', 'unsigned long',
                'float', 'double', 'long double']

    # Operator list for Binary Opeartors
    operator_list = [   r'\+', '-', r'\*', '/', '%',     # Arithmetic
                        '=', r'\+=', '-=', r'\*=', '/=', '%=', 
                        '&=', '^=', r'\|=', '<<=', '>>=', '>>>=', # Assignment
                        '==', '!=', '>', '<', '>=', '<=',       # Comparison
                        '&&', r'\|\|',    # Logical
                        '>>', '<<', '>>>', # Shift
                        ';', ',', '",']  # ';' in for loop, ',' in function call


    # <Analyzing Source Code>
    for line in line_list:
        # Feature Extraction
        #   (Feature 1 - Brace)
        if inline_NO_brace.search(line) is not None:
            features_data_dictionary['inline_NO_brace_count'] += 1
        elif inline_YES_brace.search(line) is not None:
            features_data_dictionary['inline_YES_brace_count'] += 1
        elif nextline_brace.search(line) is not None:
            features_data_dictionary['nextline_brace_count'] += 1

        #   (Feature 2 - Comment)
        if double_backslash_NO_Space.search(line) is not None:
            features_data_dictionary['double_backslash_NO_Space_count'] += 1
        elif double_backslash_YES_Space.search(line) is not None:
            features_data_dictionary['double_backslash_YES_Space_count'] += 1
        elif single_backslash_asterisk.search(line) is not None:
            features_data_dictionary['single_backslash_asterisk_count'] += 1

        #   (Feature 3 - Parenthesis)
        if NO_parenthesis.search(line) is not None:
            features_data_dictionary['NO_parenthesis_count'] += 1
        elif YES_parenthesis.search(line) is not None:
            features_data_dictionary['YES_parenthesis_count'] += 1

        #   (Feature 4 - Unary Operator)
        for data_type in type_list:
            unary_NO_space = re.compile(rf'\({data_type}\)\S')
            unary_YES_space = re.compile(rf'\({data_type}\)\s+\S')
            
            if unary_NO_space.search(line) is not None:
                features_data_dictionary['unary_NO_space_count'] += 1
            elif unary_YES_space.search(line) is not None:
                features_data_dictionary['unary_YES_space_count'] += 1

        #   (Feature 5 - Binary Operator)
        for operator in operator_list:
            NO_binary_NO = re.compile(rf'(\w|\)|\]){operator}(\w|\(|\[)')
            NO_binary_YES = re.compile(rf'(\w|\)|\]){operator}\s+(\w|\(|\[)')
            YES_binary_NO = re.compile(rf'(\w|\)|\])\s+{operator}(\w|\(|\[)')
            YES_binary_YES = re.compile(rf'(\w|\)|\])\s+{operator}\s+(\w|\(|\[)')

            if NO_binary_NO.search(line) is not None:
                features_data_dictionary['NO_binary_NO_count'] += 1
            elif NO_binary_YES.search(line) is not None:
                features_data_dictionary['NO_binary_YES_count'] += 1
            elif YES_binary_NO.search(line) is not None:
                features_data_dictionary['YES_binary_NO_count'] += 1
            elif YES_binary_YES.search(line) is not None:
                features_data_dictionary['YES_binary_YES_count'] += 1

    return features_data_dictionary