import { useState } from "react";
import { FaSearch } from "react-icons/fa";

import useWindowPosition from "../../hooks/useWindowPosition";
import "./style.css";

const Searchbar = ({ searchSubmit }) => {
  const scrollPosition = useWindowPosition();
  const [searchTerm, setSearchTerm] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    searchSubmit(searchTerm);
    setSearchTerm("");
  };

  return (
    <header
      id="header"
      className={`${scrollPosition > 25 ? "header-sticky" : ""}`}
    >
      <div className="header__inner">
        <form action="" onSubmit={(e) => handleSubmit(e)}>
          <div>
            <input
              type="text"
              placeholder="Search by ticker symbol..."
              title=""
              value={searchTerm}
              onChange={(e) => setSearchTerm(e.target.value.toUpperCase())}
              required
            />
            <button
              type="submit"
              className="search-btn"
              aria-label="Submit search"
            >
              <FaSearch className="search-icon" />
            </button>
          </div>
        </form>
      </div>
    </header>
  );
};

export default Searchbar;
