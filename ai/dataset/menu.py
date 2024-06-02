drinks = [
    # 아메리카노
    "아메리카노","아이스 아메리카노","차가운 아메리카노","따듯한 아메리카노","뜨거운 아메리카노", "아아", "뜨아",
    # 카페 라뗴
    "카페 라떼", "아이스 카페 라떼", "차가운 카페 라떼", "뜨거운 카페 라떼","따듯한 카페 라떼",
    # 바닐라 라떼
    "바닐라 라떼","아이스 바닐라 라떼","차가운 바닐라 라떼", "뜨거운 바닐라 라떼", "따듯한 바닐라 라떼",
    # 그린티 라떼
    "그린티 라떼", "아이스 그린티 라떼", "차가운 그린티 라떼", "뜨거운 그린티 라떼", "따듯한 그린티 라떼",
    # 아이슈패너
    "아인슈페너", "아이스 아인슈페너", "차가운 아인슈페너", "뜨거운 아인슈페너", "따듯한 아인슈페너",
    # 에이드
    "카푸치노", "레몬 에이드", "자몽 에이드",
    # 아이스티
    "아이스티", "레몬 아이스티", "복숭아 아이스티",
    # 나머지 메뉴
    "에스프레소","콜드브루", "카푸치노"
]

desserts = [
    "레드벨벳케이크", 
    "롤 케이크", 
    "치즈 케이크", 
    "초코 쿠키", 
    "플레인 쿠키", 
    "소금빵", 
    "스트로베리 초콜릿 생크림 케이크",
    ]

menu_dict = {

    # 아메리카노
    "아메리카노" : "ICE_americano(quantity=num); ",
    "아아" : "ICE_americano(quantity=num); ",
    "아이스 아메리카노" : "ICE_americano(quantity=num); ",
    "차가운 아메리카노" : "ICE_americano(quantity=num); ",
    "뜨아" : "HOT_americano(quantity=num); ",
    "따듯한 아메리카노" : "HOT_americano(quantity=num); ",
    "뜨거운 아메리카노" : "HOT_americano(quantity=num); ",

    # 카페 라뗴
    "카페 라떼" : "ICE_cafe_latte(quantity=num); ",
    "차가운 카페 라떼" : "ICE_cafe_latte(quantity=num); ",
    "아이스 카페 라떼" : "ICE_cafe_latte(quantity=num); ",
    "따듯한 카페 라떼" : "HOT_cafe_latte(quantity=num); ",
    "뜨거운 카페 라떼" : "HOT_cafe_latte(quantity=num); ",
    
    # 바닐라 라떼
    "바닐라 라떼" : "ICE_vanilla_latte(quantity=num); ",
    "아이스 바닐라 라떼" : "ICE_vanilla_latte(quantity=num); ",
    "차가운 바닐라 라떼" : "ICE_vanilla_latte(quantity=num); ",
    "뜨거운 바닐라 라떼" : "HOT_vanilla_latte(quantity=num); ",
    "따듯한 바닐라 라떼" : "HOT_vanilla_latte(quantity=num); ",

    # 그린티 라떼
    "그린티 라떼" : "ICE_greentea_latte(quantity=num); ",
    "아이스 그린티 라떼" : "ICE_greentea_latte(quantity=num); ",  
    "차가운 그린티 라떼" : "ICE_greentea_latte(quantity=num); ",
    "뜨거운 그린티 라떼" : "HOT_greentea_latte(quantity=num); ",
    "따듯한 그린티 라떼" : "HOT_greentea_latte(quantity=num); ",
    
    # 아이슈패너
    "아인슈페너" : "ICE_einspenner(quantity=num); ",
    "아이스 아인슈페너" : "ICE_einspenner(quantity=num); ",      
    "차가운 아인슈페너" : "ICE_einspenner(quantity=num); ",
    "뜨거운 아인슈페너" : "HOT_einspenner(quantity=num); ",
    "따듯한 아인슈페너" : "HOT_einspenner(quantity=num); ",

    # 에이드
    "레몬 에이드" : "lemon_ade(quantity=num); ",
    "자몽 에이드" : "grapefruit_ade(quantity=num); ",

    # 아이스티
    "아이스티" : "peach_ice_tea(quantity=num); ",
    "복숭아 아이스티" : "peach_ice_tea(quantity=num); ",
    "레몬 아이스티" : "lemon_ice_tea(quantity=num); ",
    
    # 나머지메뉴
    "카푸치노" : "cappuccino(quantity=num); ",
    "에스프레소" : "Espresso(quantity=num); ",
    "콜드브루" : "cold_brew(quantity=num); ",

    # 디저트
    "레드벨벳케이크" :  "red_velvet_cake(quantity=num); ",
    "롤 케이크" :  "roll_cake(quantity=num); ",
    "치즈 케이크" :  "cheese_cake(quantity=num); ",
    "초코 쿠키" :  "chocolate_cookie(quantity=num); ",
    "플레인 쿠키" :  "plain_cookie(quantity=num); ",
    "소금빵" :  "salt_bread(quantity=num); ",
    "스트로베리 초콜릿 생크림 케이크" : "strawberry_chocolate_cream_cake(quantity=num); ",
    }

num_dict = {
    " " : 1,
    "한" : 1,
    "하나" : 1,
    "1개" : 1,
    "두 개" : 2,
    "두" : 2,
    "2개": 2,
    "세" : 3,
    "세 개" : 3,
    "3개" : 3,
    "네" : 4,
    "다섯" : 5,
    "여섯" : 6,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    1 : 1,
    2 : 2,
    3 : 3,
    4 : 4,
    5 : 5,
    6 : 6
}

# 주문 문장 
order_quantity = [" ", "한", "두", "세", "네", "다섯", "여섯", 1, 2, 3, 4, 5, 6]

# 랜문장 문구 
order_phrases = ["주세요", "해줘 ", "줄래?", "부탁할게", "줘"]

# 주문 문장 생성을 위한 추가적인 연결어 리스트
connectors = [" 그리고 "," 그 외에 ",", "," 또 "]