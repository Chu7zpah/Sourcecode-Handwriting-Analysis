import re

string_exist = re.compile(r'"(.*?)"')   # RE that checks is there any string(" ~ ") in code
comment_space = re.compile(r'//\s\S+.*')
comment_NO_space = re.compile(r'//\S+.*')
comment_multiline_in_one = re.compile(r'/\*\s\S+.*\s\*/')
comment_multiline_start = re.compile(r'/\*.*\n')
comment_multiline_end = re.compile(r'\*/\n')

def preprocess(file_path):
    f = open(file_path, 'r', encoding='utf-8')
    raw_line_list = f.readlines()
    no_string_line_list = []
    cleaned_line_list = []

    for raw_line in raw_line_list:
        # Exclude Strings
        if string_exist.search(raw_line) is None:
            no_string_line_list.append(raw_line)
        elif string_exist.search(raw_line) is not None:
            for string in string_exist.findall(raw_line):       
                no_string_line_list.append(raw_line.replace(f'"{string}"', '""')) 

    flag = 0
    for no_string_line in no_string_line_list:
        # Exclude One Line Comments
        if comment_space.search(no_string_line) is not None:
            for comment in comment_space.findall(no_string_line):
                cleaned_line_list.append(no_string_line.replace(f'{comment}', f'// {comment[3]}'))
        elif comment_NO_space.search(no_string_line) is not None:
            for comment in comment_NO_space.findall(no_string_line):
                cleaned_line_list.append(no_string_line.replace(f'{comment}', f'//{comment[2]}'))
        elif comment_multiline_in_one.search(no_string_line) is not None:
            for comment in comment_multiline_in_one.findall(no_string_line):
                cleaned_line_list.append(no_string_line.replace(f'{comment}', '/* */'))
        # Exclude Multi Line Comments
        elif comment_multiline_start.search(no_string_line) is not None:
            for comment in comment_multiline_start.findall(no_string_line):
                cleaned_line_list.append(no_string_line.replace(f'{comment}', '/*\n'))
            flag = 1
        elif flag:
            if comment_multiline_end.search(no_string_line) is not None:
                for comment in comment_multiline_end.findall(no_string_line):
                    cleaned_line_list.append('    */')
                flag = 0
            else:
                continue
        else:
            cleaned_line_list.append(no_string_line)


    return cleaned_line_list