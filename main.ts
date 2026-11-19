// Entry program for the make.fun news-image-20261119 bounty.
// Copies entry.png to the output directory (default /output).
// Node 22, standard library only; no network.
import { copyFileSync, mkdirSync } from "node:fs";
import { dirname, join } from "node:path";
import { fileURLToPath } from "node:url";

const outDir = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";
mkdirSync(outDir, { recursive: true });
const here = dirname(fileURLToPath(import.meta.url));
copyFileSync(join(here, "entry.png"), join(outDir, "entry.png"));
