#!/bin/sh

ls -F input/doc | xargs -I {} /Applications/LibreOffice.app/Contents/MacOS/soffice --headless --convert-to docx ./input/doc/{} --outdir ./input/docx/