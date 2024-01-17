import random
from .responses.information.counselling import counselling as counselling
from .responses.information.helpline import helplines as helpline
from .responses.information.therapy import therapy_providers as therapy
from .generate_response import build_counselling_therapy_info
from .generate_response import build_helpline_info
from .keywords import counseling_keywords, therapy_keywords, helpline_keywords

def build_list_of_info(service_name):
    result = f'Here is the List of {service_name} Services Available:\n'
    if service_name == 'Therapy':
        for idx, ele in enumerate(random.sample(therapy, 5)):
            result += f'{build_counselling_therapy_info(ele, service_name, idx+1, False)}\n'
    elif service_name == 'Emergency Helpline':
        for idx, ele in enumerate(random.sample(helpline, 5)):
            result += f'{build_helpline_info(ele, idx+1, False)}\n'
    elif service_name == 'Counselling':
        for idx, ele in enumerate(random.sample(counselling, 5)):
            result += f'{build_counselling_therapy_info(ele, service_name, idx+1, False)}\n'
    return result

def check_keywords(user_message):
    user_message = user_message.lower()
    if any(keyword in user_message for keyword in counseling_keywords) or any(keyword in user_message for keyword in therapy_keywords) or any(keyword in user_message for keyword in helpline_keywords):
        return True
    return False

def check_service_name(user_message):
    if any(keyword in user_message for keyword in helpline_keywords):
        return 'Emergency Helpline'
    if any(keyword in user_message for keyword in therapy_keywords):
        return 'Therapy'
    return 'Counselling'

def get_support_information(user_message):
    service_name = check_service_name(user_message)
    return build_list_of_info(service_name)


