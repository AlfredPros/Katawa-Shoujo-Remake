################################################################################
## Initialization
################################################################################

init offset = -1


#init python:

    #import ctypes
    #from os import path
    
    #import abc
    #import autobahn
    #from waapi import WaapiClient, CannotConnectToWaapiException
    #from pprint import pprint
    
    #try:
    #    # Connecting to Waapi using default URL
    #    with WaapiClient() as client:
    #        # NOTE: client will automatically disconnect at the end of the scope
    #        # == Simple RPC without argument
    #        print("Getting Wwise instance information:")

    #        result = client.call("ak.wwise.core.getInfo")
    #        pprint(result)
            
    #        # == RPC with arguments
    #        print("Query the Default Work Unit information:")

    #        object_get_args = {
    #            "from": {
    #                "path": ["\\Actor-Mixer Hierarchy\\Default Work Unit"]
    #            },
    #            "options": {
    #                "return": ["id", "name", "type"]
    #            }
    #        }

    #        result = client.call("ak.wwise.core.object.get", object_get_args)
    #        pprint(result)

    #except CannotConnectToWaapiException:
    #    print("Could not connect to Waapi: Is Wwise running and Wwise Authoring API enabled?")
    


################################################################################
## Transforms
################################################################################
            
transform d2:
    alpha 0.0
    linear 0.1 alpha 1.0
    on hide:
        linear 0.2 alpha 0.0
        
transform ctc_blinks:
    alpha 0.0 align(0.985, 0.95)
    block:
        easein 0.5 alpha 1.0
        pause 0.5
        easein 0.5 alpha 0.0
        pause 0.5
        repeat
    on hide:
        linear 0.2 alpha 0.0

transform text_credit(t):
    align(0.5, 0.9) alpha 1.0
    pause t
    easein 1 alpha 0.0

transform other_credit(t):
    alpha 1.0
    pause t
    easein 1 alpha 0.0
    
transform choice_menu:
    alpha 0.0 
    pause 0.3
    easein 1.2 alpha 1.0
    
################################################################################
## Styles
################################################################################

style main_title:
    color "#686256"
    font "playtime.ttf"
    size 15
    
style main_button:
    color "#988A6F"
    idle_color "#988A6F"
    hover_color "#686256"
    font "playtime.ttf"
    size 28
    
style main_title_bold:
    color "#686256"
    font "playtime_bold.ttf"
    size 30
    
style main_prompt:
    text_align 0.5
    color "#686256"
    font "playtime.ttf"
    size 28
    
style text_lyric:
    text_align 0.5
    color "#FFF403"
    font "playtime.ttf"
    size 40

style text_thanks:
    text_align 0.5
    color "#FFF"
    font "playtime.ttf"
    size 40
    

style default:
    properties gui.text_properties()
    language gui.language

style input:
    properties gui.text_properties("input", accent=True)
    adjust_spacing False

style hyperlink_text:
    properties gui.text_properties("hyperlink", accent=True)
    hover_underline True

style gui_text:
    properties gui.text_properties("interface")


style button:
    properties gui.button_properties("button")

style button_text is gui_text:
    properties gui.text_properties("button")
    yalign 0.5


style label_text is gui_text:
    properties gui.text_properties("label", accent=True)

style prompt_text is gui_text:
    properties gui.text_properties("prompt")


