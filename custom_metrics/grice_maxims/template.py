class GriceMaximsTemplate:
    @staticmethod
    def generate_reason(input, actual_output):
        return f"""Given the input and actual output, analyze whether the actual output fulfills the four maxims of Grice.
1. The maxim of quantity: Is the actual output as informative as it could be? Does it include all necessary and relevant information, and leaves out nothing important? Is the actual output more informative than actually needed?
2. The maxim of quality: Is the actual output truthful? Does it contain factually true information that can be verified with sources, or does it contain false information that can't be verified with evidence?
3. The maxim of relation: Is the actual output relevant to the input?
4. The maxim of manner: Is the actual output clear, brief and orderly? Does it include ambiguity and/or obscurity?

Generate a single JSON object with five keys: `quantity_score`, `quality_score`, `relation_score`, `manner_score` and `reason`. The score for each maxim is weighted equally important, with a minimum score of 0 and a maximum score of 0.25.
Provide a CONCISE reason for the TOTAL score, meaning the sum of all individual scores. Explain why it is not higher, but also why it is at its current score.

The grammatical and spelling errors represent such errors in the actual output.
If there is nothing wrong, just say something positive with an upbeat encouraging tone (but don't overdo it otherwise it gets annoying).


**
IMPORTANT: Please make sure to only return in JSON format, with the 'reason' key providing the reason.
Example JSON:
{{
    "quantity_score": <your_quantity_score (float)>
    "quality_score": <your_quality_score (float)>
    "relation_score": <your_relation_score (float)>
    "manner_score": <your_manner_score (float)>
    "reason": "The score is <grice_maxim_score = your_quantity_score + your_quality_score + your_relation_score + your_manner_score> because <your_reason>."
}}
**

Actual output:
{actual_output}

Input:
{input}

JSON:
"""
