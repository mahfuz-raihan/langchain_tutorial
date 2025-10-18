from urllib.parse import urlparse, parse_qs

def get_youtube_video_id(url: str) -> str | None:
    if not isinstance(url, str):
        return None
    
    try:
        # parse the url to access its compnents
        parsed_url = urlparse(url)

        if parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
        elif parsed_url.hostname in ('www.youtube.com', 'youtube.com'):
            if parsed_url.path == '/watch':
                query_parms = parse_qs(parsed_url.query)
                return query_parms.get('v', [None])[0]
            
            if parsed_url.path[:7] == '/embed/':
                return parsed_url.path.split('/')[2]
            
            if parsed_url.path[:3] == '/v/':
                return parsed_url.path.split('/')[2]
            
            return None
        
    
    except Exception as e:
        print(f"Error happen: {e}")
        return None

# # ----- Example Usage -----
# if __name__ == "__main__":
#     test_url = [
#         "https://youtu.be/hmtuvNfytjM",
#         "https://www.youtube.com/watch?v=hmtuvNfytjM",
#         "https://www.youtube.com/embed/hmtuvNfytjM",
#         "https://www.youtube.com/v/hmtuvNfytjM",
#         "https://www.youtube.com/watch?v=hmtuvNfy",
#         "https://youtu.be/y6120QOlsfU",
#         "https://www.youtube.com/embed/9bZkp7q19f0",
#         "https://www.youtube.com/watch?v=JcEI5tvzZwQ&t=37977s",
#         "http://www.youtube.com/watch?v=0zM3nApSvMg&feature=feedrec_grec_index",
#         "not a valid url",
#         12345,
#         "https://www.google.com"
#     ]
#     print("---- Testing YouTube Video ID Extractor ----")
#     for url in test_url:
#         video_id = get_youtube_video_id(url)
#         if video_id:
#             print(f"Success! Video ID for '{url}': '{video_id}'")
#         else:
#             print(f"Failed to extract video ID from '{url}'")
#     print("---- Testing Complete ----")