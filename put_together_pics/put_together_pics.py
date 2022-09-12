import re,sys,os
from pathlib import Path
import zipfile
#ADD UNZIP STEP 



ZIP_FILE = "XXX.zip"
directory_to_extract_to = ""
#CHANGE THESE TO YOU PATH
ALL_PICS_PATH = "./allpics"
path_toall = "./allpics/altogether"
NEW_FOLDER_NAME = "altogether"

parent_path = Path(ALL_PICS_PATH)

def get_name_order(path):
    return sorted(path, key = lambda x: int(re.findall(r"\d+",x.name)[0]))

if __name__ == "__main__":
    with zipfile.ZipFile(ZIP_FILE, 'r') as zip_ref:
        zip_ref.extractall(directory_to_extract_to)
    last_index = 0
    for dir in parent_path.iterdir():
        if dir.name != NEW_FOLDER_NAME:
            #print(list((dir).iterdir()))
            #print(get_name_order(dir.iterdir()))
            print(dir)

            sub_iter = get_name_order(dir.iterdir())
            #print(sub_iter)
            # print(get_name_order(dir.))
            
            for idx in range(len(sub_iter)):
                #if int(re.findall(r"d\+",dir.name)) == 1:
                os.rename(str(sub_iter[idx]), "/".join([path_toall,f"{idx+last_index+1}.jpg"]))
            last_index += len(sub_iter)
            print(last_index)


    