style bar:
    ysize 40
    left_bar Frame("gui/bar/left.png", gui.bar_borders, tile=False)
    right_bar Frame("gui/bar/right.png", gui.bar_borders, tile=False)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vbar:
    xsize gui.bar_size
    top_bar Frame("gui/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    ysize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    xsize gui.scrollbar_size
    base_bar Frame("gui/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    ysize gui.slider_size
    base_bar Frame("gui/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/slider/horizontal_[prefix_]thumb.png"

style vslider:
    xsize gui.slider_size
    base_bar Frame("gui/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/slider/vertical_[prefix_]thumb.png"


style frame:
    padding gui.frame_borders.padding
    background Frame("gui/frame.png", gui.frame_borders, tile=gui.frame_tile)



################################################################################
## In-game screens
################################################################################

screen credit():
    tag menu
    
    zorder 110
    $ rhy = renpy.music.get_pos(channel='sound')
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    button:
        keysym "rollback"
        action NullAction()
    
    imagebutton:
        idle "blackout"
        action NullAction()
        
    
    # Lyrics
    if rhy < 2.125:
        pass
    elif rhy < 3.677:
        text "When the" at text_credit(10):
            style "text_lyric"
    elif rhy < 5.909:
        text "light is running low" at text_credit(10):
            style "text_lyric"
    elif rhy < 9.014:
        text "And the shadows start to grow" at text_credit(10):
            style "text_lyric"
    elif rhy < 12.216:
        text "And the places that you know" at text_credit(10):
            style "text_lyric"
    elif rhy < 17.649:
        text "seem like fantasy" at text_credit(3.881):
            style "text_lyric"  #fadeout (at 16:097)
    elif rhy < 19.201:
        text "There's a" at text_credit(10):
            style "text_lyric"
    elif rhy < 21.530:
        text "Light inside your soul" at text_credit(10):
            style "text_lyric"
    elif rhy < 24.635:
        text "That's still shining in the cold" at text_credit(10):
            style "text_lyric"
    elif rhy < 26.769:
        text "with the truth" at text_credit(10):
            style "text_lyric"
    elif rhy < 34.531:
        text "The promise in our hearts" at text_credit(6.307):
            style "text_lyric"  #fadeout (at 33:076)
    elif rhy < 36.278:
        text "Don't forget" at text_credit(10):
            style "text_lyric"
    else:
        text "I'm with you in the dark" at text_credit(7.762):
            style "text_lyric"  #fadeout (at 44:040)
    
    # Thank yous
    if rhy < 3.677:
        pass
    elif rhy < 6.782:
        text "Katawa Shoujo\n\"Remake\"\n\nby AlfredPros":
            ypos 150 xalign 0.5
            style "text_thanks"
    elif rhy < 9.887:
        text "{color=#C5C5C5}All of Assets\n(Image and Audio)\n(Font, etc){/color}\n\nKatawa Shoujo":
            ypos 150 xalign 0.5
            style "text_thanks"
    elif rhy < 12.992:
        text "{color=#C5C5C5}Character and GUI \nOriginal Designs{/color}\n\nKatawa Shoujo":
            ypos 150 xalign 0.5
            style "text_thanks"
    elif rhy < 19.201:
        text "{color=#C5C5C5}Programming and Writing\n(I'm fast af boi!){/color}\n\nAlfredPros" at other_credit(3.105):
            ypos 150 xalign 0.5
            style "text_thanks"  #fadeout (at 16:097)
    elif rhy < 22.306:
        text "{color=#C5C5C5}\"Don't Forget\" (Vocal Excerpt)\nPiano Arranged & Vocal Performaned by{/color}\n\nLaura Shigihara":
            ypos 150 xalign 0.5
            style "text_thanks"
    elif rhy < 25.508:
        text "{color=#C5C5C5}Special Thanks{/color}\nJ-Cafe VN\nthefahre\nDwinanda\nChristine":
            ypos 150 xalign 0.5
            style "text_thanks"
    elif rhy < 28.807:
        text "{color=#C5C5C5}Special Thanks{/color}\nBambang\nUdin\nUcok\nAll other members of J-Cafe VN":
            ypos 150 xalign 0.5
            style "text_thanks"
    else:
        text "{color=#C5C5C5}Special Thanks{/color}\nAnd You" at other_credit(4.269):
            ypos 150 xalign 0.5
            style "text_thanks"  #fadeout (at 33:076)
        
    timer 0.001 action SetVariable("y", 0) repeat True  # Used to make the screen to constantly refresh.
    timer 51.600 action MainMenu(confirm=False)
    

screen ctc():
    add "ctc" at ctc_blinks

## Say screen ##################################################################
##
## The say screen is used to display dialogue to the player. It takes two
## parameters, who and what, which are the name of the speaking character and
## the text to be displayed, respectively. (The who parameter can be None if no
## name is given.)
##
## This screen must create a text displayable with id "what", as Ren'Py uses
## this to manage text display. It can also create displayables with id "who"
## and id "window" to apply style properties.
##
## https://www.renpy.org/doc/html/screen_special.html#say

screen say(who, what):
    style_prefix "say"
    
    if who is not None:
        add "gui/namebox.png":
            align(0.5, 1.0)
        text who id "who":
            pos(22, 505)
        text what id "what":
            pos(45, 550)
    else:
        add "gui/textbox.png":
            align(0.5, 1.0)
        text what id "what":
            pos(45, 550)


    ## If there's a side image, display it above the text. Do not display on the
    ## phone variant - there's no room.
    if not renpy.variant("small"):
        add SideImage() xalign 0.0 yalign 1.0


## Make the namebox available for styling through the Character object.
init python:
    config.character_id_prefixes.append('namebox')

style window is default
style say_label is default
style say_dialogue is default
style say_thought is say_dialogue

style namebox is default
style namebox_label is say_label


style window:
    xalign 0.5
    xfill True
    yalign gui.textbox_yalign
    ysize gui.textbox_height

    background Image("gui/textbox.png", xalign=0.5, yalign=1.0)

style namebox:
    xpos gui.name_xpos
    xanchor gui.name_xalign
    xsize gui.namebox_width
    ypos gui.name_ypos
    ysize gui.namebox_height

    background Frame("gui/namebox.png", gui.namebox_borders, tile=gui.namebox_tile, xalign=gui.name_xalign)
    padding gui.namebox_borders.padding

style say_label:
    properties gui.text_properties("name", accent=True)
    xalign gui.name_xalign
    yalign 0.5

style say_dialogue:
    properties gui.text_properties("dialogue")
    xsize gui.dialogue_width
    


## Input screen ################################################################
##
## This screen is used to display renpy.input. The prompt parameter is used to
## pass a text prompt in.
##
## This screen must create an input displayable with id "input" to accept the
## various input parameters.
##
## https://www.renpy.org/doc/html/screen_special.html#input

screen input(prompt):
    style_prefix "input"

    window:

        vbox:
            xalign gui.dialogue_text_xalign
            xpos gui.dialogue_xpos
            xsize gui.dialogue_width
            ypos gui.dialogue_ypos

            text prompt style "input_prompt"
            input id "input"

style input_prompt is default

style input_prompt:
    xalign gui.dialogue_text_xalign
    properties gui.text_properties("input_prompt")

style input:
    xalign gui.dialogue_text_xalign
    xmaximum gui.dialogue_width


## Choice screen ###############################################################
##
## This screen is used to display the in-game choices presented by the menu
## statement. The one parameter, items, is a list of objects, each with caption
## and action fields.
##
## https://www.renpy.org/doc/html/screen_special.html#choice

screen choice(items):
    style_prefix "choice"

    vbox at choice_menu:
        for i in items:
            textbutton i.caption action i.action:
                text_font "playtime.ttf"
                text_idle_color "#988A6F"
                text_hover_color "#686256"
                text_size 28


## When this is true, menu captions will be spoken by the narrator. When false,
## menu captions will be displayed as empty buttons.
define config.narrator_menu = True


style choice_vbox is vbox
style choice_button is button
style choice_button_text is button_text

style choice_vbox:
    xalign 0.5
    yalign 0.5

    spacing 8

style choice_button is default:
    properties gui.button_properties("choice_button")

style choice_button_text is default:
    properties gui.button_text_properties("choice_button")


## Quick Menu screen ###########################################################
##
## The quick menu is displayed in-game to provide easy access to the out-of-game
## menus.

screen quick_menu():

    ## Ensure this appears on top of other screens.
    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"
            spacing 8

            xalign 0.5
            yalign 0.96

            textbutton _("Back") at d2 action Rollback()
            textbutton _("Skip") at d2 action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Save") at d2 action ToggleScreen("save", transition=Dissolve(0.5))
            textbutton _("Load") at d2 action ToggleScreen("load", transition=Dissolve(0.5))
            textbutton _("Options") at d2 action ToggleScreen("options", transition=Dissolve(0.5))
            textbutton _("Main menu") at d2 action MainMenu()


## This code ensures that the quick_menu screen is displayed in-game, whenever
## the player has not explicitly hidden the interface.
init python:
    config.overlay_screens.append("quick_menu")

default quick_menu = True

style quick_button is default
style quick_button_text is button_text

style quick_button:
    properties gui.button_properties("quick_button")

style quick_button_text:
    properties gui.button_text_properties("quick_button")


################################################################################
## Main Menu Screens
################################################################################

## Main Menu screen ############################################################
##
## Used to display the main menu when Ren'Py starts.
##
## https://www.renpy.org/doc/html/screen_special.html#main-menu

screen main_menu():
    tag menu
    
    $ bruh = renpy.exists("fmodstudioL.dll")

    add "main_bg"
    add "main_win":
        align(0.5, 0.5)
    add "logo_large":
        align(1.05, 0.05)
    
    vbox:
        spacing -2
        align(0.12, 0.78)
        
        textbutton _("Start") action Start():
            text_style "main_button"
        
        textbutton _("Load") action ToggleScreen("load", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75)):
            text_style "main_button"
        
        textbutton _("Extras") action ToggleScreen("extras", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75)):
            text_style "main_button"

        textbutton _("Options") action ToggleScreen("options", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75)):
            text_style "main_button"
        
        textbutton _("Quit") action Quit(confirm=not main_menu):
            text_style "main_button"
            
            
    # The title texts.
    vbox:
        spacing 2
        align (0.98, 0.977)
        text "Katawa Shoujo {i}\"Remake\"{/i}":
            style "main_title"

        text "Ren'Py [renpy.version_only]":
            style "main_title"


style main_menu_frame is empty
style main_menu_vbox is vbox
style main_menu_text is gui_text
style main_menu_title is main_menu_text
style main_menu_version is main_menu_text

style main_menu_frame:
    xsize 280
    yfill True

    background "gui/overlay/main_menu.png"

style main_menu_vbox:
    xalign 1.0
    xoffset -20
    xmaximum 800
    yalign 1.0
    yoffset -20

style main_menu_text:
    properties gui.text_properties("main_menu", accent=True)

style main_menu_title:
    properties gui.text_properties("title")

style main_menu_version:
    properties gui.text_properties("version")


## Load and Save screens #######################################################
##
## These screens are responsible for letting the player save the game and load
## it again. Since they share nearly everything in common, both are implemented
## in terms of a third screen, file_slots.
##
## https://www.renpy.org/doc/html/screen_special.html#save https://
## www.renpy.org/doc/html/screen_special.html#load

screen save():
    
    ## Ensure this appears beyond any other screens.
    zorder 1000
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    imagebutton:
        idle "main_dark"
        action NullAction()
    add "main_config":
        align(0.5, 0.5)
        
    text "Save":
        align(0.31, 0.22)
        style "main_title_bold"
        
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True
                    
        vbox:
            area(390, 200, 510, 320)
            
            viewport:
                draggable False
                mousewheel True
                scrollbars "vertical"
                
                vbox:
                    spacing 12
                    
                    for i in range(40):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            hbox:
                                spacing 19
                                
                                frame:
                                    background "main_save"
                                    add FileScreenshot(slot):
                                        align(0.5,0.5)
                                        zoom 0.5

                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    yalign 0.5
                                    style "main_button"

                                text FileSaveName(slot):
                                    yalign 0.5
                                    style "main_button" #style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
    
    textbutton _(">> Return"):
        align(0.68, 0.785)
        text_style "main_button"
        action If(main_menu, true=(Hide("save", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))), false=(If(_window, true=(Hide("save", transition=Dissolve(0.5))), false=(Hide("save", transition=Dissolve(0.5)), Return()))))
    

