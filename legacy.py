import openai, re, json, os
from encoder.encoder import get_encoder

MAX_TOKENS = 2048;
openai.api_key = '';

def handlePrompt(prompt):
    assert prompt and prompt != '', 'Unable to handle no/blank prompt';

    prompt = prompt.lower();

    return prompt;

def handleCompletion(completion):
    assert completion and completion != '', 'Unable to handle no/blank completion';

    completionText = re.sub(r'^\s+', '', completion['choices'][0]['text']);

    return completionText;

encoder = get_encoder();

def tokenizePrompt(prompt):
    return encoder.encode(prompt);

def queryPrompt(prompt, cacheCompletion=True, useCachedCompletion=True):
    prompt = handlePrompt(prompt);
    tokens = tokenizePrompt(prompt);

    if (os.path.exists('completion_cache.json')):
        with open('completion_cache.json', 'r') as cacheFile:
            try:
                prompts = json.loads(cacheFile.read());
            except (json.JSONDecodeError):
                prompts = {};

    else:
        prompts = {};

    if (useCachedCompletion):
        if (prompt in prompts):
            return handleCompletion(prompts[prompt]);

    completion = openai.Completion.create(
        engine = 'text-davinci-001',
        prompt = prompt,
        temperature = 0.65,
        max_tokens = MAX_TOKENS - len(tokens)
    );

    completionText = handleCompletion(completion);

    if (cacheCompletion):
        with open('completion_cache.json', 'w') as cacheFile:
            prompts[prompt] = completion; # We don't handle the completion here so that we get the exact completion result sent from the api
            cacheFile.write(json.dumps(prompts));

    return completionText;

while (True):
    prompt = input('Prompt: ');
    print(f'Completion: {queryPrompt(prompt)}');