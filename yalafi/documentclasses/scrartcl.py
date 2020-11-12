
#
#   YaLafi: \documentclass{scrartcl}
#

from yalafi.defs import InitModule

require_packages = []

def init_module(parser, options):
    parms = parser.parms

    macros_latex = r"""

        \newcommand{\KOMAoption}[1]{}
        \newcommand{\KOMAoptions}[1]{}

    """

    return InitModule(macros_latex=macros_latex)