screen load():
    
    ## Ensure this appears beyond any other screens.
    zorder 1000
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    imagebutton:
        idle "main_dark"
        action NullAction()
    add "main_config":
        align(0.5, 0.5)
        
    text "Load":
        align(0.31, 0.22)
        style "main_title_bold"
        
    default page_name_value = FilePageNameInputValue(pattern=_("Page {}"), auto=_("Automatic saves"), quick=_("Quick saves"))
    
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True
                    
        vbox:
            area(390, 200, 510, 320)
                
            viewport:
                draggable False
                mousewheel True
                scrollbars "vertical"
                    
                vbox:
                    spacing 12
                    
                    for i in range(40):

                        $ slot = i + 1

                        button:
                            action FileAction(slot)

                            hbox:
                                spacing 19
                                
                                frame:
                                    background "main_save"
                                    add FileScreenshot(slot):
                                        align(0.5,0.5)
                                        zoom 0.5

                                text FileTime(slot, format=_("{#file_time}%A, %B %d %Y, %H:%M"), empty=_("empty slot")):
                                    yalign 0.5
                                    style "main_button"

                                text FileSaveName(slot):
                                    yalign 0.5
                                    style "main_button" #style "slot_name_text"

                                key "save_delete" action FileDelete(slot)
    
    textbutton _(">> Return"):
        align(0.68, 0.785)
        text_style "main_button"
        action If(main_menu, true=(Hide("load", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))), false=(Hide("load", transition=Dissolve(0.5))))


