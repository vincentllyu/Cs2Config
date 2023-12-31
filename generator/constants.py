""""This module is to provide constants for generator modules"""

from helpers import DotDict

# Right now the weapon code all associate with a buy mene slot
# rather than the real weapon. For example
WEAPONS = DotDict({
    'RIFLE': {
        'scout': 'ssg08',
        'galil': 'galilar',
        'famas': 'famas',
        'sg': 'sg556',
        'aug': 'aug',
        'a4': 'm4a4',
        'a1': 'm4a1_silencer',
        'ak': 'ak47',
        'autoT': 'g3sg1',
        'autoCT': 'scar20',
        'awp': 'awp',
    },
    'SMG': {
        'mac': 'mac10',
        'ump': 'ump45',
        'p90': 'p90',
        'bizon': 'bizon',
        'mp7': 'mp7',
        'mp9': 'mp9',
        'mp5': 'mp5sd'
    },
    'SHOTGUN': {
        'auto': 'xm1014',
        'mag': 'mag7',
        'saw': 'sawedoff',
        'nova': 'nova',
        '51': 'm249',
        'negev': 'negev'
    },
    'PISTOL': {
        'dual': 'elite',
        '57': 'fiveseven',
        'deagle': 'deagle',
        'tec': 'tec9',
        'p250': 'p250',
        'r8': 'revolver',
        'usp': 'usp_silencer',
        'cz': 'cz75a',
        'p2k': 'hkp2000',
        'glock': 'glock'
    },
    'UTIL': {
        'flash': 'flashbang',
        'smoke': 'smokegrenade',
        'he': 'hegrenade',
        'fireT': 'molotov',
        'fireCT': 'incgrenade',
        'decoy': 'decoy',
        'armour': 'vest',
        'helm': 'vesthelm',
        'zeus': 'taser',
        'kit': 'defuser'
    }
})

BUTTONS = DotDict({
    'NUMPAD': {
        '4': 'kp_leftarrow',
        '.': 'kp_del',
        '1': 'kp_end',
        '2': 'kp_downarrow',
        '9': 'kp_pgup',
        '0': 'kp_ins',
        '5': 'kp_5',
        '+': 'kp_plus',
        '8': 'kp_uparrow',
        'enter': 'kp_enter',
        '3': 'kp_pgdn',
        '6': 'kp_rightarrow',
        '/': 'kp_slash',
        '-': 'kp_minus',
        '7': 'kp_home',
        '*': 'kp_multiply'
    },
    'NAV': {
        'ins': 'ins',
        'home': 'home',
        'pgup': 'pgup',
        'delete': 'del',
        'end': 'end',
        'pgdn': 'pgdn',
        'up': 'uparrow',
        'dn': 'downarrow',
        'lf': 'leftarrow',
        'rt': 'rightarrow'
    },
    'MOUSE': {
        'lf': 'mouse1',
        'rt': 'mouse2',
        'mid': 'mouse3',
        'forward': 'mouse4',
        'back': 'mouse5',
        'up': 'mwheelup',
        'dn': 'mwheeldown'
    },
    'SPECIAL': {
        'tab': 'tab',
        'cap': 'capslock',
        'control': 'ctrl',
        'shift': 'shift',
        'alt': 'alt',
        'space': 'space',
        'alt-r': 'ralt',
        'control-r': 'rctrl',
        'enter': 'enter',
        'backspace': 'backspace'
    }
})

SLOTS = DotDict({
    'primary': 'slo1',
    'pistol': 'slot2',
    'knife': 'slot3',
    'nades': 'slot4',
    'c4': 'slot5',
    'he': 'slot6',
    'flash': 'slot7',
    'smoke': 'slot8',
    'decoy': 'slot9',
    'fire': 'slot10'
})

CFGS = DotDict({
    'autoexec': 'autoexec',
    'mapruns': 'mapruns'
})

PATHS = DotDict({
    CFGS.autoexec: f"./cfg/{CFGS.autoexec}.cfg",
    CFGS.mapruns: f"./cfg/{CFGS.mapruns}.cfg"
})
