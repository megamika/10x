#------------------------------------------------------------------------
import N10X

#------------------------------------------------------------------------
def ClangFormat(filename):
	os.system("clang-format -i " + filename)

#------------------------------------------------------------------------
N10X.Editor.AddPostFileSaveFunction(ClangFormat)
