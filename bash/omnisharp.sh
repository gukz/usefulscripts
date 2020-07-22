#!/bin/bash
mono ~/.cache/omnisharp-vim/omnisharp-roslyn/omnisharp/OmniSharp.exe -v -lsp -z $@ | tee ~/omnisharp-log
