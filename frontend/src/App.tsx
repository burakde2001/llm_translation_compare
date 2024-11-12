import { Box, Button, Container } from "@mui/material";
import "./App.css";
import { apiClient } from "./ApiClient";
import { useState } from "react";
import LlmUi from "./LlmUi";

function App() {
  const [llms, setLlms] = useState();
  const [evalLLM, setEvalLLM] = useState();

  /*
    Holt vom Back End eine Liste von LLM Instanzen, auf die man in dieser Anwendung zugreifen kann.
    Returns a list of LLM instances from the Back End for the user of this app to use.
  */
  const getLLMs = (url: string) => {
    apiClient
      .get(url)
      .then((response) => {
        if (response.status === 200) {
          setLlms(response.data);
        }
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  };

  /*
    Holt vom Back End die LLM Instanz für die Evaluierung der Antworten anderer LLMS.
    Returns an LLM Instance of the LLM for the evaluation of the answers of other LLMS from the Back End.
  */
  const getEvalLLM = (url: string) => {
    apiClient
      .get(url)
      .then((response) => {
        if (response.status === 200) {
          setEvalLLM(response.data);
        }
      })
      .catch((error) => {
        console.error("Error fetching data: ", error);
      });
  };

  return (
    <div className="App" style={{ height: "100%" }}>
      <Box sx={{ display: "flex", flexDirection: "column", height: "100%" }}>
        <Container sx={{ overflow: "hidden" }}>
          <Button
            variant="contained"
            sx={{ textTransform: "none" }}
            onClick={() => getLLMs("/")}
          >
            get LLMs
          </Button>
          <Button
            variant="contained"
            sx={{ textTransform: "none", marginLeft: "10px" }}
            onClick={() => getEvalLLM("/eval")}
          >
            get Evaluation LLM
          </Button>
        </Container>
        <Container
          sx={{ maxWidth: "100%", overflow: "auto", flex: 1, marginTop: 10 }}
          maxWidth={false}
        >
          <LlmUi llms={llms} evalLLM={evalLLM} />
        </Container>
      </Box>
    </div>
  );
}

export default App;
