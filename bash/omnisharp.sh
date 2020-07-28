#!/bin/bash
mono /g/omnisharp/OmniSharp.exe -v -lsp -z $@ | tee ~/omnisharp-log
