import os
import requests

ai21_api_key = os.getenv('AI21_API_KEY', '')

def compare_job_titles(job_title1, job_title2):
    prompt = "Compare the following job descriptions into one of four similarity level from 1 to 4:\n1. Completely not" \
             " similar\n2. Somewhat similar\n3. Very similar\n4. The same\nFirst job description:\n\"AI/ML" \
             " Implementation Lead\"\nSecond job description:\n\"Biotope maintanence\"\nThe similarity level between" \
             " is: 1\n===\nCompare the following job descriptions into one of four similarity level from 1 to 4:\n1." \
             "Completely not similar\n2. Somewhat similar\n3. Very similar\n4. The same\nFirst job description:\n\"" \
             "AI/ML Engineer\"\nSecond job description:\n\"Data scientist\"\nThe similarity level between is:" \
             " 3\n===\nCompare the following job descriptions into one of four similarity level from 1 to 4:\n1." \
             " Completely not similar\n2. Somewhat similar\n3. Very similar\n4. The same\nFirst job description:\n\"" \
             "Author\"\nSecond job description:\n\"Writer\"\nThe similarity level between is: 4\n===\nCompare the" \
             " following job descriptions into one of four similarity level from 1 to 4:\n1. Completely not similar" \
             "\n2. Somewhat similar\n3. Very similar\n4. The same\nFirst job description:\n\"Researcher\"\nSecond" \
             " job description:\n\"Teacher\"\nThe similarity level between is: 2\n===\nCompare the following job" \
             " descriptions into one of four similarity level from 1 to 4:\n1. Completely not similar\n2. Somewhat" \
             " similar\n3. Very similar\n4. The same\nFirst job description:\n\""\
             + job_title1 + "\"\nSecond job description:\n\"" + job_title2 + "\"\nThe similarity level between is:"

    response = requests.post("https://api.ai21.com/studio/v1/experimental/j1-grande-instruct/complete",
                  headers={"Authorization": "Bearer YOUR_API_KEY"},
                  json={
                      "prompt": prompt,
                      "numResults": 1,
                      "maxTokens": 15,
                      "temperature": 0.53,
                      "topKReturn": 0,
                      "topP": 1,
                      "countPenalty": {
                          "scale": 0,
                          "applyToNumbers": False,
                          "applyToPunctuations": False,
                          "applyToStopwords": False,
                          "applyToWhitespaces": False,
                          "applyToEmojis": False
                      },
                      "frequencyPenalty": {
                          "scale": 0,
                          "applyToNumbers": False,
                          "applyToPunctuations": False,
                          "applyToStopwords": False,
                          "applyToWhitespaces": False,
                          "applyToEmojis": False
                      },
                      "presencePenalty": {
                          "scale": 0,
                          "applyToNumbers": False,
                          "applyToPunctuations": False,
                          "applyToStopwords": False,
                          "applyToWhitespaces": False,
                          "applyToEmojis": False
                      },
                      "stopSequences": ["==="]
                  }
    )
    print(response)
    return response.text