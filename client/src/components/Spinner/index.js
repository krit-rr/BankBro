import { ImSpinner2 } from "react-icons/im";
import "./style.css";

const Spinner = () => {
  return (
    <>
      <div className="spinner-container">
        <ImSpinner2 className="spinner" size="50px" />
      </div>
    </>
  );
};

export default Spinner;