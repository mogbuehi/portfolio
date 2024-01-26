from openai import OpenAI
import json
from dotenv import load_dotenv, find_dotenv
import os
import time
import datetime



def wait_on_run(run, thread_id):
  # Initiate client
  load_dotenv(find_dotenv()) 
  api_key = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=api_key)

  # print('THREAD....', thread_id) # debugging
  while run.status == "queued" or run.status == "in_progress":
      run = client.beta.threads.runs.retrieve(
          thread_id=thread_id,
          run_id=run.id,
      )
      time.sleep(0.5)
  return run

# ---

def get_response(thread_id):
  # Initiate client
  load_dotenv(find_dotenv()) 
  api_key = os.getenv('OPENAI_API_KEY')
  client = OpenAI(api_key=api_key)

  return client.beta.threads.messages.list(thread_id=thread_id, order="desc")


def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


# ---ai_assistant function---


def ai_assistant(user_input, thread_id, client, assistant_id='asst_4vFJMXr6BosawJJTYOJw2fBY'):
  # Use the thread_id from the session state
  
  # Send the user message to the thread
  message = client.beta.threads.messages.create(
      thread_id=thread_id,
      role="user",
      content=user_input
  )

  # Create and run the assistant, waiting for it to complete
  run = client.beta.threads.runs.create(thread_id=thread_id, assistant_id=assistant_id)
  run = wait_on_run(run, thread_id)  # Make sure that the wait_on_run function is using the thread_id, not a thread object

  # Retrieve the list of messages and extract the AI's response
  messages = get_response(thread_id)  # Make sure that the get_response function is using the thread_id, not a thread object

  ai_message = json.loads(messages.model_dump_json())
  # print(ai_message)
  ai_message = ai_message['data'][0]['content'][0]['text']['value']

  convo = f'''Time: {datetime.datetime.now()}
  User: {user_input}\n\nAI: {ai_message}\n\nThread_ID: {thread_id}'''

  return ai_message

