# ssg last end enter display made by r0hkx

# the output file is a text file that will always have the most recent end enter.
# to use in OBS, add a text source and check "Read from file",
# then enter the path to the output file

# set your user name. this path may be different on your computer, 
# please double check that the file exists in the given position
latest_world_file = "C:\\Users\\USER\\speedrunigt\\latest_world.json"

# path to output file. this program will create the file,
# do not use a preexisting file here or it will get deleted.
output_file = "C:\\path\\to\\latest_ee.txt"

# text to put before end enter time in output file
prefix = "latest ee: "

# do not edit anything under this line unless you know what you're doing

import json
from time import sleep

def get_latest_json():
  guide_file = open(latest_world_file)
  guide_json = json.load(guide_file)
  path_to_latest_world = guide_json["world_path"]
  try:
    path_to_latest_logs = path_to_latest_world + "/speedrunigt/record.json"
  except:
    return None
  return path_to_latest_logs

def extract_info_from_json(file_path):
  try:
    f = open(file_path, 'r')
    data = json.load(f)
    try:
      for x in data['timelines']:
        if x["name"] == "enter_end":
          return x["igt"]
    except:
      # print("file or value not found")
      return None
  except:
    # print("file or value not found")
    return None

def ms_to_formatted(ms):
  total_seconds = (ms / 1000)
  minutes = int(total_seconds / 60)
  seconds = total_seconds % 60

  # print("total seconds: " + str(total_seconds))
  # print("minutes: " + str(minutes))
  # print("seconds: " + str(seconds))
  return f"{minutes:01.0f}:{seconds:06.3f}"

def main():

  previous_ee = " "
  latest_ee = " " 

  print("ssg ee reader started")

  while True:
    latest_file_path = get_latest_json()
    if latest_file_path:
      information = extract_info_from_json(latest_file_path)
      if information:
        latest_ee = information
        if (latest_ee != previous_ee):
          print(str(ms_to_formatted(int(latest_ee))))
          output = open(output_file, "w")
          output.write(prefix + str(ms_to_formatted(int(latest_ee))))
          output.close()
          previous_ee = latest_ee
    else:
      print("No JSON files found in the specified folder.")
    sleep(1)

if __name__ == "__main__":
  main()
