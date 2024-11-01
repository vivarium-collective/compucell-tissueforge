"""
This module is used to register the processes with the core.
"""
from compucell_tissueforge.processes.CC3DProcess import CC3DProcess
from compucell_tissueforge.processes.TissueForgeProcess import TissueForgeProcess
from compucell_tissueforge.processes.volume_from_particles import VolumeFromParticles


def register_processes(core):
    core.register_process('TissueForge', TissueForgeProcess)
    core.register_process('CompuCell3D', CC3DProcess)
    core.register_process('VolumeFromParticles', VolumeFromParticles)

    return core
