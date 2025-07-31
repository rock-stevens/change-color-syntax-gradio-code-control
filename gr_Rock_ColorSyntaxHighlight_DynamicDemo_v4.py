# gr_Rock_ColorSyntaxHighlight_DynamicDemo_v4.py
# Dynamic Demo for Gradio's gr.Code control
# This shows the color syntax highlighting 
# Color customization method via css for the Python language
# In this fourth demo we create two different css variables.
# each variable with a different color for the COMMENTS in Python.
# Then we load that css as the css for a gr.HTML() control.
# Then we just update the gr.HTML() control. No reloading Gradio !
# So now dynamic updating is very simple to add to any Gradio gr.Code() app displaying Python.
# 14 variables, 1 small function and a gr.HTML() control is all you need to add to your code.
# You can probably use an existing gr.HTML() control in your project, 
# since the css is targeting by the document 'element id'.
# Let's get started...


# We need to import Gradio obviously.
import gradio as gr 


# ===============================================================================
# ===============================================================================
# ===============================================================================

# (14 variables)
# Main Code window font size and size attribute (I wanted a larger font !) (2)
clrFONTSIZE = 22
clrFONTSIZEATTR = "px"

# Python Default Color Syntax - Color List (12)
clrKEYWORDS = "#fda331"
clrMETHODS = "#b5bd68"
clrVARIABLES = "#6fb3d2"
clrFUNCTIONS = "#fda331" 
clrCOMMAS = "#cc99cc"
clrCURLYBRACES = "#cc99cc"
clrNUMBERS = "#fda331" 
clrEQUALS = "#cc99cc"
clrSQUAREBRACKETS = "#cc99cc" 
clrQUOTEDSTRINGS = "#b5bd68" 
clrDOUBLEQUOTEDfSTRINGS = "#8abeb7" 
clrCOMMENTS = "#808080"


# Do Not Modify
# Used to build the custom css for the language Python (1 small function)
def create_grcode_css(grcode_elem_id):
    global clrFONTSIZE, clrFONTSIZEATTR, clrKEYWORDS, clrMETHODS, clrVARIABLES
    global clrFUNCTIONS, clrCOMMAS, clrCURLYBRACES, clrNUMBERS, clrEQUALS
    global clrSQUAREBRACKETS, clrQUOTEDSTRINGS, clrDOUBLEQUOTEDfSTRINGS, clrCOMMENTS
    python_lang_types = ["KEYWORDS","METHODS","VARIABLES","FUNCTIONS","COMMAS","CURLYBRACES","NUMBERS","EQUALS","SQUAREBRACKETS","QUOTEDSTRINGS","DOUBLEQUOTEDfSTRINGS","COMMENTS"]
    fontsize_css= ".cm-editor .cm-content {font-size: " + str(clrFONTSIZE) + clrFONTSIZEATTR + " !important;}"
    # get Gradio version
    grVersion = gr.__version__
    grVs = grVersion.split('.')
    grMajorVersion = int(grVs[0])
    if grMajorVersion < 5:
        # css list for CodeMirror 5, for Gradio Versions 3 and 4.
        grcode_css_list = [".ͼ1q {color: " + clrKEYWORDS + ";}", ".ͼ1r {color: " + clrMETHODS + ";}", ".ͼ1s {color: " + clrVARIABLES + ";}", 
                       ".ͼ1t {color: " + clrFUNCTIONS + ";}", ".ͼ1w {color: " + clrCOMMAS + ";}", ".ͼ1x {color: " + clrCURLYBRACES + ";}", 
                       ".ͼ1z {color: " + clrNUMBERS + ";}", ".ͼ21 {color: " + clrEQUALS + ";}",".ͼ23 {color: " + clrSQUAREBRACKETS + ";}", 
                       ".ͼ28 {color: " + clrQUOTEDSTRINGS + ";}", ".ͼ2a {color: " + clrDOUBLEQUOTEDfSTRINGS + ";}", ".ͼ2c {color: " + clrCOMMENTS + "; font-style: italic;}"]
    else:
        # css list for CodeMirror 6, for Gradio Version 5.
        grcode_css_list = [".ͼp {color: " + clrKEYWORDS + ";}", ".ͼq {color: " + clrMETHODS + ";}", ".ͼr {color: " + clrVARIABLES + ";}", 
                       ".ͼs {color: " + clrFUNCTIONS + ";}", ".ͼv {color: " + clrCOMMAS + ";}", ".ͼw {color: " + clrCURLYBRACES + ";}", 
                       ".ͼy {color: " + clrNUMBERS + ";}", ".ͼ10 {color: " + clrEQUALS + ";}",".ͼ12 {color: " + clrSQUAREBRACKETS + ";}", 
                       ".ͼ17 {color: " + clrQUOTEDSTRINGS + ";}", ".ͼ19 {color: " + clrDOUBLEQUOTEDfSTRINGS + ";}", ".ͼ1b {color: " + clrCOMMENTS + "; font-style: italic;}"]
    
    # make a header comment, findable in the sea of css source, helpful note of version for debugging?
    grcode_css = "<style>\n"
    grcode_css = grcode_css + f"/* Rock's CSS for the Python language using the gr.Code Control - Running Gradio Version: {grVersion}*/\n"
    # add on the css for the main code font size
    grcode_css = grcode_css + f"#{grcode_elem_id} {fontsize_css}  /* MAIN FONT SIZE */\n"
    # add the css for each of the colors in the Color List, for the Python language type
    for i in range(len(python_lang_types)):
        lang_type = python_lang_types[i]
        css = grcode_css_list[i]
        grcode_css = grcode_css + f"#{grcode_elem_id} {css}  /* {lang_type}  */\n"
    
    grcode_css = grcode_css + "</style>\n"   
    
    return grcode_css


