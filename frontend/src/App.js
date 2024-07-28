import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [csvUrl, setCsvUrl] = useState("");
  const [htmlUrl, setHtmlUrl] = useState("");
  const [error, setError] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    if (!file) {
      setError({ message: "Please select a file to upload" });
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    setLoading(true);
    setError(null);

    axios
      .post("http://localhost:5000/api/upload", formData)
      .then((response) => {
        setCsvUrl(response.data.csv_file);
        setHtmlUrl(response.data.html_file);
      })
      .catch((error) => {
        setError(error);
      })
      .finally(() => {
        setLoading(false);
      });
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Stock Analyzer</h1>
        <h2>Support and Resistance Strategy</h2>
        <input type="file" onChange={handleFileChange} />
        <button onClick={handleFileUpload} disabled={loading}>
          {loading ? "Uploading..." : "Upload"}
        </button>
        {csvUrl && (
          <div>
            <h3>Download CSV File</h3>
            <a
              href={`http://localhost:5000${csvUrl}`}
              download="stock_ranking.csv"
            >
              Download CSV File
            </a>
          </div>
        )}
        {htmlUrl && (
          <div>
            <h3>Download HTML File</h3>
            <a
              href={`http://localhost:5000${htmlUrl}`}
              download="stock_ranking.html"
            >
              Download HTML File
            </a>
          </div>
        )}
        {error && <div>Error: {error.message}</div>}
      </header>
    </div>
  );
}

export default App;

///////////////////////////////////////////////////////////////////////////////////////////////

// import React, { useState } from "react";
// import axios from "axios";

// function App() {
//   const [file, setFile] = useState(null);
//   const [csvUrl, setCsvUrl] = useState("");
//   const [htmlUrl, setHtmlUrl] = useState("");
//   const [error, setError] = useState(null);

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleFileUpload = () => {
//     const formData = new FormData();
//     formData.append("file", file);

//     axios
//       .post("http://localhost:5000/api/upload", formData)
//       .then((response) => {
//         setCsvUrl(response.data.csv_file);
//         setHtmlUrl(response.data.html_file);
//       })
//       .catch((error) => {
//         setError(error);
//       });
//   };

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>File Upload and Download</h1>
//         <input type="file" onChange={handleFileChange} />
//         <button onClick={handleFileUpload}>Upload</button>
//         {csvUrl && (
//           <div>
//             <h3>Download CSV File</h3>
//             <a
//               href={`http://localhost:5000${csvUrl}`}
//               download="stock_ranking.csv"
//             >
//               Download CSV File
//             </a>
//           </div>
//         )}
//         {htmlUrl && (
//           <div>
//             <h3>Download HTML File</h3>
//             <a
//               href={`http://localhost:5000${htmlUrl}`}
//               download="stock_ranking.html"
//             >
//               Download HTML File
//             </a>
//           </div>
//         )}
//         {error && <div>Error: {error.message}</div>}
//       </header>
//     </div>
//   );
// }

// export default App;
