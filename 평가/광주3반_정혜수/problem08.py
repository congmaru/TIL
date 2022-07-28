# 함수 내부에 불필요한 print문이 있는 경우 오답으로 처리가 됩니다.
def inventory_filter(item_type, inventory):
    pass
    # 여기에 코드를 작성하여 함수를 완성합니다.
    #item type에 해당하는 inventory만 출력하는 함수를 만들어라.
    

    lst = []
    if inventory[0]['type'] == item_type:
        lst.append(inventory[0])
    if inventory[1]['type'] == item_type:
        lst.append(inventory[1])
    if inventory[2]['type'] == item_type:
        lst.append(inventory[2])
    if inventory[3]['type'] == item_type:
        lst.append(inventory[3])
    else:
        pass

    return lst

    #if문을 사용해 각 요소를 직접 비교했다.
    #for와 if문을 사용하면 훨씬 간단하게 풀릴 수 있을 것 같다. 
    #inventory의 각 요소는 딕셔너리로 이 딕셔너리의 키가 item_type과 동일할 때 해당하는 inventory의 요소를 가지고 리스트에 append하면 된다. 

    
# 아래의 코드를 수정하거나 새롭게 추가하지 않습니다.
if __name__ == '__main__':
    item_type = 'weapon'
    inventory = [
        {
            'id': 1,
            'name': 'Elder Wand',
            'type': 'weapon',
            'grade': 'legend',
        },
        {
            'id': 2,
            'name': 'Healing Potion',
            'type': 'potion',
            'grade': 'normal',
        },
        {
            'id': 3,
            'name': 'Steel Helmet',
            'type': 'armor',
            'grade': 'rare',
        },
        {
            'id': 4,
            'name': 'Long Sword',
            'type': 'weapon',
            'grade': 'normal',
        },
    ]
    print(inventory_filter(item_type, inventory)) 
    # [{'id': 1, 'name': 'Elder Wand', 'type': 'weapon', 'grade': 'legend'}, {'id': 4, 'name': 'Long Sword', 'type': 'weapon', 'grade': 'normal'}]
