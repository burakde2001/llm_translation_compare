import { Box, Button, Container } from "@mui/material";
import "./App.css";
import { apiClient } from "./ApiClient";
import { useState } from "react";
import LlmUi from "./LlmUi";

function App() {
  const [llms, setLlms] = useState();

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
        </Container>
        <Container
          sx={{ maxWidth: "100%", overflow: "auto", flex: 1, marginTop: 10 }}
          maxWidth={false}
        >
          <LlmUi llms={llms} />
        </Container>
      </Box>
    </div>
  );
}

export default App;
