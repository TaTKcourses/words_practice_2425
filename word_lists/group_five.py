def contains_reversed(file_path: str, encoding='UTF-8'):

    with open(file_path, 'r', encoding=encoding) as file:
        contents = file.read()
        contents_list = contents.split('\n')
        #print(type(contents_list))

    container = []
    for word in contents_list:
        if len(word) > 1:
            if word[::-1] in contents_list:
                container.append(word)

    return container

if __name__ == '__main__':
    test_path = 'top_freq_5000_hu.txt'
    print(contains_reversed(test_path))


