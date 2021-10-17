from gimpfu import *

def import_msl(path) :
    # img = gimp.Image(100, 100)
    # print(path)
    pass

register("python_fu_import_msl",
     "Import Processed MSL Data", 
     "Import Curiosity Rover Data",
     "Jonathan", 
     "Baurer", 
     "2021",
     "Import MSL...",
     "",
     [ (PF_DIRNAME, "path", "Data Location", "C:/Users/jonat/Documents/PlanetaryScience/MSL") ],
     # [ (PF_INT, "amt", "How much?", 50) ],
     [],       # return vals, seldom used
     import_msl,
     menu="<Image>/File/Create")
     # menu="<Image>/Filters/Enhance")

main()