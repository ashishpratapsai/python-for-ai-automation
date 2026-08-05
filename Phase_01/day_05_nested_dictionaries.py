video = {
    "title": "how to use claude Code",
    "stats" : {
        "views": 1500,
        "likes" : 230,
        "comments": 45
    },
    "channel" : {
        "name":"Automate With Ashish",
        "subscribers": 5000
    }
}

def get_video_stats(video):
    return{
        "title": video["title"],
        "likes": video["stats"]["likes"],
        "subscribers": video["channel"]["subscribers"]
    }

output = get_video_stats(video)
print(output)
