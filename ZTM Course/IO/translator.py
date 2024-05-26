from translate import Translator
# import pdb
translator = Translator(to_lang= "ja")

try:
    # pdb.set_trace()
    with open('traduce.txt',mode="r") as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        with open('translation.txt',mode='w') as my_translation:
            my_translation.write(translation)
except FileNotFoundError as e:
    print("Check your file path!")
    
