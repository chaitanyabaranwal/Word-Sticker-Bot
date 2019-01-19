import imgkit

def findMultiplier(letters):
    return 8.6 - 2.75 * pow(letters, 0.189)

def findFontSize(pixels, numOfLetters):
    return findMultiplier(numOfLetters) * pow(pixels, 0.5)

def ImageGen(text, styleClass):

    # dynamic font size (DON'T CHANGE ANY NUMBERS)
    numOfLetters = len(text)
    fontSize = findFontSize(600, numOfLetters)


    htmlString = '<html><head><link rel="stylesheet" href="test_fonts.css">\
                    </head><body style="margin:0"><div class="%s" style="text-align:center;\
                    word-break: break-word; width: 504px; padding:0; margin:0; font-size:%fpx">' % (styleClass, fontSize)\
                    + text + '</div></body></html>'

    # Image options
    options = {
        'transparent': None,
        'crop-w': 512
    }

    css = 'styles.css'
    return imgkit.from_string(htmlString, 'images/test.png', css=css, options=options)
