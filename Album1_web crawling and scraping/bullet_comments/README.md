# Fetching Bilibili Danmu

## Objective
Retrieve all danmu (bullet comments) from a Bilibili video and plot a line chart showing the number of comments over time.

## Process
1. Inspect the webpage to locate the danmu source.  
2. Send a request to the danmu URL and obtain the XML content.  
3. Parse the XML to extract the timestamps of danmu messages.  
4. Segment the timestamps for statistical analysis.  
5. Plot a line chart of comment counts over time.  

- **Danmu URL**: https://comment.bilibili.com/{cid}.xml  
-  Link to the demo video (created by me) on Google Drive: https://drive.google.com/file/d/1u7KpCOlwIEvGu4NHduv4Fp_bMAq7SNSK/view?usp=share_link  