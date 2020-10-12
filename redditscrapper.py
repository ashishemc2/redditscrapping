import praw
import pwd
import chromebrow
import urllib.request


def main():
    reddit = praw.Reddit(client_id=pwd.client_id,
                         client_secret=pwd.client_secret,
                         password=pwd.password,
                         user_agent="testscript by u/ashishemc2",
                         username=pwd.username)

    subreddit = reddit.subreddit("LivestreamFail")

    clip_urls = {}
    for submission in subreddit.hot(limit=25):

        url = ""
        if submission.url.startswith("https://clips.twitch.tv"):
            print(submission.title)
            clip_urls[submission.title] = submission.url

    src_urls = chromebrow.get_src_url(clip_urls)
    print(src_urls)
    for video_name, src_url in src_urls.items():
        urllib.request.urlretrieve(src_url, './videos/' + video_name + '.mp4')


if __name__ == '__main__':
    main()
