
#
#   YaLafi module for LaTeX package xcolor
#

from yalafi.defs import ModParm

require_packages = []

def modify_parameters(parms):

    macros_latex = r"""

        \newcommand{\color}[1]{}
        \newcommand{\colorbox}[2]{#2}
        \newcommand{\definecolor}[3]{}
        \newcommand{\fcolorbox}[3]{#3}
        \newcommand{\textcolor}[2]{#2}

    """

    macros_python = []

    environments = []

    return ModParm(macros_latex=macros_latex, macros_python=macros_python,
                        environments=environments)

