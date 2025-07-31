# this import only needed for gr.__version__
import gradio as gr 

# ===============================================================================
# ===============================================================================
# ===============================================================================
# Colors and Font Size Variables List (14 variables)
# ------------------------------------
# NOTE: THESE are the DEFAULT colors used for the Python language type.
# CHANGE THESE to change colors and font size to your preference.
# These variables are used by the function that creates the custom css code.
# -------------------------------------------------------------------------------

# Main Code window font size and size attribute (I wanted a larger font !)
clrFONTSIZE = 22
clrFONTSIZEATTR = "px"

# Python Color Syntax - Color List (12)
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
    grcode_css = f"/* Rock's CSS for the Python language using the gr.Code Control - Running Gradio Version: {grVersion}*/\n"
    # add on the css for the main code font size
    grcode_css = grcode_css + f"#{grcode_elem_id} {fontsize_css}  /* MAIN FONT SIZE */\n"
    # add the css for each of the colors in the Color List, for the Python language type
    for i in range(len(python_lang_types)):
        lang_type = python_lang_types[i]
        css = grcode_css_list[i]
        grcode_css = grcode_css + f"#{grcode_elem_id} {css}  /* {lang_type}  */\n"
    return grcode_css



