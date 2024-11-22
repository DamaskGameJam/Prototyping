
# Feature 1 
define e = Character("Eileen")
image testGIF = Movie(play="video/test.webm")

# Feature 2
# define .. = ..
# define .. = ..


label start:
    menu:
        "Issue 26 - Rendering GIF's":
            jump render_gif
        "Feature 2":
            jump feature_2
        "Feature 3":
            jump feature_3
        "Feature 4":
            jump feature_4
        "Feature 5":
            jump feature_5

label render_gif:
    "This is how gifs or video files can render. Changing the resolution in renpy does not affect the file, if separate resolution
    is required, a different file with the desired resolution should be exported"
    
    # since the file is defined as image, u can use it the same way.
    show testGIF at truecenter
    pause 4.0
    hide testGIF
    
    jump start

label feature_2:
    "Hello I am feature 2 u can add notes here if u want"
    jump start

label feature_3:
    "Hello I am feature 3 u can add notes here if u want"
    jump start

label feature_4:
    "Hello I am feature 4 u can add notes here if u want"
    jump start

label feature_5:
    "Hello I am feature 5 u can add notes here if u want"
    jump start