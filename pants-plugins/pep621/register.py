from . import pep621_requirements
from .pep621_requirements import PEP621RequirementsTargetGenerator


def rules():
    return (*pep621_requirements.rules(),)


def target_types():
    return (PEP621RequirementsTargetGenerator,)
