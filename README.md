# change-color-syntax-gradio-code-control
## Rock's Demo for Gradio's gr.Code control to Change the Color Syntax Highlighting

![Rock's Demo for Gradio's gr.Code control to Change the Color Syntax Highlighting
](screenshot.png)

## Introduction

All I wanted to do was increase the font size and the color of the comments.
(*older eyes, and I've always liked a dim green for comments*)


I set off to research the problem for a while on the internet etc... nothing.
Tried the AI mess... same thing, nothing.
Although both agreed, neither knew the answer. :)
Just kept telling me things I already knew. :(

Which was CSS.

I set out to figure out how to change it myself. Since I'm working with Gradio, I made a simple Gradio app to help me figure it out.
But once I figured out how to change the font size and comment color, it kinda went on to include the whole syntax for the languge Python.

And during my internet research, there seems to be others facing same exact problem.
***They want to change the colors for the gr.Code() control.***

And since I found no solution myself, *out there...*

Now, I'd share with everyone how simple it is to add to this to most any Gradio app that uses the gr.Code() control for displaying the language Python.

----

## gr.Code() Background.
Gradio uses 'CodeMirror' for the gr.Code() control, Gradio used CodeMirror v5 in Gradio 3.x and 4.x. But Gradio moved to CodeMirror v6 in Gradio 5.x. 

The names of the CSS elements that CodeMirror itself uses, changed between CodeMirror v5 and CodeMirror v6. Which creates more CSS values to have to work with.

But I divide them into two. One set of CSS names for each of the two versions needed. 
I programatically check for which Gradio Version I am running and swap CSS name sets to account for differences between the CSS names in the two versions.
(*Swapping css name sets, leads to something else later on.*)

But a 'CSS name set' as I am calling it, is, just a variable I've shoved a bunch of CSS text into. Then assign the variable to the 'css' property of Gradio control. I can create a number of these variables with the same, or different style in it. Then assign whichever I choose when program runs or from an external app settings file.

----

## Testing

It has been tested using the following Gradio versions.

| Gradio Version | Pass-Fail | CodeMirror Version |
| ----------- | ----------- | ----------- |
| 3.3.1 | FAIL [^1] | 5 |
| 3.41.2 | PASS | 5 |
| 4.28.3 | PASS | 5 |
| 4.44.0 | PASS | 5 |
| 5.6.0 | PASS | 6 |
| 5.30.0 | PASS | 6 |
| 5.32.0 | PASS | 6 |
| 5.37.0 | PASS | 6 |
| 5.38.0 | PASS | 6 |

[^1]: There was an error indicating that possibly Version 3.3.1 was before the gr.Code() control was introduced? (I did not look into it.)*

----

## Demo 1

Filename: **gr_Rock_ColorSyntaxHighlight_Demo_v1.py**

This 'Static' demo for Gradio's gr.Code control shows the color syntax highlighting, color customization method, via css for the Python language.

If you want to try changing the colors, edit '**gr_Rock_ColorSyntaxHighlight_Demo_v1.py**' before running.


Try it:

```
python gr_Rock_ColorSyntaxHighlight_Demo_v1.py
```

----

## Demo 2

Filename: **gr_Rock_ColorSyntaxHighlight_Demo_v2.py**<br>
Filename: **gr_Rock_CodeColors.py**

In the second 'Static' demo I placed the functional part of creating the css outside the app, and import it from the external file: '**gr_Rock_CodeColors.py**' and I import the function: '**create_grcode_css()**' from it. Makes your main file smaller, and the color syntax code is out of the way.

If you want to try changing the colors, edit '**gr_Rock_CodeColors.py**' before running.


Try it: 

```
python gr_Rock_ColorSyntaxHighlight_Demo_v2.py
```

----

## Smallest 'Static' Example (Based on Demo 2)

1. Modify '**gr_Rock_CodeColors**' to change the colors to suit.
2. Then start the app listed below and just paste some code into the code edit window.

Here's a very trimmed down ui example:

```python
import gradio as gr
from gr_Rock_CodeColors import create_grcode_css
custom_css = create_grcode_css("rk-code")
with gr.Blocks(css=custom_css) as demo:
     code_editor = gr.Code(language="python", elem_id="rk-code", interactive=True)
demo.launch()
```

----

## Live Demo 3

Filename: **gr_Rock_ColorSyntaxHighlight_LiveDemo_v3.py**

In this third demo, is the tool I made to figure this all out. 

- It loads, itself. 
- It saves, itself.

And has enough 'css' code to get it going for Gradio Version 5.0 and higher. You would have to change the CSS name(s) in the code to get it to work on Gradio Versions older than v5.0. 
I start it from the command line via gradio's ***reload method*** like so:

```
gradio gr_Rock_ColorSyntaxHighlight_LiveDemo_v3.py
```

Try and edit something in the CSS, and when you save your code changes, a few moments later, *after Gradio detects the change and reloads the program*, you'll see the changes.

'This program', and the 'F12 key' in my browser to inspect the CSS elements and code, is what I used to get all the CSS names, in both variations of the CSS in Gradio. Plus all of the testing.  
(*This program became a very useful tool. I'm sure I'll be using it again*)


I still had to find a way to reload color changes without reloading or re-starting the app !

Although this is what I refer to as 'static' and is fine for apps which need no color change while running. Also, a lot of users are ok with saving color settings, then re-starting the app. Demo 1 and Demo 2 is ok for that type of 'static' application. And Demo 3 uses *reload* which you can not use (*should not*) in production. This also relies on the user not making (saving) coding mistakes, or the app may (will) bomb out when Gradio tries to restart it.

----

## Dynamic Demo 4

Filename: **gr_Rock_ColorSyntaxHighlight_DynamicDemo_v4.py**

I use gr.Blocks() for most of my Gradio interfaces, and you can not 'update' blocks. Which is why the app has been 'static', up until now.

I figured out that if I embed my custom CSS in an gr.HTML() control, the gr.HTML() control WILL update when I reassign the custom css to it. And therefore update the CSS in my app (*on the web page*). And therefore change the colors in the gr.Code() control *without* reloading the app. You can probably use an existing (*in your app*) gr.HTML() control since the CSS names are different from everything else.


I have LIVE dynamic updating colors !!! :)


Try it: 

```
python gr_Rock_ColorSyntaxHighlight_DynamicDemo_v4.py
```

Swapping css name sets gives me the ability to jump between color schemes.

(*This could be carried further to have external files, JSON with the color values, and load them on the fly from the JSON files.*)

That is what I did to demo the LIVE dynamic ability of changing the colors.

I created two seperate custom css variables, holding different colors sets for the syntax. And then I swap which css is used. And apply it to the gr.HTML() value, and that updates the css for the gr.Code() control.

The same function 'create_grcode_css()' is used to create both custom css variables with the css in it.

----

## Live Dynamic Demo 5

Filename: **gr_Rock_ColorSyntaxHighlight_LiveDynamicDemo_v5.py**

Changes from Dynamic Demo 4

- Removed creating of the second custom css. 
- Added a color picker in the ui. 
- ***Now watch the 'COMMENTS' color change in the code window LIVE, while you move the color picker. :)***

Try it: 

```
python gr_Rock_ColorSyntaxHighlight_LiveDynamicDemo_v5.py
```

----

## Fin

***That's it !***

You can now incorporate changing the syntax highlighted colors, 'on-the-fly', with Gradio's gr.Code() control for the Python language.

***Happy coloring !!***

----

MIT License
Copyright (C) 2025-present [Rock Stevens](https://rockstevens.com)
