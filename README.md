# dbNSFP investigation

This repo houses work done for:
https://github.com/ClinGen/gene-and-variant-curation-tools/issues/350

The predecessor issue is:
https://github.com/ClinGen/gene-and-variant-curation-tools/issues/348

## Instructions

- Download dbNSFP (could take up to an hour depending on connection).
- Decompress the archive: `unzip dbNSFP[...].zip -d data/dbNSFP[...]`.
- Decompress portion you're interested in, e.g. `gzip -d dbNSFP4.3a_variant.chrX.gz`.
  This will be a tab-separated values file with millions of lines. 
- Use Unix command line tools to get relevant lines.
    - Get the column names: `head -n 1 [file]`.
    - Search for a pattern using ripgrep: `rg [pattern] [file]`.
- Output relevant lines to a `.tsv` file.
- Set the `FILE_NAME` variable in the `parse.py` script.
- Invoke `python parse.py` to print columns in a readable format.
