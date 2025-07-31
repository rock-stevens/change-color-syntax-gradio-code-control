# gr_Rock_ColorSyntaxHighlight_Demo_v2.py
# Static Demo for Gradio's gr.Code control
# This shows the color syntax highlighting 
# Color customization method via css for the Python language
# In this second demo we place the functional part of creating the css
# outside the app, and import it from an external file
# from filename: gr_Rock_CodeColors.py we import the function: create_grcode_css()
# It is very simple to add to any Gradio gr.Code() app displaying Python.
# 14 variables and 1 small function is all you need to add to your code.
# Let's get started...


# We need to import Gradio obviously.
import gradio as gr 

# import our custom css creation utils
from gr_Rock_CodeColors import create_grcode_css

# Build the css string we are going to use when we initialize gr.Blocks()
# The name you gave the 'elem_id' of the gr.Code control
# is what you pass to 'create_grcode_css()'. I named mine 'rk-code'. 
# Can be named most anything that will not conflict with other css in your ui.
# See line below and the the gr.Code control's 'elem_id' as an example.
custom_css = create_grcode_css("rk-code")


# When you build your ui, you initialize gr.Blocks() 
# and apply the custom_css code created.

# Here's an even more trimmed down ui example:

# import gradio as gr
# from gr_Rock_CodeColors import create_grcode_css
# custom_css = create_grcode_css("rk-code")
# with gr.Blocks(css=custom_css) as demo:
#     code_editor = gr.Code(language="python", elem_id="rk-code", interactive=True)
# demo.launch()


# That's it ! 
# Happy coloring and coding !!


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

# Build ui
with gr.Blocks(css=custom_css) as demo:
    
    # My ui title header
    gr.HTML("Rock's Demo for gr.Code to Change Color Syntax Highlighting Colors via CSS - Running Gradio Version: " + gr.__version__)
    
    # The actual gr.Code() editor control
    code_editor = gr.Code(language="python", elem_id="rk-code", interactive=True, lines=15)

    # Run this when the app loads - Load 'this' file into 'code_editor'.
    demo.load(load_myself, inputs=[], outputs=[code_editor])

# Launch the ui
demo.launch()


# -EOF-
