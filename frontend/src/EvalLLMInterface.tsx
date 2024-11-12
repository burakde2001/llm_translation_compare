import { Button, Container, TextField, Typography } from "@mui/material";
import { apiClient } from "./ApiClient";
import { useState } from "react";

export default function EvalLLMInterface({
  llm,
  evalLLM,
}: {
  llm: any;
  evalLLM: any;
}) {
  const [promptInput, setPromptInput] = useState("");

  const [evaluation, setEvaluation] = useState("");

  /*
    Sendet den im Textfeld der zu evaluierenden LLM eingegebenen Prompt an eine Schnittstelle im Back End, welche eine Antwort generiert und evaluieren lässt.
    Sends the prompt entered into the text field of the LLM to evaluate to an interface in the Back End, which generates an answer and lets said answer get evaluated.
  */
  const sendPromptToEval = (llm: string, prompt: string) => {
    if (prompt || /^\s*$/.test(prompt)) {
      let encodedPrompt = encodeURIComponent(prompt);
      let endpoint = `models/${llm}/${encodedPrompt}/eval`;
      apiClient
        .get(endpoint)
        .then((response) => {
          if (response.status === 200) {
            console.log(response.data);
            let thisEval = response.data.content;
            setEvaluation(thisEval);
          }
        })
        .catch((error) => {
          console.error("Error fetching data: ", error);
        });
    }
  };

  if (llm !== undefined) {
    return (
      <Container
        sx={{
          display: "flex",
          flexDirection: "column",
          border: 2,
          width: 500,
        }}
      >
        <Typography>
          LLM: {llm.model}, Evaluator LLM: {evalLLM.model}
        </Typography>
        <TextField
          id={`${llm.model}_promptField`}
          sx={{ marginTop: 5, marginBottom: 5 }}
          label={"Prompt"}
          onChange={(e) => setPromptInput(e.target.value)}
        />
        <Button
          variant="contained"
          sx={{
            textTransform: "none",
          }}
          onClick={() => sendPromptToEval(llm.model, promptInput)}
        >
          Send
        </Button>
        <TextField
          sx={{ marginTop: 5, marginBottom: 5 }}
          label={"Evaluation"}
          value={evaluation}
        />
      </Container>
    );
  } else {
    return <></>;
  }
}