## Options screen ##########################################################
##
## The preferences screen allows the player to configure the game to better suit
## themselves.
##
## https://www.renpy.org/doc/html/screen_special.html#preferences

screen options():
    
    ## Ensure this appears beyond any other screens.
    zorder 1000
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    imagebutton:
        idle "main_dark"
        action NullAction()
    add "main_config":
        align(0.5, 0.5)
        
    text "Options":
        align(0.32, 0.22)
        style "main_title_bold"
    
    vbox:
        pos(400, 200)
        spacing 4
        
        if preferences.fullscreen == False:
            textbutton "{image=menu_unchecked} Fullscreen Mode" action Preference("display", "fullscreen"):
                text_style "main_button"
        else:
            textbutton "{image=menu_checked} Fullscreen Mode" action Preference("display", "window"):
                text_style "main_button"
                
        if preferences.skip_unseen == False:
            textbutton "{image=menu_unchecked} Skip unread text" action Preference("skip", "toggle"):
                text_style "main_button"
        else:
            textbutton "{image=menu_checked} Skip unread text" action Preference("skip", "toggle"):
                text_style "main_button"
                
        null height 4
            
        text "Text Speed":
            style "main_button"
            
        hbox:
            style_prefix "slider"
            box_wrap True
            
            bar value Preference("text speed")
            
        text "Music Volume":
            style "main_button"
        
        hbox:
            style_prefix "slider"
            box_wrap True
            
            bar value Preference("music volume")
            
        text "Sound Volume":
            style "main_button"
            
        hbox:
            style_prefix "slider"
            box_wrap True
            
            bar value Preference("sound volume")
            
    textbutton _(">> Return"):
        align(0.68, 0.785)
        text_style "main_button"
        action If(main_menu, true=(Hide("options", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))), false=(Hide("options", transition=Dissolve(0.5))))
        

