# ../addons/errors.py

# =============================================================================
# >> ALL DECLARATION
# =============================================================================
# Set all to an empty list
__all__ = []


# =============================================================================
# >> CLASSES
# =============================================================================
class AddonFileNotFoundError(Exception):
    '''Addon file not found.'''