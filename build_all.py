from pathlib import Path
import runpy
base=Path(__file__).parent
for script in ['build.py','localize.py','areas.py','blog.py','offer_blog.py','seo.py']:
    runpy.run_path(str(base/script), run_name='__main__')