style pref_label is gui_label
style pref_label_text is gui_label_text
style pref_vbox is vbox

style radio_label is pref_label
style radio_label_text is pref_label_text
style radio_button is gui_button
style radio_button_text is gui_button_text
style radio_vbox is pref_vbox

style check_label is pref_label
style check_label_text is pref_label_text
style check_button is gui_button
style check_button_text is gui_button_text
style check_vbox is pref_vbox

style slider_label is pref_label
style slider_label_text is pref_label_text
style slider_slider is gui_slider
style slider_button is gui_button
style slider_button_text is gui_button_text
style slider_pref_vbox is pref_vbox

style mute_all_button is check_button
style mute_all_button_text is check_button_text

style pref_label:
    top_margin gui.pref_spacing
    bottom_margin 2

style pref_label_text:
    yalign 1.0

style pref_vbox:
    xsize 225

style radio_vbox:
    spacing gui.pref_button_spacing

style radio_button:
    properties gui.button_properties("radio_button")
    foreground "gui/button/radio_[prefix_]foreground.png"

style radio_button_text:
    properties gui.button_text_properties("radio_button")

style check_vbox:
    spacing gui.pref_button_spacing

style check_button:
    properties gui.button_properties("check_button")
    foreground "gui/button/check_[prefix_]foreground.png"

