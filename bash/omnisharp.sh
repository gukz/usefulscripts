#!/bin/bash
mono /mnt/c/dev/omnisharp/OmniSharp.exe -v -lsp -z $@ | tee ~/omnisharp-log
