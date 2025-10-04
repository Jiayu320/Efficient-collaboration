import json
import os

def transform_json_data(input_file_path, output_file_path):
    """
    Transforms the original MMLU-STEM JSON data into the desired format.

    Args:
        input_file_path (str): The full path to the original JSON file.
        output_file_path (str): The full path to save the transformed JSON file.
    """
    try:
        # Step 1: Read the original JSON file
        with open(input_file_path, 'r', encoding='utf-8') as f:
            original_data = json.load(f)

        transformed_data = []

        # Step 2: Iterate through each entry and transform it
        for item in original_data:
            question = item.get("question", "")
            choices = item.get("choices", [])
            answer_index = item.get("answer", -1)
            subject = item.get("subject", "")
            # Skip items that are malformed
            if not choices or not (0 <= answer_index < len(choices)):
                print(f"Skipping malformed item: {item}")
                continue

            # Format the choices with letters (A, B, C, D, ...)
            formatted_choices = []
            for i, choice in enumerate(choices):
                # chr(ord('A') + i) generates A, B, C, ...
                letter = chr(ord('A') + i)
                formatted_choices.append(f"{letter}. {choice}")

            choices_string = "\n".join(formatted_choices)
            # Combine the question and formatted choices into the 'problem' field
            problem_text = (
                f"{question}\n\n"
                f"{choices_string}\n\n"
                "Please select the correct answer and provide the final option letter and its corresponding content."
            )

            # Get the correct answer string from the choices list
            correct_answer_text = choices[answer_index]

            # Create the new dictionary in the desired format
            new_item = {
                "problem": problem_text,
                "answer": correct_answer_text,
                "answer_id": answer_index,
                "subject": subject
            }

            transformed_data.append(new_item)

        # Step 3: Ensure the output directory exists
        output_dir = os.path.dirname(output_file_path)
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # Step 4: Write the transformed data to the new JSON file
        with open(output_file_path, 'w', encoding='utf-8') as f:
            json.dump(transformed_data, f, indent=2, ensure_ascii=False)

        print(f"Transformation successful!")
        print(f"Original items found: {len(original_data)}")
        print(f"Transformed items written: {len(transformed_data)}")
        print(f"Output saved to: {output_file_path}")

    except FileNotFoundError:
        print(f"Error: The input file was not found at {input_file_path}")
    except json.JSONDecodeError:
        print(f"Error: The file at {input_file_path} is not a valid JSON file.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# --- Main execution part ---

# **IMPORTANT**: Define the file paths using raw strings (r"...") to avoid backslash errors on Windows.
original_file = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\original_data\MMLU-STEM.json"
output_file = r"D:\JIAYU\Documents\GitHub\Efficient-collaboration\dataset\TestData\MMLU-STEM.json"

# Run the transformation function
transform_json_data(original_file, output_file)