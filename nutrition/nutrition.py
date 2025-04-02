def main():

    fruit = input("Item: ").lower().strip()
    calorie = get_fruit_calorie(fruit)

    if calorie != None:
        print(f"Calories: {calorie}")


def get_fruit_calorie(fruit_name):

    fruit_list = [

        {
            "name": "apple",
            "calorie": 130
        },

        {
            "name": "avocado",
            "calorie": 50
        },

        {
            "name": "banana",
            "calorie": 110
        },

        {
            "name": "cantaloupe",
            "calorie": 50
        },

        {
            "name": "grapefruit",
            "calorie": 60
        },

        {
            "name": "grapes",
            "calorie": 90
        },

        {
            "name": "honeydew melon",
            "calorie": 50
        },

        {
            "name": "kiwifruit",
            "calorie": 90
        },

        {
            "name": "lemon",
            "calorie": 15
        },

        {
            "name": "lime",
            "calorie": 20
        },

        {
            "name": "nectarine",
            "calorie": 60
        },

        {
            "name": "orange",
            "calorie": 80
        },

        {
            "name": "peach",
            "calorie": 60
        },

        {
            "name": "pear",
            "calorie": 100
        },

        {
            "name": "pineapple",
            "calorie": 50
        },

        {
            "name": "plums",
            "calorie": 70
        },

        {
            "name": "strawberries",
            "calorie": 50
        },

        {
            "name": "sweet cherries",
            "calorie": 100
        },

        {
            "name": "tangerine",
            "calorie": 50
        },

        {
            "name": "watermelon",
            "calorie": 80
        },

    ]

    for fruit in fruit_list:

        if fruit['name'] == fruit_name:

            # print("found fruit")
            # print(f"{fruit['name']} : {fruit['calorie']}")

            return fruit['calorie']

main()
