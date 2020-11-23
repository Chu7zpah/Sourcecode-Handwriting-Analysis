'''
    Made by Chu7zpah
    Normalizing Values from integers(Count) to Ratio(of brace, comment, etc.)
'''

def new_normalize(features_data_dictionary):
    brace_total =         features_data_dictionary['inline_NO_brace_count'] \
                        + features_data_dictionary['inline_YES_brace_count'] \
                        + features_data_dictionary['nextline_brace_count']
    comment_total =       features_data_dictionary['double_backslash_NO_Space_count'] \
                        + features_data_dictionary['double_backslash_YES_Space_count'] \
                        + features_data_dictionary['single_backslash_asterisk_count']
    parenthesis_total =   features_data_dictionary['NO_parenthesis_count'] \
                        + features_data_dictionary['YES_parenthesis_count']
    unary_total =         features_data_dictionary['unary_NO_space_count'] \
                        + features_data_dictionary['unary_YES_space_count']
    binary_total =        features_data_dictionary['NO_binary_NO_count'] \
                        + features_data_dictionary['NO_binary_YES_count'] \
                        + features_data_dictionary['YES_binary_NO_count'] \
                        + features_data_dictionary['YES_binary_YES_count']
    if not brace_total:
        pass
    else:
        features_data_dictionary['inline_NO_brace_count'] /= brace_total
        features_data_dictionary['inline_YES_brace_count'] /= brace_total
        features_data_dictionary['nextline_brace_count'] /= brace_total
    
    if not comment_total:
        pass
    else:
        features_data_dictionary['double_backslash_NO_Space_count'] /= comment_total
        features_data_dictionary['double_backslash_YES_Space_count'] /= comment_total
        features_data_dictionary['single_backslash_asterisk_count'] /= comment_total

    if not parenthesis_total:
        pass
    else:
        features_data_dictionary['NO_parenthesis_count'] /= parenthesis_total
        features_data_dictionary['YES_parenthesis_count'] /= parenthesis_total

    if not unary_total:
        pass
    else:
        features_data_dictionary['unary_NO_space_count'] /= unary_total
        features_data_dictionary['unary_YES_space_count'] /= unary_total

    if not binary_total:
        pass
    else:
        features_data_dictionary['NO_binary_NO_count'] /= binary_total
        features_data_dictionary['NO_binary_YES_count'] /= binary_total
        features_data_dictionary['YES_binary_NO_count'] /= binary_total
        features_data_dictionary['YES_binary_YES_count'] /= binary_total

    return features_data_dictionary


