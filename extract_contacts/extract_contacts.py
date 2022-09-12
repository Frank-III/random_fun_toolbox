import re
import os
from paddleocr import PaddleOCR, draw_ocr

#creating environment
#conda create --name paddle_env python=3.8 --channel conda-forge
#conda activate paddle_env
#python3 -m pip install paddlepaddle
#pip install "paddleocr>=2.0.1"



ocr_model = PaddleOCR(lang= "ch", use_gpu=False)
def get_date_contact(file):
  result = ocr_model.ocr(file)
  contacts = []
  dates = []
  for line in result:
      if re.match(r".*\d{1,2}\.\d{1,2}",line[1][0]):
        reg = re.split(r"(.*?)(\d{1,2}\.\d{1,2})", line[1][0]) # lazy mode
        print([x for x in reg if x != ''])
        #contact, date = [x for x in reg if x != '']
        contact, date = filter(lambda x: x != '', reg)
        #print(contact)
        #print(date)
        contacts.append(contact)
        dates.append(date)
  return contacts, dates

def get_date_contact_2(file):
  result = ocr_model.ocr(file)
  contacts = []
  dates = []
  for line in result:
      words = line[1][0]
      if re.search(r"([1-9]|1[0-2])\.([1-9]|1[0-9]|2[0-9]|3[0-1])",words):
        #print(words)
        date = re.findall(r"\d{1,2}\.\d{1,2}",words)[0]
        contact = " ".join(filter(lambda x: x != '', re.split(r"\d{1,2}\.\d{1,2}",words)))
        #print(date)
        regs = re.search(r"([a-zA-Z]*)[.\W]*?([\u4e00-\u9fa5]*)[^a-zA-Z]*([a-zA-Z]*)", contact)
        reg1, reg2, reg3 = regs.groups()
        contact = "".join([reg2, " ".join([reg1, reg3])])
        contacts.append(contact)
        dates.append(date)
  return contacts, dates



def get_text(contacts, dates):
  return [date + ' ' + name + "'s birthday" for date, name in zip(dates, contacts)]

def get_text_file(contacts, dates, file):
  seq = get_text(contacts, dates)
  with open(file, 'w', encoding="utf-8") as f:
    for item in seq:
      f.write(item+"\n")
  print("file saved")




if __name__ == "__main__":
  print(os.listdir())
  file1 = "wx_contacts.png"
  file2 = "wx_contacts_2.png"
  file3 = "wx_contacts_3.png"
  file4 = "contact1_text.txt"
  file5 = "contact2_text.txt"
  file6 = "contact3_text.txt"
  file7 = "wx_contacts_4.png"
  file8 = "contact4_text.txt"
  contacts1, dates1 = get_date_contact_2(file1)
  contacts2, dates2 = get_date_contact_2(file2)
  contacts3, dates3 = get_date_contact_2(file3)
  contacts4, dates4 = get_date_contact_2(file7)
  #get_date_contact_2(file1)
  #get_date_contact_2(file2)
  #print(get_text(contacts1,dates1))
  #print(get_text(contacts2,dates2))
  print(get_text(contacts3,dates3))
  print(get_text(contacts4,dates4))
  #get_text_file(contacts1, dates1, file4)
  #get_text_file(contacts2, dates2, file5)