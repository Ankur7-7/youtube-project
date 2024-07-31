import os
import threading
import pandas as pd
import re

import openai
from dotenv import load_dotenv, find_dotenv
import json

import googleapiclient.discovery
from google.oauth2 import service_account


class youtube_api():
    def __init__(self, search):
        self.scopes = ["https://www.googleapis.com/auth/youtube.readonly"]

        # Disable OAuthlib's HTTPS verification when running locally.
        # *DO NOT* leave this option enabled in production.
        # os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

        self.searchTerm = search
        self.threads = []
        self.video_list = []
        self.video_lock = threading.Lock()
        self.comments = []
        self.comments_list=[]
        self.data_sort=[]

        self.api_service_name = "youtube"
        self.api_version = "v3"
        # Client secrets file path
        self.key_path = "app/config/youtube-api.json"

        # Get credentials and create an API client

        """
        flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
            client_secrets_file, scopes)
        credentials = flow.run_console()
        """
        self.credentials = service_account.Credentials.from_service_account_file(self.key_path, scopes=self.scopes)

        self.youtube = googleapiclient.discovery.build(
            self.api_service_name, self.api_version, credentials = self.credentials)

        self.search_params = {
            "part": "snippet",
            'maxResults': 100,
            'q': self.searchTerm
        }

        # LLM parameters
        self._start = load_dotenv(find_dotenv())
        openai.api_key = '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'
        self.reviews = []
        self.summary = ""
        self.sentiment = []
        self.funnyCom = []
        self.positiveCom = []

    def fetch_comments(self, video_id, comments_list):
        log = ""
        try:
            os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

            api_service_name = "youtube"
            api_version = "v3"
            # youtube-api
            DEVELOPER_KEY = "AIzaSyBoF_PgaeElLfFEr6r56m3Cd8gyKsdxPQU"

            # youtube-dummy
            #DEVELOPER_KEY = "AIzaSyAL-KSE9emHiADhxAOjjkLAVUQ509sVMZc"

            #dummy-project
            #DEVELOPER_KEY = "AIzaSyD18HWF4gNdGAOTCoHIBvwizdPeWADCxAQ"

            #dummy5
            #DEVELOPER_KEY = "AIzaSyBc7Tb26ZDOntAUcQfEq8uBgfUJApCsvHE"

            youtube = googleapiclient.discovery.build(
                api_service_name, api_version, developerKey=DEVELOPER_KEY)

            request = youtube.commentThreads().list(
                part="snippet,replies",
                order="relevance",
                maxResults=100,
                videoId=video_id
            )
            response = request.execute()

            comments_list.append(response["items"])

        except Exception as e:
            log = log + str(e) + " "

    def get_id(self, x):
        if (x["kind"] == "youtube#video"):
            return x["videoId"]
        return None

    def fetch_videos(self, pageToken=None):

        if (pageToken):
            self.search_params["pageToken"] = pageToken

        response = self.youtube.search().list(**self.search_params).execute()
        videos = response.get("items", [])

        self.video_list.extend(videos)

        nextPageToken = response.get("nextPageToken", "")



        if (nextPageToken != "" and len(self.video_list) < 100):
            thread1 = threading.Thread(target=self.fetch_videos, args=(nextPageToken,))
            temp_df = pd.DataFrame.from_dict(videos, orient="columns")
            temp_id = temp_df["id"].apply(self.get_id)

            for videoid in temp_id:
                thread = threading.Thread(target=self.fetch_comments, args=(videoid, self.comments))
                self.threads.append(thread)
                thread.start()

            self.threads.append(thread1)
            thread1.start()

    def get_completion(self, prompt, model="gpt-4", temperature=0):
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
            temperature=temperature,  # this is the degree of randomness of the model's output
        )
        return response.choices[0].message["content"]

    def get_summary(self):
        # get summary of the comments
        prompt = f"""
           These are comments from all videos on YouTube \
           about: {self.searchTerm}.

           Your task is to generate a short summary of the comments \
           extracted from a YouTube videos.

           Summarize the reviews in at most 100 words.

           Review: {self.reviews}
           """

        response = self.get_completion(prompt)
        return response

    def get_sentiments(self):
        # get sentiment of the comments
        prompt = f"""
           These are comments from all videos on YouTube \
           about: {self.searchTerm}.

           What is the sentiment of these comments in five words?

           Review text: {self.reviews}
           """
        response = self.get_completion(prompt)

        return response.split(", ")

    def get_funnyCom(self):
        # get top funny comments
        prompt = f"""
                    These are comments from all videos on YouTube \ 
                    about: {self.searchTerm}.

                    Your task is to fetch most sarcastic or funny comments among these comments.

                    Limit the sarcastic or funny comments to ten in json format.

                    Review: {self.reviews}
                   """

        response = json.loads(self.get_completion(prompt))
        comments = []
        for item in response:
            comments = comments + list(item.values())

        return comments

    def get_positiveCom(self):
        # get top positive comments
        prompt = f"""
                    These are comments from all videos on YouTube \
                    about: {self.searchTerm}.

                    Your task is to fetch most positive comments among these comments.

                    Limit the positive comments to ten in list format.

                    Review: {self.reviews}
                   """

        response = self.get_completion(prompt)

        # comments = []
        # for item in response:
        #     comments = comments + list(item.values())

        return response

    def format_json(self):

        comment_dict = []
        for comment_thread in self.comments:
            comment_dict = comment_dict + comment_thread

        self.data_sort = sorted(comment_dict, key=lambda x: x["snippet"]["topLevelComment"]["snippet"]['likeCount'],
                                reverse=True)


    def fetch_data(self):
        self.fetch_videos()
        for thread in self.threads:
            thread.join()

        self.format_json()

        self.reviews = [y["snippet"]["topLevelComment"]["snippet"]["textOriginal"] for y in self.data_sort[0:100]]

        self.summary = self.get_summary()
        self.sentiment = self.get_sentiments()
        # self.funnyCom = self.get_funnyCom()
        # self.positiveCom = self.get_positiveCom()

        return{
            "videos": self.video_list,
            "comments": self.reviews,
            "summary": self.summary,
            "sentiments": self.sentiment,
            "funny_com": self.funnyCom,
            "positive_com": self.positiveCom
        }
