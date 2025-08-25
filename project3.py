

# PROJECT GOOD AFTERNOON AND GOOD EVENING

from datetime import datetime

name = input("Tell me our name sir")

hour = datetime.now().hour

if 6 <= hour <12:
    print(f"Good morning {name}")

elif 12 <= hour < 17 :

    print(f"Good after noon {name}")

elif 17 <= hour < 21:

    print(f"Good evening {name}")

else:

    print(f" Good night {name}")