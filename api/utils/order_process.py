from utils import menu

def text_to_json(text):
    if text is None:
        return {'Order': []}

    orders = []
    # ';'로 명령어 분리
    commands = text.split('; ')
    for command in commands:
        if commands == "":
            continue
        
        if command.strip():
            # 괄호를 기준으로 메뉴명과 파라미터 분리
            parts = command.strip().split('(')
            menu_text = parts[0].strip()
            # 파라미터 부분에서 ','로 파라미터를 분리
            params = parts[1].strip(')').split(',')
            order_details = {}
            order_details['menu'] = menu_text

            # 각 파라미터에서 '='로 키와 값을 분리
            for param in params:
                key, value = param.split('=')
                order_details[key.strip()] = value.strip()

            if menu_text not in menu.get_menu_list():
                continue
            
            orders.append(order_details)

    return {'Order': orders}
