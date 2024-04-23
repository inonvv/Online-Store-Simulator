from Classes.Product import Product

products_map = {
    'Keyboard': Product("Keyboard", "MQ653", 143, "Computer Accessories"),
    'Monitor': Product("Monitor", "HP1567", 250, "Screens"),
    'Oven': Product("Oven", "AFQ1347", 100, "Kitchen"),
    'Refrigerator': Product("Refrigerator", "WQRQQ185", 75, "Kitchen"),
    'TV': Product("TV", "1234ASC", 500, "Screens"),
    # music
    'Guitar': Product("Guitar", "GT100", 400, "Musical Instruments"),
    'Drums': Product("Drums", "DR200", 800, "Musical Instruments"),
    'Piano': Product("Piano", "PN300", 1200, "Musical Instruments"),
    'Violin': Product("Violin", "VL400", 300, "Musical Instruments"),
    'Trumpet': Product("Trumpet", "TP500", 600, "Musical Instruments"),
    # cloths & soccer ball & basketball & racket
    'Soccer Ball': Product("Soccer Ball", "SB200", 20, "Sports Equipment"),
    'T-shirt': Product("T-shirt", "TS300", 15, "Clothing"),
    'Basketball': Product("Basketball", "BB400", 30, "Sports Equipment"),
    'Running Shoes': Product("Running Shoes", "RS500", 80, "Footwear"),
    'Baseball Glove': Product("Baseball Glove", "BG600", 50, "Sports Equipment"),
    'Dress': Product("Dress", "DS700", 120, "Clothing"),
    'Tennis Racket': Product("Tennis Racket", "TR800", 100, "Sports Equipment", discount=20)
}
