"""
TODO: import all processes here and add to core
TODO -- make a "register_types" function that takes a core, registers all types and returns the core.
"""

from compucell_tissueforge.processes import register_processes


def register_types(core):
    core.register('set_float', {
        '_inherit': 'float',
        '_apply': 'set'})

    core.register(
        'positions',
        'list[tuple[float,float,float]]')

    # TODO: provide utility to set the '_apply' method to an existing schema
    core.register(
        'domains', {
            '_type': 'map',
            '_value': {
                '_type': 'tuple',
                '_apply': 'set',
                '_0': 'positions',
                '_1': 'positions'
            }
        }
    )

    return register_processes(core)
