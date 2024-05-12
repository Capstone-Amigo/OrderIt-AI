from typing import List


def get_menu_list() -> List[str]:
    """현재 메뉴리스트 가져오기
    cold, hot, dessert
    
    Returns:
        List[str]: 'cold', 'hot' and 'dessert' 메뉴들을 list로 출력함
    """
    cold_list = ["ICE_americano", "ICE_cafe_latte", "ICE_vanilla_latte", "ICE_greentea_latte", "ICE_issupanner","lemon_ade","grapefruit_ade", "peach_ice_tea", "lemon_ice_tea"]
    hot_list =  ["HOT_americano", "HOT_cafe_latte", "HOT_vanilla_latte", "HOT_greentea_latte", "HOT_issupanner","cappuccino"]
    dessert_list = ["red_velvet_cake", "roll_cake", "cheese_cake", "chocolate_cookie", "plain_cookie", "salt_bread", "strawberry_chocolate_cream_cake", ]
    
    return cold_list + hot_list + dessert_list 