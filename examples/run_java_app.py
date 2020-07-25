import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

prompt_example_url ='https://raw.githubusercontent.com/ml4j/gtp-3-prompt-templates/master/question-answer/code-explanation/examples/java-example-1/code_explanation_example_prompt_1.json'
template_url = 'https://raw.githubusercontent.com/ml4j/gtp-3-prompt-templates/master/question-answer/code-explanation/templates/code_explanation_template_1.json'

import requests
import json

prompt_example_json = json.loads(requests.get(prompt_example_url).text)
template_json = json.loads(requests.get(template_url).text)

question_prefix = template_json['questionPrefix']
question_suffix = template_json['questionSuffix']
answer_prefix = template_json['answerPrefix']
answer_suffix = template_json['answerSuffix']

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.1,
          max_tokens=100,
          input_prefix = question_prefix,
          input_suffix = question_suffix,
          output_prefix = answer_prefix,
          output_suffix = answer_suffix,
          append_output_prefix_to_query = True)


for example in prompt_example_json['questionsAndAnswers']:
    gpt.add_example(Example(example['question'], example['answer']))

# Define UI configuration
config = UIConfig(description="Code to comment",
                  button_text="Translate",
                  placeholder=prompt_example_json['defaultPromptQuestion'])


demo_web_app(gpt, config)