style check_button_text:
    properties gui.button_text_properties("check_button")

style slider_slider:
    xsize 350

style slider_button:
    properties gui.button_properties("slider_button")
    yalign 0.5
    left_margin 10

style slider_button_text:
    properties gui.button_text_properties("slider_button")

style slider_vbox:
    xsize 450


## Extras screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen extras():
    
    ## Ensure this appears beyond any other screens.
    zorder 1000
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    imagebutton:
        idle "main_dark"
        action NullAction()
    add "main_config":
        align(0.5, 0.5)
        
    text "Extras":
        align(0.32, 0.22)
        style "main_title_bold"
        
    fixed:

        ## This ensures the input will get the enter event before any of the
        ## buttons do.
        order_reverse True
                    
        vbox:
            area(430, 200, 510, 320)
            
            viewport:
                draggable False
                mousewheel False
                
                grid 2 2:
                    
                    if persistent.hanako_end:
                        imagebutton:
                            idle "main_extra_thumb1"
                            action ToggleScreen("ex_1", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75))
                        imagebutton:
                            idle "main_extra_thumb2"
                            action ToggleScreen("ex_2", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75))
                    else:
                        add "main_extra"
                        add "main_extra"
                        
                    if persistent.lilly_end:
                        imagebutton:
                            idle "main_extra_thumb3"
                            action ToggleScreen("ex_3", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75))
                        imagebutton:
                            idle "main_extra_thumb4"
                            action ToggleScreen("ex_4", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75))
                    else:
                        add "main_extra"
                        add "main_extra"
        
        
    textbutton _(">> Return"):
        align(0.68, 0.785)
        text_style "main_button"
        action Hide("extras", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))
    
    
################################################################################
## Additional screens
################################################################################


## Extras ######################################################################

screen ex_1():
    ## Ensure this appears beyond any other screens.
    zorder 1001
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    add "main_dark"
    add "e_cantaloupes":
        align(0.5, 0.5)
    
    imagebutton:
        idle "empty"
        action Hide("ex_1", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))

screen ex_2():
    ## Ensure this appears beyond any other screens.
    zorder 1001
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    add "main_dark"
    add "e_climatic":
        align(0.5, 0.5)
    
    imagebutton:
        idle "empty"
        action Hide("ex_2", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))

screen ex_3():
    ## Ensure this appears beyond any other screens.
    zorder 1001
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    add "main_dark"
    add "e_cuddlefish":
        align(0.5, 0.5)
    
    imagebutton:
        idle "empty"
        action Hide("ex_3", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))          

screen ex_4():
    ## Ensure this appears beyond any other screens.
    zorder 1001
    
    # To prevent the player from displaying multiple windows
    button:
        keysym "game_menu"
        action NullAction()
    
    add "main_dark"
    add "e_prawns":
        align(0.5, 0.5)
    
    imagebutton:
        idle "empty"
        action Hide("ex_4", transition=ImageDissolve(im.Tile("tr-dots_col.png"), 0.75, reverse=True))         

            
## Confirm screen ##############################################################
##
## The confirm screen is called when Ren'Py wants to ask the player a yes or no
## question.
##
## https://www.renpy.org/doc/html/screen_special.html#confirm