# Build the css string we are going change the gr.Code() colors with.
# The name you gave the 'elem_id' of the gr.Code control
# is what you pass to 'create_grcode_css()'. I named mine 'rk-code'. 
# Can be named most anything that will not conflict with other css in your ui.
# See line below and the the gr.Code control's 'elem_id' as an example.

# we have not changed any colors, so create custom css set with the default colors
custom_css = create_grcode_css("rk-code")

# change a color(s), make another custom css set, with different color(s) set
clrCOMMENTS = "#339933"     # change just the 'comment' color to 'dim green'
custom_css2 = create_grcode_css("rk-code")

# ===============================================================================
# ===============================================================================
# ===============================================================================

# The rest is:
# The Gradio gr.Blocks() section.
# A function 'load_myself()' to load 'this' file in the editor.
# So when the ui is loaded, there is some code to actually look at.

def load_myself():
    """
    Loads MySelf. Obviously. And it's another type of syntax... triple quotes...
    """
    try:
        with open(__file__, 'r') as f:
            return f.read()
    except Exception as e:
        return f"Error loading file: {e}"
    return ""


# we just return the css style variable - default colors
def change_comment_color():
    global custom_css
    return custom_css
 
 
# we just return the css style variable - changed colors
def change_comment_color2():
    global custom_css2
    return custom_css2
 
 
# Build ui
with gr.Blocks() as demo:
    
    # My ui (long winded) title header
    gr.HTML("Rock's Demo for Gradio's gr.Code to Dynamically Change Color Syntax Highlighting Colors via CSS - Running Gradio Version: " + gr.__version__)

    change_comment_button = gr.Button("Change Comment to Default")
    change_comment_button2 = gr.Button("Change Comment to Dim Green")
    
    # The nothing in it but 'STYLE' gr.HTML() control
    # I use the gr.HTML() to embed the custom css
    # When this component updates, the style changes
    # I suppose I could locate it anywhere, but I keep it beside the gr.Code() control :)
    dynamic_css_html = gr.HTML(custom_css, min_height=1, max_height=1, padding=False)
    # The actual gr.Code() editor control
    code_editor = gr.Code(language="python", elem_id="rk-code", interactive=True, lines=15)

    
    change_comment_button.click(change_comment_color, inputs=[], outputs=[dynamic_css_html])
    change_comment_button2.click(change_comment_color2, inputs=[], outputs=[dynamic_css_html])

    # Run this when the app loads - Load 'this' file into 'code_editor'.
    demo.load(load_myself, inputs=[], outputs=[code_editor])

# Launch the ui
demo.launch()


# -EOF-
