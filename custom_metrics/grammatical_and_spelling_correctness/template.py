class GrammaticalAndSpellingCorrectnessTemplate:
    @staticmethod
    def generate_erroneous(actual_output):
        return f"""Given the text, breakdown and generate a list of text pieces that contain grammatical or spelling errors. 
        When it comes to grammatical errors, don't only include the erroneous parts themselves, but also a few words before and after, so that it's clearer to see how the erroneous text pieces fit in with the rest of the text.

Example:
Example text: On Monday Steve, went to the zoo. He went see elephants, rhinos, giraffes and zebras. Finaly, he went to see lions and tigers.

{{
    "erroneous_text": ["On Monday Steve, went", "He went see elephants", "Finaly"]
}}
===== END OF EXAMPLE ======

**
IMPORTANT: Please make sure to only return in JSON format, with the "erroneous_text" key mapping to a list of strings. No words or explanation is needed.
**

Text:
{actual_output}

JSON:
"""

    @staticmethod
    def generate_verdicts(actual_output, erroneous_text_pieces):
        return f"""For the provided list of erroneous text pieces, generate a list of JSON with two keys: `verdict` and `reason`.
The 'verdict' key should ALWAYS be set to 'yes'.
The 'reason' is the reason for the verdict. Focus ONLY on grammar and spelling, not on the information itself.

**
IMPORTANT: Please make sure to only return in JSON format, with the 'verdicts' key mapping to a list of JSON objects.
Example statements: ["On Monday Steve, went", "He went see elephants", "Finaly"]
Example JSON:
{{
    "verdicts": [
        {{
            "verdict": "yes",
            "reason": "Punctuation error. <erroneous_text_piece> in <actual_output> is false, because <your_reason> and should be <corrected_text_piece>."
        }},
        {{
            "verdict": "yes",
            "reason": "Grammatical error. <erroneous_text_piece> in <actual_output> is false, because <your_reason> and should be <corrected_text_piece>."
        }},
        {{
            "verdict": "yes",
            "reason": "Spelling error. <erroneous_text_piece> in <actual_output> is false, because <your_reason> and should be <corrected_text_piece>."
        }}
    ]  
}}

Since you are going to generate a verdict for each text piece, the number of 'verdicts' SHOULD BE STRICTLY EQUAL to the number of `erroneous_text`.
**

Actual Output:
{actual_output}          

ErroneousText:
{erroneous_text_pieces}

JSON:
"""

    @staticmethod
    def generate_reason(erroneous_text_pieces, input, score):
        return f"""Given the grammatical and spelling correctness score, the list of reasons of grammatical and spelling errors made in the actual output, and the input, provide a CONCISE reason for the score. Explain why it is not higher, but also why it is at its current score.
The grammatical and spelling errors represent such errors in the actual output.
If there is nothing wrong, just say something positive with an upbeat encouraging tone (but don't overdo it otherwise it gets annoying).


**
IMPORTANT: Please make sure to only return in JSON format, with the 'reason' key providing the reason.
Example JSON:
{{
    "reason": "The score is <answer_relevancy_score> because <your_reason>."
}}
**

Grammatical and Spelling Correctness Score:
{score}

Reasons why the score can't be higher based on errors in the actual output:
{erroneous_text_pieces}

Input:
{input}

JSON:
"""
