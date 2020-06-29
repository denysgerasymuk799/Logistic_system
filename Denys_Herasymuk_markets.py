class Markets(object):
    """class to create a market description"""

    def __init__(self, name, area, categories):
        """Description"""
        self.name = name
        self.area = area
        self.categories = categories

    def __str__(self):
        return 'Supermarket {} has an area of {} meters' \
               ' squared and has the following categories:' \
               ' {}.'.format(self.name, self.area, ", ".join(map(str, self.categories)))


if __name__ == "__main__":
    market_family_food = Markets('Family Food', 80, ['Bread and Bakery', 'Dairy', 'Beverages'])
    print(market_family_food.name)
    print(market_family_food.area)
    print(market_family_food.categories)
    print(market_family_food)
