import { useState, useEffect } from "react";
import fetchSymbolData from "../utils/api";

const useAppState = () => {
  const [symbolData, setSymbolData] = useState({});
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Default to searching for TSLA on initial page load
    const initialSearch = async () => {
      const data = await fetchSymbolData("TSLA");
      setSymbolData(data);
      setIsLoading(false);
    };
    initialSearch();
  }, []);

  useEffect(() => {
    // Scroll to top of the page after every search
    window.scrollTo(0, 0);
  }, [symbolData]);

  const handleSearch = async (query) => {
    setIsLoading(true);
    const data = await fetchSymbolData(query);
    setSymbolData(data);
    setIsLoading(false);
  };

  return {
    symbolData,
    isLoading,
    handleSearch,
  };
};

export default useAppState;
