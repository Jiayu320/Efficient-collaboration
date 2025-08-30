# pip3 install transformers
# python3 deepseek_tokenizer.py
import transformers
# from transformers import PreTrainedTokenizerFast

chat_tokenizer_dir = "deepseek_v3_tokenizer/"
# tokenizer = PreTrainedTokenizerFast.from_pretrained(chat_tokenizer_dir)


tokenizer = transformers.AutoTokenizer.from_pretrained( 
        chat_tokenizer_dir, 
        trust_remote_code=True
        )

result = tokenizer.encode("Hello!")
print(result)
