import sys

CODE_PATH = "C:\\Users\\jonat\\Documents\\PlanetaryScience\\MSL\\python\\gimp"
sys.path.append(CODE_PATH)
from import_msl import *


def import_msl_img_test(arg):
    # print("Hello gimp world")

    # i = Image(os.path.join(data_path, '2713ML0142060011003969C00_DRCX.IMG'))'
    test_fn()


# register("python_import_msl_img_test",
#          "MSL Import Test", "Test importing an MSL image",
#          "J", "Baurer", "2021",
#          "MSL Import test",
#          "",
#          [(PF_FILE, "ifile", N_("Color input file"), 'default.txt'), ],
#          [],
#          import_msl_img_test,
#          menu="<Image>/Filters/Enhance")
# register(
#     "MSL Import Test",  # <- this is plugin name
#     N_("brief"),  # <- description
#     "MSL Import Test",  # <- description
#     "name surname",  # <- author
#     "@Copyright 2013",  # <- copyright info
#     "2013/10/29",  # <- creation date
#     N_("MSL Import Test."),  # <- label shown in gimp's menu
#     "",  # <- kind of image requested from your script (INDEX,RGB,...and so on)
#     [  # <- input parameters array
#         (PF_FILE, "ifile", N_("Color input file"), 'default.txt'),
#     ],
#     [],  # <- output parameters array (usually empty)
#     import_msl_img_test,  # <- main method to call
#     menu="<Image>/Filters/Enhance",  # <- Where add your plugin
#     domain=("gimp20-python", gimp.locale_directory)
# )

# main()
