import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, TextFormat, QueryFormat, UIConfig
from api import demo_web_app

prompt_example_url ='https://raw.githubusercontent.com/ml4j/gpt-scrolls/master/tweets/twitter-fiction-prompt.json'
template_url = "https://raw.githubusercontent.com/ml4j/gtp-3-prompt-templates/master/question-answer/default/templates/question_answer_template_2.json"

import requests
import json

prompt_example_json = json.loads(requests.get(prompt_example_url).text)
template_json = json.loads(requests.get(template_url).text)

query_format = QueryFormat(
    TextFormat(template_json['questionPrefix'], template_json['questionSuffix']),
    TextFormat(template_json['answerPrefix'], template_json['answerSuffix']),
    True,
    TextFormat(template_json['premisePrefix'], template_json['premiseSuffix']))

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=1.1,
          max_tokens=100,
          query_format = query_format)

gpt.set_premise(prompt_example_json['premise'])

for example in prompt_example_json['questionsAndAnswers']:
    gpt.add_example(Example(example['question'], example['answer']))

# Define UI configuration
config = UIConfig(description="Twitter Fiction",
                  button_text="Generate",
                  placeholder=prompt_example_json['defaultPromptQuestion'])


demo_web_app(gpt, config)
