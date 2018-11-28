#Hangman Game
#Zachary Page
#11/23

#imports
import random
import time

#constants
hangman = (
"""
------
|     |
|
|
|
|
|
|
|
|
------
""",
"""
------
|     |
|     O
|
|
|
|
|
|
|
------
""",
"""
------
|     |
|     O
|     +
|     +
|
|
|
|
|
------
""",
"""
------
|     |
|     O
|   / +\\
|  /  + \\
|
|
|
|
|
------
""",
"""
------
|     |
|     O
|   / +\\
|   / + \\
|    |
|    |
|
|
|
------
""",
"""
------
|     |
|     O
|   / +\\
|  /  + \\
|    |  |
|    |  |
|
|
| 
------
""")


max_wrong = len(hangman) - 1
words = ()

for i in range(len(hangman)):
    print(hangman[i])
    time.sleep(5)









































