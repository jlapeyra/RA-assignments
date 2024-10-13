import glob
import os

for fn in glob.glob('plots/*.png'):
    fn = fn.replace('\\', '/')
    width = 0.32 if fn.startswith('plots/6-') else 0.48
    print(fr'    \includegraphics[width={width}\linewidth]' + '{'+fn+'}')