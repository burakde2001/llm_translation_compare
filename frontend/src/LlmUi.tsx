import { Box, Container, Link } from "@mui/material";
import { useState } from "react";
import LLMInterface from "./LLMInterface";
import EvalLLMInterface from "./EvalLLMInterface";

/*
  Zwischenkomponente, die sicherstellt, dass die LLMInterface Komponente nur angezeigt wird, wenn sich LLMs in der "llms" Liste befinden.
  Component which makes sure that the LLMInterface component is only shown when there are LLMs inside the "llms" list.
*/
export default function LlmUi({ llms, evalLLM }: { llms: any; evalLLM: any }) {
  const [currentLLM, setCurrentLLM] = useState();

  if (llms !== undefined && evalLLM !== undefined) {
    return (
      <Box sx={{ display: "flex", flexDirection: "row" }}>
        <Container
          sx={{
            display: "flex",
            flexDirection: "column",
          }}
        >
          {llms.map((llm: any) => (
            <Link
              component="button"
              variant="body2"
              onClick={() => setCurrentLLM(llm)}
            >
              {llm.model}
            </Link>
          ))}
        </Container>
        <Container sx={{ display: "flex", flexDirection: "row" }}>
          <EvalLLMInterface llm={currentLLM} evalLLM={evalLLM} />
        </Container>
      </Box>
    );
  } else {
    return <></>;
  }
}
