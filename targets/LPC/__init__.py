from .. import toolchain_makefile

class LPC_target(toolchain_makefile):
    extension = ".ld"
    DebugEnabled = False
    def getBuilderLDFLAGS(self):
        return toolchain_makefile.getBuilderLDFLAGS(self)