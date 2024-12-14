import { useState } from "react";
import OutputPage from "./pages/OutputPage";
import InputPage from "./pages/InputPage";
import Navbar from "./components/Navbar";

const App = () => {
  const [result, setResult] = useState(null);
  return (
    <>
      <Navbar />
      {result ? (
        <OutputPage result={result} setResult={setResult} />
      ) : (
        <InputPage setResult={setResult} result={result} />
      )}
    </>
  );
};

export default App;
