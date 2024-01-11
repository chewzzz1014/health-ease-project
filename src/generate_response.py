import random
from .responses.replies.replies_not_depressed import not_depressed as r_2
from .responses.replies.replies_moderate_depressed import moderate_depressed as r_1
from .responses.replies.replies_severe_depressed import severe_depressed as r_0
from .responses.information.counselling import counselling as counselling
from .responses.information.helpline import helplines as helpline
from .responses.information.therapy import therapy_providers as therapy
from .responses.bridges.advices import advices_bridge as advices_bridge
from .responses.bridges.therapy_info import help_bridge as therapy_bridge
from .responses.bridges.welcome_msgs import welcoming_messages as welcoming_msg
from .responses.advices.advices_moderate_depressed import moderate_depressed_advices as adv_moderate
from .responses.advices.advices_severe_depressed import severe_depressed_advices as adv_severe

classes = {'2': 'Not depressed', '1': 'Moderately depressed', '0': 'Severely depressed'}

def random_choose_one(arr: list):
    if not arr:
        return None
    return arr[random.randint(0, len(arr)-1)]

def random_choose_many(arr: list, n: int):
    if n > len(arr):
        raise ValueError("N is greater than the length of the list")
    chosen_elements = random.sample(arr, n)
    return chosen_elements

def build_counselling_therapy_info(ele, categoty, idx, has_cat=True):
    result = f'{idx}.**{ele["name"]}**\n'
    if has_cat:
        result += f' - Category: {categoty}\n'
    if len(ele["contact"])>0:
        result += f' - Contact Number: {"/".join(ele["contact"])}\n'
    if len(ele["email"])>0:
        result += f' - Email: {"/ ".join(ele["email"])}\n'
    if len(ele["website"])>0:
        result += f' - Website: {"/ ".join(ele["website"])}\n'
    if len(ele["address"])>0:
        result += f' - Address: {"/ ".join(ele["address"])}\n'
    return result

def build_helpline_info(ele, idx, has_cat=True):
    result = f'{idx}.**{ele["name"]}**\n'
    if has_cat:
        result += f' - Category: Emergency Helpline\n'
    if len(ele["contact"])>0:
        result += f' - Contact Number: {"/ ".join(ele["contact"])}\n'
    if len(ele["email"])>0:
        result += f' - Email: {"/ ".join(ele["email"])}\n'
    if len(ele["website"])>0:
        result += f' - Website: {"/ ".join(ele["website"])}\n'
    return result

def build_advice(arr):
    result = f'{random_choose_one(advices_bridge)}\n\n'
    for ele in arr:
        result += f' - {ele}\n'
    return result

# for moderate depression
# 1-2 therapy info @ 1-2 counselling info + 2 advices
def get_moderate_information():
    # 1-2 therapy or counselling info
    result = ''
    category = random.randint(0,1)
    if category == 0:
        choose_from = therapy
        service_name = 'Therapy'
    elif category == 1:
        choose_from = counselling
        service_name = 'Counselling'
    random_count = random.randint(1,2)
    chosen_elements = random_choose_many(choose_from,random_count)
    result += build_counselling_therapy_info(chosen_elements[0], service_name, 1)
    if len(chosen_elements) == 2:
        result += f'\n{build_counselling_therapy_info(chosen_elements[1], service_name, 2)}'
    result += f'\n\n{build_advice(random_choose_many(adv_moderate, 2))}'
    return result

# for severe depression
# 1 therapy info + 1 counselling info + 2 advices
def get_severe_information():
    result = ''
    chosen_elements = random_choose_one(helpline)
    x = build_helpline_info(chosen_elements, 1)
    result += f'{x}\n'
    chosen_elements = random_choose_one(counselling)
    x = build_counselling_therapy_info(chosen_elements, 'Counselling', 2)
    result += f'\n{x}\n\n'
    result += f'{build_advice(random_choose_many(adv_severe, 2))}'
    return result

# combine all the necessary except for depression level
# vary based on depression level
def generate_contents(depression_level):
    # only replies
    if depression_level == 2:
        replies = random_choose_one(r_2)
        return replies
    # replies + 1-2 therapy info @ 1-2 counselling info + 2 advices
    elif depression_level == 1:
        return f'{random_choose_one(r_1)}\n\n{random_choose_one(therapy_bridge)}\n{get_moderate_information()}'
    # replies + 1 helpline info + 1 therapy info + 1 counselling info + 2 advices
    elif depression_level == 0:
        return f'{random_choose_one(r_1)}\n\n{random_choose_one(therapy_bridge)}\n{get_severe_information()}'
    else:
        return ''

# generate the complete response
def generate_reply_body(depression_level: int):
    return f'Depression Level Detected: **{classes[str(depression_level)]}**\n\n{generate_contents(depression_level)}'