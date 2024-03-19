# world_count.py
# puts the number of worlds an instance has in a text file.

# if you're on windows, for the below directories,
# please use double backslashes (\\) instead of single backslashes (\).
# for example, this is good: "C:\\MultiMC\\instances\\1.16.1\\.minecraft",
# this is not good: "C:\MultiMC\instances\1.16.1\.minecraft".

# put the path of the .minecraft folder you want to track here
minecraft_folder = "path\\to\\.minecraft"

# put the path of the file you want to be created and updated with the current world count.
# if an existing file is put here, it will be completely cleared and replaced with just
# the world count.
output_file = "path\\to\\world_count.txt"

# text to put before the number of worlds
prefix = "#"
# text to put after the number of worlds
suffix = "/100"

# this number controls how frequently the program updates in seconds.
# default is once a second. decimals are accepted.
update_timer = 1

# do not change anything under this line unless you know what you are doing.

from os import listdir
from time import sleep

def update_file(num):
    text = prefix + str(num) + suffix
    print(text)
    f = open(output_file, "w")
    f.write(text)
    f.close()

print("starting world count")

world_count = len(listdir(minecraft_folder + "\\saves"))
    
last_world_count = world_count

update_file(world_count)

while True:
    last_world_count = world_count
    world_count = len(listdir(minecraft_folder + "\\saves"))

    if(world_count != last_world_count):
        update_file(world_count)

    sleep(update_timer)
