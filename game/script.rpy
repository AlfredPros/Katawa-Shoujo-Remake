
define h = Character("Hanako", color="#8A7587", image="hanako")
define l = Character("Lilly", color="#F8F3B6", image="lilly")
define m = Character("Me", color="#E6FF49")

transform t_mid:
    align(0.5, 1.0) alpha 0.0 zoom 0.98
    on show:
        parallel:
            easein 0.2 alpha 1.0
        parallel:
            easein 0.2 zoom 1.0
    on hide:
        parallel:
            easein 0.4 alpha 0.0
        parallel:
            easein 0.4 zoom 0.98
            
transform t_left:
    align(0.25, 1.0) alpha 0.0 zoom 0.98
    on show:
        parallel:
            easein 0.2 alpha 1.0
        parallel:
            easein 0.2 zoom 1.0
    on hide:
        parallel:
            easein 0.4 alpha 0.0
        parallel:
            easein 0.4 zoom 0.98

transform t_right:
    align(0.75, 1.0) alpha 0.0 zoom 0.98
    on show:
        parallel:
            easein 0.2 alpha 1.0
        parallel:
            easein 0.2 zoom 1.0
    on hide:
        parallel:
            easein 0.4 alpha 0.0
        parallel:
            easein 0.4 zoom 0.98


label start:
    scene school_hallway with Dissolve(0.4)

    window show Dissolve(0.2)
    "I walk on the corridor as I saw a figure with dark purple hair"
    
    show hanako bashful at t_mid
    
    h "Hello."
    m "Hello, Hanako."
    
    show hanako bashful:  #This redefines the transform.
        easein 0.2 xalign 0.75
        on hide:
            parallel:
                easein 0.4 alpha 0.0
            parallel:
                easein 0.4 zoom 0.98
                
    show lilly cheerful at t_left
    
    l "What's up brudda?"
    h normal "Hi, Lilly. How are you?"
    l giggle "I'm doing great today."
    m "Are you guys going outside?"
    h smile "Yes. Let's go together."
    window hide Dissolve(0.2)
    
    hide lilly 
    pause 0.2
    hide hanako
    pause 0.4
    
    menu:
        "Yeah, let's go":
            jump after_school
        "No, thanks, I got stuff to do":  #Lol, this doesn't make sense
            jump room

label after_school:
    scene school_gate with Fade(0.5, 0.2, 0.5, color="#000")
    
    window show Dissolve(0.2)
    "okay, me at school gate"
    "But they left me mid way."
    "sedd"
    window hide Dissolve(0.2)
    
    scene blackout with Dissolve(0.5)
    pause 0.5
    
    return
    
label room:
    scene school_dormhisao with Fade(0.5, 0.2, 0.5, color="#000")
    
    window show Dissolve(0.2)
    "ajsdn dijasidt asoud chol butt asdnausd"
    "And sed..."
    window hide Dissolve(0.2)
    
    scene blackout with Dissolve(0.5)
    pause 0.5
    
    return
    