#! /usr/bin/env python3

# This is a module selector and doesn't use many commands as it is used to only select module

import sys
import mod_interpreter as modinterpreter
import modules.data.OptInfHelp as data
import modules.data.AboutList as Module
from data import colors

FSUCCESS = colors.FSUCCESS
FALERT = colors.FALERT
FNORMAL = colors.FNORMAL
FURGENT = colors.FURGENT

def banner():
    print('''
                          *               *    *          *
                          *               *   *     *     *
                          *               *  *            *
    * ***   * **   ****   * ***    ****   * *      **    ****
    **   *   *    *    *  **   *  *    *  **        *     *
    *    *   *    *    *  *    *  ******  * *       *     *
    **   *   *    *    *  *    *  *       *  *      *     *
    * ***    *    *    *  **   *  *    *  *   *     *     *  *
    *        *     ****   * ***    ****   *    *  *****    **
    *
    *

    -- by theEndurance-del
    ''')

banner()

def __returnval(value, pos):
    try:
        return value[int(pos)]
    except Exception as e:
        return None

Mod = Module.moduleHelp('')

exitStatus = FSUCCESS+'0'

try:
    while True:
        value = input(FNORMAL+'[probkit]:'+f' {exitStatus}'+FNORMAL+'$> ')

        commandSplit = value.split()

        if value in [None, '']:
            exitStatus = FURGENT+"idle"

        elif value[0] == '#':
            exitStatus = FSUCCESS+'0'

        elif value in ['exit', 'terminate']:
            sys.exit()

        elif value == "help":
            exitStatus = FSUCCESS+'0'
            Data = data.Help('')
            Data.showHelp()

        elif value == "list":
            exitStatus = FSUCCESS+'0'
            Mod.listmodules()

        elif value == "banner":
            banner()

        elif __returnval(commandSplit, 0) == 'clear':
            print(chr(27)+'2[j')
            print('\x33c')
            print('\x1bc')
            exitStatus = FSUCCESS+'0'
            if __returnval(commandSplit, 1) in ['exit', 'terminate']:
                sys.exit()

        elif __returnval(commandSplit, 0) == 'use':
            if __returnval(commandSplit, 1) in Module.moduleHelp.modules:
                exitStatus = FSUCCESS+'0'
                modinterpreter.interpreter(__returnval(commandSplit, 1))
            elif not __returnval(commandSplit, 1):
                print(FALERT+'Error: no module specified')
                exitStatus = FALERT+'1'
            else:
                print(FALERT+'Error: Invalid module specified')
                exitStatus = FALERT+'1'

        elif __returnval(commandSplit, 0) == 'about':
            if __returnval(commandSplit, 1):
                mod = __returnval(commandSplit, 1)
                Module.moduleHelp(mod).aboutModule(mod)
                exitStatus = FSUCCESS+'0'
            else :
                print(FALERT+'Error: No module specified')
                exitStatus = FALERT+'1'

        else:
            print(FALERT+'Error: Invalid Syntax')
            exitStatus = FALERT+'1'

except EOFError:
    print(FALERT+f'\nprobKit: exiting session')
