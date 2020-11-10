#! /opt/env/bin/python
import shutil, time

# Run as sudo
tic = time.perf_counter()
 
for i in range(1500):
    destfile = "/data/ironsafe/bundle/fis_zip_bundles/fis_zip_bundle" + str(i) + ".zip"
    try:
        shutil.copyfile("fis_zip_bundle.zip", destfile)
    except Exception as e:
        print(e)
        time.sleep(5)
toc = time.perf_counter()

print(f"DB stressor completed in {toc - tic:0.4f} seconds")
 