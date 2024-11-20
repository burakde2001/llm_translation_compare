import { Button, Container, TextField, Typography } from "@mui/material";
import { apiClient } from "./ApiClient";
import { useState } from "react";

export default function LLMInterface(llm: any) {
  llm = llm.llm;

  const [promptInput, setPromptInput] = useState("");

  const [answer, setAnswer] = useState("");

  /*
    Sendet den im Textfeld eingegebenen Prompt an eine Schnittstelle im Back End, welche eine Antwort zurückliefert.
    Sends the prompt entered into the text field to an interface in the Back End, which returns an answer.
  */
  const sendPrompt = (llm: string, prompt: string) => {
    if (prompt || /^\s*$/.test(prompt)) {
      let endpoint = `models/postreq`;
      const promptRequest = {
        llm: llm,
        prompt_text: prompt,
      };
      apiClient
        .post(endpoint, promptRequest, {
          headers: { "Content-Type": "application/json" },
        })
        .then((response) => {
          if (response.status === 200) {
            let thisAnswer = response.data.content;
            setAnswer(thisAnswer);
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
        <Typography>{llm.model}</Typography>
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
          onClick={() => sendPrompt(llm.model, promptInput)}
        >
          Send
        </Button>
        <TextField
          sx={{ marginTop: 5, marginBottom: 5 }}
          label={"Answer"}
          value={answer}
        />
      </Container>
    );
  } else {
    return <></>;
  }
}