screen confirm(message, yes_action, no_action):

    ## Ensure other screens do not get input while this screen is displayed.
    modal True

    zorder 1001

    style_prefix "confirm"

    add "gui/overlay/confirm.png"

    frame:

        vbox:
            xalign .5
            yalign .5
            spacing 30

            label _(message):
                text_style "main_prompt" #style "confirm_prompt"
                xalign 0.5

            hbox:
                xalign 0.5
                spacing 100

                textbutton _("Yes") action yes_action
                textbutton _("No") action no_action
    
    add "main_hanako":
        zoom 1.3
        align(0.67, 0.61)

    ## Right-click and escape answer "no".
    key "game_menu" action no_action


style confirm_frame is gui_frame
style confirm_prompt is gui_prompt
style confirm_prompt_text is gui_prompt_text
style confirm_button is gui_medium_button
style confirm_button_text is gui_medium_button_text

style confirm_frame:
    background Frame([ "gui/confirm_frame.png", "gui/frame.png"], gui.confirm_frame_borders, tile=gui.frame_tile)
    padding gui.confirm_frame_borders.padding
    xalign .5
    yalign .5

style confirm_prompt_text:
    text_align 0.5
    layout "subtitle"

style confirm_button:
    properties gui.button_properties("confirm_button")

style confirm_button_text:
    properties gui.button_text_properties("confirm_button")


## Skip indicator screen #######################################################
##
## The skip_indicator screen is displayed to indicate that skipping is in
## progress.
##
## https://www.renpy.org/doc/html/screen_special.html#skip-indicator

screen skip_indicator():

    zorder 100
    
    add "gui/skip.png":
        align(0.985, 0.03)
        zoom 1.3


## Notify screen ###############################################################
##
## The notify screen is used to show the player a message. (For example, when
## the game is quicksaved or a screenshot has been taken.)
##
## https://www.renpy.org/doc/html/screen_special.html#notify-screen

screen notify(message):

    zorder 100
    style_prefix "notify"

    frame at notify_appear:
        text "[message!tq]"

    timer 3.25 action Hide('notify')


transform notify_appear:
    on show:
        alpha 0
        linear .25 alpha 1.0
    on hide:
        linear .5 alpha 0.0


style notify_frame is empty
style notify_text is gui_text

style notify_frame:
    ypos gui.notify_ypos

    background Frame("gui/notify.png", gui.notify_frame_borders, tile=gui.frame_tile)
    padding gui.notify_frame_borders.padding

style notify_text:
    properties gui.text_properties("notify")


## NVL screen ##################################################################
##
## This screen is used for NVL-mode dialogue and menus.
##
## https://www.renpy.org/doc/html/screen_special.html#nvl


screen nvl(dialogue, items=None):

    window:
        style "nvl_window"

        has vbox:
            spacing gui.nvl_spacing

        ## Displays dialogue in either a vpgrid or the vbox.
        if gui.nvl_height:

            vpgrid:
                cols 1
                yinitial 1.0

                use nvl_dialogue(dialogue)

        else:

            use nvl_dialogue(dialogue)

        ## Displays the menu, if given. The menu may be displayed incorrectly if
        ## config.narrator_menu is set to True, as it is above.
        for i in items:

            textbutton i.caption:
                action i.action
                style "nvl_button"

    add SideImage() xalign 0.0 yalign 1.0


screen nvl_dialogue(dialogue):

    for d in dialogue:

        window:
            id d.window_id

            fixed:
                yfit gui.nvl_height is None

                if d.who is not None:

                    text d.who:
                        id d.who_id

                text d.what:
                    id d.what_id


## This controls the maximum number of NVL-mode entries that can be displayed at
## once.
define config.nvl_list_length = gui.nvl_list_length

style nvl_window is default
style nvl_entry is default

style nvl_label is say_label
style nvl_dialogue is say_dialogue

style nvl_button is button
style nvl_button_text is button_text

style nvl_window:
    xfill True
    yfill True

    background "gui/nvl.png"
    padding gui.nvl_borders.padding

style nvl_entry:
    xfill True
    ysize gui.nvl_height

style nvl_label:
    xpos gui.nvl_name_xpos
    xanchor gui.nvl_name_xalign
    ypos gui.nvl_name_ypos
    yanchor 0.0
    xsize gui.nvl_name_width
    min_width gui.nvl_name_width
    text_align gui.nvl_name_xalign

