import "./style.css";

const Error = ({ data }) => {
  return (
    <>
      <div className="error">
        <img src={`${process.env.PUBLIC_URL}/images/error.svg`} alt="Error" />
        <h1>{data.message}</h1>
      </div>
    </>
  );
};

export default Error;
