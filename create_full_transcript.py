import os

# Define the directory containing the txt files
input_directory = './txt_sm04'  # Replace with your folder path
output_file = 'compiled_sentences.txt'

# Check if the directory exists
if not os.path.exists(input_directory):
    print(f"The directory {input_directory} does not exist.")
else:
    # Create or open the output file in write mode
    with open(output_file, 'w') as outfile:
        # Iterate through each file in the directory
        for filename in os.listdir(input_directory):
            # Check if the file is a txt file
            if filename.endswith('.txt'):
                file_path = os.path.join(input_directory, filename)
                # Open and read the content of the file
                with open(file_path, 'r') as infile:
                    sentence = infile.read().strip()
                    # Write the sentence to the output file
                    outfile.write(sentence + '\n')

    print(f"All sentences have been compiled into {output_file}")

## To use with http://www.speech.cs.cmu.edu/tools/lmtool-new.html

## Out:
# SESSION 1719420836_420588
# [_INFO_] Found corpus: 2330 sentences, 24269 unique words
# [_INFO_] Found 0 words in extras  (0)
# [_INFO_] Language model completed  (0)
# [_INFO_] Pronounce completed  (0)
# [_STAT_] Elapsed time: 117.118 sec
# Please include these messages in bug reports.