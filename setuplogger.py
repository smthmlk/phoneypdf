'''
Logging wrappers
This file is part of the phoneyPDF Framework

Copyright (c) 2013, VERISIGN, Inc

All rights reserved.

Redistribution and use in source and binary forms, with or without modification,
are permitted provided that the following conditions are met:

    * Redistributions of source code must retain the above copyright notice,
      this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above copyright notice,
      this list of conditions and the following disclaimer in the documentation
      and/or other materials provided with the distribution.
    * Neither the name of VERISIGN nor the names of its contributors
      may be used to endorse or promote products derived from this software
      without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR
CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF
LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
'''
import logging, sys

logger = None
def getSetupLogger(name=None, level=logging.DEBUG) :

    if name is None :
        name = 'analysis'

    global logger

    # Default, root logger setup.
    if logger is not None:
        return logger

    logger = logging.getLogger()
    logger.setLevel( level )

    handler = logging.StreamHandler( sys.stdout )
    handler.setFormatter( logging.Formatter('[%(levelname)s %(module)s:%(funcName)s] %(message)s') )

    logger.addHandler( handler )

    return logger

def getNoInfoLogger(name=None, level=logging.DEBUG):
    if name is None :
        name = 'general'

    logger = logging.getLogger(name)
    logger.setLevel( level )

    handler = logging.StreamHandler( sys.stdout )
    handler.setFormatter( logging.Formatter('%(message)s') )

    logger.addHandler( handler )

    return logger
