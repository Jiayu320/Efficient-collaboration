from util.io_file import read_json, write_json

file_path = "data/structure/limo/0.json"  # Replace with your actual file path
data = read_json(file_path)[0]
question = data.get("question", "")
sentence_groups = data.get("analysis", {}).get("sentence_groups", {})

print(f"Question: {question}")
print(f"Number of groups: {len(sentence_groups)}")
print(sentence_groups)
