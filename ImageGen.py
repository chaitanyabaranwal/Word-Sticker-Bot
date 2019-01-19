import imgkit 

def ImageGen(text, styleClass):

    # text = text.split('\n') 
    # height = len(text)
    # biggest = max(text)

    # width = len(biggest)

    # # this checks whether the user sends too many words but I'm not sure about the limits
    # if width > 30 or height > 6:
    #     bot.sendMessage(chatId, "Too many words")
    #     return None

    # "styleClass" will be whatever style class that Yanch creates
    # seperator = '</span><br><span class="%s">' % (styleClass)
    htmlString = '<html><head><link rel="stylesheet" href="test_fonts.css">\
    </head><body style="margin:0"><div class="%s" style="text-align:center;\
    overflow-wrap: normal; width: 504px; padding:0; margin:0;">' % (styleClass)\
    + text + '</div></body></html>'

    # Image options
    options = {
        'transparent': None,
        'crop-w': 512
    }
    # need to resize the image! (not done)
    # remember to change the following css file location
    css = 'test_fonts.css'
    return imgkit.from_string(htmlString, 'test.png', css=css, options=options)

ImageGen("Hello", "rainbow")
