"""generator provides generator functions for different cfg files"""
import os
from helpers import alias, bind, buy, exec_cfg
from constants import BUTTONS, WEAPONS, PATHS, SLOTS, CFGS


def generate_autoexec():
    """generate_autoexec generates autoexec.cfg"""
    path = os.path.abspath(PATHS.autoexec)
    with open(path, 'w', encoding='utf-8', ) as file:
        # first line won't be executed
        file.write('// file generated with code, do not edit.\n\n')

        # buy bindings
        file.write(bind(BUTTONS.NAV.ins, buy(WEAPONS.UTIL.decoy)))
        file.write(bind(BUTTONS.NAV.home, buy(
            WEAPONS.UTIL.fireT), buy(WEAPONS.UTIL.fireCT)))
        file.write(bind(BUTTONS.NAV.pgup, buy(WEAPONS.UTIL.zeus)))
        file.write(bind(BUTTONS.NAV.delete, buy(WEAPONS.UTIL.flash)))
        file.write(bind(BUTTONS.NAV.end, buy(WEAPONS.UTIL.he)))
        file.write(bind(BUTTONS.NAV.pgdn, buy(WEAPONS.UTIL.smoke)))
        file.write(bind(BUTTONS.NAV.lf, buy(WEAPONS.UTIL.helm)))
        file.write(bind(BUTTONS.NAV.dn, buy(WEAPONS.UTIL.armour)))
        file.write(bind(BUTTONS.NAV.rt, buy(WEAPONS.UTIL.kit)) + '\n')

        # weapon slot switch bind
        file.write(bind('v', SLOTS.flash))
        file.write(bind('n', SLOTS.smoke))
        file.write(bind('m', SLOTS.fire) + '\n')

        # exec
        file.write(bind('.', exec_cfg(CFGS.mapruns)) + '\n')

        # jump throw binds
        file.write(bind('h', '+jump', '-attack', '-attack2', '-jump'))
        file.write(bind('o', '+jump', '+forward', '-attack', '-attack2', '-forward', '-jump'))

        # mouse
        file.write(bind(BUTTONS.MOUSE.up, '+jump'))
        file.write(bind(BUTTONS.MOUSE.dn, '+duck') + '\n')

        # general bindings
        file.write(bind('j', 'teammenu'))
        file.write(bind('t', '+spray_menu'))
        file.write(bind('/', 'kill', 'mp_restartgame 1', 'mp_warmup_end'))
        file.write(bind(BUTTONS.SPECIAL.alt, 'noclip'))
        file.write(bind(BUTTONS.NAV.up, 'toggle voice_enable 0 1') + '\n')

        # alias
        file.write(alias('dd', 'disconnect'))
        file.write(alias('qq', 'quit') + '\n')
