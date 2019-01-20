HELP_TEXT = """
Welcome to text-sticker bot! Here is a list of commands
to help you navigate through. :)

/help - Shows this help dialogue.
/text - Create a new sticker out of text. Enter text, select style and get your sticker! A maximum of 100 characters is allowed.
/styles - View available styles. Choose from: Basic, Bold, Fancy, Handwritten, Wordart, and Decorative.
/set_default - Set the default style
/delete - Delete a previously created sticker. Send the sticker you want to delete or its index in the pack.
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
    ['wordart', 'decorative']
]

style_categories_no_default = [
    ['basic', 'bold'],
    ['fancy', 'handwritten'],
    ['wordart', 'decorative']
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

decorative_styles = [
    ['dreams', 'chrome'],
    ['wilderness', 'future'],
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
    elif styleCategory == 'decorative':
        return decorative_styles