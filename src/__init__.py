from robots import DynamicCore


class AWSLib(DynamicCore):

    ROBOT_EXIT_ON_FAILURE = True
    ROBOT_LIBRARY_SCORE = 'GLOBAL'

    def __init__(self, library_components):
        DynamicCore.__init__(self, lib)
