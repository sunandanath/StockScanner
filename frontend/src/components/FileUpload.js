// import React, { useState } from "react";
// import axios from "axios";
// import "./FileUpload.css";

// const FileUpload = () => {
//   const [file, setFile] = useState(null);
//   const [message, setMessage] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [resultsAvailable, setResultsAvailable] = useState(false);

//   const onChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const onSubmit = async (e) => {
//     e.preventDefault();
//     if (!file) {
//       setMessage("Please select a file to upload");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     try {
//       setLoading(true);
//       setMessage("");
//       setResultsAvailable(false);
//       const res = await axios.post("/api/upload", formData, {
//         headers: {
//           "Content-Type": "multipart/form-data",
//         },
//       });
//       setMessage(res.data.message);
//       if (res.data.message === "File successfully processed") {
//         setResultsAvailable(true);
//       }
//     } catch (err) {
//       setMessage("Error uploading file");
//     } finally {
//       setLoading(false);
//     }
//   };

//   const downloadResults = async () => {
//     try {
//       const res = await axios.get("/api/results", {
//         responseType: "blob",
//       });
//       const url = window.URL.createObjectURL(new Blob([res.data]));
//       const link = document.createElement("a");
//       link.href = url;
//       link.setAttribute("download", "stock_ranking.csv");
//       document.body.appendChild(link);
//       link.click();
//       link.parentNode.removeChild(link);
//     } catch (err) {
//       setMessage("Error downloading results");
//     }
//   };

//   return (
//     <div className="file-upload">
//       <form onSubmit={onSubmit}>
//         <div className="file-upload-input">
//           <input type="file" onChange={onChange} />
//         </div>
//         <button type="submit" disabled={loading}>
//           Upload
//         </button>
//       </form>
//       {message && <p>{message}</p>}
//       {resultsAvailable && (
//         <div>
//           <h2>Results</h2>
//           <button onClick={downloadResults}>Download Results</button>
//         </div>
//       )}
//     </div>
//   );
// };

// export default FileUpload;

////////////////////////////////////////////////////////////////////////////////////////////////////////////

import React, { useState } from "react";
import axios from "axios";
// import "./FileUpload.css";

const FileUpload = () => {
  const [file, setFile] = useState(null);
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [results, setResults] = useState(null);

  const onChange = (e) => {
    setFile(e.target.files[0]);
  };

  const onSubmit = async (e) => {
    e.preventDefault();
    if (!file) {
      setMessage("Please select a file to upload");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      setLoading(true);
      setMessage("");
      const res = await axios.post("/api/upload", formData, {
        headers: {
          "Content-Type": "multipart/form-data",
        },
      });
      setMessage(res.data.message);
      fetchResults();
    } catch (err) {
      setMessage("Error uploading file");
    } finally {
      setLoading(false);
    }
  };

  const fetchResults = async () => {
    try {
      const res = await axios.get("/api/results", {
        responseType: "blob",
      });
      const url = window.URL.createObjectURL(new Blob([res.data]));
      setResults(url);
    } catch (err) {
      setMessage("Error fetching results");
    }
  };

  return (
    <div className="file-upload">
      <form onSubmit={onSubmit}>
        <div className="file-upload-input">
          <input type="file" onChange={onChange} />
        </div>
        <button type="submit" disabled={loading}>
          Upload
        </button>
      </form>
      {message && <p>{message}</p>}
      {results && (
        <div>
          <h2>Results</h2>
          <a href={results} download="stock_ranking.csv">
            Download Results
          </a>
        </div>
      )}
    </div>
  );
};

export default FileUpload;
