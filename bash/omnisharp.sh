#!/bin/bash
mono /g/omnisharp-roslyn/omnisharp/OmniSharp.exe -v -lsp -z $@ | tee ~/omnisharp-log
