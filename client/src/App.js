import useAppState from "./hooks/useAppState";
import Searchbar from "./components/Searchbar";
import Content from "./components/Content";
import Spinner from "./components/Spinner";
import "./App.css";

const App = () => {
  const { symbolData, isLoading, handleSearch } = useAppState();

  return (
    <div id="App">
      <Searchbar searchSubmit={handleSearch} />
      <main>{isLoading ? <Spinner /> : <Content data={symbolData} />}</main>
    </div>
  );
};

export default App;
