'''
DIRECTIONS
==========

1. In `get_friends_favorite_candy_count()`, return a dictionary of candy names and the
amount of times each candy appears in the `friend_favorites` list.

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

2. Given the list `friend_favorites`, create 
a new data structure in the function `create_new_candy_data_structure` 
that describes the different kinds of candy paired with a list of friends that 
like that candy. 

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

3. In `get_friends_who_like_specified_candy()`, return 
a tuple of friends who like the candy specified in the candy_name parameter.

4. In, `create_candy_set()`, return a set of all the candies from
the data structure made in `create_new_candy_data_structure()`.

5. Starting with nominal cases, write tests for each of the functions below then 
write tests to handle edge cases.
'''

#1
def get_friends_favorite_candy_count(favorites):
    candy_count = 0
    candy_counts = {}

    for friend in favorites:
        for candy in friend[1]:
            candy_count = candy_counts.get(candy,0)
            candy_counts[candy] = candy_count + 1

    return candy_counts 


#2
def create_new_candy_data_structure(data):
    candy_dict = {}
    friend_name = []
    candy = ""

    for friend in data:
        friend_name = friend[0]

        for i in range(len(friend[1])):
            candy = friend[1][i]

            if candy not in candy_dict:
                candy_dict.update({candy:[friend_name]})
            else:
                candy_dict[candy].append(friend_name)
            
    return candy_dict 

#3
def get_friends_who_like_specific_candy(data, candy_name):
    friend_likes = create_new_candy_data_structure(data)
    candy_tuple = tuple(friend_likes[candy_name])

    return candy_tuple

#4
def create_candy_set(data):
    candy_dict = create_new_candy_data_structure(data)
    candies = set()
    candy=""

    for candy in candy_dict:
        candies.add(candy)

    return candies

friend_favorites = [
    ["Sally", ["lollipop", "bubble gum", "laffy taffy" ]],
    ["Bob", ["milky way", "licorice", "lollipop" ]],
    ["Arlene", ["chocolate bar", "milky way", "laffy taffy" ]],
    ["Carlie", ["nerds", "sour patch kids", "laffy taffy" ]]
]

# result1 = get_friends_favorite_candy_count(friend_favorites)
# print(f"{result1=}\n")

# result2 = create_new_candy_data_structure(friend_favorites)
# print(f"{result2=}\n")

# result3 = get_friends_who_like_specific_candy(friend_favorites, "lollipop")
# print(f"{result3=}\n")

# result4 = create_candy_set(friend_favorites)
# print(f"{result4=}\n")

lollipop_friends = get_friends_who_like_specific_candy(friend_favorites, "lollipop")
print(lollipop_friends)