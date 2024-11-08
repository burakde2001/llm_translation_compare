import { Button, Container, TextField, Typography } from "@mui/material";
import { apiClient } from "./ApiClient";
import { useState } from "react";

export default function LLMInterface(llm: any) {
  llm = llm.llm;

  const [promptInput, setPromptInput] = useState("");

  const [answer, setAnswer] = useState("");

  const sendPrompt = (llm: string, prompt: string) => {
    if (prompt || /^\s*$/.test(prompt)) {
      let encodedPrompt = encodeURIComponent(prompt);
      let endpoint = `models/${llm}/${encodedPrompt}`;
      apiClient
        .get(endpoint)
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
