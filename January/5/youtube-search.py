#!/usr/bin/python

# Script I use in conjunction with a Google Chrome extensions "Hide Youtube Progress Bar" to not get spoiled when watching (e)Sports
# Creates a html file with links to the videos it finds, so you can avoid seeing how long videos are before opening them
#
# This script uses python 2.7, and relies on the Youtube Data API
# Use pip or whatever to install "google-api-python-client"
#
# You'll also need to setup a project with a Youtube Data API Key through a google account (free)
#
# Use for example as follows (from terminal): python run.py --q ronnie\ o\'sullivan\ final\ john\ higgins\ 2016
#
# Below code modified from an example found here: https://developers.google.com/youtube/v3/code_samples/python

from apiclient.discovery import build
from apiclient.errors import HttpError
from oauth2client.tools import argparser

# Set DEVELOPER_KEY to the API key value from the APIs & auth > Registered apps
# tab of
#   https://cloud.google.com/console
# Please ensure that you have enabled the YouTube Data API for your project.
DEVELOPER_KEY = ""
YOUTUBE_API_SERVICE_NAME = "youtube"
YOUTUBE_API_VERSION = "v3"
MAX_RESULTS = 25

def youtube_search(options):
    youtube = build(YOUTUBE_API_SERVICE_NAME, YOUTUBE_API_VERSION,
                    developerKey=DEVELOPER_KEY)

    # Call the search.list method to retrieve results matching the specified
    # query term.
    search_response = youtube.search().list(
        q=options.q,
        part="id,snippet",
        maxResults=options.max_results
    ).execute()

    titles = []
    links = []

    # Add each result to the appropriate list, and then display the lists of
    # matching videos, channels, and playlists.
    for search_result in search_response.get("items", []):
        if search_result["id"]["kind"] == "youtube#video":
            titles.append("%s" % search_result["snippet"]["title"])
            links.append("%s" % "https://www.youtube.com/watch?v=" + search_result["id"]["videoId"])

    file = open("results.html", "w")
    s = "<html><body>\n"
    file.write(s.encode("utf8"))
    for i in range(0, len(links)):
        s = "<a href=\"" + links[i] + "\">" + titles[i] + "</a>\n<br>\n"
        file.write(s.encode("utf8"))
    s = "</body></html>"
    file.write(s.encode("utf8"))

    file.close()


if __name__ == "__main__":
    argparser.add_argument("--q", help="Search term", default="Google")
    argparser.add_argument("--max-results", help="Max results", default=MAX_RESULTS)
    args = argparser.parse_args()

    try:
        youtube_search(args)
    except HttpError, e:
        print "An HTTP error %d occurred:\n%s" % (e.resp.status, e.content)
