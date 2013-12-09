import logging
import sys

class SpecificLevelsFilter(logging.Filter):
    def __init__(self, lvl):
        self.level = lvl
    def filter(self, record):
        return record.levelno <= self.level


def buildLogger():
    # This handler only applies to DEBUG and INFO levels and outputs to console in a way that doesn't interfere
    # with the msg formatting.
    debugInfoHandler = logging.StreamHandler( sys.stdout )
    debugInfoHandler.setLevel(logging.DEBUG)
    debugInfoHandler.addFilter( SpecificLevelsFilter(logging.INFO) )
    debugInfoHandler.setFormatter( logging.Formatter("%(message)s [%(funcName)s()]") )

    # This handler applies to WARNING, CRITICAL and ERROR levels, and shows a lot of detail.
    noteworthyHandler = logging.StreamHandler( sys.stdout )
    noteworthyHandler.setLevel(logging.WARNING)
    noteworthyHandler.setFormatter( logging.Formatter("[%(levelname)s %(filename)s:%(funcName)s:%(lineno)d] %(message)s") )

    # Adding these two handlers to the pcaphandler logger instance.
    lggr = logging.getLogger('phoneyPDF')
    lggr.addHandler( debugInfoHandler )
    lggr.addHandler( noteworthyHandler )

    return lggr
