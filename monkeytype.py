import pyautogui
import pytesseract
import cv2
import time

time.sleep(5)

try:
    while True:
        
        #STEP 1 (GET SCREENSHOT)
        go = pyautogui.screenshot(region=(0,280,1400,200))
        go.save("rawimg.png")

        # STEP 2(EXTRACT TEXT)

        img = cv2.imread("rawimg.png")
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

        word = pytesseract.image_to_string(img)
        
        print(word)
        print("---")
        
        # Convert parapgraph to a single line

        list_word = list(word.split(" "))
        print("List form:")
        print(list_word)
        
        new = [y.replace('\n', ' ') for y in list_word]

        final_word = " ".join(new)
        print("  ")
        print("Text Extracted Complete: ")
        print(final_word)

        #STEP 3 (TYPE TEXT)
        Type_Speed = 0.03

        pyautogui.write(str(final_word), interval=Type_Speed)
        
        ###Start New###
        time.sleep(2)
        pyautogui.scroll(300)
        
        pyautogui.moveTo(320, 187)

        pyautogui.click()
        time.sleep(0.5)
        
except KeyboardInterrupt:
    print('\n')
    print('\n')
