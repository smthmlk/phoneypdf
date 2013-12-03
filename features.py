'''
PDF Feature extraction for Machine Learning
This file is part of the phoneyPDF Framework

Various features in PDF Format, used in ML
Legend:
 P_ : Presence
 F_ : Feature
 S_ : Stats
 C_ : Count
 L_ : Length / Size

Kiran Bandla <kbandla@intovoid.com>

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

# JavaScript related Features
F_P_JS_SUSPICIOUS_HEAPSPRAY = "F_JS_SUSPICIOUS_HEAPSPRAY"
F_P_JS_RAWVALUE = "F_JS_RAWVALUE"

# PDF related Features
F_P_PDF_OPENACTION    =   "F_PDF_OPENACTION"
F_P_PDF_RENDITION     =   "F_PDF_RENDITION"
F_P_PDF_ = ""
F_L_PDF_LENGTH      =   "F_L_PDF_LENGTH"

# Statistical Features
F_C_JS_SCRIPTS_EXECUTION_FAILED =   "F_C_JS_SCRIPTS_EXECUTION_FAILED"
F_C_JS_SCRIPTS_FOUND    =   "F_C_JS_SCRIPTS_FOUND"
F_C_JS_SCRIPTS_EXECUTED =   "F_C_JS_SCRIPTS_EXECUTED"
F_L_JS_SCRIPTS_LENGTH_TOTAL =   "F_L_JS_SCRIPTS_LENGTH_TOTAL"

F_S_PERCENTAGE_SCRIPT   =   "F_S_PERCENTAGE_SCRIPT"

# JavaScript Execution Features
F_C_JS_UNESCAPE_CALLS =   "c_unescape_calls"
F_C_JS_UNESCAPE_LONG_PARAMS = "c_unescape_long_params"
F_L_JS_UNESCAPE_LENGTH  =   "l_unescape_param"
