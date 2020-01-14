# Download data from the GDELT Project

This project is written for downloading data from [the GDELT Project](https://www.gdeltproject.org/data.html#rawdatafiles).

## V1 Dataset
To download GDELT 1.0 dataset, run scrip `Crawl_V1_From_HTML.py`.

## V2 Dataset
To download GDELT 2.0 dataset, please visit web page [GDELT 2.0: Our Global World in Realtime](https://blog.gdeltproject.org/gdelt-2-0-our-global-world-in-realtime/). 
At the page bottom, there are several ways to get download links. 
For the automated download script in this project, please visit the [Master CSV Data File List – English](http://data.gdeltproject.org/gdeltv2/masterfilelist.txt) at the bottom and save the file as `raw_V2_from_website.txt`. Then run following code to extract.

```
import pandas as pd
raw_V2_from_website = pd.read_table('raw_V2_from_website.txt',delimiter=' ',names=['index','size','link'])
raw_V2_from_website.link = raw_V2_from_website.link.astype(str)
V2events = raw_V2_from_website[raw_V2_from_website.link.apply(lambda x: 'export' in x)].link
V2gkgs = raw_V2_from_website[raw_V2_from_website.link.apply(lambda x: 'gkg' in x)].link
V2mentions = raw_V2_from_website[raw_V2_from_website.link.apply(lambda x: 'mentions' in x)].link
pd.DataFrame(V2events).to_csv('V2events.csv',index=False)
pd.DataFrame(V2gkgs).to_csv('test.csv',index=False)
pd.DataFrame(V2mentions).to_csv('V2mentions.csv',index=False)
```

Finally, run script `Download_V2.py`.