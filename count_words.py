import easygui

sentence=easygui.enterbox("Write a sentence")
easygui.msgbox('You Wrote " '+sentence+' "')
word=sentence.split()
reply=easygui.choicebox("Choose your word to study",choices=word)
easygui.msgbox("Today's word :\n"+reply)
