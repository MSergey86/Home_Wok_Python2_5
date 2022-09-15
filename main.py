
from logger import logger

@logger("D:/Sergey/Learning Fullstack/Home_Work_Python2/5_decorator/")
def flat_generator(list):
    list_cursor = 0
    nested_list_cursor = 0
    while list_cursor < len(list):
      if nested_list_cursor == len(list[list_cursor]):
          list_cursor += 1
          nested_list_cursor = 0
      if list_cursor != len(list):
        yield list[list_cursor][nested_list_cursor]
      nested_list_cursor += 1

if __name__ == '__main__':
    nested_list = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f'],
        [1, 2, None],
    ]
    print([item for item in flat_generator(nested_list)])
