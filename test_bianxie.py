import dspy
lm = dspy.LM('openai/gpt-3.5-turbo', api_base="https://api.bianxie.ai/v1", api_key="sk-vKirQEe0vJmMN3X9UAENCCdheTHII81VCQm0NZHzG781H95Y", max_tokens=4000)
dspy.configure(lm=lm)

lm("Say this is a test!", temperature=0.7)  # => ['This is a test!']
print(lm(messages=[{"role": "user", "content": "Hello, How are you?"}]))  # => ['Hello, How are you?']

# https://api.bianxie.ai/pricing