style nvl_dialogue:
    xpos gui.nvl_text_xpos
    xanchor gui.nvl_text_xalign
    ypos gui.nvl_text_ypos
    xsize gui.nvl_text_width
    min_width gui.nvl_text_width
    text_align gui.nvl_text_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_thought:
    xpos gui.nvl_thought_xpos
    xanchor gui.nvl_thought_xalign
    ypos gui.nvl_thought_ypos
    xsize gui.nvl_thought_width
    min_width gui.nvl_thought_width
    text_align gui.nvl_thought_xalign
    layout ("subtitle" if gui.nvl_text_xalign else "tex")

style nvl_button:
    properties gui.button_properties("nvl_button")
    xpos gui.nvl_button_xpos
    xanchor gui.nvl_button_xalign

style nvl_button_text:
    properties gui.button_text_properties("nvl_button")



################################################################################
## Mobile Variants
################################################################################

style pref_vbox:
    variant "medium"
    xsize 450

## Since a mouse may not be present, we replace the quick menu with a version
## that uses fewer and bigger buttons that are easier to touch.
screen quick_menu():
    variant "touch"

    zorder 100

    if quick_menu:

        hbox:
            style_prefix "quick"

            xalign 0.5
            yalign 1.0

            textbutton _("Back") action Rollback()
            textbutton _("Skip") action Skip() alternate Skip(fast=True, confirm=True)
            textbutton _("Menu") action ShowMenu()


style window:
    variant "small"
    background "gui/phone/textbox.png"

style radio_button:
    variant "small"
    foreground "gui/phone/button/radio_[prefix_]foreground.png"

style check_button:
    variant "small"
    foreground "gui/phone/button/check_[prefix_]foreground.png"

style nvl_window:
    variant "small"
    background "gui/phone/nvl.png"

style main_menu_frame:
    variant "small"
    background "gui/phone/overlay/main_menu.png"

style game_menu_outer_frame:
    variant "small"
    background "gui/phone/overlay/game_menu.png"

style game_menu_navigation_frame:
    variant "small"
    xsize 340

style game_menu_content_frame:
    variant "small"
    top_margin 0

style pref_vbox:
    variant "small"
    xsize 400

style bar:
    variant "small"
    ysize gui.bar_size
    left_bar Frame("gui/phone/bar/left.png", gui.bar_borders, tile=gui.bar_tile)
    right_bar Frame("gui/phone/bar/right.png", gui.bar_borders, tile=gui.bar_tile)

style vbar:
    variant "small"
    xsize gui.bar_size
    top_bar Frame("gui/phone/bar/top.png", gui.vbar_borders, tile=gui.bar_tile)
    bottom_bar Frame("gui/phone/bar/bottom.png", gui.vbar_borders, tile=gui.bar_tile)

style scrollbar:
    variant "small"
    ysize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/horizontal_[prefix_]bar.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/horizontal_[prefix_]thumb.png", gui.scrollbar_borders, tile=gui.scrollbar_tile)

style vscrollbar:
    variant "small"
    xsize gui.scrollbar_size
    base_bar Frame("gui/phone/scrollbar/vertical_[prefix_]bar.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)
    thumb Frame("gui/phone/scrollbar/vertical_[prefix_]thumb.png", gui.vscrollbar_borders, tile=gui.scrollbar_tile)

style slider:
    variant "small"
    ysize gui.slider_size
    base_bar Frame("gui/phone/slider/horizontal_[prefix_]bar.png", gui.slider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/horizontal_[prefix_]thumb.png"

style vslider:
    variant "small"
    xsize gui.slider_size
    base_bar Frame("gui/phone/slider/vertical_[prefix_]bar.png", gui.vslider_borders, tile=gui.slider_tile)
    thumb "gui/phone/slider/vertical_[prefix_]thumb.png"

style slider_pref_vbox:
    variant "small"
    xsize None

style slider_pref_slider:
    variant "small"
    xsize 600
