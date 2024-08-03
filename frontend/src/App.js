import React, { useState } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [file, setFile] = useState(null);
  const [csvUrl, setCsvUrl] = useState("");
  const [htmlUrl, setHtmlUrl] = useState("");
  const [message, setMessage] = useState("");
  const [loading, setLoading] = useState(false);
  const [tooltipVisible, setTooltipVisible] = useState(false);
  const [maPeriod1, setMaPeriod1] = useState(9);
  const [maPeriod2, setMaPeriod2] = useState(21);

  const handleFileChange = (e) => {
    setFile(e.target.files[0]);
  };

  const handleFileUpload = () => {
    if (!file) {
      setMessage("Please select a file to upload");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("ma_period1", maPeriod1);
    formData.append("ma_period2", maPeriod2);

    setLoading(true);
    setMessage("Uploading...");
    setTimeout(() => {
      setMessage("Data Processing");
      axios
        .post("http://localhost:5000/api/upload", formData)
        .then((response) => {
          setCsvUrl(response.data.csv_file);
          setHtmlUrl(response.data.html_file);
          setMessage(response.data.message);
        })
        .catch((error) => {
          setMessage("Error uploading file");
        })
        .finally(() => {
          setLoading(false);
        });
    }, 500); // Delay to show "Data Processing"
  };

  return (
    <div className="App">
      <header className="App-header">
        <h1>Stock Analyzer</h1>
        <h2>Support and Resistance Strategy</h2>
        <label
          htmlFor="file-upload"
          className="file-upload-label"
          onMouseEnter={() => setTooltipVisible(true)}
          onMouseLeave={() => setTooltipVisible(false)}
        >
          Choose File
          {tooltipVisible && (
            <span className="tooltip">
              Choose a CSV File Including Stocks Symbols
            </span>
          )}
        </label>
        <input
          type="file"
          id="file-upload"
          className="file-upload-input"
          onChange={handleFileChange}
        />
        <div className="ma-inputs">
          <div className="ma-input">
            <label htmlFor="ma-period1">MA Fast</label>
            <input
              type="number"
              id="ma-period1"
              value={maPeriod1}
              onChange={(e) => setMaPeriod1(e.target.value)}
            />
          </div>
          <div className="ma-input">
            <label htmlFor="ma-period2">MA Slow</label>
            <input
              type="number"
              id="ma-period2"
              value={maPeriod2}
              onChange={(e) => setMaPeriod2(e.target.value)}
            />
          </div>
        </div>
        <button onClick={handleFileUpload} disabled={loading}>
          {loading ? message : "Upload"}
        </button>
        {message && <div className="message">{message}</div>}
        <div className="results">
          {csvUrl && (
            <a
              href={`http://localhost:5000${csvUrl}`}
              download="stock_ranking.csv"
            >
              Download CSV File
            </a>
          )}
          {htmlUrl && (
            <a
              href={`http://localhost:5000${htmlUrl}`}
              download="stock_ranking.html"
            >
              Download HTML File
            </a>
          )}
        </div>
      </header>
    </div>
  );
}

export default App;
////////////////////////////////////////////////////////////////////////////////////////////////

// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [csvUrl, setCsvUrl] = useState("");
//   const [htmlUrl, setHtmlUrl] = useState("");
//   const [message, setMessage] = useState("");
//   const [loading, setLoading] = useState(false);
//   const [tooltipVisible, setTooltipVisible] = useState(false);

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleFileUpload = () => {
//     if (!file) {
//       setMessage("Please select a file to upload");
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     setLoading(true);
//     setMessage("Uploading...");
//     setTimeout(() => {
//       setMessage("Data Processing");
//       axios
//         .post("http://localhost:5000/api/upload", formData)
//         .then((response) => {
//           setCsvUrl(response.data.csv_file);
//           setHtmlUrl(response.data.html_file);
//           setMessage(response.data.message);
//         })
//         .catch((error) => {
//           setMessage("Error uploading file");
//         })
//         .finally(() => {
//           setLoading(false);
//         });
//     }, 500); // Delay to show "Data Processing"
//   };

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Stock Analyzer</h1>
//         <h2>Support and Resistance Strategy</h2>
//         <label
//           htmlFor="file-upload"
//           className="file-upload-label"
//           onMouseEnter={() => setTooltipVisible(true)}
//           onMouseLeave={() => setTooltipVisible(false)}
//         >
//           Choose File
//           {tooltipVisible && (
//             <span className="tooltip">
//               Choose a CSV File Including Stocks Symbols
//             </span>
//           )}
//         </label>
//         <input
//           type="file"
//           id="file-upload"
//           className="file-upload-input"
//           onChange={handleFileChange}
//         />
//         <input
//           type="file"
//           id="file-upload"
//           className="file-upload-input"
//           onChange={handleFileChange}
//         />
//         <button onClick={handleFileUpload} disabled={loading}>
//           {loading ? message : "Upload"}
//         </button>
//         {message && <div className="message">{message}</div>}
//         <div className="results">
//           {csvUrl && (
//             <a
//               href={`http://localhost:5000${csvUrl}`}
//               download="stock_ranking.csv"
//             >
//               Download CSV File
//             </a>
//           )}
//           {htmlUrl && (
//             <a
//               href={`http://localhost:5000${htmlUrl}`}
//               download="stock_ranking.html"
//             >
//               Download HTML File
//             </a>
//           )}
//         </div>
//       </header>
//     </div>
//   );
// }

// export default App;

/////////////////////////////////////////////////////////////////////////////////////////////////////

// import React, { useState } from "react";
// import axios from "axios";
// import "./App.css";

// function App() {
//   const [file, setFile] = useState(null);
//   const [csvUrl, setCsvUrl] = useState("");
//   const [htmlUrl, setHtmlUrl] = useState("");
//   const [error, setError] = useState(null);
//   const [loading, setLoading] = useState(false);

//   const handleFileChange = (e) => {
//     setFile(e.target.files[0]);
//   };

//   const handleFileUpload = () => {
//     if (!file) {
//       setError({ message: "Please select a file to upload" });
//       return;
//     }

//     const formData = new FormData();
//     formData.append("file", file);

//     setLoading(true);
//     setError(null);

//     axios
//       .post("http://localhost:5000/api/upload", formData)
//       .then((response) => {
//         setCsvUrl(response.data.csv_file);
//         setHtmlUrl(response.data.html_file);
//       })
//       .catch((error) => {
//         setError(error);
//       })
//       .finally(() => {
//         setLoading(false);
//       });
//   };

//   return (
//     <div className="App">
//       <header className="App-header">
//         <h1>Stock Analyzer</h1>
//         <h2>Support and Resistance Strategy</h2>
//         <input type="file" onChange={handleFileChange} />
//         <button onClick={handleFileUpload} disabled={loading}>
//           {loading ? "Uploading..." : "Upload"}
//         </button>
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
