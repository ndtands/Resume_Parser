import re
pattern_email = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)+$'
EX = ["EX_COMPANY","EX_DESCRIPTION","EX_END_DATE","EX_LOCATION","EX_POSITISION","EX_START_DATE"]
CER = ["CER_DATE","CER_NAME"]
EDU =['EDU_DEGREE','EDU_UNIVERSITY','EDU_END_DATE','EDU_START_DATE']
PROJECT = ['PROJECT_DESCRIPTION','PROJECT_END_TIME','PROJECT_NAME','PROJECT_START_TIME']

def get_text(infos: list) -> str:
    if infos == []:
        return ''
    return ' '.join([i[1] for i in infos])


def get_list(infos: list) -> list:
    if infos == []:
        return []
    return [i[1] for i in infos]


def get_email(info_email: list, info_url: list) -> str:
    emails = [i[1] for i in info_email]
    urls = [i[1] for i in info_url]
    if emails != []:
        return ' '.join(emails[0])
    else:
        for url in urls:
            if re.fullmatch(pattern_email, url):
                return url
    return ''

def check_distance(box1: list, box2: list, x_thesh: int=10, y_thresh: int=4) -> bool:
    w_dist = abs(box2[0]-box1[2])
    h_dist = abs(box1[1]-box2[1])
    return w_dist < x_thesh and h_dist <x_thesh


def get_detail(detail: list) -> list:
    if detail == []:
        return []
    curr_tag = detail[0][2]
    curr_word = detail[0][1]
    out = []
    for info in detail[1:]:
        tag = info[2]
        word = info[1]
        if tag == curr_tag:
            curr_word = curr_word + ' ' + word
        else:
            out.append((curr_word,curr_tag))
            curr_tag = tag
            curr_word = word
    out.append((curr_word,curr_tag))

    list_dict = []
    temp = dict()
    tag_start = out[0][1]
    for info in out:
        words = info[0]
        tag = info[1]
        if tag not in temp:
            temp[tag] = words
        else:
            if tag == tag_start:
                list_dict.append(temp)
                temp = dict()
                temp[tag] = words
            else:
                temp[tag] += words
    list_dict.append(temp)
    return list_dict

def get_list_advance(info: list) -> list:
    if info == []:
        return []
    lists = []
    temp = info[0][1]
    for i in range(len(info) - 1):
        if check_distance(info[i][0], info[i+1][0]):
            temp += f" {info[i+1][1]}"
        else:
            lists.append(temp)
            temp = info[i+1][1]
    lists.append(temp)
    return lists