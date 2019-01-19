HELP_TEXT = """
Welcome to text-sticker bot! Here is a list of commands
to help you navigate through. :)

/help - Look here if you get stuck!
/text - Enter text, select style and get your sticker!
/styles - View available styles
/image - Input image and resize it in standard sticker size
/default_style - Set the default style
"""

TEXT_CONVERT_TEXT = """
Okay, please enter the text you want to stylise!
"""

STYLE_TEXT = """
Okay, here are the style categories you can select from!
"""

DELETE_STICKER = """
Please enter the index of the sticker you want to delete (starting from 1).
"""

# List with available stylec-categories
style_categories = [
    ['Default'],
    ['basic', 'bold'],
    ['fancy', 'handwritten'],
    ['wordart', 'retro']
]

style_categories_no_default = [
    ['basic', 'bold'],
    ['fancy', 'handwritten'],
    ['wordart', 'retro']
]

# Lists with styles in each category
basic_styles = [
    ['arial', 'comic-sans'],
    ['courier', 'el-messiri'],
    ['impact']
]

bold_styles = [
    ['bangers', 'luckiest-guy'],
    ['nosifer', 'staatliches'],
]

fancy_styles = [
    ['abril-fatface', 'galada'],
    ['mystery-quest', 'sail'],
    ['spirax', 'srisakdi']
]

handwritten_styles = [
    ['finger-paint', 'calligraffitti'],
    ['homemade-apple', 'sacramento']
]

wordart_styles = [
    ['rainbow', 'blues'],
    ['horizon', 'purple']
]

retro_styles = [
    ['dreams', 'chrome'],
    ['victory', 'future'],
    ['cop']
]

def selectStyleCategory(styleCategory):
    if styleCategory == 'basic':
        return basic_styles
    elif styleCategory == 'bold':
        return bold_styles
    elif styleCategory == 'fancy':
        return fancy_styles
    elif styleCategory == 'handwritten':
        return handwritten_styles
    elif styleCategory == 'wordart':
        return wordart_styles
    elif styleCategory == 'retro':
        return retro_styles