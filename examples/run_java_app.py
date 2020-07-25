import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

from api import GPT, Example, UIConfig
from api import demo_web_app

question_prefix = 'What does the code below do? Write one comment for each of the following numbered statements:\n\n'
question_suffix = "\n\n"
answer_prefix = "Comments:\n\n"
answer_suffix = "\n\n"

# Construct GPT object and show some examples
gpt = GPT(engine="davinci",
          temperature=0.1,
          max_tokens=100,
          input_prefix = question_prefix,
          input_suffix = question_suffix,
          output_prefix = answer_prefix,
          output_suffix = answer_suffix,
          append_input_suffix_and_output_prefix_to_query = True,
          stop = "\n" + question_prefix)

gpt.add_example(Example('Statement 1) stream().map(Dimension::getName).collect(Collectors.toList()).toString();\n' +
'Statement 2) stream().flatMap(c -> c.decompose().stream()).collect(Collectors.toList());\n' +
'Statement 3) allDecomposedAliases.add(decompose().stream().collect(Collectors.toList()));\n' +
'Statement 4) box.getScaledCorners(originalImage.getWidth(), originalImage.getHeight()));\n' +
'Statement 5) List<Image> subImages = channelConcatImages.subList(channelRangeStart, channelRangeEnd);',
'Statement 1) // Obtain the names of the dimensions, collect them into a list, and return the list as a string.\n' +
'Statement 2) // Call decompose recursively on each of the elements of the stream and collect the results into a list\n' +
'Statement 3) // Collect the aliases from the stream returned by the decompose() method into a list, and add them to allDecomposedAliases\n' +
'Statement 4) // Get the scaled corners of a bounding box using its width and height of the original image\n' +
'Statement 5) // Obtain a list of the elements of subImages with indexes been channelRangeStart (inclusive) and channelRangeEnd (exclusive) and assign the list to a local variable called subImages',question_prefix, question_suffix, answer_prefix, answer_suffix))


# Define UI configuration
config = UIConfig(description="Code to comment",
                  button_text="Translate",
                  placeholder="Statement 1) List<User> friendsList = me.getFriends();\n"
"Statement 2) List<User> genXFriends = friendsList.stream().filter(user.getAge() > 40 user.getAge() <= 55).collect(Collectiors.toList());\n" +
"Statement 3) genXFriends.forEach(user -> user.sendMessage(\"Hi \" + user.getScreenName() + \"you are the best!\");")


demo_web_app(gpt, config)
