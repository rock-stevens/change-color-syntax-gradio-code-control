# gr_Rock_ColorSyntaxHighlight_LiveDemo_v3.py
# You can edit this code, live, used Gradio's reload feature
# I used this to figure out Gradio's gr.Code 
# control color syntax highlighting css.
# 

import gradio as gr 

# A function to load 'this' file in the editor. Loaded when the ui is loaded.
def load_myself():
    try:
        with open(__file__, 'r') as f:
            return f.read()
    except Exception as e:
        gr.Info(f"Error loading file: {e}", duration=5.0, title="Error Loading")
        
# A function to save file in the editor.
def save_myself(content):
    try:
        with open(__file__, 'w') as f:
            f.write(content)
    except Exception as e:
        gr.Info(f"Error saving file: {e}", duration=5.0, title="Error Saving")


# In the very begining, there was this part... only...
# But, I used Gradio's 'reload' feature, then just did the normal
# Run, Debug, Edit, Save (Gradio reloads) Run, Debug, Edit...
# Just to figure out this small bit of code below, then the rest of the names...

custom_css = """
#rk-code .cm-editor .cm-content {font-size: 22px !important;} /* FONTSIZE - 22px */
#rk-code .ͼ1b {color: #559955; font-style: italic;} /* COMMENTS - DIM GREEN*/
"""

# Build the ui.
with gr.Blocks(css=custom_css) as demo:
    gr.HTML("Rock's LIVE - Demo for Gradio gr.Code to Change Color Syntax Highlighting Colors - Running Gradio Version: " + gr.__version__)
    save_button = gr.Button("Save Changes")
    code_editor = gr.Code(language="python", value="", interactive=True, lines=15, elem_id="rk-code")
    save_button.click(save_myself, inputs=code_editor, outputs=None)
    
    # Run this when the app loads - Load 'this' file into 'code_editor'.
    demo.load(load_myself, inputs=[], outputs=[code_editor])
    
# Launch the ui
demo.launch()


# -EOF-