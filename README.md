# PyYouTube 


Get Video Data from YouTube link 

## Installation 
```bash
pip install py-youtube
```

## How to use it ?
#### Get Videos Data 

```python
from py_youtube import Data
data = Data("https://youtu.be/HhHzCfrqsoE").data()
print(data)
```
<details>
  <summary><b>Example Results</summary>
<br/>

```json
{
  'id': 'HhHzCfrqsoE',
   'title': 'How To Create MongoDB Database  Url', 
   'thumbnails': 'https://i.ytimg.com/vi/HhHzCfrqsoE/hqdefault.jpg?sqp=-oaymwEiCKgBEF5IWvKriqkDFQgBFQAAAAAYASUAAMhCPQCAokN4AQ==\\u0026rs=AOn4CLBOkJZAdEpYxQOVdaUxFHdbThH_DQ',  
   'views': '709', 
   'likes': '27', 
   'dislikes': '1', 
   'publishdate': '2021-08-04', 
   'category': 'Howto \\u0026 Style', 
   'channel_name': 'Ln Technical', 
   'subscriber': '1.67K', 
   'keywords': 'video, sharing, camera phone, video phone, free, upload'
}
```

</details>
