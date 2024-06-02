import json, random

import menu


def write_file(order_functions_dict=None, mode = "a"):
    """
    입력된 주문 데이터를 JSON 형태로 변환하여 파일에 저장
    
    Args:
    order_functions_dict (dict): 주문과 관련된 텍스트와 함수를 담은 딕셔너리
    mode (str): 파일 열기 모드 ('w'는 쓰기 모드, 'a'는 추가 모드)
    """
    
    with open("test.jsonl", mode) as f:
        f.write(json.dumps(order_functions_dict, ensure_ascii=False) + "\n")
        
        
def generate_menu(menu_type="drink"):
    """
    단일 메뉴 주문을 생성하는 함수
    주어진 메뉴 유형에 따라 무작위로 메뉴 항목을 선택하고, 주문 문장을 생성
    
    Args:
    menu_type (str): 메뉴 유형 ('drink' 또는 'dessert')
    
    Returns:
    tuple: 생성된 주문 문장과 관련 함수
    """
    
    order = []

    if menu_type=="drink":
        menu = random.choice( drinks)
        unit = "잔"
    else:
        menu = random.choice( desserts)
        unit = "개"
    
    quantity = random.choice( order_quantity)
    
    if quantity in [1, 2, 3, 4, 5, 6]:
        order.append(f"{menu} {quantity}{unit} {random.choice( order_phrases)}")
    elif quantity == " ":
        order.append(f"{menu} {random.choice( order_phrases)}")
    else:
        order.append(f"{menu} {quantity} {unit} {random.choice( order_phrases)}")
    
    functions =  menu_dict[menu].replace("num",str( num_dict[quantity]))
    
    return (' '.join(order), functions)


def generate_multiple_order(menu_type="drink"):
    """
    다수의 메뉴 주문을 생성하는 함수
    지정된 메뉴 유형에 따라 여러 개의 주문을 연결하여 하나의 문자열로 만듬
    
    Args:
    menu_type (str): 메뉴 유형 ('drink' 또는 'dessert')
    
    Returns:
    tuple: 생성된 복수 주문 문장과 관련 함수
    """
    
    functions = ""
    orders = ""
    
    # 디저트 메뉴 선택
    random_num = random.sample(range(2,5), 1)[0]
    
    for i in range(random_num):
        tmp_order, tmp_functions = generate_menu(menu_type)
        
        connector = random.choice( connectors) if i < random_num-1 else ''

        
        # 함수, 주문 중첩 생성
        functions = functions + tmp_functions
        orders = orders + tmp_order  + connector

    return (orders, functions)


def generate_multiple_random_order():
    """
    무작위로 선택된 메뉴 유형으로 다수의 주문을 생성하는 함수
    음료와 디저트를 조합하여 복수의 주문을 생성
    
    Returns:
    tuple: 생성된 복수 주문 문장과 관련 함수
    """
    
    functions = ""
    orders = ""
    
    # 디저트 메뉴 선택
    random_num = random.sample(range(2,5), 1)[0]
    
    for i in range(random_num):
        
        selected_func = random.sample(["drink","dessert"],1)[0]
        tmp_order, tmp_functions = generate_menu(selected_func)
        
        connector = random.choice( connectors) if i < random_num-1 else ''

        # 함수, 주문 중첩 생성
        functions = functions + tmp_functions
        orders = orders + tmp_order  + connector

    return (orders, functions)

# 영수증 출력하도록 해주는 함수
def add_receipt(orders="", functions=""):
    """
    주문 문장에 결제 요청을 추가하는 함수
    주문 문자열 끝에 결제 관련 문구를 추가
    
    Args:
    orders (str): 기존 주문 문장
    functions (str): 기존 함수 호출 문자열
    
    Returns:
    tuple: 결제 요청이 추가된 주문 문장과 함수
    """
    
    random_receipt = random.sample([" 그리고 결제해줘", " 결제해줘", " 그리고 계산해줘", " 계산해줘", "계산", "결제"], 1)[0]
    orders += random_receipt
    functions += "receipt(quantity=-1); "
    
    return orders, functions


if __name__ == "__main__":
    # 메뉴를 생성하며, 10개의 주문마다 영수증 출력 오더 추가
    
    drinks = menu.drinks
    desserts = menu.desserts
    order_quantity = menu.order_quantity
    order_phrases = menu.order_phrases
    num_dict = menu.num_dict
    connectors = menu.connectors
    menu_dict = menu.menu_dict
    
    
    lst = set()

    write_file(mode="w")

    for i in range(100):
        tmp_order, tmp_functions = add_receipt()
        write_file({"Text" : tmp_order, "function" : tmp_functions})

    # 단일 메뉴 생성
    for i in range(400):
        tmp_order, tmp_functions = generate_menu("dessert")
        if i % 10 == 0:
            tmp_order, tmp_functions = add_receipt(tmp_order, tmp_functions)
        
        if tmp_order not in lst:
            lst.add(tmp_order)
            write_file({"Text" : tmp_order, "function" : tmp_functions})

    # 단일 디저트 메뉴 생성
    for i in range(400):
        tmp_order, tmp_functions = generate_menu("drink")
        if i % 10 == 0:
            tmp_order, tmp_functions = add_receipt(tmp_order, tmp_functions)
        
        if tmp_order not in lst:
            lst.add(tmp_order)
            write_file({"Text" : tmp_order, "function" : tmp_functions})

    # 디저트 + 디저트
    for i in range(600):
        tmp_order, tmp_functions = generate_multiple_order("dessert")
        if i % 10 == 0:
            tmp_order, tmp_functions = add_receipt(tmp_order, tmp_functions)
            
        
        if tmp_order not in lst:
            lst.add(tmp_order)
            write_file({"Text" : tmp_order, "function" : tmp_functions})

    # 음료 + 음료
    for i in range(600):
        tmp_order, tmp_functions = generate_multiple_order("drink")
        if i % 10 == 0:
            tmp_order, tmp_functions = add_receipt(tmp_order, tmp_functions)
            
        if tmp_order not in lst:
            lst.add(tmp_order)
            write_file({"Text" : tmp_order, "function" : tmp_functions})

    # 디저트 + 음료
    for i in range(2000):
        tmp_order, tmp_functions = generate_multiple_random_order()
        if i % 10 == 0:
            tmp_order, tmp_functions = add_receipt(tmp_order, tmp_functions)
            
        if tmp_order not in lst:
            lst.add(tmp_order)
            write_file({"Text" : tmp_order, "function" : tmp_functions})