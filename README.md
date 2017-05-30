# FIRMify
Batch convert your a9lh payloads to firm format.

Just put this in your luma/payloads directory, run it, and it should convert all of your a9lh .bin payloads to boot9strap compatible .firm format (as separate files). This should work with python2 or 3. Never install any payloads generated with this script to NAND, it's only intended for arm9 payloads. Not all converted a9lh payloads will work in a boot9strap environment without source modifications.
